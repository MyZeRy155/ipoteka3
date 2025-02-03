from db_utils import get_session
from models import *
import hashlib
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.env")

protected_salt = os.getenv('PROTECTED_SALT')

from datetime import datetime


def add_client():
    session = get_session()
    client = Client()
    session.add(client)
    session.commit()


def add_mortgage(interest_rate, mortgageamount, mortgage_term, monhly_payment, overpayment, total_debt):
    session = get_session()
    mortgages = Ipoteka(interest_rate=interest_rate, mortgageamount=mortgageamount, mortgage_term=mortgage_term, monhly_payment=monhly_payment, overpayment=overpayment, total_debt=total_debt)
    session.add(mortgages)
    session.commit()

def get_mortgage():
    session = get_session()
    mortgages = session.query(Ipoteka).all()
    return mortgages

all_mortgage = get_mortgage()
for mortgage in all_mortgage:
    print(mortgage.id, mortgage.procent_stavka, mortgage.summa_ipoteki, mortgage.srok_ipoteki, mortgage.month_payment, mortgage.overpayment, mortgage.obshiDolg)

   ## register and authentication

   ## хешируем пароль
def hash_password(password:str):
    salt = protected_salt
    password_salt = password + salt
    hashed_password = hashlib.md5(password_salt.encode())
    return hashed_password.hexdigest()

    ## проверяем пароль
def check_password(password:str, hash_pass):
     salt = protected_salt
     password_salt = password + salt
     decrypted_text = hashlib.md5(password_salt.encode()).hexdigest()
     if hash_pass != decrypted_text:
         return False
     else:
         return True

def register(username:str, password:str):
    session = get_session()
    hash_pass = hash_password(password)
    user = User(username=username, password=str(hash_pass))
    session.add(user)
    session.commit()

def login_in(username, password):
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    if user and check_password(password, user.password):
        return True
    return False

def register_user(username, password):
    session = get_session()
    hash_pass = hash_password(password)
    created_at = datetime.now()
    user = User(username=username,
                password=str(hash_pass),
                created_at=created_at
    )
    session.add(user)
    session.commit()