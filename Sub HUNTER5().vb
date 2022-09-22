Sub HUNTER5()

'
' HUNTER5 Macro
' Macro recorded 22.6.2022 by r.manov
'

'

Application.ScreenUpdating = False
Windows("05-PROMO-VLOOKUP.xlsm").Activate
R = ActiveCell.ROW
If R = 1 Then MsgBox ("IZBRAN E ZAGLAVNIA RED!!!")
If R = 1 Then End

'PROVERIAVA PROGNOZATA NA VERIGATA
If Cells(R, "M").Value > 0 Then PROGNOZAVERIGA = Cells(R, "M").Value

Cells(R, 8).Select
ActiveWindow.ScrollRow = ActiveCell.ROW
'DA NAPRAVI PROMOCIATA I TOGAVA DA PROVERI DALI E OTMENENA

'=============================================================================
'PROVERIAVA DALI E OTMENENA I AKO DA - KAKVO DA PRAVI
Cells(R, 12).Select
If ActiveCell.Value = ("ÎÒÌÅÍÅÍÀ") Then
MsgBox ("PROMOCIATA E OTMENENA!!!")
'AKO E OTMENENA DA PROVERI DALI E OCVETENA I DA LIKVIDIRA CVETOVETE
Cells(R, 1).Select
'KOPIRA NA4ALNA I KRAINA DATA NA PROMOCIATA
Selection.Resize(1, 2).Select
Selection.Copy
Cells(R, 31).Select
Selection.PasteSpecial Paste:=xlValues, Operation:=xlNone, _
        SkipBlanks:=False, Transpose:=False
'FORMATIRA DATITE
Selection.NumberFormat = "dd/mm/yyyy ""ã."";@"
'IZ4ISLIAVA PREDHODNA I PROMOCIONALNI SEDMICI
Cells(R, 33).Select
ActiveCell.FormulaR1C1 = "=(RC[+1])-1"
Cells(R, 34).Select
ActiveCell.FormulaR1C1 = "=WEEKNUM(RC[-3],2)-0" 'SMENIA SE PRI SMIANA NA GODINITE
Cells(R, 35).Select
ActiveCell.FormulaR1C1 = "=WEEKNUM(RC[-3],2)-0" 'SMENIA SE PRI SMIANA NA GODINITE
P = Cells(R, 33).Value
E = Cells(R, 35).Value
'TARSI ART. NOMER NA PROMO PRODUKTA V F1
N = Cells(R, 8).Value
Cells(R, 8).Select
'Cells(R + 1, 8).Select   'IZBIRA SLEDVA6TIA RED S ART.NOMER - GOTOVNOST SLEDVA6TO PUSKANE
If Cells(R, "K").Value <> 0 Then MsgBox (Cells(R, "K").Value)

'ZAPO4VA SA6INSKOTO TARSENE NA ART.NOMER
Windows("01-SEDMI4NI PRODAJBI.xlsm").Activate
Columns(1).Select
Selection.Find(What:=N, After:=ActiveCell, LookIn:=xlValues, LookAt:= _
        xlWhole, SearchOrder:=xlByRows, SearchDirection:=xlNext, MatchCase:=False _
        , SearchFormat:=False).Activate
ActiveWindow.ScrollRow = ActiveCell.ROW
BR = ActiveCell.ROW
'TRAGVA PO REDA DOKATO SRE6NE ZELENO ILI JALTO ZA DA OTIDE V AKTUALNATA GODINA, A NE V STARATA
Cells(BR, 3).Select
Do While Selection.Interior.ColorIndex <> 35 And Selection.Interior.ColorIndex <> 4 And Selection.Interior.ColorIndex <> 6
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
'PROVERIAVA DALI IZBRANATA SEDMICA E PREDHODNA
BK = ActiveCell.Column
Do Until Cells(2, BK).Value >= P
'If Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Then
'ActiveCell.Offset(0, 1).Select
'BK = BK + 1
'Else
BK = BK + 1
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
'End If
Loop
'OCVETIAVA V ZELENO I NAMALIAVA PROMOCIONALNITTE SEDMICI
If Cells(2, BK).Value = P And Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Then

'PROVERIAVA CVETA NA PREDNATA KLETKA I ZAPOMNIA STOINOSTTA I
'!!!!!!!!!!!!POTENCIALNO ZACIKLIANE PRI POSLEDNITE SEDMICI - DA SE REGULIRA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Do Until Selection.Interior.ColorIndex = 35 Or Selection.Interior.ColorIndex = 4 Or Selection.Interior.ColorIndex = 6
ActiveCell.Offset(0, 3).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
S = ActiveCell.Value
Cells(BR, BK).Select
'[Else BK = BK + 1 AND ActiveCell.Offset(0, 1).Select]
End If

'OCVETIAVA V ZELENO I NAMALIAVA PROMOCIONALNITTE SEDMICI
Do While Cells(2, BK).Value >= P And Cells(2, BK).Value <= E And Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36
ActiveCell.Value = S
With Selection.Interior
        .ColorIndex = 4
        .Pattern = xlSolid
    End With
    'DA SLOJI KOMENTAR V KLETKATA
    '!!!!!!!!!!!!!!!!DA SE PROVERI DALI IMA VE4E KOMENTAR V KLETKATA!!!!!!!!
    'Application.CutCopyMode = False
    ActiveCell.AddComment
    'ActiveCell.Comment.Visible = False
    ActiveCell.Comment.Text Text:="r.manov:" & Chr(10) & "OTMENENA PROMOCIA!"
    ActiveCell.Offset(0, 1).Select
    S = S * 1.015
    BK = BK + 1
Loop

ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=5
ActiveCell.EntireRow.Select
Application.ScreenUpdating = True
Else



'PRIKLU4VA S DEISTVIATA PRI OTMENENA PROMOCIA
'===================================================================================

'DEISTVIA PRI NE OTMENENA PROMOCIA

Cells(R, 1).Select
'KOPIRA NA4ALNA I KRAINA DATA NA PROMOCIATA
Selection.Resize(1, 2).Select
Selection.Copy
Cells(R, 31).Select
Selection.PasteSpecial Paste:=xlValues, Operation:=xlNone, _
        SkipBlanks:=False, Transpose:=False
'FORMATIRA DATITE
Selection.NumberFormat = "dd/mm/yyyy ""ã."";@"
'IZ4ISLIAVA PREDHODNA I PROMOCIONALNI SEDMICI
Cells(R, 33).Select
ActiveCell.FormulaR1C1 = "=(RC[+1])-1"
Cells(R, 34).Select
ActiveCell.FormulaR1C1 = "=WEEKNUM(RC[-3],2)-0" 'SMENIA SE PRI SMIANA NA GODINITE
Cells(R, 35).Select
ActiveCell.FormulaR1C1 = "=WEEKNUM(RC[-3],2)-0" 'SMENIA SE PRI SMIANA NA GODINITE
P = Cells(R, 33).Value
E = Cells(R, 35).Value
'TARSI ART. NOMER NA PROMO PRODUKTA V F1
N = Cells(R, 8).Value
Cells(R, 8).Select
'DA SE OTMENI KOGATO SVAR6IM Cells(R + 1, 8).Select   'IZBIRA SLEDVA6TIA RED S ART.NOMER - GOTOVNOST SLEDVA6TO PUSKANE
If Cells(R, "K").Value <> 0 Then MsgBox (Cells(R, "K").Value)
Cells(R + 1, 8).Select

'ZAPO4VA SA6INSKOTO TARSENE NA ART.NOMER
Windows("01-SEDMI4NI PRODAJBI.xlsm").Activate
Columns(1).Select
Selection.Find(What:=N, After:=ActiveCell, LookIn:=xlValues, LookAt:= _
        xlWhole, SearchOrder:=xlByRows, SearchDirection:=xlNext, MatchCase:=False _
        , SearchFormat:=False).Activate
ActiveWindow.ScrollRow = ActiveCell.ROW
BR = ActiveCell.ROW
'MARKIRA KOLONA BE KATO PROMOCIONALNA
'Cells(BR, "BE").Select
Cells(BR, "BE").Value = 1
'TRAGVA PO REDA DOKATO SRE6NE ZELENO ILI JALTO ZA DA OTIDE V AKTUALNATA GODINA, A NE V STARATA
Cells(BR, 3).Select
Do While Selection.Interior.ColorIndex <> 35 And Selection.Interior.ColorIndex <> 4 And Selection.Interior.ColorIndex <> 6
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
'PROVERIAVA DALI IZBRANATA SEDMICA E PREDHODNA I ZELENIASVA
BK = ActiveCell.Column
GREENCOL = BK
Do Until Cells(2, BK).Value >= P
If Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Then
ActiveCell.Offset(0, 1).Select
BK = BK + 1
If ActiveCell.Column > 112 Then GoTo ENDINGS
Else
BK = BK + 1
With Selection.Interior
        .ColorIndex = 4
        .Pattern = xlSolid
    End With
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
End If
Loop

'======================================
'SABIRANE NA DANNI I IZ4ISLENIA

'OCVETIAVA I ZAVI6AVA PROMOCIONALNITTE SEDMICI
If Cells(2, BK).Value = P And Selection.Interior.ColorIndex <> 39 And Selection.Interior.ColorIndex <> 36 Then


'1.DA PROVERI DALI IMA STARI PROMOCII - AKO NIAMA DA NAPRAVI H2

'PROMORESULT3=DELETEYELLOW
    
    '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
YELLOW:
    'DA SELECTIRA REDA DO PARVATA ZELENA
    Cells(BR, 3).Select
    NEWCOL = GREENCOL - 3
    Selection.Resize(1, NEWCOL).Select
    'BROI PROMOCIITE
    YELLOWCOUNT = 0
    For Each CELL In Selection
        If CELL.Interior.ColorIndex = 36 Then
            YELLOWCOUNT = YELLOWCOUNT + 1
        End If
    Next CELL

'===========================================
'PROVERIAVA DALI IMA PROMOCII - AKO NIAMA *H2*
If YELLOWCOUNT = 0 Then

Cells(BR, 3).Select
'TRAGVA PO REDA DOKATO SRE6NE ZELENO ILI JALTO
Do While Selection.Interior.ColorIndex <> 35 And Selection.Interior.ColorIndex <> 4 And Selection.Interior.ColorIndex <> 6
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
'PROVERIAVA DALI IZBRANATA SEDMICA E PREDHODNA I ZELENIASVA
BK = ActiveCell.Column
Do Until Cells(2, BK).Value >= P
If Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Then
ActiveCell.Offset(0, 1).Select
BK = BK + 1
If ActiveCell.Column > 112 Then GoTo ENDINGS
Else
BK = BK + 1
With Selection.Interior
        .ColorIndex = 4
        .Pattern = xlSolid
    End With
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
End If
Loop
'OCVETIAVA I ZAVI6AVA PROMOCIONALNITTE SEDMICI
If Cells(2, BK).Value = P And Selection.Interior.ColorIndex <> 39 And Selection.Interior.ColorIndex <> 36 Then
t = InputBox("VAVEDI ZAVI6AVANE ZA 1PW")
I = Val(t)
ActiveCell.Value = ActiveCell.Value * (I * 0.65)

'SRAVNIAVA PROGNOZATA NA VERIGATA S PREDHODNATA
If PROGNOZAVERIGA <> 0 Then ActiveCell.Value = PROGNOZAVERIGA

With Selection.Interior
        .ColorIndex = 36
        .Pattern = xlSolid
    End With
    ActiveCell.Offset(0, 1).Select
[Else BK = BK + 1 AND ActiveCell.Offset(0, 1).Select]
End If
If Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Or ActiveCell.Offset(0, 1).Interior.ColorIndex = 39 Then
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=2
ActiveCell.EntireRow.Select
Application.ScreenUpdating = True
Else
Cells(BR, BK + 1).Select
BK = BK + 1
Do While Cells(2, BK).Value <= E
ActiveCell.Value = ActiveCell.Value * I
With Selection.Interior
        .ColorIndex = 39
        .Pattern = xlSolid
    End With
BK = BK + 1
I = I * 0.69
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
'TRAGVA PO REDA I ZELENIASVA DO DOSTIGANE NA BIALA KLETKA
Do Until Selection.Interior.ColorIndex <> 35 And Selection.Interior.ColorIndex <> 4 And Selection.Interior.ColorIndex <> 6
With Selection.Interior
        .ColorIndex = 4
        .Pattern = xlSolid
    End With
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
Loop
'OT PARVATA BIALA KLETKA TRAGVA NAZAD PO REDA DO PARVATA SRE6NATA PROMOCIA
Do Until Selection.Interior.ColorIndex = 39
ActiveCell.Offset(0, -1).Select
Loop
End If
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=5
ActiveCell.EntireRow.Select
Application.ScreenUpdating = True
End
End If


Else

'SRAVNIAVA PROGNOZATA NA VERIGATA S PREDHODNATA
If Cells(2, BK).Value <> P Or Cells(2, BK + 1).Value <> P Then W = P - Cells(2, BK).Value
Cells(BR, BK + W).Select
If PROGNOZAVERIGA > Cells(BR, BK + W).Value Or PROGNOZAVERIGA > Cells(BR, BK + W + 1).Value Then
'ActiveCell.Value = PROGNOZAVERIGA
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=5
Application.ScreenUpdating = True
MsgBox ("PROGNOZATA NA VERIGATA E PO GOLIAMA: " & PROGNOZAVERIGA)
End
End If


On Error Resume Next
Windows("05-PROMO-VLOOKUP.xlsm").Activate
Cells(R + 1, 8).Select
ActiveWindow.ScrollRow = ActiveCell.ROW
ActiveCell.EntireRow.Select
Application.ScreenUpdating = True
End 'DA PRIKLU4I AKO PROMOCIATA VE4E E NAPRAVENA

End If



'KRAI NA DEISTVIATA PRI LIPSA NA STARI PROMOCII
'===========================================
'2 AKO IMA STARI PROMOCII - PRODALJAVA

'===============OPIT 07.08.2013
    'NE E NUJNO DA SE ZANULIAVAT
    'AVERAGE0 = 0
    'AVERAGE1 = 0
    'AVERAGE2 = 0
    'AVERAGE3 = 0
    'AVERAGE4 = 0
    'AVERAGE5 = 0
    'AVERAGE6 = 0
    'AVERAGE7 = 0
    
    'PROMO1 = 0 'BROIA4I ZA PROMOCIITE S TOLKOVA SEDMICI
    'PROMO2 = 0
    'PROMO3 = 0
    'PROMO4 = 0
    'PROMO5 = 0
    'PROMO6 = 0
    'PROMO7 = 0
     
     'dolnite 20 reda da se sprat i da se napravi po drug na4in
'    For Each CELL In Selection
    'IZ4ISLIAVA SREDNATA OT TRI SDEDMICI PREDI PREDHODNATA
       ' If CELL.Interior.ColorIndex = 0 Then
       ' TEMP = 0
       ' CELL.Value = TEMP
       ' ActiveCell.FormulaR1C1 = "=AVERAGE(RC[-3]:RC[-1])"
       ' Selection.Copy
       ' Selection.PasteSpecial Paste:=xlPasteValues, Operation:=xlNone, SkipBlanks _
       ' :=False, Transpose:=False
        'Application.CutCopyMode = False
       ' CELL.Value = SUBPROMO
        'TEMP = CELL.Value
       ' SUBPROMO9 = SUBPROMO9 + SUBPROMO
        'PREPROMO = PREPROMO + 1
    'gornite 20 reda da se sprat i da se napravi po drug na4in
        'AVERAGEc = 0
        'PROMOq = 0
    For Each CELL In Selection
    'IZ4ISLIAVA SREDNATA OT TRI SDEDMICI PREDI PREDHODNATA
       'If CELL.Interior.ColorIndex = 36 Then
       ' CELL.Offset(0, -1).Select
       ' jk = ActiveCell.Column   'ZAPISVA KOLONA NA jalta KLETKA
       ' jr = ActiveCell.ROW       'ZAPISVA REDA NA jalta KLETKA
        'For I = 1 To 5
        'CELL.Offset(0, -1).Select
       'If CELL.Interior.ColorIndex = 0 Or CELL.Interior.ColorIndex = 2 Then
        'AVERAGEc = AVERAGEc + CELL.Offset(0, -1).Value + CELL.Offset(0, -2).Value + CELL.Offset(0, -3).Value + CELL.Offset(0, -4).Value + CELL.Offset(0, -5).Value
        'PROMOq = PROMOq + 1
       ' ActiveCell.Offset(0, -1).Select
        'End If
       ' Next I
       ' CELL.Select
       ' End If
       ' AVERAGEc = AVERAGEc / PROMOq


       
    'For Each CELL In Selection
    'IZ4ISLIAVA JALTITE KLETKI I PARVA PROMOCIONALANA
        If CELL.Interior.ColorIndex = 36 Then
        AVERAGEc = (AVERAGEc + CELL.Offset(0, -1).Value + CELL.Offset(0, -2).Value + CELL.Offset(0, -3).Value + CELL.Offset(0, -4).Value + CELL.Offset(0, -5).Value) / 5
        AVERAGE0 = AVERAGE0 + CELL.Value
        AVERAGE1 = AVERAGE1 + CELL.Offset(0, 1).Value
        PROMO1 = PROMO1 + 1
    'IZ4ISLIAVA VTORA PROMOCIONALNA
        If CELL.Offset(0, 2).Interior.ColorIndex = 39 And CELL.Offset(0, 1).Interior.ColorIndex = 39 Then
        AVERAGE2 = AVERAGE2 + CELL.Offset(0, 2).Value
        PROMO2 = PROMO2 + 1
        End If
    'IZ4ISLIAVA TRETA PROMOCIONALNA
        If CELL.Offset(0, 3).Interior.ColorIndex = 39 And CELL.Offset(0, 2).Interior.ColorIndex = 39 Then
        AVERAGE3 = AVERAGE3 + CELL.Offset(0, 3).Value
        PROMO3 = PROMO3 + 1
        End If
    'IZ4ISLIAVA 4ETVARTA PROMOCIONALNA
        If CELL.Offset(0, 4).Interior.ColorIndex = 39 And CELL.Offset(0, 3).Interior.ColorIndex = 39 Then
        AVERAGE4 = AVERAGE4 + CELL.Offset(0, 4).Value
        PROMO4 = PROMO4 + 1
        End If
    'IZ4ISLIAVA PETA PROMOCIONALNA
        If CELL.Offset(0, 5).Interior.ColorIndex = 39 And CELL.Offset(0, 4).Interior.ColorIndex = 39 Then
        AVERAGE5 = AVERAGE5 + CELL.Offset(0, 5).Value
        PROMO5 = PROMO5 + 1
        End If
    'IZ4ISLIAVA 6ESTA PROMOCIONALNA
        If CELL.Offset(0, 6).Interior.ColorIndex = 39 And CELL.Offset(0, 5).Interior.ColorIndex = 39 Then
        AVERAGE6 = AVERAGE6 + CELL.Offset(0, 6).Value
        PROMO6 = PROMO6 + 1
        End If
    'IZ4ISLIAVA SEDMA PROMOCIONALNA
        If CELL.Offset(0, 7).Interior.ColorIndex = 39 And CELL.Offset(0, 6).Interior.ColorIndex = 39 Then
        AVERAGE7 = AVERAGE7 + CELL.Offset(0, 7).Value
        PROMO7 = PROMO7 + 1
        End If
        End If 'GOLIAM IF ZA RED 292
    Next CELL
    
    
   'SUBPROMO9 = SUBPROMO9 / PREPROMO 'IZ4ISLIAVA SREDNOTO NA SREDNITE NA TRITE PREDPROMOCIONALNI SEDMICI
    
    AVERAGE0 = AVERAGE0 / YELLOWCOUNT
    AVERAGE1 = AVERAGE1 / PROMO1 'NE TRIABVA DA SE DELIAT NA YELLOWCOUNT
    On Error Resume Next
    AVERAGE2 = AVERAGE2 / PROMO2
    AVERAGE3 = AVERAGE3 / PROMO3
    AVERAGE4 = AVERAGE4 / PROMO4
    AVERAGE5 = AVERAGE5 / PROMO5
    AVERAGE6 = AVERAGE6 / PROMO6
    AVERAGE7 = AVERAGE7 / PROMO7
    

'iz4isliava srednata na prognozite i korekcionen koeficient spriamo tiah
srednaprognoza = 0
broiach = 0
Cells(BR, BK).Select
'Do Until ActiveCell.Offset(0, -5).Interior.ColorIndex = 39 or ActiveCell.Offset(0, -5).Interior.ColorIndex = 36 As ObjectType = lower To Upper
For I = 0 To 4
    If ActiveCell.Offset(0, -I).Interior.ColorIndex = 35 Or ActiveCell.Offset(0, -I).Interior.ColorIndex = 4 Or ActiveCell.Offset(0, -I).Interior.ColorIndex = 6 Then
        broiach = broiach + 1
        srednaprognoza = srednaprognoza + ActiveCell.Offset(0, -I).Value
    End If
    
ActiveCell.Offset(0, -1).Select
'srednaprognoza = srednaprognoza + ActiveCell.Value
'broiach = broiach + 1

Next I


'Loop
srednaprognoza = srednaprognoza / broiach

control_koef = srednaprognoza / AVERAGEc

If control_koef > 1.7 Then control_koef = 1.7
If control_koef < 0.3 Then control_koef = 0.3

AVERAGE0 = AVERAGE0 * control_koef
AVERAGE1 = AVERAGE1 * control_koef
AVERAGE2 = AVERAGE2 * control_koef
AVERAGE3 = AVERAGE3 * control_koef
AVERAGE4 = AVERAGE4 * control_koef
AVERAGE5 = AVERAGE5 * control_koef
AVERAGE6 = AVERAGE6 * control_koef
AVERAGE7 = AVERAGE7 * control_koef



  '===============OPIT 07.08.2013
  
'==============================
'PEISTVANE NA DANNITE I OCVETIAVANE NA SEDMICITE

Cells(BR, BK).Select
If Selection.Interior.ColorIndex = 39 Or Selection.Interior.ColorIndex = 36 Or ActiveCell.Offset(0, 1).Interior.ColorIndex = 39 Then
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=2
ActiveCell.EntireRow.Select
Application.ScreenUpdating = True
Else
With Selection.Interior
        .ColorIndex = 36
        .Pattern = xlSolid
    End With
    ActiveCell.Value = AVERAGE0
ActiveCell.Offset(0, 1).Select
If ActiveCell.Column > 112 Then GoTo ENDINGS
ActiveCell.Value = AVERAGE1
[Else BK = BK + 1 AND ActiveCell.Offset(0, 1).Select]
End If

'SRAVNIAVA PROGNOZATA NA VERIGATA S AVERAGE0
If PROGNOZAVERIGA > AVERAGE0 Then MsgBox ("PROGNOZATA NA VERIGATA E PO GOLIAMA: " & PROGNOZAVERIGA)

'===================
'VARIANT BEZ OBHOJDANE
BK = BK + 1
F = E - P
Selection.Resize(1, F).Select
With Selection.Interior
        .ColorIndex = 39
        .Pattern = xlSolid
    End With

'PROVERKA DALI IMA AVERAGE2, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE2 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 1).Value = AVERAGE2
BK = BK + 1

'PROVERKA DALI IMA AVERAGE3, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE3 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 2).Value = AVERAGE3
BK = BK + 1

'PROVERKA DALI IMA AVERAGE4, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE4 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 3).Value = AVERAGE4
BK = BK + 1

'PROVERKA DALI IMA AVERAGE5, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE5 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 4).Value = AVERAGE5
BK = BK + 1

'PROVERKA DALI IMA AVERAGE6, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE6 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 5).Value = AVERAGE6
BK = BK + 1

'PROVERKA DALI IMA AVERAGE7, AKO NIAMA OSTANALITE AVERAGE SA6TO GI NIAMA
If Not AVERAGE7 = 0 And Cells(2, BK + 1).Value <= E Then
ActiveCell.Offset(0, 6).Value = AVERAGE7
BK = BK + 1

End If
End If
End If
End If
End If

End If

GoTo SLIDE:
'ZAVI6AVA PROMOCIONALNITE SEDMICI SLED PARVATA, AKO NIAMA PO RAN6NI AVERAGE2

For D = 1 To F - 1
ActiveCell.Offset(0, D).Value = 2.2 * ActiveCell.Offset(0, D).Value
BK = BK + 2
Next D



'OPERATIVEN RED

'VARIANT BEZ OBHOJDANE
'===================

'KRAI NA IZ4ISLENIATA I PEISTA
'======================================


SLIDE:

Cells(BR, BK + 1).Select
'TRAGVA PO REDA I ZELENIASVA DO DOSTIGANE NA BIALA KLETKA
Do Until Selection.Interior.ColorIndex <> 35 And Selection.Interior.ColorIndex <> 4 And Selection.Interior.ColorIndex <> 6
With Selection.Interior
        .ColorIndex = 4
        .Pattern = xlSolid
    End With
ActiveCell.Offset(0, 1).Select
Loop
'OT PARVATA BIALA KLETKA TRAGVA NAZAD PO REDA DO PARVATA SRE6NATA PROMOCIA
'Do Until Selection.Interior.ColorIndex = 39
'ActiveCell.Offset(0, -1).Select
'Loop
'Cells(BR, K + F - 1).Select
Cells(BR, BK).Select
End If
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=5




End



ENDINGS:
ActiveWindow.ScrollColumn = ActiveCell.Column
ActiveWindow.SmallScroll ToLEFT:=5
'ActiveCell.EntireRow.Select
Windows("05-PROMO-VLOOKUP.xlsm").Activate
Application.ScreenUpdating = True

'SRAVNIAVA PROGNOZATA NA VERIGATA S AVERAGE0
If PROGNOZAVERIGA > AVERAGE0 Then MsgBox ("PROGNOZATA NA VERIGATA E PO GOLIAMA: " & PROGNOZAVERIGA)

End Sub


