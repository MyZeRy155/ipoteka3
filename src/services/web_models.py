from pydantic import BaseModel, Field

class LoginRegisterModel(BaseModel):
    username: str = Field(description="Username or your Personality", min_length=6, max_length=20, examples=["Your Personality"])
    password: str = Field(description="Probably you want create strong password or enter your account", min_length=6, max_length=20, examples=["aA!@$53`~pass"])

class MortgageCalculationModel(BaseModel):
    mortgage_amount: float = Field(description="Сумма кредита", examples=[100000])
    mortgage_term: int = Field(description="Срок кредита в месяцах", examples=[36])
    interest_rate: float = Field(description="Процентная ставка", examples=[10])

class MortgageResultModel(BaseModel):
    total_debt: float = Field(description="Общий долг", examples=[100000])
    monthly_payment: float = Field(description="Месячный платеж", examples=[1000])
    overpayment: float = Field(description="Переплата", examples=[10000])