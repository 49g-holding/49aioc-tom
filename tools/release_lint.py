"""The release lint of [ORG]AIOC-TOM (blueprint Annex D item 19; Annex E.15).

A release part says nothing about how the work was made, beyond the fixed forms of the
quality checks. This lint enforces it by code, from the deny-list
tests/release-lint/DENY-LIST.json:

  - rule set A (how the work was made): every release part, including the string values of
    the manifest, the design ledgers and the trace; in CI, docs/OUTPUT.md and the enum strings
    of contracts/tom-release.schema.json;
  - rule set B (internal codes): every human-readable part, that is every part except the
    manifest, the design ledgers and the trace.

Matching. Case-sensitive words match on word boundaries; so do case-insensitive words and
phrases, where a hyphen is part of a word ("AI-or-human" is caught by A-P1, not by the word
list). Whitespace inside a phrase matches any run of whitespace. Patterns are applied as the
deny-list writes them: rule set A patterns case-insensitive, rule set B patterns as given.

The one exemption. A rule-set-A hit passes only when it is the organisation's own subject
matter: it lies inside an element marked <!-- el:<element ID> --> (up to the next marker or
heading), and an atom text of that element contains the same word, case-insensitive. The atom
texts come from a sidecar, <file>.atoms.json, of the form
    {"elements": {"<element ID>": ["<atom text>", ...]}}
An atom may also be given as {"atom_id": "<atom ID>", "text": "<atom text>"}; its atom ID is
then recorded as the exemption's atom ref. For an atom given as text only (the CI form), the
ref is its position in the sidecar, "<element ID>#<n>". There is never an exemption in the
quality checks, in the manifest, in the fixed framing (text outside an element marker), in
rule set B, or in a file given with --file that has no sidecar.

API:
    load_deny_list(path) -> rules
    lint_text(text, rule_sets, element_atoms=None, rules=None) -> hits
    lint_release(release_dir, manifest_path, atoms_dir=None, deny_list=None) -> report (Annex E.15)

CLI:
    python3 tools/release_lint.py --file <path> --rules A|B|AB [--atoms <sidecar>]
    python3 tools/release_lint.py --release <dir> --manifest <file> [--atoms <dir>]
Exit 0 on pass, 1 on any hit that is not exempt. Standard library only.
"""
import argparse, hashlib, json, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_DENY_LIST = ROOT / "tests" / "release-lint" / "DENY-LIST.json"

# The twenty release parts (contracts/tom-release.schema.json), and their file-name slugs.
PARTS = ["design brief", "structure", "blueprint", "rationale and evidence brief", "design ledger",
         "hand-offs register", "counterparty register", "legal and regulatory perimeter",
         "deferred-boundary register", "seam findings", "role register", "walkthrough report", "quality checks",
         "decision package", "registers", "trace", "strategy frame", "outside-party journeys", "value case",
         "current-state activity profile"]
SLUGS = {p.replace(" ", "-"): p for p in PARTS}
MACHINE_PARTS = {"manifest", "design ledger", "trace"}      # rule set B does not apply
NEVER_EXEMPT = {"manifest", "quality checks"}

L_EDGE, R_EDGE = r"(?<![\w-])", r"(?![\w-])"               # a hyphen is part of a word
MARKER = re.compile(r"<!--\s*el:([^\s>]+)\s*-->")
HEADING = re.compile(r"^#{1,6}\s", re.M)


def _word_regex(word, case_sensitive):
    body = re.sub(r"(\\ )+", r"\\s+", re.escape(word))
    return re.compile(L_EDGE + body + R_EDGE, 0 if case_sensitive else re.I)


def load_deny_list(path=DEFAULT_DENY_LIST):
    """Read the deny-list; return {'version', 'sha256', 'path', 'rules': [(set, rule ID, regex)]}."""
    path = pathlib.Path(path)
    raw = path.read_bytes()
    doc = json.loads(raw.decode("utf-8"))
    rules = []
    for set_id, rule_set in doc["rule_sets"].items():
        for e in rule_set["entries"]:
            if e["kind"] == "words":
                for w in e["words"]:
                    rules.append((set_id, e["id"], _word_regex(w, e["case_sensitive"])))
            else:
                flags = 0 if e["case_sensitive"] else re.I
                rules.append((set_id, e["id"], re.compile(e["pattern"], flags)))
    return {"version": doc["version"], "sha256": hashlib.sha256(raw).hexdigest(), "path": str(path), "rules": rules}


_DEFAULT = None


def _default_rules():
    global _DEFAULT
    if _DEFAULT is None:
        _DEFAULT = load_deny_list(DEFAULT_DENY_LIST)
    return _DEFAULT


def _regions(text):
    """Element regions: a list of (start offset, element ID or None), sorted by offset."""
    bounds = [(m.end(), m.group(1)) for m in MARKER.finditer(text)]
    bounds += [(m.start(), None) for m in HEADING.finditer(text)]
    return sorted(bounds, key=lambda b: b[0])


def _element_at(regions, offset):
    current = None
    for start, element in regions:
        if start > offset:
            break
        current = element
    return current


def _atom_text_and_ref(atom, element_id, n):
    if isinstance(atom, dict):
        return atom.get("text", ""), atom.get("atom_id") or f"{element_id}#{n}"
    return str(atom), f"{element_id}#{n}"


def lint_text(text, rule_sets, element_atoms=None, rules=None):
    """Lint one text. rule_sets: 'A', 'B' or 'AB'. element_atoms: {element ID: [atom, ...]} or
    None; None means no exemption is possible (quality checks, manifest, a file with no sidecar).
    Returns hits: {rule, pattern_id, element_id, exempt, atom_refs, line, match}."""
    rules = rules or _default_rules()
    masked = MARKER.sub(lambda m: " " * len(m.group(0)), text)   # markers are never linted
    regions = _regions(text)
    hits = []
    for set_id, rule_id, rx in rules["rules"]:
        if set_id not in rule_sets:
            continue
        for m in rx.finditer(masked):
            element = _element_at(regions, m.start())
            exempt, refs = False, []
            if set_id == "A" and element_atoms is not None and element is not None:
                same = _word_regex(" ".join(m.group(0).split()), False)
                for n, atom in enumerate(element_atoms.get(element, []), start=1):
                    atom_text, ref = _atom_text_and_ref(atom, element, n)
                    if same.search(atom_text):
                        refs.append(ref)
                exempt = bool(refs)
            hits.append({"rule": set_id, "pattern_id": rule_id, "element_id": element, "exempt": exempt,
                         "atom_refs": refs, "line": text.count("\n", 0, m.start()) + 1, "match": m.group(0)})
    hits.sort(key=lambda h: (h["line"], h["pattern_id"]))
    return hits


def load_sidecar(path):
    """Read a sidecar <file>.atoms.json; return {element ID: [atom, ...]}."""
    return json.loads(pathlib.Path(path).read_text(encoding="utf-8"))["elements"]


def _json_strings(node, element=None, out=None):
    """Every string value of a JSON document, with the element it sits in: the nearest enclosing
    object's 'element_id' or 'id' (a reading until the design-ledger schema is built)."""
    out = [] if out is None else out
    if isinstance(node, dict):
        here = node.get("element_id") if isinstance(node.get("element_id"), str) else (
            node.get("id") if isinstance(node.get("id"), str) else element)
        for v in node.values():
            _json_strings(v, here, out)
    elif isinstance(node, list):
        for v in node:
            _json_strings(v, element, out)
    elif isinstance(node, str):
        out.append((node, element))
    return out


def _lint_json(doc, rule_sets, element_atoms, rules):
    hits = []
    for value, element in _json_strings(doc):
        text = value if element is None else f"<!-- el:{element} -->{value}"
        for h in lint_text(text, rule_sets, element_atoms, rules):
            h["line"] = None
            hits.append(h)
    return hits


def lint_release(release_dir, manifest_path, atoms_dir=None, deny_list=None):
    """Lint every part of a frozen release and the string values of its manifest.
    Returns the lint report (blueprint Annex E.15): deny_list_version, deny_list_sha256,
    parts_checked, hits, result."""
    rules = load_deny_list(deny_list) if deny_list else _default_rules()
    release_dir, manifest_path = pathlib.Path(release_dir), pathlib.Path(manifest_path)
    raw = manifest_path.read_bytes()
    manifest = json.loads(raw.decode("utf-8"))
    checked = [{"part": "manifest", "sha256": hashlib.sha256(raw).hexdigest()}]
    hits = [dict(h, part="manifest") for h in _lint_json(manifest, "A", None, rules)]
    for p in manifest.get("parts", []):
        part, f = p["part"], release_dir / p["path"]
        data = f.read_bytes()
        checked.append({"part": part, "sha256": hashlib.sha256(data).hexdigest()})
        rule_sets = "A" if part in MACHINE_PARTS else "AB"
        atoms = None
        if atoms_dir is not None and part not in NEVER_EXEMPT:
            side = pathlib.Path(atoms_dir) / (p["path"] + ".atoms.json")
            if side.exists():
                atoms = load_sidecar(side)
        if f.suffix == ".json":
            found = _lint_json(json.loads(data.decode("utf-8")), rule_sets, atoms, rules)
        else:
            found = lint_text(data.decode("utf-8"), rule_sets, atoms, rules)
        hits += [dict(h, part=part) for h in found]
    report_hits = [{k: h[k] for k in ("part", "rule", "pattern_id", "element_id", "exempt", "atom_refs")} for h in hits]
    return {"deny_list_version": rules["version"], "deny_list_sha256": rules["sha256"],
            "parts_checked": checked, "hits": report_hits,
            "result": "fail" if any(not h["exempt"] for h in hits) else "pass"}


def part_of(path):
    """The release part a file name names (<case>.<part>.md), or None."""
    stem = pathlib.Path(path).name.split(".")
    return SLUGS.get(stem[-2]) if len(stem) >= 3 else None


def main(argv=None):
    ap = argparse.ArgumentParser(description="The release lint of [ORG]AIOC-TOM.")
    ap.add_argument("--file")
    ap.add_argument("--rules", choices=["A", "B", "AB"])
    ap.add_argument("--atoms", help="--file: the sidecar; --release: the directory of sidecars")
    ap.add_argument("--release")
    ap.add_argument("--manifest")
    ap.add_argument("--deny-list", default=str(DEFAULT_DENY_LIST))
    a = ap.parse_args(argv)
    if a.file and a.rules and not a.release:
        rules = load_deny_list(a.deny_list)
        side = pathlib.Path(a.atoms) if a.atoms else pathlib.Path(a.file + ".atoms.json")
        part = part_of(a.file)
        atoms = load_sidecar(side) if side.exists() and part not in NEVER_EXEMPT else None
        hits = lint_text(pathlib.Path(a.file).read_text(encoding="utf-8"), a.rules, atoms, rules)
        for h in hits:
            tail = f" (exempt: own subject matter, {', '.join(h['atom_refs'])})" if h["exempt"] else ""
            print(f"{a.file}:{h['line']}: {h['pattern_id']} {h['match']!r}{tail}")
        bad = sum(1 for h in hits if not h["exempt"])
        print(f"{len(hits)} hits, {bad} not exempt: {'fail' if bad else 'pass'} (deny-list {rules['version']})")
        return 1 if bad else 0
    if a.release and a.manifest and not a.file:
        report = lint_release(a.release, a.manifest, a.atoms, a.deny_list)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 0 if report["result"] == "pass" else 1
    ap.error("use --file <path> --rules A|B|AB [--atoms <sidecar>], or --release <dir> --manifest <file> [--atoms <dir>]")


if __name__ == "__main__":
    sys.exit(main())
