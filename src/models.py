from sqlalchemy import Column, Integer, Float
from sqlalchemy.orm import DeclarativeBase

class BaseEntity(DeclarativeBase):
    id = Column(Integer, primary_key=True, autoincrement=True)

class Client(BaseEntity):
    __tablename__ = 'client'


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

