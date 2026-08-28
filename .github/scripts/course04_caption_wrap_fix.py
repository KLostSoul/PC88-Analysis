from pathlib import Path

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

old = '.shot{margin:20px 0;border:1px solid var(--line);border-radius:15px;overflow:hidden;background:#0b0f16;box-shadow:0 6px 18px rgba(23,32,51,.08)}.shot img{display:block;width:100%;height:auto;background:#000}.shot figcaption{background:#f8faff;color:#334155;padding:13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65}'
new = '.shot{margin:20px 0;border:1px solid var(--line);border-radius:15px;overflow:hidden;background:#0b0f16;box-shadow:0 6px 18px rgba(23,32,51,.08);min-width:0;max-width:100%}.shot img{display:block;width:100%;height:auto;background:#000}.shot figcaption{background:#f8faff;color:#334155;padding:13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65;min-width:0;max-width:100%;white-space:normal;overflow-wrap:anywhere;word-break:normal}'

if s.count(old) != 1:
    raise SystemExit(f'caption base CSS: expected 1 match, got {s.count(old)}')
s = s.replace(old, new, 1)

old2 = '.shot figcaption b{color:#183c98}'
new2 = '.shot figcaption b{color:#183c98}.shot figcaption code{white-space:normal;overflow-wrap:anywhere;word-break:break-word}'
if s.count(old2) != 1:
    raise SystemExit(f'caption code CSS: expected 1 match, got {s.count(old2)}')
s = s.replace(old2, new2, 1)

p.write_text(s, encoding='utf-8')
print('course04 caption wrap fix complete')
