def get_entry():
    value = " "
    if value:
        print(value)
    else:
        print('Empty Value')

def process_ipoteka_data(procent_stavka: float, summa_ipoteki: float, srok_ipoteki: int) -> tuple[float, float, float]:

    mesyacni_platezh = calc_monthly_payment(procent_stavka, summa_ipoteki, srok_ipoteki)
    total_dolg = calc_total_dolg(mesyacni_platezh, srok_ipoteki)
    calc_overpayments = calc_overpayment(total_dolg, summa_ipoteki)
    return mesyacni_platezh, total_dolg, calc_overpayments

def calc_total_dolg(mesyacni_platezh: float, srok_ipoteki: int) -> float:
    return mesyacni_platezh * srok_ipoteki

def calc_overpayment(total_dolg: float, summa_ipoteki: float) -> float:
    return total_dolg - summa_ipoteki

def calc_monthly_payment(procent_stavka: float, summa_ipoteki: float, srok_ipoteki: int) -> float:
    # Рассчитываем месячную процентную ставку
    monthly_rate = procent_stavka / 100 / 12

    # Общее количество платежей
    n = srok_ipoteki
    # Рассчитываем ежемесячный платеж (аннуитетная формула)
    if monthly_rate > 0:
        monhly_payment = (summa_ipoteki * monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)
    else:
        monhly_payment = summa_ipoteki / n  # Если ставка 0, просто делим сумму на количество месяцев
    return monhly_payment