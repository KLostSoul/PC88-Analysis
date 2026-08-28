from pathlib import Path
import re

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')
new = '''<section id="realpc"><div class="kicker">실기가 없어도 같은 내용을 실습한다</div><h2>4. 실제 PC-88을 구하기 어려운 지금, 왜 Emulator를 사용하는가</h2><p>실제 PC-88에도 machine-language monitor처럼 프로그램을 조사할 수 있는 수단이 있었고, 실기를 가지고 있다면 실제 기기에서 프로그램을 실행하고 분석할 수도 있습니다. 문제는 오늘날 실제 PC-88을 보유한 사람이 많지 않고, 상태가 좋은 본체와 필요한 주변기기까지 구해 실습 환경을 마련하기도 쉽지 않다는 점입니다.</p><p>이 강좌는 실기 보유 여부와 관계없이 PC-88 게임 분석을 따라갈 수 있어야 합니다. 그래서 <b>Emulator로 PC-88의 실행 환경을 재현하고, 그 환경에서 Debugger를 사용해 분석 과정을 실습</b>합니다. Emulator를 사용하는 이유는 실기에서 분석할 수 없기 때문이 아니라, <b>실제 PC-88을 구하기 어려운 현재의 현실적인 조건에서도 같은 분석 원리를 직접 테스트할 수 있게 하기 위해서</b>입니다.</p><div class="flow"><b>PC-88 실기에서도<br>분석 가능</b><span class="arrow">→</span><b>하지만 실기 확보와<br>실습 환경 마련이 어려움</b><span class="arrow">→</span><b>Emulator로<br>PC-88 환경 재현</b><span class="arrow">→</span><b>Debugger로<br>직접 실습</b></div><div class="beginner"><b>핵심:</b> 실기가 있는 사람만 따라갈 수 있는 강좌로 만들지 않기 위해 Emulator를 사용합니다. 여기서 배우는 대상은 Emulator 자체가 아니라 PC-88 프로그램의 실행과 분석 방법입니다.</div></section>'''
s2, n = re.subn(r'<section\s+id="realpc">.*?</section>', new, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'realpc section replacement count={n}')
p.write_text(s2, encoding='utf-8')
