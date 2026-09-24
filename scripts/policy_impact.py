#!/usr/bin/env python3
"""Policy impact alert.

Run by .github/workflows/policy-impact.yml on every push to main that changes
content/. For each changed policy it lists the other LIVE published policies
linked to it (by wikilink or `related_policies` front-matter), groups them by
`owner_role`, and flags wording in those policies that the change removed
(timescales, stage names) so the owner knows what to check.

Prints a Markdown report to stdout, or nothing if no policy changed.
Usage: policy_impact.py <before_sha> <after_sha>
"""
import os, re, subprocess, sys
from collections import defaultdict

SITE = "https://policies.nudgeeducation.online"
SKIP = re.compile(r"(^|/)(index|change-log)\.md$|^content/(00-index|audience)/")
LINK = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
PHRASE = re.compile(
    r"\b\d+\s+(?:working |calendar |school |clear )?(?:days?|weeks?|months?|hours?)\b"
    r"|\bStage\s+\d\b|\bpanel hearing\b|\bthree[- ]stage\b",
    re.I,
)


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=False).stdout


def frontmatter(text):
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return fm
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    rel = fm.get("related_policies", "")
    fm["related"] = {x.strip().strip("'\"") for x in rel.strip("[]").split(",") if x.strip()}
    return fm


def slug(path):
    return os.path.splitext(os.path.basename(path))[0]


def load_pages():
    pages = {}
    for root, _, files in os.walk("content"):
        for f in files:
            if not f.endswith(".md"):
                continue
            p = os.path.join(root, f)
            if SKIP.search(p):
                continue
            text = open(p, encoding="utf-8").read()
            fm = frontmatter(text)
            pages[slug(p)] = {
                "path": p,
                "text": text,
                "title": fm.get("title", slug(p)).strip("'\""),
                "owner": fm.get("owner_role", "Owner not set").strip("'\""),
                "status": fm.get("status", ""),
                "version": fm.get("version", ""),
                "related": fm["related"],
                "links": {slug(t.strip()) for t in LINK.findall(text)},
            }
    return pages


def url(page):
    rel = page["path"][len("content/"):-3]
    return f"{SITE}/{rel}"


STOP = {"policy", "procedure", "procedures", "including", "nudge", "education", "online", "and", "the", "for"}


def topic_words(title):
    """Significant words from a policy title, stemmed crudely (complaints -> complain)."""
    words = re.findall(r"[a-z]+", title.lower())
    return {w[:7] for w in words if len(w) >= 5 and w not in STOP}


def still_uses(text, phrase, topics, window=250):
    """True if `phrase` appears in `text` near a word about the changed policy's topic."""
    low = text.lower()
    for m in re.finditer(re.escape(phrase), low):
        ctx = low[max(0, m.start() - window): m.end() + window]
        if any(t in ctx for t in topics):
            return True
    return False


def removed_phrases(before, after, path):
    diff = git("diff", "--unified=0", before, after, "--", path)
    removed, added = set(), set()
    for line in diff.splitlines():
        if line.startswith("-") and not line.startswith("---"):
            removed |= {p.lower() for p in PHRASE.findall(line)}
        elif line.startswith("+") and not line.startswith("+++"):
            added |= {p.lower() for p in PHRASE.findall(line)}
    return sorted(removed - added)


def main():
    before, after = sys.argv[1], sys.argv[2]
    if not before or set(before) == {"0"}:
        return
    changed = [
        p for p in git("diff", "--name-only", before, after, "--", "content").split()
        if p.endswith(".md") and not SKIP.search(p) and os.path.exists(p)
    ]
    if not changed:
        return
    pages = load_pages()
    by_owner = defaultdict(list)
    sections = []
    for path in changed:
        c = slug(path)
        if c not in pages:
            continue
        cp = pages[c]
        gone = removed_phrases(before, after, path)
        rows = []
        for s, p in sorted(pages.items(), key=lambda kv: kv[1]["title"]):
            if s == c or p["status"] != "live":
                continue
            why = []
            if c in p["links"]:
                why.append("links to it")
            if c in p["related"]:
                why.append("lists it as related")
            if s in cp["related"]:
                why.append("named as related by the changed policy")
            if not why:
                continue
            topics = topic_words(cp["title"])
            still = [g for g in gone if still_uses(p["text"], g, topics)] if (c in p["links"] or c in p["related"]) else []
            rows.append((p, why, still))
            by_owner[p["owner"]].append((p, cp, still))
        if not rows:
            continue
        lines = [f"### {cp['title']} ({cp['version']}) — [view]({url(cp)})", ""]
        if gone:
            lines.append("Wording removed by this change: " + ", ".join(f"`{g}`" for g in gone))
            lines.append("")
        lines.append("| Affected policy | Owner | Why | Still says |")
        lines.append("|---|---|---|---|")
        for p, why, still in rows:
            flag = ", ".join(f"⚠️ `{x}`" for x in still) or "—"
            lines.append(f"| [{p['title']}]({url(p)}) | {p['owner']} | {'; '.join(why)} | {flag} |")
        sections.append("\n".join(lines))
    if not sections:
        return
    out = [
        "A policy change has been published to policies.nudgeeducation.online. "
        "The policies below are linked to what changed, so their owners should check them.",
        "",
        "## Who needs to check what",
        "",
    ]
    for owner in sorted(by_owner):
        items = by_owner[owner]
        urgent = [p for p, _, still in items if still]
        titles = sorted({p["title"] for p, _, _ in items})
        note = f" — **{len(urgent)} still use removed wording**" if urgent else ""
        out.append(f"- **{owner}**: {len(titles)} polic{'y' if len(titles) == 1 else 'ies'}{note}")
    out += ["", "## Detail by changed policy", ""] + sections + [
        "",
        "---",
        "⚠️ means the affected policy still contains wording (a timescale or stage name) that the change removed — "
        "it probably needs updating. Links are found from wikilinks and `related_policies` front-matter. "
        f"Commit: `{after[:7]}`. Close this issue when the owners have checked.",
    ]
    print("\n".join(out))


if __name__ == "__main__":
    main()
