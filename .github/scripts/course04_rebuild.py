from pathlib import Path
import re

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

pat = r'<section\b(?=[^>]*\bid="runstop")[^>]*>.*?</section>'
new = '''<section id="runstop"><div class="kicker">관찰 가능한 순간</div><h2>8. 실행 중에는 상태가 계속 바뀌고, 멈춘 뒤에야 한 순간을 조사할 수 있다</h2><p>CPU가 계속 실행되는 동안 PC와 register, memory 상태도 계속 바뀝니다. Debugger로 필요한 사건에서 실행을 멈추면 그 순간의 상태를 고정해서 차분히 조사할 수 있습니다.</p><div class="note"><b>QUASI88 예제:</b> <code>g</code>로 실행을 계속하고 breakpoint가 발생하면 Monitor로 돌아옵니다. 이때 QUASI88은 해당 CPU의 register 상태와 PC 주변 instruction을 자동으로 표시하므로 항상 <code>reg</code>부터 다시 입력할 필요는 없습니다.</div></section>'''
s, n = re.subn(pat, new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'runstop replacement: {n}')

old = '<div class="warn"><b>현재 PC만 보고 판단하지 마십시오.</b> memory access breakpoint는 접근이 일어난 뒤 debugger로 돌아오는 구현이 많아 현재 PC가 다음 instruction을 가리킬 수 있습니다. Break 메시지의 access 주소와 주변 disassembly를 함께 봅니다.</div>'
new = '<div class="warn"><b>현재 PC만 보고 판단하지 마십시오.</b> Debugger에 따라 memory access 뒤에 정지하여 현재 PC가 다음 instruction을 가리킬 수 있습니다. 이 QUASI88 예에서도 실제 READ는 <code>C0A5 LD A,(HL)</code>에서 일어났고 정지 후 PC는 C0A6입니다. Break 메시지의 access 주소와 주변 disassembly를 함께 봅니다.</div>'
if old not in s:
    raise SystemExit('read warning marker not found')
s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')

rp = Path('README.md')
r = rp.read_text(encoding='utf-8')
r = r.replace('강좌의 스크린샷은 debugger 사용과 실행 흐름 설명을 위한 교육용 예시로 사용합니다.', '강좌의 실행 화면은 debugger 사용과 실행 흐름 설명을 위한 교육용 예시로 사용합니다.')
rp.write_text(r, encoding='utf-8')
