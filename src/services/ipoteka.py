def mortgage_calculation(interest_rate: float, mortgage_amount: float, mortgage_term: int) -> tuple[float, float, float]:

    monhly_payment = calc_monthly_payment(interest_rate, mortgage_amount, mortgage_term)
    total_debt = calc_total_debt(monhly_payment, mortgage_term)
    calc_overpayments = calc_overpayment(total_debt, mortgage_amount)
    return monhly_payment, total_debt, calc_overpayments

def calc_total_debt(monhly_payment: float, mortgage_term: int) -> float:
    return monhly_payment * mortgage_term

def calc_overpayment(total_debt: float, mortgage_amount: float) -> float:
    return total_debt - mortgage_amount

def calc_monthly_payment(interest_rate: float, mortgage_amount: float, mortgage_term: int) -> float:
    # Рассчитываем месячную процентную ставку
    monthly_rate = interest_rate / 100 / 12

    # Общее количество платежей
    amount_ofpayments = mortgage_term
    # Рассчитываем ежемесячный платеж (аннуитетная формула)
    if monthly_rate > 0:
        monhly_payment = (mortgage_amount * monthly_rate * (1 + monthly_rate) ** amount_ofpayments) / ((1 + monthly_rate) ** amount_ofpayments - 1)
    else:
        monhly_payment = mortgage_amount / amount_ofpayments  # Если ставка 0, просто делим сумму на количество месяцев
    return monhly_payment
