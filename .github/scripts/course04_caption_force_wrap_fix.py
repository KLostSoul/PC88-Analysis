from pathlib import Path

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

old = '.shot figcaption{background:#f8faff;color:#334155;padding:13px 28px 13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65;min-width:0;max-width:100%;white-space:normal!important;overflow-wrap:break-word!important;word-break:keep-all!important}.shot figcaption b{color:#183c98}.shot figcaption code{white-space:normal!important;overflow-wrap:anywhere!important;word-break:break-all!important}'
new = '.shot figcaption{background:#f8faff;color:#334155;padding:13px 36px 13px 15px;border-top:1px solid var(--line);font-size:1rem;line-height:1.65;min-width:0;max-width:100%;box-sizing:border-box!important;white-space:normal!important;overflow-wrap:anywhere!important;word-break:break-all!important;line-break:anywhere}.shot figcaption,.shot figcaption *{white-space:normal!important;overflow-wrap:anywhere!important;word-break:break-all!important}.shot figcaption b{color:#183c98}'

count = s.count(old)
if count != 1:
    raise SystemExit(f'expected one caption CSS block, got {count}')

s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
print('force-wrap captions before the right edge without changing card width')
