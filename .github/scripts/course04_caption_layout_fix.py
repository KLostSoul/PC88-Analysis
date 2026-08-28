from pathlib import Path

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

repls = [
    (
        '.shot figcaption{background:#f8faff;color:#334155;padding:12px 14px;border-top:1px solid var(--line);font-size:.93rem;line-height:1.6}',
        '.shot figcaption{background:#f8faff;color:#334155;padding:13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65}',
        'desktop caption'
    ),
    (
        '.shots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px}',
        '.shots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}',
        'shots grid alignment'
    ),
    (
        '.shot figcaption{font-size:.88rem}',
        '.shot figcaption{font-size:.96rem}',
        'mobile caption'
    ),
]

for old, new, label in repls:
    count = s.count(old)
    if count != 1:
        raise SystemExit(f'{label}: expected 1 match, got {count}')
    s = s.replace(old, new, 1)

p.write_text(s, encoding='utf-8')
print('course04 screenshot layout/caption fix complete')
