from db_utils import get_session
from models import *

def add_client():
    session = get_session()
    client = Client()
    session.add(client)
    session.commit()

def add_ipoteka(procent_stavka, summa_ipoteki, srok_ipoteki, month_payment, overpayment, obshiDolg):
    session = get_session()
    ipoteka = Ipoteka(procent_stavka=procent_stavka, summa_ipoteki=summa_ipoteki, srok_ipoteki=srok_ipoteki, month_payment=month_payment, overpayment=overpayment, obshiDolg=obshiDolg)
    session.add(ipoteka)
    session.commit()
