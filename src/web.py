from fastapi import FastAPI
from repository.ipoteka import register, login_in
from services.ipoteka import mortgage_calculation
from dotenv import load_dotenv
import os
from services.web_models import LoginRegisterModel, MortgageCalculationModel, MortgageResultModel

load_dotenv(dotenv_path="../config.env")

app = FastAPI()

db_url = os.getenv('DATABASE_URL')


@app.post("/register")
async def web_register(user: LoginRegisterModel):
    return register(user.username, user.password)

@app.post("/login")
async def web_login(user: LoginRegisterModel):
    return login_in(user.username, user.password)

@app.post("/mortgage/calculate", response_model=MortgageResultModel)
async def handle_mortgage(data: MortgageCalculationModel):
    monthly_payment, total_debt, overpayment = mortgage_calculation(
        data.interest_rate,
        data.mortgage_amount,
        data.mortgage_term
    )
    return {
    "monthly_payment": monthly_payment,
    "total_debt": total_debt,
    "overpayment": overpayment
}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, app_dir=".", env_file="../config.env")