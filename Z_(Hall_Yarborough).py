import math
shod = 0.00001


# Объемные доли компонентов газа
c1 = 0.9788  # метан
c2 = 0.0082  # этан
N2 = 0.0109  # азот
CO2 = 0.0021  # диоксид углерода

sum_comp = c1 + c2 + N2 + CO2
# print("sum_comp = " + str(sum_comp))

# Давления и температура
P_ish = 0.75  # МПа
T_ish = 273.65  # Kelvin degree (0.5 Celsius degree)

# Критические давления и температуры для компонентов
c1_Pc = 4.5988
c1_Tc = 190.555
c2_Pc = 4.882
c2_Tc = 305.83
N2_Pc = 3.399
N2_Tc = 126.25
CO2_Pc = 7.387
CO2_Tc = 304.15

# Критические P смеси
c1_Ppc = c1_Pc * c1
# print("c1_Ppc = " + str(c1_Ppc))
c2_Ppc = c2_Pc * c2
# print("c2_Ppc = " + str(c2_Ppc))
N2_Ppc = N2_Pc * N2  #
# print("N2_Ppc = " + str(N2_Ppc))
CO2_Ppc = CO2_Pc * CO2
# print("CO2_Ppc = " + str(CO2_Ppc))

# Критические T смеси
c1_Tpc = c1_Tc * c1
# print("c1_Tpc = " + str(c1_Tpc))
c2_Tpc = c2_Tc * c2
# print("c2_Tpc = " + str(c2_Tpc))
N2_Tpc = N2_Tc * N2
# print("N2_Tpc = " + str(N2_Tpc))
CO2_Tpc = CO2_Tc * CO2
# print("CO2_Tpc = " + str(CO2_Tpc))

# Сумма критических Р и T смеси
Sum_Ppc = c1_Ppc + c2_Ppc + N2_Ppc + CO2_Ppc
Sum_Tpc = c1_Tpc + c2_Tpc + N2_Tpc + CO2_Tpc
# print("P = " + str(Sum_Ppc) + "\n" + "T = " + str(Sum_Tpc))

# Приведенные Р и T смеси
Ppr = P_ish / Sum_Ppc
Tpr = T_ish / Sum_Tpc
# print("Ppr = " + str(Ppr) + "\n" + "Tpr = " + str(Tpr))

# |||||||||||||||||||||||||||||||||||||||||||||||||

# ДЛЯ РАСЧЕТА ПО МЕТОДУ ХОЛЛА-ЯРБОРО (Hall-Yarborough)

# Обратная величина приведенной T (t)
t = Sum_Tpc / T_ish
print("t = " + str(t))

# Cлагаемое "приведенной" плотности уравнения Холла-Ярборо (на основе ур-я Стерлинга-Карнагана)
# первое
stepen = float(-1.2 * (1 - t) ** 2)
Perv = -0.06125 * Ppr * t * math.exp(stepen)
print("Perv = " + str(Perv))

yy = 0
for y in range(0, 131072, 1):
    yy = (y/131072)
    dva = ((yy + yy ** 2 + yy ** 3 - yy ** 4) / (1 - yy) ** 3)
    tri = ((14.76 * t - 9.76 * t ** 2 + 4.58 * t ** 3) * yy ** 2)
    four = (90.7 * t - 242.2 * t ** 2 + 42.4 * t ** 3) * yy ** (2.18 + 2.82 * t)

    Shod_end = Perv + dva - tri + four

    if Shod_end >= shod:
        print("dva = " + str(dva))
        print("tri = " + str(tri))
        print("four = " + str(four))
        print("yy = " + str(yy))

        break

z = math.fabs(Perv / yy)
print("z = " + str(z))

# Next
# # lbl_Z_HallYarborough:
#                 'MsgBox("y = " & y) : MsgBox("dva = " & dva) : MsgBox("tri = " & tri)
#                 'MsgBox("four = " & four) : MsgBox("Shod_end = " & Shod_end)
#                 Z = Math.Abs(Perv / y)
#                 If .TB_Z_Accuracy.Text = "" Or .TB_Z_Accuracy.Text = "0" Then .TB_Z_Accuracy.Text = "3" 'число знаков после запятой по Z
#                 .TB_Z.Text = FormatNumber(Z, .TB_Z_Accuracy.Text)
