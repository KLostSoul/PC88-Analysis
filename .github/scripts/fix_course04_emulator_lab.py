from pathlib import Path
import re

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

s = s.replace('<li><a href="#realpc">왜 Emulator를 쓰는가</a></li>', '<li><a href="#realpc">Emulator를 이용한 실습</a></li>', 1)
s = s.replace('<li><a href="#realpc">Emulator를 통한 실습</a></li>', '<li><a href="#realpc">Emulator를 이용한 실습</a></li>', 1)

new = '''<section id="realpc"><div class="kicker">실습 환경</div><h2>4. Emulator를 이용해 PC-88 분석을 실습한다</h2><p>실제 PC-88에도 machine-language monitor 등 프로그램을 조사하고 테스트할 수 있는 수단이 있습니다. 다만 오늘날에는 PC-88 실기를 보유한 사람이 많지 않고, 새로 구해 필요한 실습 환경을 마련하기도 쉽지 않습니다. 따라서 이 강좌에서는 <b>실기 보유 여부와 관계없이 같은 분석 과정을 직접 따라갈 수 있도록 Emulator를 이용해 실습</b>합니다.</p><p>Emulator를 사용한다고 해서 실기에서의 분석을 부정하거나 다른 원리를 배우는 것은 아닙니다. PC-88의 실행 환경을 Emulator로 재현한 뒤 breakpoint, register 확인, disassembly, memory 관찰, single-step 등을 실제로 사용하면서 <b>PC-88 프로그램의 실행을 멈추고 상태를 관찰해 원인을 좁혀 가는 분석 방법</b>을 익힙니다.</p><div class="flow"><b>PC-88 분석 원리</b><span class="arrow">→</span><b>Emulator로<br>실행 환경 재현</b><span class="arrow">→</span><b>Debugger로<br>직접 실습</b><span class="arrow">→</span><b>분석 방법 익히기</b></div><div class="beginner"><b>이 강좌의 실습 방식:</b> 실제 PC-88에서도 분석할 수 있지만, 실기를 가지고 있지 않아도 강좌를 따라갈 수 있도록 이후 실습은 Emulator 환경에서 진행합니다.</div></section>'''

s2, n = re.subn(r'<section\s+id="realpc">.*?</section>', new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'realpc section replacement count={n}')

p.write_text(s2, encoding='utf-8')
