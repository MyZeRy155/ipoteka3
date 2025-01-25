from db_utils import get_session
from models import *

def add_client():
    session = get_session()
    client = Client()
    session.add(client)
    session.commit()

def add_mortgage(interest_rate, mortgage_amount, mortgage_term, monhly_payment, overpayment, total_debt):
    session = get_session()
    mortgages = Ipoteka(interest_rate=interest_rate, mortgage_amount=mortgage_amount, mortgage_term=mortgage_term, monhly_payment=monhly_payment, overpayment=overpayment, total_debt=total_debt)
    session.add(mortgages)
    session.commit()

def get_mortgage():
    session = get_session()
    mortgages = session.query(Ipoteka).all()
    return mortgages

all_mortgage = get_mortgage()
for mortgage in all_mortgage:
    print(mortgage.id, mortgage.procent_stavka, mortgage.summa_ipoteki, mortgage.srok_ipoteki, mortgage.month_payment, mortgage.overpayment, mortgage.obshiDolg)