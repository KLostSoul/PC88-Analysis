from pathlib import Path

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

old = '.shot{margin:20px 0;border:1px solid var(--line);border-radius:15px;overflow:visible;background:#0b0f16;box-shadow:0 6px 18px rgba(23,32,51,.08);min-width:0;max-width:100%;width:100%}.shot img{display:block;width:100%;max-width:100%;height:auto;background:#000;border-radius:14px 14px 0 0}.shot figcaption{display:block;width:100%;min-width:0;max-width:100%;height:auto!important;max-height:none!important;background:#f8faff;color:#334155;padding:13px 15px;border-top:1px solid var(--line);border-radius:0 0 14px 14px;font-size:1rem;line-height:1.65;white-space:normal!important;overflow:visible!important;text-overflow:clip!important;overflow-wrap:anywhere!important;word-break:break-word!important;-webkit-line-clamp:unset!important}.shot figcaption *{max-width:100%;white-space:normal!important;overflow-wrap:anywhere!important;word-break:break-word!important}.shot figcaption b{color:#183c98}.shots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start;grid-auto-rows:auto}.shots .shot{margin:0;min-width:0;width:100%}'
new = '.shot{margin:20px 0;border:1px solid var(--line);border-radius:15px;overflow:hidden;background:#0b0f16;box-shadow:0 6px 18px rgba(23,32,51,.08);min-width:0;max-width:100%}.shot img{display:block;width:100%;height:auto;background:#000}.shot figcaption{background:#f8faff;color:#334155;padding:13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65;min-width:0;max-width:100%;white-space:normal;overflow-wrap:anywhere;word-break:normal}.shot figcaption b{color:#183c98}.shot figcaption code{white-space:normal;overflow-wrap:anywhere;word-break:break-word}.shots{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;align-items:start}.shots .shot{margin:0;min-width:0}'

count = s.count(old)
if count != 1:
    raise SystemExit(f'expected one aggressive caption CSS block, got {count}')

s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
print('restored fixed card layout; captions wrap inside cards')
