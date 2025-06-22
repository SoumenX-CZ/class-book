.MODEL SMALL
.STACK 100h

.DATA
students DB "Anna",0,"David",0,"Lukas",0
status   DB 3 DUP('N')  ; 'P' = přítomen, 'N' = nepřítomen
menu     DB 13,10, "Dochazka:",13,10, "$"
prompt1  DB 13,10,"Zadej cislo studenta (0-2): $"
prompt2  DB 13,10,"1 - Prítomen, 0 - Nepritomen: $"
done     DB 13,10,"Zaznam ulozen.$"

.CODE
MAIN:
    MOV AX, @DATA
    MOV DS, AX

Start:
    LEA DX, menu
    MOV AH, 09h
    INT 21h

    LEA DX, prompt1
    MOV AH, 09h
    INT 21h

    MOV AH, 01h       ; vstup studenta
    INT 21h
    SUB AL, '0'
    MOV BL, AL

    LEA DX, prompt2
    MOV AH, 09h
    INT 21h

    MOV AH, 01h       ; vstup přítomnosti
    INT 21h
    SUB AL, '0'
    CMP AL, 1
    JE  MarkPresent

MarkAbsent:
    MOV AL, 'N'
    JMP SaveStatus
MarkPresent:
    MOV AL, 'P'
SaveStatus:
    MOV SI, OFFSET status
    ADD SI, BX
    MOV [SI], AL

    LEA DX, done
    MOV AH, 09h
    INT 21h

    JMP Start

END MAIN