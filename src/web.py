from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from repository.ipoteka import register, login_in
from services.ipoteka import mortgage_calculation
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="../config.env")

app = FastAPI()

db_url = os.getenv('DATABASE_URL')

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.post("/register")
async def web_register(username: str, password: str):
    return register(username, password)

@app.post("/login")
async def web_login(username: str, password: str):
    return login_in(username, password)

@app.post("/mortgage/calculate")
async def handle_mortgage(interest_rate: float, mortgage_amount:float, mortgage_term:int) -> tuple[float, float, float]:
    monhly_payment, total_debt, overpayment = mortgage_calculation(
        interest_rate, mortgage_amount, mortgage_term
    )
    return monhly_payment, total_debt, overpayment

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, app_dir=".", env_file="../config.env")