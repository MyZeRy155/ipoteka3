from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.services.ipoteka import mortgage_calculation
from backend.services.web_models import MortgageCalculationModel
from backend.utils.session import get_flashed_messages, redirect_with_flash
from backend.routes.auth import get_current_user
from backend.config import get_db_url

router = APIRouter()

@router.get("/mortgage", response_class=HTMLResponse)
async def mortgage_page(
    request: Request,
    current_user: str = Depends(get_current_user),
    templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))
):

    context = {
        "request": request,
        "messages": get_flashed_messages(request),
        "form_data": {
        "mortgage_amount": "",
        "mortgage_term": "",
        "interest_rate": ""
        }
    }
    return templates.TemplateResponse("mortgage.html", context)

@router.post("/mortgage/calculate", response_class=HTMLResponse)
async def mortgage_submit(
    request: Request,
    mortgage_amount: str = Form(...),
    mortgage_term: int = Form(...),
    interest_rate: float = Form(...),
    current_user: str = Depends(get_current_user),
    templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates")),
    db_url: str = Depends(get_db_url)
):
    try:

        mortgage_amount_clean = mortgage_amount.replace(" ", "")
        mortgage_amount_float = float(mortgage_amount_clean)

        data = MortgageCalculationModel(
            mortgage_amount=mortgage_amount_float,
            mortgage_term=mortgage_term,
            interest_rate=interest_rate
        )


        result = mortgage_calculation(data.interest_rate, data.mortgage_amount, data.mortgage_term)


        monthly_payment = "{:,.2f}".format(result[0]).replace(',', ' ')
        total_debt = "{:,.2f}".format(result[1]).replace(',', ' ')
        overpayment = "{:,.2f}".format(result[2]).replace(',', ' ')

        context = {
            "request": request,
            "messages": get_flashed_messages(request),
            "form_data": {
                "mortgage_amount": "{:,.0f}".format(data.mortgage_amount).replace(',', ' '),
                "mortgage_term": data.mortgage_term,
                "interest_rate": data.interest_rate
            },
            "result": {
                "monthly_payment": monthly_payment,
                "total_debt": total_debt,
                "overpayment": overpayment
            }
        }
        return templates.TemplateResponse("mortgage.html", context)
    except ValueError as e:

        context = {
            "request": request,
            "messages": get_flashed_messages(request),
            "form_data": {
                "mortgage_amount": mortgage_amount,
                "mortgage_term": mortgage_term,
                "interest_rate": interest_rate
            }
        }
        return templates.TemplateResponse("mortgage.html", context, status_code=400)