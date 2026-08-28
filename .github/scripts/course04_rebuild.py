from pathlib import Path
import re

p = Path('course/04.html')
s = p.read_text(encoding='utf-8')

def sec(section_id, html):
    global s
    pat = rf'<section\b(?=[^>]*\bid="{re.escape(section_id)}")[^>]*>.*?</section>'
    s2, n = re.subn(pat, html.strip(), s, count=1, flags=re.S)
    if n != 1:
        raise SystemExit(f'section {section_id}: {n}')
    s = s2

old = '.btn.active,.btn.correct{background:#3157d5;color:#fff;border-color:#3157d5}.btn:disabled{opacity:.55;cursor:not-allowed}'
new = '.btn.active{background:#3157d5;color:#fff;border-color:#3157d5}.btn.correct{background:var(--ok);color:#fff;border-color:var(--ok)}.btn:disabled{opacity:.55;cursor:not-allowed}.btn.correct:disabled{opacity:1}'
if old not in s:
    raise SystemExit('button css marker not found')
s = s.replace(old, new, 1)

s = s.replace('<li><a href="#emulators">특정 Emulator에 고정하지 않기</a></li>', '<li><a href="#emulators">Emulator가 달라도 분석 목적은 같다</a></li>')
s = s.replace('<li><a href="#quasi88">QUASI88을 예시로 쓰는 이유</a></li>', '<li><a href="#quasi88">실제 예제로 QUASI88 사용하기</a></li>')
s = s.replace('<li><a href="#pcbreak">PC Breakpoint</a></li>', '<li><a href="#pcbreak">실행 위치 Breakpoint</a></li>')
s = s.replace('<li><a href="#final-lab">종합 실습</a></li><li><a href="#quiz">확인 문제</a></li>', '<li><a href="#final-lab">종합 실습</a></li><li><a href="#summary">핵심 정리</a></li><li><a href="#quiz">확인 문제</a></li><li><a href="#next-part">5부로 이어가기</a></li>')

sec('emulators', '''
<section id="emulators"><div class="kicker">도구보다 질문이 먼저다</div><h2>5. Emulator가 달라도 분석 목적은 같다</h2><p>PC-88 emulator마다 debugger의 화면 구성과 명령 이름은 다를 수 있습니다. 하지만 분석할 때 던지는 질문과 필요한 기능은 크게 달라지지 않습니다.</p><table><tr><th>알고 싶은 것</th><th>일반적인 Debugger 기능</th></tr><tr><td class="left">특정 code가 실행되는 순간은 언제인가?</td><td>Execution / PC Breakpoint</td></tr><tr><td class="left">이 data를 어느 code가 읽는가?</td><td>Read Breakpoint / Watchpoint</td></tr><tr><td class="left">이 값을 어느 code가 바꾸는가?</td><td>Write Breakpoint / Watchpoint</td></tr><tr><td class="left">지금 CPU는 어디에서 무엇을 실행하는가?</td><td>PC / Register / Disassembly</td></tr><tr><td class="left">이 주소에 실제로 어떤 byte가 있는가?</td><td>Memory View / Dump</td></tr><tr><td class="left">instruction 하나가 무엇을 바꾸는가?</td><td>Single-step</td></tr></table><div class="why"><b>강좌의 기준:</b> 명령 이름을 먼저 외우지 않습니다. <b>무엇을 알고 싶은가 → 어떤 기능이 필요한가 → 결과에서 무엇을 읽을 것인가</b> 순서로 생각합니다.</div></section>
''')

sec('quasi88', '''
<section id="quasi88"><div class="kicker">공통 원리를 실제 화면에서 확인한다</div><h2>6. 이 강좌에서는 실제 조작 예제로 QUASI88을 사용한다</h2><p>이후의 화면과 명령 입력 예시는 QUASI88 0.7.4 Monitor를 사용합니다. <b>배우는 대상은 QUASI88 자체가 아니라 앞 절에서 정리한 공통 debugger 기능</b>이며, QUASI88은 그 기능을 실제 PC-88 게임에서 확인하기 위한 예제입니다.</p><figure class="shot"><img src="../images/course04/01.png" alt="QUASI88 본체와 Monitor 전체 실습 환경"><figcaption>오른쪽은 PC-88 게임이 실행되는 본체 화면, 왼쪽은 실행 상태를 조사하는 Monitor입니다. 이후에는 같은 화면을 보며 PC·register·code·memory와 breakpoint 동작을 확인합니다.</figcaption></figure><table><tr><th>공통 기능</th><th>QUASI88에서 사용하는 예</th></tr><tr><td>계속 실행</td><td><code>g</code></td></tr><tr><td>CPU 상태 확인</td><td>Breakpoint 정지 시 자동 표시 / <code>reg</code></td></tr><tr><td>Code 확인</td><td><code>disasm</code></td></tr><tr><td>Memory 확인</td><td><code>dump</code></td></tr><tr><td>관심 사건에서 정지</td><td><code>break ...</code></td></tr><tr><td>한 단계 실행</td><td><code>trace</code>, <code>step</code></td></tr></table><div class="note"><b>중요:</b> 다른 emulator에서는 명령 이름과 조작법이 달라질 수 있습니다. 이후 예제를 볼 때도 먼저 “이 명령이 어떤 분석 기능을 구현하는가”를 봅니다.</div></section>
''')

sec('breakpoint', '''
<section id="breakpoint"><div class="kicker">관찰할 사건을 고른다</div><h2>13. Breakpoint는 주소를 외우는 기능이 아니라 관심 있는 사건을 잡는 기능이다</h2><p>먼저 <b>어떤 일이 일어나는 순간을 보고 싶은지</b> 정합니다. 그 질문에 따라 필요한 breakpoint의 종류가 달라집니다.</p><table><tr><th>질문</th><th>필요한 기능</th></tr><tr><td class="left">이 routine 또는 instruction이 언제 실행되는가?</td><td>Execution / PC Breakpoint</td></tr><tr><td class="left">이 data를 어느 code가 읽는가?</td><td>Read Breakpoint / Watchpoint</td></tr><tr><td class="left">이 값을 어느 code가 바꾸는가?</td><td>Write Breakpoint / Watchpoint</td></tr></table><div class="lab"><h3>Lab — 질문에 맞는 Breakpoint 고르기</h3><div id="bpq" class="readout"></div><div class="controls"><button class="btn" data-bp="pc">실행 위치 (PC)</button><button class="btn" data-bp="read">읽기 (READ)</button><button class="btn" data-bp="write">쓰기 (WRITE)</button><button class="btn" id="bpnext">다음</button></div><div id="bpr" class="readout">질문을 읽고 먼저 잡아야 할 사건을 고릅니다.</div></div><div class="beginner"><b>핵심:</b> “어디에 breakpoint를 걸까?”보다 먼저 “무슨 사건이 일어나는 순간을 보고 싶은가?”를 묻습니다.</div></section>
''')

sec('pcbreak', '''
<section id="pcbreak"><div class="kicker">실행 시점을 잡는다</div><h2>14. 특정 Code가 실행되는 순간을 보고 싶다면 실행 위치를 잡는다</h2><p>routine이 실제로 호출되는지, 특정 instruction까지 CPU가 도달하는지를 알고 싶다면 <b>그 주소가 실행 위치가 되는 순간</b>에 멈춥니다. 많은 debugger에서 Execution Breakpoint 또는 PC Breakpoint라고 부르는 기능입니다.</p><div class="note"><b>QUASI88 예제</b><pre>break CLEARALL #0
break pc 0xC0A2 #1
g</pre></div><figure class="shot"><img src="../images/course04/08.PNG" alt="C0A2 실행 위치 breakpoint" loading="lazy"><figcaption>C0A2h를 실행 위치로 지정한 뒤 게임을 계속 실행하자 PC=C0A2에서 멈췄습니다. 이제 이 시점의 register와 주변 code를 조사할 수 있습니다.</figcaption></figure><div class="why"><b>이 기능이 답하는 질문:</b> “이 code가 실제로 실행되는가?”, “언제 이 위치에 도달하는가?”</div></section>
''')

sec('readbreak', '''
<section id="readbreak"><div class="kicker">누가 읽는가</div><h2>15. 이 Data를 어느 Code가 사용하는지 알고 싶다면 읽기 사건을 잡는다</h2><p>값이 저장된 memory 주소를 알고 있을 때, 그 값을 <b>어느 code가 읽어 가는지</b> 찾고 싶다면 Read Breakpoint 또는 Read Watchpoint를 사용합니다.</p><div class="note"><b>QUASI88 예제</b><pre>break CLEARALL #0
break read 0xD9A5 #1
g</pre></div><figure class="shot"><img src="../images/course04/09.PNG" alt="D9A5 READ breakpoint" loading="lazy"><figcaption>Break 메시지의 <code>READ addr=D9A5H, data=8EH</code>에서 실제로 읽힌 주소와 값을 확인할 수 있습니다. 정지 뒤 PC는 C0A6을 가리키지만 바로 앞 <code>C0A5 LD A,(HL)</code>가 D9A5h를 읽었습니다.</figcaption></figure><div class="warn"><b>현재 PC만 보고 판단하지 마십시오.</b> memory access breakpoint는 접근이 일어난 뒤 debugger로 돌아오는 구현이 많아 현재 PC가 다음 instruction을 가리킬 수 있습니다. Break 메시지의 access 주소와 주변 disassembly를 함께 봅니다.</div><div class="note"><b>QUASI88에서의 추가 주의:</b> READ breakpoint는 instruction fetch와도 연결될 수 있습니다. code가 놓인 주소를 READ로 감시할 때는 data read인지 instruction fetch인지 주변 code와 함께 구분합니다.</div></section>
''')

sec('writebreak', '''
<section id="writebreak"><div class="kicker">누가 바꾸는가</div><h2>16. 이 값이 왜 바뀌었는지 알고 싶다면 쓰기 사건을 잡는다</h2><p>memory의 값이 예상과 다르게 변했다면 <b>그 주소에 값을 쓴 code</b>를 찾는 것이 가장 직접적입니다. 이때 Write Breakpoint 또는 Write Watchpoint를 사용합니다.</p><div class="note"><b>QUASI88 예제</b><pre>break CLEARALL #0
break write 0xC0A2 #1
g</pre></div><figure class="shot"><img src="../images/course04/10.PNG" alt="C0A2 WRITE breakpoint" loading="lazy"><figcaption>C0A2h에 write가 발생했을 때 멈춘 화면입니다. HL=C0A2h, A=00h이고 바로 앞 <code>87AD LD (HL),A</code>가 실제로 값을 쓴 instruction입니다. 정지 후 PC는 다음 <code>87AE INC HL</code>을 가리킵니다.</figcaption></figure><div class="beginner"><b>READ와 WRITE의 차이:</b> <b>사용하는 code</b>를 찾고 싶으면 READ, <b>바꾼 code</b>를 찾고 싶으면 WRITE입니다.</div></section>
''')

sec('stepmodes', '''
<section id="stepmodes"><div class="kicker">호출을 어떻게 볼 것인가</div><h2>18. Step Into · Step Over · Step Out은 조사 목적이 다르다</h2><p>세 기능은 명령 이름보다 <b>호출된 routine을 지금 얼마나 자세히 볼 것인가</b>를 기준으로 구분합니다.</p><table><tr><th>개념</th><th>언제 쓰는가</th></tr><tr><td>Step Into</td><td class="left">CALL 내부 routine 자체가 원인인지 조사하고 싶다.</td></tr><tr><td>Step Over</td><td class="left">CALL 내부는 지금 중요하지 않고, 호출이 끝난 뒤 caller의 다음 code부터 보고 싶다.</td></tr><tr><td>Step Out</td><td class="left">현재 routine의 조사를 끝내고 caller로 돌아가고 싶다.</td></tr></table><figure class="shot"><img src="../images/course04/12.PNG" alt="CALL 내부로 들어가는 실제 실행" loading="lazy"><figcaption><code>C0CE CALL 085BH</code>에서 호출 내부로 들어가자 PC가 085Bh로 이동했습니다. 이것이 Step Into에서 관찰하려는 동작입니다.</figcaption></figure><div class="note"><b>QUASI88 0.7.4에서는:</b> <code>trace</code>가 Step Into에 해당하고, <code>step</code>은 CALL/RST에서 Step Over 동작을 합니다. <code>return</code>은 Step Out 용도로 제공되지만 experimental 기능으로 표시되어 있어 이번 강좌의 핵심 실습에는 사용하지 않습니다.</div><div class="note"><b>참고:</b> QUASI88에는 CALL/RST 외에 DJNZ·반복 block instruction·HALT 등도 더 넓게 건너뛰는 <code>next</code>가 있지만 4부에서는 별도 실습하지 않습니다.</div></section>
''')

sec('callret', '''
<section id="callret"><div class="kicker">Caller와 Callee를 구분한다</div><h2>19. CALL과 RET를 따라가면 호출과 복귀 관계를 실제 실행으로 확인할 수 있다</h2><p>CALL은 다른 routine으로 실행 위치를 옮기고, RET는 caller의 다음 instruction으로 돌아옵니다. 내부 routine이 중요한지에 따라 Step Into와 Step Over를 선택합니다.</p><pre>Caller
C13D  CALL C232H
        │
        ├─ Step Into → C232H 내부를 직접 조사
        │
        └─ Step Over → C232H 내부 실행
                         ...
                       C256 RET
                         ↓
Caller
C140  DEC BC        ← 호출이 끝난 뒤 다시 관찰</pre><figure class="shot"><img src="../images/course04/13.PNG" alt="C13D CALL C232 step over" loading="lazy"><figcaption>실제 예에서는 먼저 조건분기를 따라 C13Dh에 도달한 뒤, <code>C13D CALL C232H</code>에서 호출 내부를 건너뛰어 caller의 다음 주소 C140h에서 다시 관찰했습니다.</figcaption></figure><div class="why"><b>판단 기준:</b> 호출 내부가 원인 후보라면 Step Into, 이미 역할을 알고 있거나 지금 관심 밖이라면 Step Over를 사용합니다.</div></section>
''')

sec('branchloop', '''
<section id="branchloop"><div class="kicker">가능한 경로보다 실제 경로</div><h2>20. 조건분기와 Loop에서는 이번 실행에서 실제 선택된 경로를 확인한다</h2><p>Disassembly만 보면 조건분기의 여러 경로가 보입니다. 동적 분석에서는 <b>현재 flag와 register 값</b>을 이용해 이번 실행에서 어느 경로가 실제로 선택됐는지 확인합니다.</p><div class="grid2"><div class="card"><h3>정적으로 볼 때</h3><pre>JR NZ,C13D
; 분기할 수도 있고
; 다음으로 갈 수도 있음</pre></div><div class="card"><h3>실행 중에 볼 때</h3><pre>Z = 0
JR NZ,C13D
→ NZ 조건 성립
→ PC = C13D</pre></div></div><div class="note">앞의 실제 실행에서도 첫 한 단계 실행은 <code>C143 JR NZ,C13D</code>의 조건을 따라 C13Dh로 이동했고, 그 다음에 CALL을 관찰했습니다.</div><div class="beginner"><b>핵심:</b> 가능한 경로를 머릿속으로만 추측하지 말고 현재 flag·counter·pointer 값을 보고 <b>이번 실행에서 실제로 간 경로</b>를 기록합니다.</div></section>
''')

sec('dual', '''
<section id="dual"><div class="kicker">PC-88의 두 CPU 환경</div><h2>22. 지금 보고 있는 Code가 MAIN CPU인지 SUB CPU인지 확인해야 할 때가 있다</h2><p>PC-88의 대표적인 FDD 구성에서는 MAIN CPU와 disk 처리를 담당하는 SUB CPU가 따로 동작합니다. 따라서 같은 숫자의 PC address가 보여도 <b>어느 CPU의 address space를 보고 있는지</b> 먼저 구분해야 합니다.</p><figure class="shot"><img src="../images/course04/14.PNG" alt="SUB CPU 상태가 표시된 Monitor" loading="lazy"><figcaption><code>[SUB]</code>와 <code>PC:76C3</code>가 현재 관찰 대상이 SUB CPU임을 보여 줍니다. 이 화면의 목적은 특정 port의 의미를 분석하는 것이 아니라 <b>현재 어느 CPU를 보고 있는지 구분하는 법</b>을 확인하는 것입니다.</figcaption></figure><div class="note"><b>QUASI88 예제:</b> CPU 전환 시점을 관찰할 때 <code>change</code>를 사용할 수 있으며, 이 명령은 <code>-cpu 0</code> 설정에서 동작합니다. 다른 emulator에서는 CPU 선택·전환 방식이 다를 수 있습니다.</div></section>
''')

sec('workflow', '''
<section id="workflow"><div class="kicker">정지 후 반복할 관찰 순서</div><h2>23. 처음 멈췄을 때는 같은 순서로 보면 중요한 단서를 놓치기 어렵다</h2><div class="steps"><div class="step"><b>1. 어느 CPU인지 확인한다.</b> MAIN/SUB처럼 실행 주체가 둘 이상이면 먼저 대상을 확정합니다.</div><div class="step"><b>2. PC를 확인한다.</b> CPU가 지금 어느 code 위치에 멈췄는지 찾습니다.</div><div class="step"><b>3. 현재와 주변 disassembly를 본다.</b> 어디에서 왔고, 지금 무엇을 하며, 다음 어디로 갈 수 있는지 봅니다.</div><div class="step"><b>4. 중요한 register를 code와 연결한다.</b> 단순 값인지, counter인지, memory를 가리키는 pointer인지 판단합니다.</div><div class="step"><b>5. 필요한 memory를 확인한다.</b> pointer가 가리키는 실제 byte와 주변 data를 봅니다.</div><div class="step"><b>6. 조건분기라면 flag와 조건값을 본다.</b> 이번 실행에서 실제 선택될 경로를 판단합니다.</div><div class="step"><b>7. 필요한 경우 한 instruction만 실행한다.</b> 전후 PC·register·memory 상태의 변화를 비교합니다.</div><div class="step"><b>8. 다음 질문에 맞는 breakpoint를 고른다.</b> 실행 위치·READ·WRITE 중 다음 단서를 가장 직접적으로 줄 기능을 선택합니다.</div></div><div class="wrong"><b>Debugger는 처음부터 끝까지 전부 step하는 도구가 아닙니다.</b> 관심 없는 구간은 실행하고, 중요한 사건을 breakpoint로 잡은 뒤 필요한 몇 instruction만 자세히 봅니다.</div></section>
''')

sec('final-lab', '''
<section class="em" id="final-lab"><div class="kicker">종합 Lab</div><h2>24. 명령 이름이 아니라 무엇을 알고 싶은지에서 출발한다</h2><p>앞의 여러 실습에서 배운 관찰 방법을 하나의 분석 절차로 묶어 봅니다. 아래 Lab은 특정 emulator 명령을 맞히는 문제가 아니라 <b>상황에 맞는 관찰 방법을 고르는 연습</b>입니다.</p><div class="lab"><h3>Lab — 현상에서 다음 조사 방법 결정하기</h3><div id="finalQ" class="readout" aria-live="polite"></div><div id="finalChoices" class="controls"></div><div id="finalR" class="readout" aria-live="polite"></div><div class="controls"><button class="btn" id="finalNext" disabled>다음</button></div></div><div class="beginner"><b>종합 Lab의 목표:</b> “이 emulator에서 무슨 명령을 입력하지?”가 아니라, <b>지금 가진 단서에서 다음으로 어떤 사건과 상태를 관찰해야 하는가</b>를 판단할 수 있어야 합니다.</div></section>
''')

summary = '''
<section id="summary"><div class="kicker">4부 핵심 정리</div><h2>도구 이름보다 분석 질문과 관찰 순서를 기억한다</h2><div class="flow"><b>현상 발견</b><span class="arrow">→</span><b>질문 만들기</b><span class="arrow">→</span><b>사건에서 정지</b><span class="arrow">→</span><b>CPU / PC / Register</b><span class="arrow">→</span><b>Code / Memory</b><span class="arrow">→</span><b>필요한 만큼만 Step</b></div><div class="grid3"><div class="card"><h3>실행 시점</h3><p>특정 routine이 언제 실행되는지 알고 싶으면 실행 위치를 잡습니다.</p></div><div class="card"><h3>Data 사용</h3><p>누가 읽는지는 READ, 누가 바꾸는지는 WRITE를 잡습니다.</p></div><div class="card"><h3>실제 경로</h3><p>CALL·RET·조건분기는 가능한 경로보다 현재 실행에서 실제 선택된 경로를 확인합니다.</p></div></div><div class="why"><b>4부에서 얻어야 할 능력:</b> 처음 보는 emulator에서도 기능 이름을 대응시킨 뒤 같은 분석 질문과 관찰 순서를 적용할 수 있는 것.</div></section>
'''
if '<section class="quiz" id="quiz">' not in s:
    raise SystemExit('quiz marker not found')
s = s.replace('<section class="quiz" id="quiz">', summary.strip() + '\n\n<section class="quiz" id="quiz">', 1)

sec('quiz', '''
<section class="quiz" id="quiz"><div class="kicker">확인 문제</div><h2>4부 확인 문제</h2>
<details><summary>1. Debugger가 필요한 가장 기본적인 이유는?</summary><div class="answer">실행 중인 프로그램을 필요한 순간에 멈추고 PC, register, memory, code 상태를 관찰해 실제 실행 과정을 확인하기 위해서입니다.</div></details>
<details><summary>2. Disassembly와 동적 실행 추적의 차이는?</summary><div class="answer">Disassembly는 존재하는 code와 가능한 흐름을 보여 주고, debugger는 이번 실행에서 실제로 선택된 code와 실제 값을 확인하게 합니다.</div></details>
<details><summary>3. 특정 routine이 실제로 실행되는 순간을 알고 싶다면?</summary><div class="answer">Execution / PC Breakpoint처럼 CPU가 해당 실행 위치에 도달했을 때 멈추는 기능을 사용합니다.</div></details>
<details><summary>4. 어떤 RAM data를 어느 code가 읽는지 알고 싶다면?</summary><div class="answer">Read Breakpoint 또는 Read Watchpoint를 사용합니다.</div></details>
<details><summary>5. 어떤 RAM 값이 왜 바뀌었는지 알고 싶다면?</summary><div class="answer">Write Breakpoint 또는 Write Watchpoint를 사용해 실제 writer를 찾습니다.</div></details>
<details><summary>6. Memory access breakpoint에 걸렸는데 현재 PC가 접근 instruction 다음을 가리킨다면?</summary><div class="answer">현재 PC만 보지 말고 Break 메시지의 access 주소와 바로 앞을 포함한 주변 disassembly를 함께 확인합니다.</div></details>
<details><summary>7. Register를 볼 때 값 자체보다 함께 판단해야 할 것은?</summary><div class="answer">그 register가 현재 code에서 일반 값, counter, 주소, pointer 가운데 어떤 역할로 쓰이는지 판단해야 합니다.</div></details>
<details><summary>8. Step Into와 Step Over의 차이는?</summary><div class="answer">Step Into는 CALL 내부 routine까지 들어가 조사하고, Step Over는 호출 내부를 실행한 뒤 caller의 다음 위치부터 다시 관찰합니다.</div></details>
<details><summary>9. 조건분기에서 실제 경로를 판단하려면?</summary><div class="answer">분기 instruction과 그 조건에 사용되는 flag 또는 counter 값을 함께 봅니다.</div></details>
<details><summary>10. PC address와 D88 file offset은 같은 좌표인가?</summary><div class="answer">아닙니다. PC는 CPU address space의 실행 위치이고 D88 offset은 disk image 파일 안의 byte 위치입니다.</div></details>
<details><summary>11. MAIN CPU만 보면 항상 충분한가?</summary><div class="answer">아닙니다. disk subsystem처럼 SUB CPU가 관여하는 대상은 현재 어느 CPU를 관찰하고 있는지 구분해야 합니다.</div></details>
<details><summary>12. 처음부터 끝까지 모든 instruction을 single-step 하는 것이 좋은 방법인가?</summary><div class="answer">아닙니다. 관심 없는 구간은 실행하고, 중요한 사건을 breakpoint로 잡은 뒤 필요한 몇 instruction만 자세히 비교하는 편이 효율적입니다.</div></details>
</section>
''')

next_part = '''
<section class="em" id="next-part"><div class="kicker">다음 5부로</div><h2>이제 Debugger를 실제 게임 Data와 Code의 흐름에 적용한다</h2><div class="flow"><b>4부<br>어떻게 멈추고 무엇을 볼 것인가</b><span class="arrow">→</span><b>5부<br>Data가 어디서 와서 어떤 Code를 지나 어디로 가는가</b></div><p>4부에서는 필요한 순간을 잡고 CPU·PC·register·code·memory를 읽는 법을 배웠습니다. 5부에서는 이 방법을 실제 게임 분석에 사용하여 특정 값이 어디에서 읽히고 어떤 routine을 거쳐 어디에 쓰이는지를 추적합니다.</p></section>
'''
footer = '<footer>PC-88 게임 분석 기초 · 4부</footer>'
if footer not in s:
    raise SystemExit('footer marker not found')
s = s.replace(footer, next_part.strip() + '\n' + footer, 1)

script = r'''<script>
(()=>{
 const qs=[['이 routine이 실제로 언제 실행되는지 알고 싶다.','pc','실행 위치가 관심 대상이므로 Execution / PC breakpoint가 맞습니다.'],['RAM D9A5h를 어느 code가 읽는지 알고 싶다.','read','data를 사용하는 code를 찾으므로 READ가 맞습니다.'],['RAM C0A2h의 값을 누가 바꾸는지 알고 싶다.','write','값을 바꾼 code를 찾으므로 WRITE가 맞습니다.']];
 let i=0,done=false;const q=document.getElementById('bpq'),r=document.getElementById('bpr'),n=document.getElementById('bpnext'),bs=[...document.querySelectorAll('[data-bp]')];
 function draw(){done=false;q.textContent=`${i+1} / ${qs.length}  ${qs[i][0]}`;r.textContent='질문을 읽고 먼저 잡아야 할 사건을 고릅니다.';n.disabled=true;bs.forEach(b=>{b.disabled=false;b.classList.remove('correct','active')})}
 bs.forEach(b=>b.onclick=()=>{if(done)return;bs.forEach(x=>x.classList.remove('active'));b.classList.add('active');if(b.dataset.bp===qs[i][1]){done=true;b.classList.remove('active');b.classList.add('correct');bs.forEach(x=>x.disabled=true);r.textContent='정답. '+qs[i][2];n.disabled=false}else r.textContent='다시 생각해 보세요. 실행 위치 / 읽기 / 쓰기 중 어떤 사건이 질문에 직접 답합니까?'});n.onclick=()=>{if(done){i=(i+1)%qs.length;draw()}};draw();
})();
(()=>{
 const stages=[
 {q:'게임에서 특정 RAM 값이 바뀌었다. “누가 이 값을 바꾸는가?”가 첫 질문이다. 무엇을 잡아야 하는가?',c:[['실행 위치','exec'],['READ','read'],['WRITE','write'],['Single-step','step']],a:'write',ok:'WRITE 사건을 잡으면 그 주소에 실제 값을 쓴 code를 직접 찾을 수 있습니다.'},
 {q:'정지 결과가 WRITE addr=C0A2, data=00 / PC=87AE / HL=C0A2 / A=00 이다. 실제 writer를 찾으려면 다음 무엇을 보는가?',c:[['현재 PC만 본다','pc'],['주변 Disassembly를 본다','near'],['D88 offset을 찾는다','d88'],['Kanji ROM을 본다','kanji']],a:'near',ok:'Memory access 뒤에 정지했다면 현재 PC와 함께 바로 앞을 포함한 주변 code를 봐야 합니다.'},
 {q:'주변 code가 87AD LD (HL),A / 87AE INC HL 이고 HL=C0A2, A=00이다. 실제로 C0A2에 00을 쓴 instruction은?',c:[['87AD LD (HL),A','writer'],['87AE INC HL','inc'],['둘 다','both']],a:'writer',ok:'LD (HL),A가 HL이 가리키는 C0A2에 A=00을 씁니다.'},
 {q:'추적 중 CALL을 만났고 호출된 routine 내부가 원인인지 직접 확인하고 싶다. 어떤 실행 방식이 맞는가?',c:[['Step Into','into'],['Step Over','over'],['계속 실행','go']],a:'into',ok:'호출 내부 자체가 조사 대상이면 Step Into로 callee에 들어갑니다.'},
 {q:'같은 CALL이지만 내부 routine의 역할은 이미 알고 있고 caller의 다음 code가 관심 대상이다. 무엇을 쓰는가?',c:[['Step Into','into'],['Step Over','over'],['READ','read']],a:'over',ok:'호출 내부가 현재 관심 밖이면 Step Over로 복귀 뒤부터 관찰합니다.'},
 {q:'현재 code가 JR NZ,target이고 Z=0이다. 이번 실행에서 실제 경로는?',c:[['분기한다','taken'],['분기하지 않는다','not']],a:'taken',ok:'Z=0이면 NZ 조건이 성립하므로 target으로 분기합니다.'},
 {q:'추적 대상이 disk subsystem 쪽 code로 이어졌다. 다음에 추가로 확인해야 할 것은?',c:[['현재 CPU가 MAIN인지 SUB인지','cpu'],['화면 색상','color'],['파일 이름','name']],a:'cpu',ok:'PC-88의 disk subsystem에서는 MAIN/SUB 실행 주체를 구분해야 같은 주소값을 잘못 해석하지 않습니다.'}
 ];
 let i=0,locked=false;const q=document.getElementById('finalQ'),box=document.getElementById('finalChoices'),r=document.getElementById('finalR'),next=document.getElementById('finalNext');
 function draw(){locked=false;const st=stages[i];q.textContent=`${i+1} / ${stages.length}  ${st.q}`;r.textContent='가장 직접적인 다음 관찰 방법을 고르십시오.';box.innerHTML='';next.disabled=true;next.textContent='다음';st.c.forEach(([label,val])=>{const b=document.createElement('button');b.className='btn';b.textContent=label;b.dataset.v=val;b.onclick=()=>answer(b);box.appendChild(b)})}
 function answer(b){if(locked)return;[...box.children].forEach(x=>x.classList.remove('active'));b.classList.add('active');const st=stages[i];if(b.dataset.v===st.a){locked=true;b.classList.remove('active');b.classList.add('correct');[...box.children].forEach(x=>x.disabled=true);r.textContent='정답. '+st.ok;next.disabled=false;next.textContent=(i===stages.length-1)?'처음부터':'다음'}else r.textContent='다시 판단해 보세요. 지금 질문에 가장 직접적으로 답하는 관찰 방법이 무엇인지 생각합니다.'}
 next.onclick=()=>{if(!locked)return;i=(i+1)%stages.length;draw()};draw();
})();
</script>'''
s2, n = re.subn(r'<script>.*?</script>\s*</body>', script + '\n</body>', s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'script: {n}')
s = s2

for marker in ['id="final-lab"','id="summary"','id="next-part"','break read 0xD9A5 #1','break write 0xC0A2 #1','Step Over','현재 CPU가 MAIN인지 SUB인지']:
    if marker not in s:
        raise SystemExit(f'missing {marker}')
for img in ['01.png'] + [f'{i:02d}.PNG' for i in range(2,15)]:
    if f'../images/course04/{img}' not in s:
        raise SystemExit(f'missing image {img}')
p.write_text(s, encoding='utf-8')

rp = Path('README.md')
r = rp.read_text(encoding='utf-8')
r = r.replace('4부의 실습 설명에는 **실제 QUASI88 실행 로그와 스크린샷**을 사용하며, HTML Lab은 원리를 이해하기 위한 보조 도구로 사용합니다.', '4부의 실습 설명에는 **실제 QUASI88 실행 로그와 실행 화면**을 사용하며, HTML Lab은 특정 emulator 명령을 외우는 용도가 아니라 공통 분석 원리를 이해하기 위한 보조 도구로 사용합니다.')
r = r.replace('별도의 웹 서버는 필요하지 않습니다. 4부의 실제 스크린샷도 HTML 파일 안에 포함되어 있어 로컬에서 그대로 볼 수 있습니다.', '별도의 웹 서버는 필요하지 않습니다. 4부의 실제 실행 화면은 `images/course04/`의 이미지 파일을 `course/04.html`에서 불러옵니다. 저장소 전체를 내려받으면 로컬에서도 그대로 볼 수 있습니다.')
r = re.sub(r'```text\nPC88-Analysis/\n├─ index\.html\n├─ README\.md\n└─ course/\n   ├─ 00\.html\n   ├─ 01\.html\n   ├─ 02\.html\n   ├─ 03\.html\n   └─ 04\.html\n```', '''```text
PC88-Analysis/
├─ index.html
├─ README.md
├─ course/
│  ├─ 00.html
│  ├─ 01.html
│  ├─ 02.html
│  ├─ 03.html
│  └─ 04.html
└─ images/
   └─ course04/
      ├─ 01.png
      ├─ 02.PNG
      ├─ ...
      └─ 14.PNG
```''', r, count=1)
rp.write_text(r, encoding='utf-8')
