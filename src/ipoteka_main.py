print("Считаем ипотеку \n"
      "Для того чтобы высчитать нужную вам информацию, нужно знать следующее:\n1.Срок ипотеки\n2.Сумма Ипотеки\n3.Процентная ставка")
mesyac = " месяц"
mesyaca = " месяца"
mesyacev = " месяцев"
print("Введите срок ипотеки:")
srokIpoteki = input()
if srokIpoteki.endswith("1") and srokIpoteki!= "11" and srokIpoteki != "111" and srokIpoteki != "211" and srokIpoteki != "311":
    print("Срок ипотеки: " + srokIpoteki + mesyac)
elif srokIpoteki.endswith("2") or srokIpoteki.endswith("3") or srokIpoteki.endswith("4"):
    print("Срок ипотеки: " + srokIpoteki + mesyaca)
else:
    print("Срок ипотеки: " + srokIpoteki + mesyacev)

print("Введите сумма ипотеки:")
sumIpoteki = input()
print("Сумма ипотеки: " + sumIpoteki)

print("Введите процентную ставку:")
procentStavka = input()
print("Процентная ставка: " + procentStavka)

mesyacniPlatezh = float(sumIpoteki) * float(procentStavka) / 12

obshiDolgProcenta = mesyacniPlatezh * float(srokIpoteki)

obshiDolg = float(sumIpoteki) + obshiDolgProcenta

print("Месячный платеж составит: " + str(mesyacniPlatezh) +
      "\nОбщий долг по ипотеки составит: "
      + str(obshiDolg)
      + "\nОбщая переплата по процентам составит: " + str(obshiDolgProcenta))