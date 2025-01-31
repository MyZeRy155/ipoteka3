from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class BaseEntity(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)

class Client(BaseEntity):
    __tablename__ = 'client'
    username = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)


class User(BaseEntity):
    __tablename__ = 'user'
    username = Column(String, unique=True)
    password = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())


class Ipoteka(BaseEntity):
    __tablename__ = 'mortgage'
    interest_rate = Column(Float)
    mortgage_amount = Column(Float)
    mortgage_term = Column(Integer)
    monhly_payment = Column(Float)
    total_debt = Column(Float)
    overpayment = Column(Float, nullable=True)

class PaymentIpoteka(BaseEntity):
    __tablename__ = 'payment'


