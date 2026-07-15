import os, re

root = r"F:\WORKSTATION\Github\system-design"
link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
mermaid_re = re.compile(r"```mermaid.*?```", re.DOTALL)

md_files = []
for dp, dirs, files in os.walk(root):
    for fn in files:
        if fn.endswith(".md"):
            md_files.append(os.path.join(dp, fn))

# --- link check ---
broken = []
total_links = 0
for path in md_files:
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    base = os.path.dirname(path)
    for m in link_re.finditer(content):
        t = m.group(2).strip()
        if t.startswith(("http://", "https://", "mailto:", "#")):
            continue
        tp = t.split("#")[0]
        if not tp:
            continue
        total_links += 1
        if not os.path.exists(os.path.normpath(os.path.join(base, tp))):
            broken.append((os.path.relpath(path, root), t))

# --- mermaid check ---
total_diagrams = 0
unclosed = []
residual = []
for path in md_files:
    with open(path, "r", encoding="utf-8", newline="") as f:
        content = f.read()
    opens = content.count("```mermaid")
    blocks = mermaid_re.findall(content)
    total_diagrams += len(blocks)
    if len(blocks) != opens:
        unclosed.append(os.path.relpath(path, root))
    for b in blocks:
        if "\\n" in b:
            residual.append(os.path.relpath(path, root)); break

print(f"Markdown files:          {len(md_files)}")
print(f"Internal links checked:  {total_links}")
print(f"Broken links:            {len(broken)}")
for s, t in broken:
    print(f"   BROKEN {s} -> {t}")
print(f"Mermaid diagrams:        {total_diagrams}")
print(f"Unclosed mermaid fences: {len(unclosed)}  {unclosed if unclosed else ''}")
print(f"Residual \\n in mermaid:  {len(residual)}  {residual if residual else ''}")
print("\nRESULT:", "ALL GREEN ✅" if not broken and not unclosed and not residual else "ISSUES FOUND ❌")
