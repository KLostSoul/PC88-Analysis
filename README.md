# PC-88 게임 분석을 위한 기초 강좌

PC-8801 게임을 직접 분석하기 위해 필요한 기초 지식을 단계적으로 정리하는 강좌입니다.

컴퓨터의 기본 구조부터 시작해 PC-88의 하드웨어와 메모리, Z80 어셈블리, 플로피 디스크와 D88 구조를 익힌 뒤, 에뮬레이터 디버거를 이용한 실행 흐름 추적과 실제 게임 데이터 분석으로 이어지는 것을 목표로 합니다.

이 저장소의 강좌는 **PC-88 게임을 처음 분석하는 사람도 앞부분부터 순서대로 따라갈 수 있도록 구성**하고 있습니다.

## 강좌 사이트

GitHub Pages에서 바로 볼 수 있습니다.

**https://klostsoul.github.io/PC88-Analysis/**

## 강좌 구성

| 부 | 내용 | 상태 | 파일 |
|---|---|---|---|
| 0부 | 컴퓨터의 기본 원리 — bit에서 stack까지 | 완료 | [`course/00.html`](course/00.html) |
| 1부 | PC-8801은 어떤 컴퓨터인가 — 하드웨어와 메모리 구조 | 완료 | [`course/01.html`](course/01.html) |
| 2부 | Z80 어셈블리 코드를 읽는 법 | 완료 | [`course/02.html`](course/02.html) |
| 3부 | 플로피·μPD765·D88·Kanji ROM | 완료 | [`course/03.html`](course/03.html) |
| 4부 | 에뮬레이터 디버거로 실행 흐름 추적하기 | 완료 | [`course/04.html`](course/04.html) |
| 5부 | 실제 게임에서 Data와 Code의 흐름 추적하기 | 완료 | [`course/05.html`](course/05.html) |
| 6부 | 문자·Font·화면 출력 경로를 분석하는 방법 | 완료 | [`course/06.html`](course/06.html) |
| 7부 | 처음 보는 PC-88 게임을 역분석하는 방법 | 완료 | [`course/07.html`](course/07.html) |

## 각 부에서 배우는 내용

### 0부 — 컴퓨터의 기본 원리

PC-88이나 Z80을 보기 전에 필요한 가장 기본적인 개념을 다룹니다.

- bit와 byte
- 2진수와 16진수
- 논리 연산
- register
- RAM과 address
- CPU와 machine language
- assembler와 disassembler
- stack

### 1부 — PC-8801 하드웨어와 메모리

PC-8801이 어떤 컴퓨터인지부터 시작해 게임 분석에 직접 필요한 구조를 설명합니다.

- PC-8801 계열과 SR 이후의 구조
- Z80 CPU와 동작 속도
- Main RAM과 ROM
- GVRAM과 Text VRAM
- bank switching
- 확장 RAM
- FDD SUB 시스템
- Kanji ROM
- PC-88의 I/O 구조

### 2부 — Z80 어셈블리 코드 읽기

기계어를 전부 외우는 것이 아니라, 디스어셈블된 코드를 따라가며 프로그램의 동작을 읽는 데 필요한 Z80 명령과 사고법을 익힙니다.

- register와 register pair
- `LD`, `INC`, `DEC`
- 산술·논리 연산
- `JP`, `JR`, `CALL`, `RET`
- 조건 분기와 flag
- stack과 `PUSH` / `POP`
- 반복 처리
- 메모리와 포인터
- I/O 명령
- 간단한 실행 흐름 읽기

### 3부 — 플로피·FDC·D88·Kanji ROM

게임 데이터가 실제 플로피 디스크에서 어떻게 읽혀 RAM으로 들어오고, D88 이미지에서는 어떻게 표현되는지를 연결해서 설명합니다.

- Track / Head / Sector
- C/H/R/N
- FDC와 μPD765
- PC-88의 MAIN CPU와 FDD SUB CPU
- 디스크 읽기와 RAM 전송
- D88 Track Table과 Sector Header
- RAW sector data
- 디스크상의 위치와 RAM address의 차이
- Kanji ROM
- JIS code와 glyph 접근

### 4부 — 에뮬레이터 디버거로 실행 흐름 추적하기

실행 중인 PC-88 게임을 실제 debugger로 멈추고, 그 순간의 CPU 상태와 실행 흐름을 읽는 방법을 다룹니다.

PC-88 에뮬레이터마다 debugger 기능과 조작법은 다를 수 있으므로 강좌의 개념을 특정 프로그램에 고정하지 않습니다. 실제 PC-88에도 프로그램을 조사하고 디버깅하기 위한 수단은 있지만, 오늘날 실기를 보유하지 않은 사람도 많고 새로 실습 환경을 마련하기 쉽지 않으므로 **이 강좌에서는 QUASI88 0.7.4의 Monitor를 대표 실습 예시로 사용합니다.**

- Debugger가 무엇이고 왜 필요한가
- 정적 code 읽기와 동적 실행 추적의 차이
- PC와 register 확인
- disassembly와 memory dump 연결
- PC / READ / WRITE breakpoint
- breakpoint hit 직후 자동으로 출력되는 CPU 상태 읽기
- single-step 전후 비교
- Step Into / Step Over / Step Out
- 실제 CALL / RET와 조건분기 추적
- I/O instruction 관찰
- MAIN / SUB CPU 구분
- 질문에 맞는 breakpoint와 관찰 방법 선택

4부의 실습 설명에는 **실제 QUASI88 실행 로그와 실행 화면**을 사용하며, HTML Lab은 특정 emulator 명령을 외우는 용도가 아니라 공통 분석 원리를 이해하기 위한 보조 도구로 사용합니다.

### 5부 — 실제 게임에서 Data와 Code의 흐름 추적하기

타이틀 화면에서 화면 변화를 관찰하고, 실행 중인 PC와 주변 Code를 확인하면서 Data와 Code의 관계를 좁혀 가는 과정을 설명합니다.

- 화면에서 조사 대상을 정하는 방법
- 강제 브레이크 후 PC와 주변 disassembly 확인
- 반복·분기 구조와 register 역할 분석
- single-step과 dump를 이용한 Memory 변화 검증
- stack과 반환 주소를 이용한 호출자 추적
- 공통 처리 Code와 입력 Data·출력 위치 연결
- 잘못 잡은 후보를 실행 근거로 분류하는 방법
- 관찰 사실·판단·근거·다음 질문을 분석 기록으로 남기는 방법

5부의 예시는 실제 QUASI88 Monitor 로그와 `images/course05/`의 실행 화면을 사용합니다. 화면에 나타난 요소 하나를 출발점으로 삼아, 확인한 근거에서 다음 조사 질문을 정하는 흐름을 보여 줍니다.

### 6부 — 문자·Font·화면 출력 경로를 분석하는 방법

《몽환전사 바리스》 첫 이벤트를 예제로, 화면 비교에서 시작해 Stack 반환 주소와 Script 처리기, 문자 출력 Code, Kanji ROM I/O까지 한 글자의 출력 경로를 추적합니다. QUASI88의 실제 명령과 레지스터를 읽고, 이어 RAM의 문자값과 ROM의 글리프를 각각 수정해 두 방식의 차이를 확인합니다.

- **Script 수정:** `969Fh`의 `B8 62`를 `C8 18`로 바꾸어 첫 글자 「雨」를 「が」로 출력
- **글리프 수정:** HxD에서 `KANJI1.ROM`의 `C560h~C57Fh`에 16×16 「가」 글리프 32바이트를 덮어써 첫 글자를 「가」로 출력
- **기초 원리:** 16×16 점 무늬를 왼쪽 8비트와 오른쪽 8비트로 나누어 2바이트씩 16행으로 저장

[6부 강좌](course/06.html) · [QUASI88 원문 로그](course/06-logs.md) · [분석 근거 및 실습 자료](course/06-evidence.md) · [실습 캡처](images/course06/README.md)

### 7부 — 처음 보는 PC-88 게임을 역분석하는 방법

0~6부의 PC-88 기초 지식을 하나의 역분석 절차로 통합합니다. 5부의 타이틀 화면과 6부의 이벤트 문자 분석에서 확인된 실제 QUASI88 로그를 바탕으로, 처음 보는 게임에서 무엇을 조사할지 스스로 결정하는 종합 실습입니다.

- 원본과 실험용 D88·ROM 준비, 조사할 화면 요소 하나 선택
- CPU 주소·D88 파일 오프셋·Kanji ROM 등 서로 다른 위치 구분
- RAM 데이터와 D88 후보를 서로 대조하되, 로드·Track/Sector·전송 근거가 맞을 때만 원본 위치로 확정하는 기준
- 질문에 따라 PC·READ·WRITE breakpoint, reg·disasm·dump·step 선택
- 발견한 Z80 Code를 읽기·쓰기 → 값·주소 → pointer → 실제 분기 → CALL 관계 순으로 해석
- 새 실험 전 breakpoint·reset·RAM/ROM 상태를 정리하고, 수정 검증이 필요할 때는 한 번에 한 요소만 변경
- 실제 호출자와 입력·출력 후보를 확인하고 화면 초기화 Code 같은 잘못된 후보 제외
- 이번 장면의 문자 Token 변경과 ROM Glyph 변경으로 서로 다른 가설 검증
- 관찰한 사실·가설·미확인 부분을 분리한 분석 기록 작성
- 기존 5·6부의 첫 관찰 상태로 다음 조사 방법을 직접 정하는 독립 과제
- 아무 주소도 모르는 새 PC-88 게임에서 사용할 빈 분석 시작표

[7부 강좌](course/07.html) · [0~6부 근거 자료 대응표](course/07-source-map.md)

## 실전 분석으로 이어지는 흐름

5부는 화면의 변화에서 시작해 실행 중인 Code와 Memory를 추적합니다. 6부는 이 조사 방법을 첫 이벤트의 문자 출력에 적용하고, Script와 Font를 각각 수정해 결과를 비교합니다. 7부에서는 두 실습의 실제 기록을 이용해 0~6부의 지식을 하나의 역분석 절차로 연결하고, 다음 조사 방법을 스스로 선택하는 연습을 합니다.

```text
5부  화면 변화에서 시작해 Data와 Code의 흐름을 연결한다
        ↓
6부  문자·Font·화면 출력 경로를 분석한다
        ↓
7부  0~6부를 통합해 조사·검증·기록의 순서를 스스로 설계한다
```

5부에서 익힌 것은 특정 게임의 주소나 명령을 외우는 일이 아닙니다. 화면에서 질문을 만들고, 관찰한 근거로 다음 조사 방법을 선택하는 분석 절차입니다.

## 강좌 보는 방법

강좌는 `course/00.html`~`course/07.html`과 공통 반응형 스타일시트 [`assets/course-responsive.css`](assets/course-responsive.css)로 구성됩니다.

1. [GitHub Pages 강좌 목록](https://klostsoul.github.io/PC88-Analysis/)에서 원하는 강좌를 엽니다.
2. 로컬에서 보려면 **HTML 파일만 따로 받지 말고 저장소 전체를 내려받아** `index.html` 또는 `course` 폴더의 HTML 파일을 웹 브라우저로 엽니다. 공통 CSS와 이미지 폴더의 상대경로가 유지되어야 합니다.
3. 처음 배우는 경우 `00.html`부터 순서대로 보는 것을 권장합니다.

4~6부의 실제 실행·실습 화면은 각각 `images/course04/`, `images/course05/`, `images/course06/`에서 불러옵니다. 기본 본문과 이미지는 별도 웹 서버 없이 로컬에서 열 수 있지만, **5~6부의 Mermaid 흐름도는 외부 CDN을 사용하므로 인터넷 연결이 필요합니다.**

## 반응형 화면 지원

강좌 목록과 **0~7부 전체**에 공통 스타일시트를 적용했습니다. 화면 너비에 맞춰 본문·카드·이미지를 조정하고, 좁은 화면에서는 나란히 놓인 캡처를 한 장씩 세로로 표시합니다. 이미지 설명은 자동 줄바꿈되며, 긴 표와 Monitor 로그는 페이지 전체가 밀려나지 않도록 해당 영역 안에서 가로로 스크롤할 수 있습니다. 3부의 도식과 6부의 16×16 글리프 그림도 좁은 화면에 맞춰 표시하도록 구성했습니다.

페이지별 스타일은 각 HTML 안에 두고, 공통 반응형 규칙은 [`assets/course-responsive.css`](assets/course-responsive.css)에서 관리합니다. HTML에서 공통 CSS 링크를 삭제하거나 해당 파일을 제외하고 배포하면 모바일 레이아웃이 달라질 수 있습니다.

## 저장소 구조

```text
PC88-Analysis/
├─ index.html
├─ README.md
├─ assets/
│  └─ course-responsive.css
├─ course/
│  ├─ 00.html
│  ├─ 01.html
│  ├─ 02.html
│  ├─ 03.html
│  ├─ 04.html
│  ├─ 05.html
│  ├─ 06.html
│  ├─ 06-logs.md
│  ├─ 06-evidence.md
│  ├─ 07.html
│  └─ 07-source-map.md
└─ images/
   ├─ course04/
   │  ├─ 01.png
   │  ├─ 02.PNG
   │  ├─ ...
   │  └─ 14.PNG
   ├─ course05/
   │  ├─ 01.PNG
   │  ├─ 02.png
   │  ├─ 06.PNG
   │  └─ 09.PNG
   └─ course06/
      ├─ 01.PNG
      ├─ 02.PNG
      ├─ 03.PNG
      ├─ 04.PNG
      ├─ 05.PNG
      ├─ 06.PNG
      ├─ 07.PNG
      └─ README.md
```

## 이 강좌의 범위

이 강좌의 중심은 **PC-88 게임의 구조를 이해하고, 디버거를 이용해 스스로 분석할 수 있는 기초 역량을 만드는 것**입니다.

따라서 기초 강좌에서는 특정 게임용 한글 패처 제작, 번역 데이터 자동화 파이프라인, 재현 빌드 시스템 같은 제작 단계보다 다음 질문에 답할 수 있게 만드는 데 초점을 둡니다.

- 지금 보고 있는 값은 코드인가, 데이터인가?
- 이 데이터는 디스크의 어디에서 왔는가?
- 어떤 코드가 이 메모리를 읽거나 쓰는가?
- 화면에 나타난 문자와 그래픽은 어떤 경로로 출력되는가?
- breakpoint를 어디에 걸어야 다음 단서를 얻을 수 있는가?
- 가설이 맞는지 최소한의 수정으로 어떻게 확인할 수 있는가?

## 참고

이 저장소에는 상용 게임의 디스크 이미지나 ROM 데이터는 포함하지 않습니다. 강좌의 스크린샷은 debugger 사용과 실행 흐름 설명을 위한 교육용 예시로 사용합니다.
