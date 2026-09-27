# 6부 — 실제 관찰 근거와 미확보 자료

현재 상태: 6부 강좌 뼈대. 이 문서는 제공받은 QUASI88 0.7.4 실측 결과와 아직 수행하지 않은 실험을 분리한다.

## 사용 자료

- 첫 이벤트 원문: `雨がやんでる・・・いつの間に・・・？`
- `01.PNG`: 정상 KANJI1.ROM, 정상 첫 이벤트 화면 (제공받음, GitHub PNG 등록 대기)
- `02.PNG`: KANJI1.ROM 제거·재시작 후 동일 장면, 문자 영역 비정상 표시 (제공받음, 등록 대기)
- `03.PNG`: 「雨が」가 보이는 초기 출력 화면 (제공받음, 등록 대기)
- [바리스 1 재현 빌드](https://github.com/KLostSoul/PC88-Valis1-Localization-Build)
- [확정 Kanji 글리프 배치](https://github.com/KLostSoul/PC88-Valis1-Localization-Build/blob/main/source/accepted/tables/kanji/assignments.csv)
- [가 글리프 원천 TXT](https://github.com/KLostSoul/PC88-Valis1-Localization-Build/blob/main/source/accepted/kanji/glyphs/glyph_0001_U%2BAC00_slot0378_tokA017_off02F40.txt)

## 4. 강제 Monitor 진입

```text
[MAIN]
AF:0993 BC:0000 DE:0AD0 HL:96A3 PC:04BD SP:00FA
04BD 3A9202  LD A,(0292H)
04C0 BA      CP D
04C1 38FA    JR C,04BDH
04C7 D1      POP DE
04C8 C9      RET
```

첫 문자 출력 직전이 아니라 이미 「雨が」가 보이는 시점이다. `04BD`는 대기 루프다.

## 5. Stack에서 호출자 / Script로 이동

```text
QUASI88> dump 0x00FA #16
00FA : D0 18 4F 04 CB 01 31 00 01 CD E4 01 3E 48 D3 32

0443 CD8F0B CALL 0B8FH
0446 3E08   LD A,08H
0448 D332   OUT (32H),A
044A 3E0A   LD A,0AH
044C CDAE04 CALL 04AEH
044F C3E402 JP 02E4H
```

`04AE` 내부 `PUSH DE`에 의해 저장된 `D0 18`은 DE=18D0. 반환 주소 `4F 04`는 `044Fh`. `04AE`는 `0292h` 카운터를 기다린다.

## 6. Script consumer와 문자 Token

```text
02ED 5E       LD E,(HL)
02EE 23       INC HL
02EF 7B       LD A,E
02F0 32840C   LD (0C84H),A
02F3 E60F     AND 0FH
031B FE08     CP 08H
031D CAB803   JP Z,03B8H

QUASI88> dump 0x969F #16
969F : B8 62 C8 18 48 38 38 39 78 28 B8 38 60 12 60 12

QUASI88> dump 0x0C84 #1
0C84 : C8 ...
```

원본 `雨=B8 62`, `が=C8 18`, 다음 `や=48 38`. 현재 `HL=96A3h`.

```text
03B8 LD A,E
03B9 AND F0H
03BB LD E,A
03BC LD D,(HL)
03BD INC HL
03BE LD A,(0C84H)
03C1 AND 08H
03C3 JP NZ,043FH
043F LD A,48H
0441 OUT (32H),A
0443 CALL 0B8FH
```

이번 문자 Token의 구성: `B8 62 → 62B0`, `C8 18 → 18C0`, `48 38 → 3840`. 일반화 범위는 이번 분기에 한정한다.

## 7. Kanji ROM I/O 실제 Break

```text
QUASI88> break 0x0BE1 #1
QUASI88> go
*** Break at 0BE1H *** ( MAIN[#1] : PC )
[MAIN] AF:3800 BC:0000 DE:3840 HL:EBD4 PC:0BE1 SP:004E

0BE4 OUT (E8H),A
0BE7 OUT (E9H),A
0BED IN A,(E8H)
0BEF LD C,A
0BF0 IN A,(E9H)
0BF2 LD B,A
0BF5 INC DE
0BFE LD (HL),B
0BFF INC HL
0C00 LD (HL),C
```

이번 breakpoint는 첫 문자가 아니라 세 번째 문자 「や」의 첫 Glyph 행이다.

## 8. 첫 두 Glyph 행과 GVRAM 관련 주의

```text
QUASI88> break 0x0BFE #2
QUASI88> g
*** Break at 0BFEH *** ( MAIN[#2] : PC )
[MAIN] BC:0000 DE:3841 HL:EBD4 PC:0BFE
QUASI88> dump 0xEBD4 #4
EBD4 : FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

QUASI88> step
[MAIN] PC:0BFF HL:EBD4
QUASI88> step
[MAIN] PC:0C00 HL:EBD5
QUASI88> step
[MAIN] PC:0C01 HL:EBD5
QUASI88> dump 0xEBD4 #4
EBD4 : FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF

QUASI88> g
*** Break at 0BE1H *** ( MAIN[#1] : PC )
[MAIN] BC:0000 DE:3841 HL:EC24 PC:0BE1
QUASI88> g
*** Break at 0BFEH *** ( MAIN[#2] : PC )
[MAIN] BC:0180 DE:3842 HL:EC24 PC:0BFE
```

두 번째 행 출력 주소는 +50h. `0BFE/0C00`의 실행은 확인됐지만 일반 dump는 여전히 FF이므로 그래픽 접근 상태와 일반 RAM 조회를 구분한다.

## 9번 비발화 Token 선택 근거

기존 바리스 분석은 같은 Glyph의 첫 바이트에 `08h` 비트를 OR하면 발화를 억제한다고 기록한다. 이미 확인된 `20 18`(「あ」 발화체)을 이번 실험에서 그대로 사용하지 않는다. 대신 `28 18`을 사용한다. 현재 실측된 `03B8~03C3`의 코드에서도 `28 AND F0h = 20h`로 Glyph 주소의 하위 바이트가 보존되고, `28 AND 08h != 0`이므로 비발화 경로인 `043Fh`로 분기한다. 다만 첫 이벤트의 `969Fh`에서 실제로 출력한 검증 결과는 아직 확보되지 않았다.

## 아직 필요한 실험

| 번호 | 수집 대상 | 상태 |
|---|---|---|
| 9 | `969F:B8 62`를 비발화체 `28 18`로 바꾸는 실측 QUASI88 write 로그 | 미확보 |
| 10 | 같은 첫 이벤트 첫 문자가 「あ」로 바뀐 실제 화면 | 미확보 |
| 11 | HxD 원본 ROM `C560~C57F` 캡처 | 미확보 |
| 12 | HxD에서 아래 「가」 32바이트로 Overwrite하고 길이 비교한 캡처 | 미확보 |
| 13 | Script 원본 유지·수정 ROM 재시작 후 「가」 출력 화면 | 미확보 |

```text
00 08 1F C8 00 48 00 48
00 48 00 48 00 48 00 4E
00 88 01 08 01 08 02 08
04 08 04 08 18 08 00 08
```

위 바이트는 재현 빌드의 `가` 원천 TXT를 16×16 한 줄당 상위/하위 바이트로 계산한 값이다. `C560` HxD 수동 실험의 성공 여부는 아직 확인하지 않았다. 재현 빌드에서 정식 `가`는 slot 378 / offset `0x02F40`이다.

강좌에서는 미검증 단계에 성공 로그·사진을 만들어 넣지 않는다.
