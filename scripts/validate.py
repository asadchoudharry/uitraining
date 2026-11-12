#!/usr/bin/env python3
"""UITraining corpus validation. Run from the repository root: python3 scripts/validate.py
Checks: JSON/JSONL parse, case-study frontmatter, internal relative links in Markdown,
forbidden binary assets outside assets/licensed-only, and scoreboard count consistency."""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []

# 1. JSON + JSONL parse
for p in sorted(ROOT.rglob('*.json')) + sorted(ROOT.rglob('*.jsonl')):
    if '.git' in p.parts:
        continue
    try:
        if p.suffix == '.json':
            json.loads(p.read_text(encoding='utf-8'))
        else:
            for i, line in enumerate(p.read_text(encoding='utf-8').splitlines(), 1):
                if line.strip():
                    json.loads(line)
    except Exception as e:
        errors.append(f'{p.relative_to(ROOT)}: {e}')

# 2. Case-study frontmatter (must start with a JSON block in --- fences or a JSON object)
for p in sorted((ROOT / 'case-studies').rglob('*.md')):
    t = p.read_text(encoding='utf-8')[:400]
    if not (t.startswith('---') or t.startswith('{')):
        warnings.append(f'{p.relative_to(ROOT)}: no leading frontmatter block')

# 3. Internal relative links in Markdown resolve
link_re = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
for p in sorted(ROOT.rglob('*.md')):
    if '.git' in p.parts:
        continue
    for m in link_re.finditer(p.read_text(encoding='utf-8')):
        href = m.group(1).split('#')[0].strip()
        if not href or href.startswith(('http://', 'https://', 'mailto:', 'sandbox:')):
            continue
        target = (p.parent / href).resolve()
        if not target.exists():
            errors.append(f'{p.relative_to(ROOT)}: broken relative link -> {href}')

# 4. Forbidden binaries outside assets/licensed-only
BIN = {'.png', '.jpg', '.jpeg', '.gif', '.webp', '.zip', '.woff', '.woff2', '.ttf', '.mp4'}
for p in sorted(ROOT.rglob('*')):
    if '.git' in p.parts or not p.is_file():
        continue
    if p.suffix.lower() in BIN and 'assets/licensed-only' not in str(p.relative_to(ROOT)):
        errors.append(f'{p.relative_to(ROOT)}: binary asset outside assets/licensed-only')

# 5. Scoreboard consistency: coverage + features + pages counts present in README
def count_lines(fp):
    return sum(1 for l in (ROOT / fp).read_text(encoding='utf-8').splitlines() if l.strip())
readme = (ROOT / 'README.md').read_text(encoding='utf-8')
for label, fp in [('coverage', 'data/coverage.jsonl'), ('features', 'feature-atlas/feature-master-inventory.jsonl'), ('pages', 'data/pages.jsonl')]:
    n = count_lines(fp)
    if str(n) not in readme:
        warnings.append(f'README scoreboard does not mention {label} count {n} (check manually)')

print(f'errors: {len(errors)}')
for e in errors:
    print('  E:', e)
print(f'warnings: {len(warnings)}')
for w_ in warnings:
    print('  W:', w_)
sys.exit(1 if errors else 0)
