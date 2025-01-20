from sqlalchemy import Column, String, Integer, Float
from sqlalchemy.orm import DeclarativeBase



class Base(DeclarativeBase):
    pass

class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True, autoincrement=True)

class Ipoteka(Base):
    __tablename__ = 'ipoteka'
    id = Column(Integer, primary_key=True, autoincrement=True)
    procent_stavka = Column(Float)
    summa_ipoteki = Column(Float)
    srok_ipoteki = Column(Integer)
    month_payment = Column(Float)
    obshiDolg = Column(Float)
    overpayment = Column(Float, nullable=True)

class PaymentIpoteka(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, autoincrement=True)
