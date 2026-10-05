#!/usr/bin/env python3
"""Check every SKILL.md: valid YAML frontmatter, a name, and a description of at most 1,024 characters.

Claude's skill format caps the description at 1,024 characters; a longer one can stop the skill from loading.
Usage: python3 scripts/check_skills.py [root ...]   (defaults to the repo root)
"""
import glob, os, re, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

LIMIT = 1024


def check(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return "no YAML frontmatter"
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        return "frontmatter is not valid YAML: " + str(e).splitlines()[0]
    if not meta.get("name"):
        return "missing name"
    desc = str(meta.get("description") or "")
    if not desc:
        return "missing description"
    if len(desc) > LIMIT:
        return f"description is {len(desc)} characters (limit {LIMIT})"
    return None


def main():
    roots = sys.argv[1:] or [os.path.dirname(os.path.dirname(os.path.abspath(__file__)))]
    failures = 0
    files = sorted(f for r in roots for f in glob.glob(os.path.join(r, "**", "SKILL.md"), recursive=True))
    for f in files:
        problem = check(f)
        if problem:
            failures += 1
            print(f"FAIL {f}: {problem}")
    print(f"{len(files)} skills checked, {failures} failing")
    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
