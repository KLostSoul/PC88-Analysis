# 6부 이미지 수집·배치 목록

기존 강좌와 같은 위치 규칙: `images/course06/`.

| 파일 | 내용 | 상태 |
|---|---|---|
| `01.PNG` | 정상 `KANJI1.ROM` 첫 이벤트 전체 문장 | GitHub PNG 등록 및 강좌 삽입 완료 |
| `02.PNG` | ROM 제거·재시작 후 같은 장면의 문자 영역 이상 | GitHub PNG 등록 및 강좌 삽입 완료 |
| `03.PNG` | 「雨が」 출력된 순간의 화면 | GitHub PNG 등록 및 강좌 삽입 완료 |
| 분석 로그 04~08 | 강제 Monitor / Stack / dispatcher / Kanji I/O / Glyph 1·2행 | `course/06-logs.md`에 원문 그대로 기록; 별도 로그 스크린샷은 사용하지 않음 |
| `04.PNG` | 첫 글자 `B8 62 → C8 18` 수정 후 「ががやん」이 출력된 실제 화면 | GitHub PNG 등록 및 강좌 삽입 완료 |
| `05.PNG` | HxD에서 원본 `C560~C57F` 글리프 32바이트를 선택한 화면 (11번) | GitHub PNG 등록 및 강좌 삽입 완료 |
| `06.PNG` | 해당 범위를 「가」 글리프 32바이트로 덮어쓴 화면 (12번) | GitHub PNG 등록 및 강좌 삽입 완료 |
| `07.PNG` | 수정한 ROM으로 실행해 첫 글자가 「가」로 나타난 게임 화면 (13번) | GitHub PNG 등록 및 강좌 삽입 완료 |
| `09-10` | 같은 실험의 초기 Breakpoint·원본 dump·write·수정 dump 전체 로그 | `course/06-logs.md`에 원문 그대로 기록 완료 |
| `11-13` | HxD 원본·수정·QUASI88 출력 비교 | `05.PNG`~`07.PNG`으로 실습 내용 반영 |

`01.PNG`~`07.PNG`은 모두 저장소의 `images/course06/`에 등록되었으며 `course/06.html`의 각 실습 위치에 배치했다. QUASI88 Monitor 출력은 이미지로 요약하지 않고 `course/06-logs.md`에 원문 그대로 보관한다.
