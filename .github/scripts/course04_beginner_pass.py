from pathlib import Path

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')


def rep(old, new, label):
    global s
    n = s.count(old)
    if n != 1:
        raise SystemExit(f'{label}: expected 1 match, got {n}')
    s = s.replace(old, new, 1)

# 6. 실습 준비: QUASI88 고유 조작은 예제 박스로만 둔다.
old = '''<div class="note"><b>중요:</b> 다른 emulator에서는 명령 이름과 조작법이 달라질 수 있습니다. 이후 예제를 볼 때도 먼저 “이 명령이 어떤 분석 기능을 구현하는가”를 봅니다.</div></section>'''
new = '''<div class="note"><b>중요:</b> 다른 emulator에서는 명령 이름과 조작법이 달라질 수 있습니다. 이후 예제를 볼 때도 먼저 “이 명령이 어떤 분석 기능을 구현하는가”를 봅니다.</div><div class="beginner"><b>QUASI88 실습 준비:</b> 사용할 PC-88 게임을 실행한 뒤 DEBUG Monitor를 사용할 수 있는 상태로 준비합니다. QUASI88 0.7.4에서는 <code>-debug</code> 옵션으로 Monitor에 들어갈 수 있게 할 수 있고, <code>-monitor</code> 옵션으로 Monitor mode에서 시작할 수도 있습니다. Monitor에서 <code>?</code>를 입력해 도움말이 표시되면 이후 실습의 명령을 확인할 준비가 된 것입니다.</div></section>'''
rep(old, new, 'section6 prep')

# 10. register를 주소 전용처럼 보이게 하지 않는다.
old = '''<div class="grid2"><div class="card"><h3>주소로 자주 보는 값</h3><p>PC, SP, HL, DE, BC</p></div><div class="card"><h3>작업값·조건으로 보는 값</h3><p>A와 flag register F</p></div></div>'''
new = '''<div class="grid2"><div class="card"><h3>역할이 비교적 분명한 Register</h3><p><b>PC</b>는 실행 위치, <b>SP</b>는 stack 위치를 가리킵니다. <b>A</b>는 연산과 data 처리에 자주 쓰이고, <b>F</b>는 조건 판단에 쓰이는 flag를 담습니다.</p></div><div class="card"><h3>현재 Code를 보고 역할을 판단할 Register</h3><p><b>HL·DE·BC</b> 등은 상황에 따라 주소·pointer·counter·일반 값으로 모두 쓰일 수 있습니다. 이름만 보고 용도를 정하지 말고 현재 instruction에서 어떻게 사용되는지 확인합니다.</p></div></div>'''
rep(old, new, 'section10 registers')

# 13. Watchpoint 용어 설명.
old = '''</table><div class="lab"><h3>Lab — 질문에 맞는 Breakpoint 고르기</h3>'''
new = '''</table><div class="note"><b>용어:</b> emulator나 debugger에 따라 memory의 읽기·쓰기를 감시하는 기능을 <b>Read/Write Breakpoint</b> 또는 <b>Watchpoint</b>라고 부를 수 있습니다. 이름이 달라도 “특정 memory access가 일어나는 순간을 잡는다”는 목적은 같습니다.</div><div class="lab"><h3>Lab — 질문에 맞는 Breakpoint 고르기</h3>'''
rep(old, new, 'section13 watchpoint')

# 14. 16진수 표기와 QUASI88 breakpoint 명령을 처음 한 번 해독한다.
old = '''<p>routine이 실제로 호출되는지, 특정 instruction까지 CPU가 도달하는지를 알고 싶다면 <b>그 주소가 실행 위치가 되는 순간</b>에 멈춥니다. 많은 debugger에서 Execution Breakpoint 또는 PC Breakpoint라고 부르는 기능입니다.</p><div class="note"><b>QUASI88 예제</b><pre>break CLEARALL #0\nbreak pc 0xC0A2 #1\ng</pre></div>'''
new = '''<p>routine이 실제로 호출되는지, 특정 instruction까지 CPU가 도달하는지를 알고 싶다면 <b>그 주소가 실행 위치가 되는 순간</b>에 멈춥니다. 많은 debugger에서 Execution Breakpoint 또는 PC Breakpoint라고 부르는 기능입니다.</p><div class="beginner"><b>16진수 표기:</b> 이 강좌의 <code>0xC0A2</code>, <code>C0A2h</code>, Monitor에 표시되는 <code>C0A2H</code>는 모두 같은 16진수 주소입니다. 표기 방식만 다릅니다.</div><div class="note"><b>QUASI88 예제</b><pre>break CLEARALL #0\nbreak pc 0xC0A2 #1\ng</pre></div><table><tr><th>명령의 부분</th><th>뜻</th></tr><tr><td><code>break CLEARALL #0</code></td><td class="left">앞서 설정된 breakpoint를 모두 지우고 이번 실습 조건부터 다시 시작합니다.</td></tr><tr><td><code>break pc</code></td><td class="left">CPU의 실행 위치(PC)를 기준으로 breakpoint를 설정합니다.</td></tr><tr><td><code>0xC0A2</code></td><td class="left">멈추고 싶은 대상 주소입니다.</td></tr><tr><td><code>#1</code></td><td class="left">이 breakpoint에 사용하는 번호입니다.</td></tr><tr><td><code>g</code></td><td class="left">설정을 마친 뒤 프로그램 실행을 계속합니다.</td></tr></table>'''
rep(old, new, 'section14 command decode')

# 15. QUASI88 사례와 일반 debugger를 분리한다.
old = '''<div class="warn"><b>현재 PC만 보고 판단하지 마십시오.</b> memory access breakpoint는 접근이 일어난 뒤 debugger로 돌아오는 구현이 많아 현재 PC가 다음 instruction을 가리킬 수 있습니다. Break 메시지의 access 주소와 주변 disassembly를 함께 봅니다.</div>'''
new = '''<div class="warn"><b>현재 PC만 보고 판단하지 마십시오.</b> 이 QUASI88 예제에서는 memory read가 일어난 뒤 Monitor로 돌아오므로 현재 PC가 다음 instruction을 가리킵니다. 다른 debugger의 정지 시점과 화면 표시는 구현에 따라 다를 수 있습니다. 따라서 Break 메시지의 access 주소와 현재 PC 주변 disassembly를 함께 확인합니다.</div>'''
rep(old, new, 'section15 timing')

# 16. 실행 위치 BP와 memory access BP 화면을 초보자가 비교할 수 있게 한다.
old = '''<div class="beginner"><b>READ와 WRITE의 차이:</b> <b>사용하는 code</b>를 찾고 싶으면 READ, <b>바꾼 code</b>를 찾고 싶으면 WRITE입니다.</div></section>'''
new = '''<div class="beginner"><b>READ와 WRITE의 차이:</b> <b>사용하는 code</b>를 찾고 싶으면 READ, <b>바꾼 code</b>를 찾고 싶으면 WRITE입니다.</div><table><tr><th>잡은 사건</th><th>정지 화면에서 먼저 볼 것</th></tr><tr><td>Execution / PC Breakpoint</td><td class="left">지정한 실행 위치와 현재 PC가 일치하는지 확인합니다.</td></tr><tr><td>READ / WRITE Breakpoint</td><td class="left">실제 access 주소·값을 확인하고, 현재 PC와 바로 앞을 포함한 주변 instruction에서 access를 일으킨 code를 찾습니다.</td></tr></table><div class="note">Memory access breakpoint가 정확히 어느 시점에 debugger로 제어를 넘기는지는 emulator마다 다를 수 있습니다. 따라서 “현재 PC가 곧 access instruction”이라고 가정하지 않는 습관이 중요합니다.</div></section>'''
rep(old, new, 'section16 breakpoint compare')

# 18. Caller/Callee 용어를 사용 전에 정의한다.
old = '''<p>세 기능은 명령 이름보다 <b>호출된 routine을 지금 얼마나 자세히 볼 것인가</b>를 기준으로 구분합니다.</p><table>'''
new = '''<p>세 기능은 명령 이름보다 <b>호출된 routine을 지금 얼마나 자세히 볼 것인가</b>를 기준으로 구분합니다.</p><div class="note"><b>용어:</b> <b>Caller</b>는 다른 routine을 호출한 쪽, <b>Callee</b>는 호출되어 실행되는 routine을 뜻합니다. 예를 들어 <code>CALL C232H</code>를 실행한 code가 caller이고 C232h에서 시작하는 routine이 callee입니다.</div><table>'''
rep(old, new, 'section18 caller callee')

# 20. 제목에 있는 Loop를 실제 예로 설명한다.
old = '''</div></div><div class="note">앞의 실제 실행에서도 첫 한 단계 실행은 <code>C143 JR NZ,C13D</code>의 조건을 따라 C13Dh로 이동했고, 그 다음에 CALL을 관찰했습니다.</div>'''
new = '''</div></div><h3>Loop도 같은 방법으로 본다</h3><p>Loop는 조건분기가 여러 번 반복되는 경우입니다. 예를 들어 counter가 줄어들 때는 <b>현재 counter 값과 flag가 반복 여부를 어떻게 바꾸는지</b> 확인합니다.</p><pre>B = 03\nLOOP: DEC B        ; 03 → 02, Z=0\n      JR NZ,LOOP   ; NZ 성립 → 다시 반복\n      ...\nB = 01\n      DEC B        ; 01 → 00, Z=1\n      JR NZ,LOOP   ; NZ 불성립 → Loop 종료</pre><div class="note">앞의 실제 실행에서도 첫 한 단계 실행은 <code>C143 JR NZ,C13D</code>의 조건을 따라 C13Dh로 이동했고, 그 다음에 CALL을 관찰했습니다.</div>'''
rep(old, new, 'section20 loop')

# 21. IN/OUT 방향을 초보자가 바로 읽을 수 있게 한다.
old = '''<p>Z80의 <code>IN</code>, <code>OUT</code>은 memory가 아니라 I/O port와 데이터를 주고받습니다. 키 입력, sound, disk subsystem 등 hardware와 연결된 처리를 조사할 때 I/O instruction이 단서가 됩니다.</p><div class="warn">'''
new = '''<p>Z80의 <code>IN</code>, <code>OUT</code>은 memory가 아니라 I/O port와 데이터를 주고받습니다. 키 입력, sound, disk subsystem 등 hardware와 연결된 처리를 조사할 때 I/O instruction이 단서가 됩니다.</p><pre>IN  A,(10h)    ; I/O port 10h의 값 → A\nOUT (10h),A    ; A의 값 → I/O port 10h</pre><p><code>LD A,(9000h)</code>처럼 memory를 읽는 것과 <code>IN A,(10h)</code>처럼 port를 읽는 것은 서로 다른 종류의 access입니다. Disassembly에서 <code>IN</code>이나 <code>OUT</code>을 만나면 memory 주소가 아니라 I/O port를 보고 있다는 점부터 구분합니다.</p><div class="warn">'''
rep(old, new, 'section21 io basics')

# 종합 Lab의 memory access 설명도 특정 구현의 동작처럼 일반화하지 않는다.
old = '''ok:'Memory access 뒤에 정지했다면 현재 PC와 함께 바로 앞을 포함한 주변 code를 봐야 합니다.'}'''
new = '''ok:'이 예처럼 현재 PC가 access instruction 다음을 가리킨다면, 현재 PC만 보지 말고 바로 앞을 포함한 주변 code를 함께 봐야 합니다.'}'''
rep(old, new, 'final lab timing')

p.write_text(s, encoding='utf-8')
print('course04 beginner pass complete')
