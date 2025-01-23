def get_entry():
    value = " "
    if value:
        print(value)
    else:
        print('Empty Value')

def func_calc_ipoteka(str_procent_stavka, str_summa_ipoteki, str_srok_ipoteki):
    # Преобразуем входные параметры
    procent_stavka = float(str_procent_stavka) / 100
    summa_ipoteki = float(str_summa_ipoteki)
    srok_ipoteki = int(str_srok_ipoteki)

    # Рассчитываем месячную процентную ставку
    monthly_rate = procent_stavka / 12

    # Общее количество платежей
    n = srok_ipoteki

    # Рассчитываем ежемесячный платеж (аннуитетная формула)
    if monthly_rate > 0:
        mesyacniPlatezh = (summa_ipoteki * monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
    else:
        mesyacniPlatezh = summa_ipoteki / n  # Если ставка 0, просто делим сумму на количество месяцев

    obshiDolg = mesyacniPlatezh * n
    overpayment = obshiDolg - summa_ipoteki
    return obshiDolg, mesyacniPlatezh, overpayment