from pydantic import BaseModel, Field, model_validator


class BaseRegisterModel(BaseModel):
    username: str = Field(description="Username or your Personality", min_length=6, max_length=20, examples=["username"])
    password: str = Field(description="Use your password", min_length=6, max_length=20, examples=["password"])
    approve_password: str = Field(description="Confirm your password", min_length=6, max_length=20, examples=["password"])

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.password != self.approve_password:
            raise ValueError("Пароль и подтверждение пароля должны совпадать")
        return self


class RegisterModel(BaseRegisterModel):
    pass


class RegisterTemporaryModel(BaseModel):
    username: str = Field(description="Create Username or your Personality with temporary password", min_length=6, max_length=20, examples=["username"])
    temporary_password: str = Field(description="Use your temporary password", min_length=6, max_length=20, examples=["temp_password"])
    approve_password: str = Field(description="Confirm your temporary password", min_length=6, max_length=20, examples=["temp_password"])

    @model_validator(mode="after")
    def check_passwords_match(self):
        if self.temporary_password != self.approve_password:
            raise ValueError("Пароль и подтверждение пароля должны совпадать")
        return self


class LoginModel(BaseModel):
    username: str = Field(description="Username or your Personality", min_length=6, max_length=20, examples=["username"])
    password: str = Field(description="Use your password", min_length=6, max_length=20, examples=["password"])


class MortgageCalculationModel(BaseModel):
    mortgage_amount: float = Field(description="Сумма кредита", examples=[100000])
    mortgage_term: int = Field(description="Срок кредита в месяцах", examples=[36])
    interest_rate: float = Field(description="Процентная ставка", examples=[10])


class MortgageResultModel(BaseModel):
    total_debt: float = Field(description="Общий долг", examples=[100000])
    monthly_payment: float = Field(description="Месячный платеж", examples=[1000])
    overpayment: float = Field(description="Переплата", examples=[10000])