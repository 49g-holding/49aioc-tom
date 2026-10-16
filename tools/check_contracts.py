"""Check the contracts of [ORG]AIOC-TOM.

1. Every schema in contracts/ is a sound JSON Schema 2020-12.
2. Every example in contracts/examples/valid/ validates against the schema named by the
   first part of its file name (<schema>.<case>.json), with format assertion on.
3. Every example in contracts/examples/must-fail/ fails against its schema.
4. A TOM Release example carries the right content address: release_id equals 'TOMR-' +
   SHA-256 of the canonical manifest body without release_id (docs/OUTPUT.md §3).
5. An Input Pack example carries the right content address: pack_id equals 'TOMI-' + the
   content address of the pack without pack_id (blueprint Annex E.1). One canon for both:
   content_address(obj, id_field, prefix). A must-fail example is otherwise valid, so its
   release_id or pack_id is its content address too.
6. Must-fail reasons: each must-fail example fails, and at least one of its errors has the
   JSON pointer (path) and the keyword of its entry in contracts/examples/MUST-FAIL-REASONS.json.
   A must-fail file with no entry, or an entry with no file, fails the check.
7. Listed-type subset: the listed_type enums of needs-request, needs-answer and tom-release are
   each a subset of the decision_types[].id of the signature list given by --signature-list,
   whose SHA-256 must equal contracts/PINS.json signature_list.sha256; and each holds no type
   that changes an engine, a gateway, a budget, a test or a review mode. Without
   --signature-list this check prints SKIPPED and the script exits 2, never 0.
8. Adapter fixtures: for each adapters/*.adapter.md (not the TEMPLATE), its one fenced block
   that starts 'adapter:'; its refusal_reasons equal the refused[].reason enum of
   input-pack.schema.json; each fixture under adapters/<source-type>/fixtures/ has its outcome
   computed from the block (refusal checks in the fixed order, then mappings, defaults, status
   cap and labels, blueprint Annex E.2) and compared with its 'expect', field by field. Every
   valid fixture is admitted (or recorded as an unknown) as expected; every must-fail fixture
   is refused with exactly its reason; the must-fail fixtures cover every refusal reason.
9. Release lint in CI (tools/release_lint.py): rule set A over docs/OUTPUT.md and over the enum
   strings of tom-release.schema.json (parts[].part, decisions[].decision.value, final_status);
   every fixture under tests/release-lint/fixtures/: pass/ must pass, and fail/<rule ID>--... must
   fail with that rule, and only that rule.
10. The reference-model catalogue (blueprint Annex E.19): upstream/reference-model-catalogue.seed.json
   validates against contracts/reference-model-catalogue.schema.json; rule sets A and B of the release
   lint find no hit in any string value of the seed; and contracts/PINS.json reference_model_catalogue
   has status 'not in the Library' with version, commit and sha256 null, or 'in the Library' with all
   three set. When it is 'in the Library', --catalogue gives the catalogue file, which must validate
   against the same schema, carry the pinned version, and have the pinned SHA-256. Without
   --catalogue, check 10 then prints SKIPPED and the script exits 2, never 0 (as check 7).
11. The design return contract (blueprint §5.10): --design-return gives the Library's
   library/contracts/design-return.schema.json, whose SHA-256 must equal contracts/PINS.json
   design_return_contract.sha256; every example in contracts/examples/design-return/ validates against
   it; and an example of an `accepted` return that has ended is `answered by release`, by the release
   it names. Without --design-return, check 11 prints SKIPPED and the script exits 2, never 0.
   The ID of a release notice is its content address too ('TOMN-', as check 4).

Usage: python3 tools/check_contracts.py --signature-list <path> --design-return <path> [--catalogue <path>]
  --signature-list: the 49GAION hub's upstream/human-floor-signature-types.json (check 7)
  --catalogue: the catalogue file pinned in contracts/PINS.json, when it is in the Library (check 10)
  --design-return: the Library's design return contract at the commit pinned in contracts/PINS.json (check 11)
Exit 0 when every check passes; 1 on any failure; 2 when check 7, 10 or 11 was skipped and nothing failed.
"""
import argparse, datetime, hashlib, importlib.util, json, pathlib, re, sys
import jsonschema, yaml
from referencing import Registry, Resource

ROOT = pathlib.Path(__file__).resolve().parent.parent
C = ROOT / "contracts"
EXAMPLES = C / "examples"
ADAPTERS = ROOT / "adapters"
LINT_FIXTURES = ROOT / "tests" / "release-lint" / "fixtures"
OUTPUT_MD = ROOT / "docs" / "OUTPUT.md"
SEED = ROOT / "upstream" / "reference-model-catalogue.seed.json"
ID_FIELDS = {"tom-release": ("release_id", "TOMR-"), "input-pack": ("pack_id", "TOMI-"),
             "release-notice": ("notice_id", "TOMN-")}
RETURN_EXAMPLES = EXAMPLES / "design-return"
DENIED_LISTED_TYPES = ["move-work-toward-ai", "change-gateway-policy", "widen-ai-budget-or-unattended-action",
                       "change-fixed-test-or-threshold", "set-or-rotate-golden-set", "approve-change-or-promote-challenger"]
LABEL_ORDER = ["source-backed", "inferred", "organisation-stated", "assumed", "unknown"]   # Annex B.1, highest first


def load_schemas():
    schemas, resources = {}, []
    for f in sorted(C.glob("*.schema.json")):
        doc = json.loads(f.read_text(encoding="utf-8"))
        jsonschema.Draft202012Validator.check_schema(doc)
        name = f.name[: -len(".schema.json")]
        schemas[name] = doc
        resources.append((doc["$id"], Resource.from_contents(doc)))
    return schemas, Registry().with_resources(resources)


def content_address(obj, id_field, prefix):
    """prefix + SHA-256 of the canonical JSON of obj without id_field: keys sorted,
    separators ',' and ':', UTF-8, non-ASCII kept. The canon of the release and the Input Pack."""
    body = {k: v for k, v in obj.items() if k != id_field}
    canon = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return prefix + hashlib.sha256(canon.encode("utf-8")).hexdigest()


def pointer(path):
    return "".join("/" + str(p).replace("~", "~0").replace("/", "~1") for p in path)


RFC3339 = re.compile(r"^\d{4}-\d{2}-\d{2}[Tt]\d{2}:\d{2}:\d{2}(\.\d+)?([Zz]|[+-]\d{2}:\d{2})$")


def format_checker():
    """The 2020-12 format checker, asserting 'date-time' too. jsonschema checks 'date-time' only
    when an optional package is installed; without it, this standard-library check is used."""
    fc = jsonschema.Draft202012Validator.FORMAT_CHECKER
    if "date-time" not in fc.checkers:
        @fc.checks("date-time", raises=ValueError)
        def _date_time(value):
            if not isinstance(value, str):
                return True
            if not RFC3339.match(value):
                return False
            datetime.datetime.fromisoformat(value[:-1] + "+00:00" if value[-1] in "Zz" else value)
            return True
    return fc


def check_examples(schemas, registry):
    """Checks 2 to 6."""
    fmt = format_checker()
    reasons_file = EXAMPLES / "MUST-FAIL-REASONS.json"
    reasons = json.loads(reasons_file.read_text(encoding="utf-8")) if reasons_file.exists() else {}
    failures, counts = 0, {"valid": 0, "must-fail": 0}
    seen = set()
    for kind in ("valid", "must-fail"):
        for f in sorted((EXAMPLES / kind).glob("*.json")):
            counts[kind] += 1
            name = f.name.split(".")[0]
            if name not in schemas:
                print(f"FAIL {kind}/{f.name}: no schema named {name}"); failures += 1; continue
            v = jsonschema.Draft202012Validator(schemas[name], registry=registry, format_checker=fmt)
            doc = json.loads(f.read_text(encoding="utf-8"))
            errs = sorted(v.iter_errors(doc), key=lambda e: list(e.absolute_path))
            address_ok = True
            if name in ID_FIELDS and isinstance(doc, dict):
                id_field, prefix = ID_FIELDS[name]
                address_ok = doc.get(id_field) == content_address(doc, id_field, prefix)
            if kind == "valid":
                ok = not errs and address_ok
                why = errs[0].message if errs else f"{ID_FIELDS.get(name, ('id',))[0]} is not the content address of the body"
                print(("pass" if ok else "FAIL") + f" valid/{f.name}" + ("" if ok else f": {why}"))
            else:
                seen.add(f.name)
                entry = reasons.get(f.name)
                found = {(pointer(e.absolute_path), e.validator) for e in errs}
                if not errs:
                    ok, why = False, "NOT REJECTED"
                elif entry is None:
                    ok, why = False, "no entry in MUST-FAIL-REASONS.json"
                elif (entry["path"], entry["keyword"]) not in found:
                    ok, why = False, f"rejected, but not at {entry['path']!r} by '{entry['keyword']}': {sorted(found)}"
                elif not address_ok:
                    ok, why = False, f"{ID_FIELDS[name][0]} is not the content address: not otherwise valid"
                else:
                    ok, why = True, f"rejected at {entry['path'] or '(root)'} by '{entry['keyword']}'"
                print(("pass" if ok else "FAIL") + f" must-fail/{f.name}" + (f" ({why})" if ok else f": {why}"))
            failures += 0 if ok else 1
    for name in sorted(set(reasons) - seen):
        print(f"FAIL MUST-FAIL-REASONS.json: entry {name} names no must-fail file"); failures += 1
    return failures, counts


def listed_type_enums(schemas):
    return {
        "needs-request": schemas["needs-request"]["properties"]["listed_type"]["enum"],
        "needs-answer": schemas["needs-answer"]["properties"]["decision"]["properties"]["listed_type"]["enum"],
        "tom-release": schemas["tom-release"]["properties"]["decisions"]["items"]["properties"]["decision"]["allOf"][0]["properties"]["listed_type"]["enum"],
    }


def check_listed_types(schemas, signature_list):
    """Check 7. Returns (failures, skipped)."""
    if not signature_list:
        print("SKIPPED check 7 (listed-type subset): no --signature-list given")
        return 0, True
    pins = json.loads((C / "PINS.json").read_text(encoding="utf-8"))
    raw = pathlib.Path(signature_list).read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != pins["signature_list"]["sha256"]:
        print(f"FAIL check 7: the signature list has SHA-256 {got}, not the pinned {pins['signature_list']['sha256']}")
        return 1, False
    ids = {t["id"] for t in json.loads(raw.decode("utf-8"))["decision_types"]}
    failures = 0
    for name, enum in listed_type_enums(schemas).items():
        outside, denied = sorted(set(enum) - ids), sorted(set(enum) & set(DENIED_LISTED_TYPES))
        ok = not outside and not denied
        where = f"the pinned list ({len(ids)} types, tag {pins['signature_list']['tag']})"
        print(f"pass listed_type of {name} {enum}: a subset of {where}, with no denied type" if ok else
              f"FAIL listed_type of {name} {enum}: not in {where}: {outside}; denied types: {denied}")
        failures += 0 if ok else 1
    return failures, False


# ---------------------------------------------------------------- check 8: adapters
def adapter_block(md):
    blocks = re.findall(r"```ya?ml\n(adapter:\n.*?)```", md.read_text(encoding="utf-8"), re.S)
    if len(blocks) != 1:
        raise ValueError(f"{len(blocks)} fenced blocks start 'adapter:'; exactly one is needed")
    return yaml.safe_load(blocks[0])["adapter"]


def cap(label, to):
    """A cap lowers only what ranks above it in the order of Annex B.1; it never raises a label.
    'history-only' caps as 'inferred' (Annex E.2, How the block is applied)."""
    if to in (None, "none"):
        return label
    if to == "history-only":
        to = "inferred"
    return to if LABEL_ORDER.index(label) < LABEL_ORDER.index(to) else label


def adapter_outcome(block, served, ctx):
    """The outcome of one served item, by the machine block (Annex E.2)."""
    def refuse(reason):
        return {"admitted": False, "refusal_reason": reason, "origin_kind": None, "status": None, "confidentiality": None,
                "defaulted": [], "status_cap": None, "unknown": None, "as_of": None, "labels": []}
    if ctx["channel"] != "adapter":
        return refuse("human port" if ctx["channel"] == "human port" else "other channel")
    if not served or not served.get("source_id"):
        return refuse("no reference")
    held = served.get("held") == "held"
    if held and not (served.get("version") and served.get("sha256")):
        return refuse("no reference")
    if ctx["revoked"]:
        return refuse("connection revoked")
    if not ctx["in_scope"]:
        return refuse("outside scope")
    if datetime.date.fromisoformat(ctx["read_on"]) > datetime.date.fromisoformat(ctx["scope_expires"]):
        return refuse("scope expired")
    if not ctx["resolves"]:
        return refuse("does not resolve")
    if held and ctx["computed_sha256"] != served["sha256"]:
        return refuse("hash mismatch")
    if ctx["carries_secret"]:
        return refuse("carries a secret")
    if ctx["person_level_records"]:
        return refuse("person-level records")
    if held and not ctx["atomisable"]:
        return refuse("not atomisable")
    m, defaulted, values = block["mappings"], [], {}
    for key, name in (("origin_kind", "origin kind"), ("status", "status"), ("confidentiality", "confidentiality")):
        if key in served:
            values[key] = m[key][served[key]]          # a value outside the closed table raises
        else:
            values[key] = m[key]["<not served>"]
            defaulted.append(name)
    status_cap = m["status_cap"][values["status"]]
    out = {"admitted": True, "refusal_reason": None, **values, "defaulted": defaulted, "status_cap": status_cap,
           "unknown": None if held else "not held",
           "as_of": served.get("as_of") if values["origin_kind"] == "export" else None, "labels": []}
    return out


def adapter_labels(block, served, ctx, anchors):
    m = block["mappings"]
    served_labels = {x["anchor"]: x["sl_label"] for x in served.get("statement_labels", [])}
    table = m["statement_label"]["conversation" if ctx["conversation_derived"] else "document"]
    status = m["status"][served["status"]] if "status" in served else m["status"]["<not served>"]
    ceiling = block["trust_ceiling"]
    labels = []
    for a in anchors:
        label = table[served_labels.get(a, "stated")]          # no label served: read as 'stated'
        label = cap(label, m["status_cap"][status])
        if "origin_kind" not in served:
            label = cap(label, block["defaulted_origin_kind_cap"])
        if LABEL_ORDER.index(label) < LABEL_ORDER.index(ceiling):
            label = ceiling                                     # no label rises above the trust ceiling
        labels.append({"anchor": a, "label": label})
    return labels


def check_adapters(schemas, registry):
    failures, count = 0, 0
    reasons_enum = schemas["input-pack"]["properties"]["refused"]["items"]["properties"]["reason"]["enum"]
    sr = jsonschema.Draft202012Validator(schemas["source-reference"], registry=registry,
                                         format_checker=format_checker())
    files = sorted(ADAPTERS.glob("*.adapter.md"))
    if not [f for f in files if f.name != "TEMPLATE.adapter.md"]:
        print("FAIL check 8: no adapter file in adapters/"); return 1, 0
    for md in files:
        if md.name == "TEMPLATE.adapter.md":
            print(f"skip adapters/{md.name} (the empty form; it has no fixtures)"); continue
        try:
            block = adapter_block(md)
        except Exception as e:                                  # noqa: BLE001 - reported as a failure
            print(f"FAIL adapters/{md.name}: {e}"); failures += 1; continue
        rr = block.get("refusal_reasons", [])
        ok = len(rr) == len(set(rr)) and set(rr) == set(reasons_enum)
        print(("pass" if ok else "FAIL") + f" adapters/{md.name} {block.get('id')} {block.get('version')}: refusal_reasons "
              + ("equal the refused[].reason enum of input-pack" if ok else f"{rr} != {reasons_enum}"))
        failures += 0 if ok else 1
        fx = ADAPTERS / md.name[: -len(".adapter.md")] / "fixtures"
        refused_reasons = set()
        for kind in ("valid", "must-fail"):
            for f in sorted((fx / kind).glob("*.json")):
                count += 1
                doc = json.loads(f.read_text(encoding="utf-8"))
                expect, served, ctx = doc["expect"], doc["served"], doc["context"]
                problems = []
                if served is not None:
                    problems += [f"served: {e.message}" for e in sr.iter_errors(served)]
                try:
                    got = adapter_outcome(block, served, ctx)
                    if got["admitted"] and got["unknown"] is None:
                        got["labels"] = adapter_labels(block, served, ctx, [x["anchor"] for x in expect.get("labels", [])])
                except KeyError as e:
                    got, problems = None, problems + [f"a served value is outside the closed tables: {e}"]
                if got is not None:
                    problems += [f"{k}: expected {expect.get(k)!r}, got {got.get(k)!r}" for k in sorted(set(expect) | set(got))
                                 if expect.get(k) != got.get(k)]
                    if kind == "valid" and not got["admitted"]:
                        problems.append("a valid fixture must be admitted")
                    if kind == "must-fail":
                        if got["admitted"]:
                            problems.append("a must-fail fixture must be refused")
                        refused_reasons.add(got["refusal_reason"])
                ok = not problems
                what = (f"refused: {got['refusal_reason']}" if got and not got["admitted"] else
                        f"admitted{' as an unknown' if got and got['unknown'] else ''}") if got else "no outcome"
                print(("pass" if ok else "FAIL") + f" {fx.relative_to(ROOT)}/{kind}/{f.name} ({what})" + ("" if ok else ": " + "; ".join(problems)))
                failures += 0 if ok else 1
        missing = sorted(set(rr) - refused_reasons)
        if missing:
            print(f"FAIL {fx.relative_to(ROOT)}: no must-fail fixture for {missing}"); failures += 1
    return failures, count


# ---------------------------------------------------------------- check 9: release lint
def load_release_lint():
    spec = importlib.util.spec_from_file_location("release_lint", ROOT / "tools" / "release_lint.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def check_lint(schemas):
    rl = load_release_lint()
    rules = rl.load_deny_list(rl.DEFAULT_DENY_LIST)
    failures, count = 0, 0
    print(f"release lint: deny-list {rules['version']} (sha256 {rules['sha256'][:12]}…)")
    if OUTPUT_MD.exists():
        hits = rl.lint_text(OUTPUT_MD.read_text(encoding="utf-8"), "A", None, rules)
        for h in hits:
            print(f"  docs/OUTPUT.md:{h['line']}: {h['pattern_id']} {h['match']!r}")
        ok = not hits
        print(("pass" if ok else "FAIL") + f" docs/OUTPUT.md, rule set A: {len(hits)} hits")
    else:
        ok = False
        print("FAIL docs/OUTPUT.md: not found")
    failures += 0 if ok else 1
    rel = schemas["tom-release"]["properties"]
    enums = {"parts[].part": rel["parts"]["items"]["properties"]["part"]["enum"],
             "decisions[].decision.value": rel["decisions"]["items"]["properties"]["decision"]["allOf"][0]["properties"]["value"]["enum"],
             "final_status": rel["final_status"]["enum"]}
    for where, values in enums.items():
        hits = [(s, h) for s in values for h in rl.lint_text(s, "A", None, rules)]
        ok = not hits
        print(("pass" if ok else "FAIL") + f" tom-release.schema.json {where} ({len(values)} strings), rule set A"
              + ("" if ok else ": " + "; ".join(f"{s!r} {h['pattern_id']}" for s, h in hits)))
        failures += 0 if ok else 1
    for kind in ("pass", "fail"):
        for f in sorted((LINT_FIXTURES / kind).glob("*.md")):
            count += 1
            part = rl.part_of(f)
            side = f.with_name(f.name + ".atoms.json")
            atoms = rl.load_sidecar(side) if side.exists() and part not in rl.NEVER_EXEMPT else None
            hits = rl.lint_text(f.read_text(encoding="utf-8"), "A" if part in rl.MACHINE_PARTS else "AB", atoms, rules)
            bad = sorted({h["pattern_id"] for h in hits if not h["exempt"]})
            exempt = [h for h in hits if h["exempt"]]
            if kind == "pass":
                ok = not bad
                why = (f"{len(exempt)} exempt" if exempt else "no hit") if ok else f"must pass, fails with {bad}"
            else:
                rule = f.name.split("--")[0]
                ok, why = bad == [rule], f"fails with {bad}" + ("" if bad == [rule] else f", expected only [{rule!r}]")
            print(("pass" if ok else "FAIL") + f" tests/release-lint/fixtures/{kind}/{f.name} ({why})")
            failures += 0 if ok else 1
    return failures, count


# ---------------------------------------------------------------- check 10: reference-model catalogue
def string_values(x):
    if isinstance(x, str):
        yield x
    elif isinstance(x, dict):
        for v in x.values():
            yield from string_values(v)
    elif isinstance(x, list):
        for v in x:
            yield from string_values(v)


def check_catalogue(schemas, registry, catalogue):
    """Check 10. Returns (failures, skipped, patterns in the seed)."""
    failures, skipped = 0, False
    v = jsonschema.Draft202012Validator(schemas["reference-model-catalogue"], registry=registry,
                                        format_checker=format_checker())
    if not SEED.exists():
        print(f"FAIL check 10: {SEED.relative_to(ROOT)} not found")
        return 1, False, 0
    seed = json.loads(SEED.read_text(encoding="utf-8"))
    errs = sorted(v.iter_errors(seed), key=lambda e: list(e.absolute_path))
    n = len(seed.get("patterns", [])) if isinstance(seed, dict) else 0
    ok = not errs
    print(("pass" if ok else "FAIL") + f" {SEED.relative_to(ROOT)}: {n} patterns, "
          + ("valid against reference-model-catalogue.schema.json" if ok else
             f"{pointer(errs[0].absolute_path) or '(root)'}: {errs[0].message}"))
    failures += 0 if ok else 1
    rl = load_release_lint()
    rules = rl.load_deny_list(rl.DEFAULT_DENY_LIST)
    hits = [(s, h) for s in string_values(seed) for h in rl.lint_text(s, "AB", None, rules)]
    ok = not hits
    print(("pass" if ok else "FAIL") + f" {SEED.relative_to(ROOT)}, rule sets A and B: {len(hits)} hits"
          + ("" if ok else ": " + "; ".join(f"{h['pattern_id']} {h['match']!r}" for _, h in hits)))
    failures += 0 if ok else 1
    pin = json.loads((C / "PINS.json").read_text(encoding="utf-8")).get("reference_model_catalogue")
    keys = ("version", "commit", "sha256")
    if pin is None:
        print("FAIL check 10: contracts/PINS.json has no reference_model_catalogue")
        return failures + 1, False, n
    if pin.get("status") == "not in the Library":
        ok = all(pin.get(k) is None for k in keys)
        print(("pass" if ok else "FAIL") + " PINS.json reference_model_catalogue: not in the Library"
              + (", version, commit and sha256 null; every run declares the catalogue unavailable" if ok else
                 ", but version, commit or sha256 is set"))
        failures += 0 if ok else 1
    elif pin.get("status") == "in the Library":
        if not all(pin.get(k) for k in keys):
            print("FAIL PINS.json reference_model_catalogue: in the Library, but version, commit or sha256 is missing")
            failures += 1
        elif not catalogue:
            print("SKIPPED check 10 (catalogue pin): the catalogue is in the Library and no --catalogue was given")
            skipped = True
        else:
            raw = pathlib.Path(catalogue).read_bytes()
            got = hashlib.sha256(raw).hexdigest()
            doc = json.loads(raw.decode("utf-8"))
            problems = [] if got == pin["sha256"] else [f"SHA-256 {got}, not the pinned {pin['sha256']}"]
            problems += [f"{pointer(e.absolute_path) or '(root)'}: {e.message}" for e in v.iter_errors(doc)]
            if isinstance(doc, dict) and doc.get("version") != pin["version"]:
                problems.append(f"version {doc.get('version')!r}, not the pinned {pin['version']!r}")
            ok = not problems
            print(("pass" if ok else "FAIL") + f" the pinned catalogue {pin['version']}"
                  + (": valid, version and SHA-256 as pinned" if ok else ": " + "; ".join(problems)))
            failures += 0 if ok else 1
    else:
        print(f"FAIL PINS.json reference_model_catalogue: status {pin.get('status')!r} is neither "
              "'not in the Library' nor 'in the Library'")
        failures += 1
    return failures, skipped, n


# ---------------------------------------------------------------- check 11: design return contract
def check_design_return(path):
    """Check 11. Returns (failures, skipped, examples)."""
    pins = json.loads((C / "PINS.json").read_text(encoding="utf-8"))
    pin = pins.get("design_return_contract")
    if not pin or not all(pin.get(k) for k in ("repository", "path", "commit", "sha256")):
        print("FAIL check 11: contracts/PINS.json has no complete design_return_contract pin"); return 1, False, 0
    files = sorted(RETURN_EXAMPLES.glob("*.json"))
    if not path:
        print("SKIPPED check 11 (design return contract): no --design-return given"); return 0, True, len(files)
    raw = pathlib.Path(path).read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    if got != pin["sha256"]:
        print(f"FAIL check 11: the design return contract has SHA-256 {got}, not the pinned {pin['sha256']}"); return 1, False, len(files)
    schema = json.loads(raw.decode("utf-8"))
    jsonschema.Draft202012Validator.check_schema(schema)
    v = jsonschema.Draft202012Validator(schema, format_checker=format_checker())
    failures = 0
    if not files:
        print("FAIL check 11: no example in contracts/examples/design-return/"); failures += 1
    for f in files:
        doc = json.loads(f.read_text(encoding="utf-8"))
        errs = list(v.iter_errors(doc))
        ok, why = not errs, (errs[0].message if errs else "")
        if ok and doc.get("kind") == "accepted" and doc.get("status") != "open":
            if doc.get("status") != "answered by release" or doc.get("answered_by") != doc["release"]["release_id"]:
                ok, why = False, "an accepted return ends as answered by release, by the release it names (§5.10, limit 3)"
        print(("pass" if ok else "FAIL") + f" design-return/{f.name}" + ("" if ok else f": {why}"))
        failures += 0 if ok else 1
    return failures, False, len(files)


def main(argv=None):
    ap = argparse.ArgumentParser(description="Check the contracts of [ORG]AIOC-TOM.")
    ap.add_argument("--signature-list", help="the 49GAION hub's upstream/human-floor-signature-types.json")
    ap.add_argument("--catalogue", help="the reference-model catalogue file pinned in contracts/PINS.json (check 10)")
    ap.add_argument("--design-return", help="the Library's design return contract at the commit pinned in contracts/PINS.json (check 11)")
    a = ap.parse_args(argv)
    schemas, registry = load_schemas()
    print(f"{len(schemas)} schemas sound (2020-12): {', '.join(schemas)}")
    failures, counts = check_examples(schemas, registry)
    f7, skipped = check_listed_types(schemas, a.signature_list)
    f8, adapter_count = check_adapters(schemas, registry)
    f9, lint_count = check_lint(schemas)
    f10, skipped10, patterns = check_catalogue(schemas, registry, a.catalogue)
    f11, skipped11, returns = check_design_return(a.design_return)
    failures += f7 + f8 + f9 + f10 + f11
    print(f"{counts['valid']} valid, {counts['must-fail']} must-fail, adapter fixtures {adapter_count}, "
          f"lint fixtures {lint_count}, catalogue seed {patterns} patterns, design-return examples {returns}; "
          f"check 7 {'SKIPPED' if skipped else 'run'}; check 10 {'SKIPPED' if skipped10 else 'run'}; "
          f"check 11 {'SKIPPED' if skipped11 else 'run'}; {failures} failures")
    if failures:
        return 1
    return 2 if (skipped or skipped10 or skipped11) else 0


if __name__ == "__main__":
    sys.exit(main())
