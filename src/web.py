from fastapi import FastAPI, Request, HTTPException
from repository.ipoteka import register, login_in, delete_user
from services.ipoteka import mortgage_calculation
from dotenv import load_dotenv
import os
from services.web_models import LoginModel, RegisterModel, RegisterTemporaryModel, MortgageCalculationModel, MortgageResultModel
from exceptions import InvalidCredentialsError, TemporaryPasswordExpiredError
from fastapi.responses import JSONResponse

load_dotenv(dotenv_path="../config.env")

app = FastAPI()

db_url = os.getenv('DATABASE_URL')

@app.post("/login")
async def web_login(user: LoginModel):
    try:
        return login_in(user.username, user.password)
    except ValueError as e:
        raise InvalidCredentialsError(detail=str(e))
    except TemporaryPasswordExpiredError as e:
        raise e

@app.post("/register")
async def web_register(user: RegisterModel):
    return register(user.username, user.password, is_temporary=False)

@app.post("/register/temporary")
async def web_register_temporary(user: RegisterTemporaryModel):
    try:
        result = register(user.username, user.temporary_password, is_temporary=True)
        return result
    except TemporaryPasswordExpiredError as e:
        raise e

@app.post("/mortgage/calculate", response_model=MortgageResultModel)
async def handle_mortgage(data: MortgageCalculationModel):
    monthly_payment, total_debt, overpayment = mortgage_calculation(
        data.interest_rate,
        data.mortgage_amount,
        data.mortgage_term
    )
    return MortgageResultModel(
        monthly_payment=monthly_payment,
        total_debt=total_debt,
        overpayment=overpayment
    )

@app.delete("/delete-user")
async def web_delete_user(username: str):
    try:
        delete_user(username)
        return {"message": "Пользователь успешно удален"}
    except HTTPException as e:
        raise e

@app.exception_handler(HTTPException)
async def http_exception_handler(_request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
        headers=exc.headers
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, app_dir=".", env_file="../config.env")