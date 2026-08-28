from pathlib import Path

# course/04.html
p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

def rep(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, got {n}')
    s = s.replace(old, new, 1)

rep(
'''<div class="beginner"><b>QUASI88 실습 준비:</b> 사용할 PC-88 게임을 실행한 뒤 DEBUG Monitor를 사용할 수 있는 상태로 준비합니다. QUASI88 0.7.4에서는 <code>-debug</code> 옵션으로 Monitor에 들어갈 수 있게 할 수 있고, <code>-monitor</code> 옵션으로 Monitor mode에서 시작할 수도 있습니다. Monitor에서 <code>?</code>를 입력해 도움말이 표시되면 이후 실습의 명령을 확인할 준비가 된 것입니다.</div>''',
'''<div class="beginner"><b>QUASI88 실습 준비:</b> QUASI88을 <code>-debug</code> 옵션으로 실행한 뒤 사용할 PC-88 게임을 구동합니다. 처음부터 Monitor mode에서 시작하려면 <code>-monitor</code> 옵션을 사용할 수도 있습니다. Monitor에서 <code>?</code>를 입력해 도움말이 표시되면 이후 실습의 명령을 확인할 준비가 된 것입니다.</div>''',
'section6 launch order')

rep(
'''<section id="runstop"><div class="kicker">관찰 가능한 순간</div><h2>8. 실행 중에는 상태가 계속 바뀌고, 멈춘 뒤에야 한 순간을 조사할 수 있다</h2><p><code>g</code>로 실행을 계속하면 게임이 움직입니다. Breakpoint가 발생하면 Monitor로 돌아오며 해당 CPU의 register 상태와 PC 주변 instruction이 자동으로 표시됩니다.</p><div class="beginner"><b>중요:</b> Breakpoint에 걸린 직후에는 기본 CPU 상태가 이미 출력되므로 항상 <code>reg</code>부터 다시 입력할 필요는 없습니다.</div></section>''',
'''<section id="runstop"><div class="kicker">관찰 가능한 순간</div><h2>8. 실행 중에는 상태가 계속 바뀌고, 멈춘 뒤에야 한 순간을 조사할 수 있다</h2><p>프로그램을 계속 실행하면 CPU 상태는 계속 변합니다. 분석하려는 사건에서 실행을 멈춘 뒤 그 순간의 PC와 register, 주변 code를 조사합니다.</p><div class="note"><b>QUASI88 예제:</b> <code>g</code>로 실행을 계속하며, breakpoint에 걸리면 Monitor로 돌아와 해당 CPU의 register 상태와 PC 주변 instruction이 자동으로 표시됩니다.</div><div class="beginner"><b>중요:</b> QUASI88에서는 breakpoint에 걸린 직후 기본 CPU 상태가 이미 출력되므로 항상 <code>reg</code>부터 다시 입력할 필요는 없습니다. 다른 emulator의 화면 표시 방식은 다를 수 있습니다.</div></section>''',
'section8 quasi scope')

rep(
'''<tr><td><code>break CLEARALL #0</code></td><td class="left">앞서 설정된 breakpoint를 모두 지우고 이번 실습 조건부터 다시 시작합니다.</td></tr>''',
'''<tr><td><code>break CLEARALL #0</code></td><td class="left">앞서 설정된 breakpoint를 모두 지우고 이번 실습 조건부터 다시 시작합니다. 여기서 <code>#0</code>은 일반 breakpoint 번호가 아니라 CLEARALL 실행을 확인하기 위한 형식입니다.</td></tr>''',
'clearall number explanation')

rep(
'''<section id="io"><div class="kicker">Memory 밖의 사건</div><h2>21. PC-88에서는 I/O Port 접근도 중요한 사건이 될 수 있다</h2><p>Z80의 <code>IN</code>, <code>OUT</code>은 memory가 아니라 I/O port와 데이터를 주고받습니다. 키 입력, sound, disk subsystem 등 hardware와 연결된 처리를 조사할 때 I/O instruction이 단서가 됩니다.</p><pre>IN  A,(10h)    ; I/O port 10h의 값 → A\nOUT (10h),A    ; A의 값 → I/O port 10h</pre>''',
'''<section id="io"><div class="kicker">Memory 밖의 사건</div><h2>21. PC-88에서는 I/O Port 접근도 중요한 사건이 될 수 있다</h2><p>Z80의 <code>IN</code>, <code>OUT</code>은 memory가 아니라 I/O port와 데이터를 주고받습니다. 키 입력, sound, disk subsystem 등 hardware와 연결된 처리를 조사할 때 I/O instruction이 단서가 됩니다.</p><div class="note"><b>아래 예는 I/O port의 실제 용도를 설명하는 것이 아니라 IN/OUT의 데이터 방향만 보여 주기 위한 가상 예입니다.</b></div><pre>IN  A,(10h)    ; I/O port 10h의 값 → A\nOUT (10h),A    ; A의 값 → I/O port 10h</pre>''',
'section21 example disclaimer')

p.write_text(s, encoding='utf-8')

# README.md
r = Path('README.md')
t = r.read_text(encoding='utf-8')
old = '''PC-88 에뮬레이터마다 debugger 기능과 조작법은 다를 수 있으므로 강좌의 개념을 특정 프로그램에 고정하지 않습니다. 실제 PC-88에서 같은 동적 분석 환경을 재현하기 쉽지 않기 때문에 **QUASI88 0.7.4의 Monitor를 대표 실습 예시**로 사용합니다.'''
new = '''PC-88 에뮬레이터마다 debugger 기능과 조작법은 다를 수 있으므로 강좌의 개념을 특정 프로그램에 고정하지 않습니다. 실제 PC-88에도 프로그램을 조사하고 디버깅하기 위한 수단은 있지만, 오늘날 실기를 보유하지 않은 사람도 많고 새로 실습 환경을 마련하기 쉽지 않으므로 **이 강좌에서는 QUASI88 0.7.4의 Monitor를 대표 실습 예시로 사용합니다.**'''
if t.count(old) != 1:
    raise SystemExit(f'README wording: expected 1 match, got {t.count(old)}')
t = t.replace(old, new, 1)
r.write_text(t, encoding='utf-8')

print('final course04 fixes complete')
