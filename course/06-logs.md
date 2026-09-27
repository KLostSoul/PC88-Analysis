# 6부 — QUASI88 실제 로그 원문

아래 블록은 이 강좌 제작 과정에서 제공받은 Monitor 출력입니다. 명령어·레지스터·CPU 상태·덤프 헤더·디스어셈블리·step 결과를 생략하거나 축약하지 않고 기록합니다. 각 로그 사이의 해설은 강좌 HTML에서 확인합니다.

## 01 · 강제 Monitor 진입: reg와 disasm #80

```text
QUASI88> reg
[MAIN]
 AF:0993[S..H..NC] BC:0000  DE:0AD0  HL:96A3  IX:0000  PC:04BD  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:00FA  (ck=214400715)
            04C1 38FA      JR    C,04BDH
   \------> 04BD 3A9202    LD    A,(0292H)
            04C0 BA        CP    D
QUASI88> disasm #80
04BD 3A9202    LD    A,(0292H)
04C0 BA        CP    D
04C1 38FA      JR    C,04BDH
04C3 AF        XOR   A
04C4 329202    LD    (0292H),A
04C7 D1        POP   DE
04C8 C9        RET
04C9 3ACD02    LD    A,(02CDH)
04CC CB7F      BIT   7,A
04CE 28F9      JR    Z,04C9H
04D0 3ACD02    LD    A,(02CDH)
04D3 CB7F      BIT   7,A
04D5 20F9      JR    NZ,04D0H
04D7 3ACD02    LD    A,(02CDH)
04DA CB7F      BIT   7,A
04DC 28F9      JR    Z,04D7H
04DE D1        POP   DE
04DF C9        RET
04E0 E5        PUSH  HL
04E1 C5        PUSH  BC
04E2 47        LD    B,A
04E3 210010    LD    HL,1000H
04E6 2B        DEC   HL
04E7 7D        LD    A,L
04E8 B4        OR    H
04E9 C2E604    JP    NZ,04E6H
04EC 10F5      DJNZ  04E3H
04EE C1        POP   BC
04EF E1        POP   HL
04F0 C9        RET
04F1 C9        RET
04F2 C9        RET
04F3 D9        EXX
04F4 210029    LD    HL,2900H
04F7 D9        EXX
04F8 23        INC   HL
04F9 7E        LD    A,(HL)
04FA 23        INC   HL
04FB 46        LD    B,(HL)
04FC FE01      CP    01H
04FE CA1205    JP    Z,0512H
0501 FE02      CP    02H
0503 CA2305    JP    Z,0523H
0506 FE03      CP    03H
0508 CA3405    JP    Z,0534H
050B FE04      CP    04H
050D FE05      CP    05H
050F C3A304    JP    04A3H
0512 3E28      LD    A,28H
0514 32F607    LD    (07F6H),A
0517 E5        PUSH  HL
0518 C5        PUSH  BC
0519 CD4D08    CALL  084DH
051C C1        POP   BC
051D 10F9      DJNZ  0518H
051F E1        POP   HL
0520 C3A304    JP    04A3H
0523 3E28      LD    A,28H
0525 32F607    LD    (07F6H),A
0528 E5        PUSH  HL
0529 C5        PUSH  BC
052A CDE808    CALL  08E8H
052D C1        POP   BC
052E 10F9      DJNZ  0529H
0530 E1        POP   HL
0531 C3A304    JP    04A3H
0534 3E78      LD    A,78H
0536 32A507    LD    (07A5H),A
0539 E5        PUSH  HL
053A C5        PUSH  BC
053B CD9209    CALL  0992H
053E C1        POP   BC
053F 10F9      DJNZ  053AH
0541 E1        POP   HL
0542 C3A304    JP    04A3H
0545 C9        RET
0546 3E48      LD    A,48H
0548 D332      OUT   (32H),A
054A AF        XOR   A
054B D335      OUT   (35H),A
QUASI88>
```

## 02 · 현재 Stack 덤프

```text
QUASI88> dump 0x00FA #16
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
00FA : D0 18 4F 04 CB 01 31 00 01 CD E4 01 3E 48 D3 32 |..O...1.....>H.2|
```

## 03 · 반환 주소 044Fh 주변 disasm

```text
QUASI88> disasm 0x0443 #32
0443 CD8F0B    CALL  0B8FH
0446 3E08      LD    A,08H
0448 D332      OUT   (32H),A
044A 3E0A      LD    A,0AH
044C CDAE04    CALL  04AEH
044F C3E402    JP    02E4H
0452 7B        LD    A,E
0453 E6F0      AND   F0H
0455 5F        LD    E,A
0456 56        LD    D,(HL)
0457 7A        LD    A,D
0458 23        INC   HL
0459 FE12      CP    12H
045B DA7804    JP    C,0478H
045E F5        PUSH  AF
045F 3E48      LD    A,48H
0461 D332      OUT   (32H),A
0463 CD8F0B    CALL  0B8FH
0466 3E08      LD    A,08H
0468 D332      OUT   (32H),A
046A F1        POP   AF
046B FE17      CP    17H
046D DA7804    JP    C,0478H
0470 E5        PUSH  HL
0471 215906    LD    HL,0659H
0474 CD1606    CALL  0616H
0477 E1        POP   HL
0478 3E04      LD    A,04H
047A CDAE04    CALL  04AEH
047D 7E        LD    A,(HL)
047E CB3F      SRL   A
0480 CB3F      SRL   A
QUASI88>
```

## 04 · Script 처리기와 대기 루틴

```text
QUASI88> disasm 0x02E4 #48
02E4 3ACC02    LD    A,(02CCH)
02E7 CB7F      BIT   7,A
02E9 C8        RET   Z
02EA AF        XOR   A
02EB D335      OUT   (35H),A
02ED 5E        LD    E,(HL)
02EE 23        INC   HL
02EF 7B        LD    A,E
02F0 32840C    LD    (0C84H),A
02F3 E60F      AND   0FH
02F5 CAB803    JP    Z,03B8H
02F8 FE01      CP    01H
02FA CA5204    JP    Z,0452H
02FD FE02      CP    02H
02FF CA4203    JP    Z,0342H
0302 FE03      CP    03H
0304 CAF304    JP    Z,04F3H
0307 FE04      CP    04H
0309 CA7705    JP    Z,0577H
030C FE05      CP    05H
030E CA1006    JP    Z,0610H
0311 FE06      CP    06H
0313 CA0906    JP    Z,0609H
0316 FE07      CP    07H
0318 CA0206    JP    Z,0602H
031B FE08      CP    08H
031D CAB803    JP    Z,03B8H
0320 FE09      CP    09H
0322 CA4605    JP    Z,0546H
0325 FE0A      CP    0AH
0327 CA9605    JP    Z,0596H
032A FE0B      CP    0BH
032C CA5B06    JP    Z,065BH
032F FE0C      CP    0CH
0331 CAF104    JP    Z,04F1H
0334 FE0D      CP    0DH
0336 CAF204    JP    Z,04F2H
0339 FE0E      CP    0EH
033B 3A840C    LD    A,(0C84H)
033E FE0F      CP    0FH
0340 C8        RET   Z
0341 C9        RET
0342 7B        LD    A,E
0343 E6F0      AND   F0H
0345 5F        LD    E,A
0346 56        LD    D,(HL)
0347 23        INC   HL
0348 7E        LD    A,(HL)
QUASI88> disasm 0x04AE #20
04AE D5        PUSH  DE
04AF 57        LD    D,A
04B0 3ACD02    LD    A,(02CDH)
04B3 CB7F      BIT   7,A
04B5 2812      JR    Z,04C9H
04B7 CB77      BIT   6,A
04B9 2002      JR    NZ,04BDH
04BB 1600      LD    D,00H
04BD 3A9202    LD    A,(0292H)
04C0 BA        CP    D
04C1 38FA      JR    C,04BDH
04C3 AF        XOR   A
04C4 329202    LD    (0292H),A
04C7 D1        POP   DE
04C8 C9        RET
04C9 3ACD02    LD    A,(02CDH)
04CC CB7F      BIT   7,A
04CE 28F9      JR    Z,04C9H
04D0 3ACD02    LD    A,(02CDH)
04D3 CB7F      BIT   7,A
QUASI88>
```

## 05 · 문자 Token 분기 disasm #80

```text
QUASI88> disasm 0x03B8 #80
03B8 7B        LD    A,E
03B9 E6F0      AND   F0H
03BB 5F        LD    E,A
03BC 56        LD    D,(HL)
03BD 23        INC   HL
03BE 3A840C    LD    A,(0C84H)
03C1 E608      AND   08H
03C3 C23F04    JP    NZ,043FH
03C6 7A        LD    A,D
03C7 FE17      CP    17H
03C9 383B      JR    C,0406H
03CB 3E02      LD    A,02H
03CD CD7506    CALL  0675H
03D0 3A0428    LD    A,(2804H)
03D3 CDAE04    CALL  04AEH
03D6 3E03      LD    A,03H
03D8 CD7506    CALL  0675H
03DB 3E48      LD    A,48H
03DD D332      OUT   (32H),A
03DF CD8F0B    CALL  0B8FH
03E2 3E08      LD    A,08H
03E4 D332      OUT   (32H),A
03E6 E5        PUSH  HL
03E7 215906    LD    HL,0659H
03EA CD1606    CALL  0616H
03ED E1        POP   HL
03EE 3E02      LD    A,02H
03F0 CD7506    CALL  0675H
03F3 3A0428    LD    A,(2804H)
03F6 CDAE04    CALL  04AEH
03F9 3E01      LD    A,01H
03FB CD7506    CALL  0675H
03FE 3E05      LD    A,05H
0400 CDAE04    CALL  04AEH
0403 C3E402    JP    02E4H
0406 FE12      CP    12H
0408 7B        LD    A,E
0409 321B04    LD    (041BH),A
040C 3E48      LD    A,48H
040E D332      OUT   (32H),A
0410 DA1A04    JP    C,041AH
0413 CD8F0B    CALL  0B8FH
0416 3E08      LD    A,08H
0418 D332      OUT   (32H),A
041A 3E00      LD    A,00H
041C 1632      LD    D,32H
041E FE30      CP    30H
0420 2816      JR    Z,0438H
0422 161E      LD    D,1EH
0424 FE20      CP    20H
0426 2810      JR    Z,0438H
0428 FE60      CP    60H
042A 280C      JR    Z,0438H
042C 1620      LD    D,20H
042E FE90      CP    90H
0430 2806      JR    Z,0438H
0432 FEA0      CP    A0H
0434 2802      JR    Z,0438H
0436 1610      LD    D,10H
0438 7A        LD    A,D
0439 CDAE04    CALL  04AEH
043C C3E402    JP    02E4H
043F 3E48      LD    A,48H
0441 D332      OUT   (32H),A
0443 CD8F0B    CALL  0B8FH
0446 3E08      LD    A,08H
0448 D332      OUT   (32H),A
044A 3E0A      LD    A,0AH
044C CDAE04    CALL  04AEH
044F C3E402    JP    02E4H
0452 7B        LD    A,E
0453 E6F0      AND   F0H
0455 5F        LD    E,A
0456 56        LD    D,(HL)
0457 7A        LD    A,D
0458 23        INC   HL
0459 FE12      CP    12H
045B DA7804    JP    C,0478H
045E F5        PUSH  AF
045F 3E48      LD    A,48H
QUASI88>
```

## 06 · 원본 Script dump · 현재 Token · 문자 출력 루틴

```text
QUASI88> dump 0x969F #16
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
969F : B8 62 C8 18 48 38 38 39 78 28 B8 38 60 12 60 12 |.b..H889x(.8\`.\`.|

QUASI88> dump 0x0C84 #1
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
0C84 : C8 18 03 02 00 D4 EB D0 EB 00 00 00 00 00 00 00 |................|

QUASI88> disasm 0x0B8F #64
0B8F E5        PUSH  HL
0B90 7A        LD    A,D
0B91 B7        OR    A
0B92 284B      JR    Z,0BDFH
0B94 2A890C    LD    HL,(0C89H)
0B97 ED73DD0B  LD    (0BDDH),SP
0B9B 315000    LD    SP,0050H
0B9E CDE10B    CALL  0BE1H
0BA1 39        ADD   HL,SP
0BA2 CDE10B    CALL  0BE1H
0BA5 39        ADD   HL,SP
0BA6 CDE10B    CALL  0BE1H
0BA9 CDE10B    CALL  0BE1H
0BAC 39        ADD   HL,SP
0BAD CDE10B    CALL  0BE1H
0BB0 39        ADD   HL,SP
0BB1 CDE10B    CALL  0BE1H
0BB4 CDE10B    CALL  0BE1H
0BB7 39        ADD   HL,SP
0BB8 CDE10B    CALL  0BE1H
0BBB 39        ADD   HL,SP
0BBC CDE10B    CALL  0BE1H
0BBF 39        ADD   HL,SP
0BC0 CDE10B    CALL  0BE1H
0BC3 CDE10B    CALL  0BE1H
0BC6 39        ADD   HL,SP
0BC7 CDE10B    CALL  0BE1H
0BCA 39        ADD   HL,SP
0BCB CDE10B    CALL  0BE1H
0BCE CDE10B    CALL  0BE1H
0BD1 39        ADD   HL,SP
0BD2 CDE10B    CALL  0BE1H
0BD5 39        ADD   HL,SP
0BD6 CDE10B    CALL  0BE1H
0BD9 CD060C    CALL  0C06H
0BDC 31FA00    LD    SP,00FAH
0BDF E1        POP   HL
0BE0 C9        RET
0BE1 D3EB      OUT   (EBH),A
0BE3 7B        LD    A,E
0BE4 D3E8      OUT   (E8H),A
0BE6 7A        LD    A,D
0BE7 D3E9      OUT   (E9H),A
0BE9 D3EA      OUT   (EAH),A
0BEB 00        NOP
0BEC 00        NOP
0BED DBE8      IN    A,(E8H)
0BEF 4F        LD    C,A
0BF0 DBE9      IN    A,(E9H)
0BF2 47        LD    B,A
0BF3 D3EB      OUT   (EBH),A
0BF5 13        INC   DE
0BF6 3E07      LD    A,07H
0BF8 D334      OUT   (34H),A
0BFA 3E80      LD    A,80H
0BFC D335      OUT   (35H),A
0BFE 70        LD    (HL),B
0BFF 23        INC   HL
0C00 71        LD    (HL),C
0C01 2B        DEC   HL
0C02 AF        XOR   A
0C03 D335      OUT   (35H),A
0C05 C9        RET
0C06 E5        PUSH  HL
QUASI88>
```

## 07 · Kanji ROM 읽기 시작: break 0BE1h / disasm #24

```text
QUASI88> break 0x0BE1 #1
set break point MAIN - #1 [ PC : 0BE1H ]
QUASI88> go
*** Break at 0BE1H *** ( MAIN[#1] : PC )
[MAIN]
 AF:3800[........] BC:0000  DE:3840  HL:EBD4  IX:0000  PC:0BE1  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530234)
            0B9E CDE10B    CALL  0BE1H
    ------> 0BE1 D3EB      OUT   (EBH),A
            0BE3 7B        LD    A,E
QUASI88> disasm #24
0BE1 D3EB      OUT   (EBH),A
0BE3 7B        LD    A,E
0BE4 D3E8      OUT   (E8H),A
0BE6 7A        LD    A,D
0BE7 D3E9      OUT   (E9H),A
0BE9 D3EA      OUT   (EAH),A
0BEB 00        NOP
0BEC 00        NOP
0BED DBE8      IN    A,(E8H)
0BEF 4F        LD    C,A
0BF0 DBE9      IN    A,(E9H)
0BF2 47        LD    B,A
0BF3 D3EB      OUT   (EBH),A
0BF5 13        INC   DE
0BF6 3E07      LD    A,07H
0BF8 D334      OUT   (34H),A
0BFA 3E80      LD    A,80H
0BFC D335      OUT   (35H),A
0BFE 70        LD    (HL),B
0BFF 23        INC   HL
0C00 71        LD    (HL),C
0C01 2B        DEC   HL
0C02 AF        XOR   A
0C03 D335      OUT   (35H),A
QUASI88>
```

## 08 · 첫 Glyph 행 읽기와 기록 직전 덤프

```text
QUASI88> break 0x0BFE #2
set break point MAIN - #2 [ PC : 0BFEH ]
QUASI88> g
*** Break at 0BFEH *** ( MAIN[#2] : PC )
[MAIN]
 AF:8000[........] BC:0000  DE:3841  HL:EBD4  IX:0000  PC:0BFE  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530377)
            0BFC D335      OUT   (35H),A
    ------> 0BFE 70        LD    (HL),B
            0BFF 23        INC   HL
QUASI88> dump 0xEBD4 #4
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
EBD4 : FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF |................|

QUASI88>
```

## 09 · 세 번의 step · reg · 변경 후 덤프

```text
QUASI88> step
[MAIN]
 AF:8000[........] BC:0000  DE:3841  HL:EBD4  IX:0000  PC:0BFF  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530384)
            0BFE 70        LD    (HL),B
    ------> 0BFF 23        INC   HL
            0C00 71        LD    (HL),C
QUASI88> step
[MAIN]
 AF:8000[........] BC:0000  DE:3841  HL:EBD5  IX:0000  PC:0C00  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530390)
            0BFF 23        INC   HL
    ------> 0C00 71        LD    (HL),C
            0C01 2B        DEC   HL
QUASI88> step
[MAIN]
 AF:8000[........] BC:0000  DE:3841  HL:EBD5  IX:0000  PC:0C01  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530397)
            0C00 71        LD    (HL),C
    ------> 0C01 2B        DEC   HL
            0C02 AF        XOR   A
QUASI88> reg
[MAIN]
 AF:8000[........] BC:0000  DE:3841  HL:EBD5  IX:0000  PC:0C01  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530397)
            0C00 71        LD    (HL),C
    ------> 0C01 2B        DEC   HL
            0C02 AF        XOR   A
QUASI88> dump 0xEBD4 #4
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
EBD4 : FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF FF |................|

QUASI88>
```

## 10 · 두 번째 Glyph 행: g · g

```text
QUASI88> g
*** Break at 0BE1H *** ( MAIN[#1] : PC )
[MAIN]
 AF:0044[.Z...P..] BC:0000  DE:3841  HL:EC24  IX:0000  PC:0BE1  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530456)
            0BA2 CDE10B    CALL  0BE1H
    ------> 0BE1 D3EB      OUT   (EBH),A
            0BE3 7B        LD    A,E
QUASI88> g
*** Break at 0BFEH *** ( MAIN[#2] : PC )
[MAIN]
 AF:8044[.Z...P..] BC:0180  DE:3842  HL:EC24  IX:0000  PC:0BFE  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':3E97  IY:E55C  SP:004E  (ck=214530599)
            0BFC D335      OUT   (35H),A
    ------> 0BFE 70        LD    (HL),B
            0BFF 23        INC   HL
QUASI88>
```

## 11 · 첫 Script Token을 기존 が Token으로 직접 변경

```text
QUASI88> QUASI88> break clearall #0
clear break point MAIN - all
QUASI88> break pc 0x02ED #1
set break point MAIN - #1 [ PC : 02EDH ]
QUASI88> reset
QUASI88> g
*** Break at 02EDH *** ( MAIN[#1] : PC )
[MAIN]
 AF:0044[.Z...P..] BC:005C  DE:FE81  HL:9680  IX:1290  PC:02ED  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':EC71  IY:E55C  SP:00FE  (ck=507152666)
            02EB D335      OUT   (35H),A
    ------> 02ED 5E        LD    E,(HL)
            02EE 23        INC   HL
QUASI88> reg
[MAIN]
 AF:0044[.Z...P..] BC:005C  DE:FE81  HL:9680  IX:1290  PC:02ED  I:00 IM:2 IFF:1
 A':C47D[.Z.H.P.C] B':0000  D':0500  H':EC71  IY:E55C  SP:00FE  (ck=507152666)
            02EB D335      OUT   (35H),A
    ------> 02ED 5E        LD    E,(HL)
            02EE 23        INC   HL
QUASI88> dump 0x969F #16
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
969F : B8 62 C8 18 48 38 38 39 78 28 B8 38 60 12 60 12 |.b..H889x(.8\`.\`.|

QUASI88> write MAIN 0x969F 0xC8
WRITE memory MAIN[ 969FH ] <- C8  (= 200 | -56 | 11001000B )
QUASI88> write MAIN 0x96A0 0x18
WRITE memory MAIN[ 96A0H ] <- 18  (= 24 | +24 | 00011000B )
QUASI88> dump 0x969F #16
addr : +0 +1 +2 +3 +4 +5 +6 +7 +8 +9 +A +B +C +D +E +F
---- : -----------------------------------------------
969F : C8 18 C8 18 48 38 38 39 78 28 B8 38 60 12 60 12 |....H889x(.8\`.\`.|

QUASI88> break clearall #0
clear break point MAIN - all
QUASI88> g
```

## 화면 증거

- `01.PNG` — 정상 ROM 첫 이벤트
- `02.PNG` — ROM 제거 후 동일 장면
- `03.PNG` — 「雨が」가 출력된 화면
- `04.PNG` — `969F~96A0` 수정 뒤 「ががやん」이 표시된 실제 화면

이미지의 원격 저장소 등록 여부는 `images/course06/README.md`를 확인합니다.
