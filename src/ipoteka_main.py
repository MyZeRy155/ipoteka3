from import_data import *
print("Считаем ипотеку \n"
      "Для того чтобы высчитать нужную вам информацию, нужно знать следующее:\n1.Срок ипотеки\n2.Сумма Ипотеки\n3.Процентная ставка")
mesyac = " месяц"
mesyaca = " месяца"
mesyacev = " месяцев"


print("Введите срок ипотеки:")
str_srokIpoteki = input()
srokIpoteki = float(str_srokIpoteki)


if str_srokIpoteki.endswith("1") and str_srokIpoteki!= "11" and str_srokIpoteki != "111" and str_srokIpoteki != "211" and str_srokIpoteki != "311":
    print("Срок ипотеки: " + str_srokIpoteki + mesyac)
elif str_srokIpoteki.endswith("2") or str_srokIpoteki.endswith("3") or str_srokIpoteki.endswith("4"):
    print("Срок ипотеки: " + str_srokIpoteki + mesyaca)
else:
    print("Срок ипотеки: " + str_srokIpoteki + mesyacev)


print("Введите сумма ипотеки:")
str_sumIpoteki = float(input())
sumIpoteki = float(str_sumIpoteki)
print(f"Сумма ипотеки: {str_sumIpoteki}")


print("Введите процентную ставку:")
procentStavka = float(input())
print(f"Процентная ставка:   {procentStavka}")


mesyacniPlatezh = sumIpoteki * float(procentStavka) / 12
overpayment = mesyacniPlatezh * srokIpoteki
obshiDolg = overpayment + sumIpoteki



##obshiDolg = float(sumIpoteki) + obshiDolgProcenta

print(f"""Месячный платеж составит: {mesyacniPlatezh} 
      \nОбщий долг по ипотеки составит: 
       {obshiDolg}
       \nОбщая переплата по процентам составит: {overpayment}""")

add_ipoteka(procentStavka, str_sumIpoteki, str_srokIpoteki, mesyacniPlatezh, overpayment, obshiDolg)