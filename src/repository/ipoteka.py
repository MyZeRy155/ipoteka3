from datetime import timezone, datetime
from sqlalchemy.exc import IntegrityError
from db_utils import get_session
from models import *
import hashlib
from dotenv import load_dotenv
import os
from exceptions import UserExistsError, InvalidCredentialsError, TemporaryPasswordExpiredError, UserNotFoundError

load_dotenv(dotenv_path="config.env")

protected_salt = os.getenv('PROTECTED_SALT')

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
    print(mortgage.id, mortgage.interest_rate, mortgage.mortgageamount, mortgage.mortgage_term, mortgage.monhly_payment, mortgage.overpayment, mortgage.total_debt)

def hash_password(password: str):
    salt = protected_salt
    password_salt = password + salt
    hashed_password = hashlib.md5(password_salt.encode())
    return hashed_password.hexdigest()

def check_password(password: str, hash_pass):
    salt = protected_salt
    password_salt = password + salt
    decrypted_text = hashlib.md5(password_salt.encode()).hexdigest()
    if hash_pass != decrypted_text:
        return False
    else:
        return True

def register(username: str, password: str | None, is_temporary: bool = False):
    with get_session() as session:
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            raise UserExistsError()

        if password is None:
            raise ValueError("Пароль должен быть указан")
        hash_pass = hash_password(password)
        user = User(username=username, password=hash_pass, is_temporary=is_temporary)
        if is_temporary:
            user.password_created_at = datetime.now(timezone.utc)
        try:
            session.add(user)
            session.commit()
            return {"message": "Пользователь успешно зарегистрирован"}
        except IntegrityError:
            session.rollback()
            session.expire_all()
            if session.query(User).filter_by(username=username).first():
                raise UserExistsError()
            else:
                raise

def login_in(username: str, password: str):
    with get_session() as session:
        user = session.query(User).filter_by(username=username).first()

        if not user:
            raise InvalidCredentialsError(detail="Пользователь не найден")

        if user.is_temporary:
            if user.password_created_at is None:
                pass  # Пароль временный, но неизвестно когда создан и не может быть проверен
            else:
                # Вычисляем количество дней, прошедших с момента создания пароля
                days_passed = (datetime.now(timezone.utc) - user.password_created_at).days
                if days_passed > 30:
                    raise TemporaryPasswordExpiredError()

        if not check_password(password, user.password):
            raise InvalidCredentialsError(detail="Неверный пароль")
        return {"message": "Успешный вход с временным паролем" if user.is_temporary else "Успешный вход"}

def register_user(username: str, password: str):
    session = get_session()
    hash_pass = hash_password(password)
    user = User(username=username, password=hash_pass)
    session.add(user)
    session.commit()

def delete_user(username: str):
    with get_session() as session:
        user = session.query(User).filter_by(username=username).first()
        if not user:
            raise UserNotFoundError()
        session.delete(user)
        session.commit()