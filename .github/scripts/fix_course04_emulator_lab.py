from pathlib import Path
import re

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

s = s.replace('<li><a href="#realpc">왜 Emulator를 쓰는가</a></li>', '<li><a href="#realpc">Emulator를 통한 실습</a></li>', 1)

new = '''<section id="realpc"><div class="kicker">에뮬레이터를 이용한 실습</div><h2>4. 이 강좌에서는 Emulator를 통해 실습한다</h2><p>실제 PC-88에도 machine-language monitor 등 프로그램을 조사하고 테스트할 수 있는 수단이 있습니다. 이 강좌에서는 실기 환경을 전제로 하지 않고, PC-88의 동작을 재현할 수 있는 Emulator에서 Debugger를 사용해 실습을 진행합니다.</p><p>따라서 이후의 breakpoint, register 확인, disassembly, memory 관찰, single-step 같은 과정은 Emulator Debugger를 통해 직접 따라갑니다. 중요한 것은 특정 Emulator 사용법을 익히는 것이 아니라, <b>PC-88 프로그램의 실행을 멈추고 상태를 관찰하며 원인을 좁혀 가는 분석 방법</b>을 익히는 것입니다.</p><div class="flow"><b>PC-88 프로그램</b><span class="arrow">→</span><b>Emulator에서 실행</b><span class="arrow">→</span><b>Debugger로 관찰</b><span class="arrow">→</span><b>분석 방법 익히기</b></div><div class="beginner"><b>이 강좌의 실습 환경:</b> 실제 PC-88에서도 분석은 가능하지만, 이후 실습은 Emulator 환경에서 진행합니다.</div></section>'''

s2, n = re.subn(r'<section\s+id="realpc">.*?</section>', new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'realpc section replacement count={n}')

p.write_text(s2, encoding='utf-8')
