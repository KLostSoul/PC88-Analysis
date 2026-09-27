# 6부 — 분석 근거 및 실습 자료

[6부 강좌](06.html)에서 사용한 QUASI88 0.7.4 Monitor 기록과 실제 화면 자료를 정리한 문서입니다. 실행 당시의 명령·레지스터·disassembly·dump·step 출력은 [원문 로그](06-logs.md)의 01~11번에 기록되어 있습니다.

## 실제 화면과 HxD 캡처

| 파일 | 확인할 내용 |
|---|---|
| [01.PNG](../images/course06/01.PNG) | 원본 KANJI1.ROM을 사용한 첫 이벤트의 정상 대사 화면 |
| [02.PNG](../images/course06/02.PNG) | Kanji ROM을 사용할 수 없을 때 대사가 정상적으로 표시되지 않는 비교 화면 |
| [03.PNG](../images/course06/03.PNG) | 첫 두 글자 「雨が」가 표시된 시점 |
| [04.PNG](../images/course06/04.PNG) | RAM의 첫 Token을 `B8 62 → C8 18`로 바꾼 뒤 「ががやん」으로 시작하는 화면 |
| [05.PNG](../images/course06/05.PNG) | HxD에서 원본 ROM의 `C560h~C57Fh` 32바이트를 선택한 화면 |
| [06.PNG](../images/course06/06.PNG) | 같은 32바이트를 「가」의 점 무늬로 덮어쓴 화면 |
| [07.PNG](../images/course06/07.PNG) | 수정 ROM을 적용하여 첫 글자가 「가」로 나타난 실제 게임 화면 |

## Monitor 기록 01~11

| 번호 | 실행 내용 |
|---|---|
| 01 | 강제 Monitor 진입: `reg`, `disasm #80` |
| 02 | `dump 0x00FA #16`으로 Stack 확인 |
| 03 | `disasm 0x0443 #32`로 반환 주소 주변 확인 |
| 04 | `disasm 0x02E4 #48`, `disasm 0x04AE #20` |
| 05 | `disasm 0x03B8 #80`으로 문자 Token 분기 조사 |
| 06 | `dump 0x969F #16`, `dump 0x0C84 #1`, `disasm 0x0B8F #64` |
| 07 | `break 0x0BE1 #1`, `go`, `disasm #24` |
| 08 | `break 0x0BFE #2`, `g`, `dump 0xEBD4 #4` |
| 09 | `step` 세 번, `reg`, `dump 0xEBD4 #4` |
| 10 | `g` 두 번으로 다음 글리프 행의 읽기 시작과 기록 직전 비교 |
| 11 | `reset` 뒤 원본 Script 확인, 첫 Token 수정, 수정 후 확인 및 실행 |

## 실제 실행에서 확인한 주요 값

| 관찰 지점 | 레지스터·주소·데이터 | 확인한 내용 |
|---|---|---|
| 초기 정지 | `PC=04BDh`, `HL=96A3h`, `SP=00FAh` | 이미 「雨が」가 표시된 상태에서 대기 루프 실행 |
| Stack | `00FAh: D0 18 4F 04` | 저장된 `DE=18D0h` 다음에 반환 주소 `044Fh`가 위치 |
| Script 읽기 | `02EDh LD E,(HL)` | Script를 한 바이트씩 읽음 |
| 첫 세 글자 | `969Fh: B8 62 C8 18 48 38` | 차례로 「雨」「が」「や」 |
| 첫 Token 처리 | `B8 62 → DE=62B0h` | `03B8h`의 변환 후 글리프 접근값 |
| 「や」 1행 읽기 시작 | `PC=0BE1h`, `DE=3840h`, `BC=0000h`, `HL=EBD4h` | 첫 번째 행을 읽기 직전 |
| 「や」 1행 기록 직전 | `PC=0BFEh`, `DE=3841h`, `BC=0000h`, `HL=EBD4h` | 읽은 두 바이트가 모두 `00h` |
| 「や」 2행 읽기 시작 | `PC=0BE1h`, `DE=3841h`, `BC=0000h`, `HL=EC24h` | 다음 행의 ROM 접근값 |
| 「や」 2행 기록 직전 | `PC=0BFEh`, `DE=3842h`, `BC=0180h`, `HL=EC24h` | 두 번째 행의 실제 데이터는 `01 80` |
| RAM 수정 실습 | `969Fh: B8 62 → C8 18` | 첫 글자를 「が」로 출력 |

첫 `02EDh` breakpoint에 걸린 RAM 수정 실습의 `HL`은 `9680h`였습니다. 수정 주소 `969Fh`는 별도 `dump`로 확인했습니다. `0BFEh`와 `0C00h`의 기록 명령을 step한 뒤에도 같은 주소의 일반 RAM `dump`는 `FF`였으므로, 일반 RAM 읽기와 GVRAM 접근을 구별해야 합니다.

## HxD 글리프 수정

원본 `KANJI1.ROM`에서 「雨」의 글리프를 찾은 파일 오프셋은 `C560h`입니다. `C560h~C57Fh`의 32바이트를 다음 「가」 글리프 값으로 덮어썼습니다.

```text
C560 : 00 08 1F C8 00 48 00 48 00 48 00 48 00 48 00 4E
C570 : 00 88 01 08 01 08 02 08 04 08 04 08 18 08 00 08
```

16×16 점 무늬의 각 행은 왼쪽 8비트와 오른쪽 8비트로 나뉘어 2바이트가 됩니다. 위 32바이트는 [바리스 1 재현 빌드의 「가」 글리프 원천](https://github.com/KLostSoul/PC88-Valis1-Localization-Build/blob/main/source/accepted/kanji/glyphs/glyph_0001_U%2BAC00_slot0378_tokA017_off02F40.txt)을 참조했습니다. 원본 글리프의 위치를 실습용으로 덮어쓴 것이며, 재현 빌드의 「가」 배정 위치인 `02F40h`과는 다릅니다.

[05.PNG](../images/course06/05.PNG)과 [06.PNG](../images/course06/06.PNG)은 교체 전후의 해당 영역을 보여 줍니다. [07.PNG](../images/course06/07.PNG)은 수정 ROM 실행 결과입니다. **ROM 전체 파일 크기를 보여 주는 별도 기록은 없으므로**, 실습에서는 덮어쓰기 전후의 파일 크기를 직접 비교하도록 안내합니다.

마지막의 「や」 교체 독립 과제는 수강생이 직접 실행하는 과제이며, 위의 원문 로그나 스크린샷에 포함된 별도 실측 결과는 아닙니다.
