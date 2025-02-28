from sqlalchemy import Column, Integer, Float, String, DateTime, Boolean
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

    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_temporary = Column(Boolean, default=True, server_default="true", nullable=False)
    created_at = Column(DateTime, nullable=True, default=datetime.now())


class Ipoteka(BaseEntity):
    __tablename__ = 'mortgage'
    interest_rate = Column(Float)
    mortgageamount = Column(Float)
    mortgage_term = Column(Integer)
    monhly_payment = Column(Float)
    total_debt = Column(Float)
    overpayment = Column(Float, nullable=True)

class PaymentIpoteka(BaseEntity):
    __tablename__ = 'payment'
