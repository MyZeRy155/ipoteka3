from fastapi import APIRouter, Request, Form, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from backend.repository.ipoteka import register, login_in
from backend.services.web_models import LoginModel, RegisterModel, RegisterTemporaryModel
from backend.utils.session import get_flashed_messages, redirect_with_flash
from backend.config import get_db_url
from backend.exceptions import UserExistsError, InvalidCredentialsError, TemporaryPasswordExpiredError

router = APIRouter()

# Зависимость для проверки авторизации
def get_current_user(request: Request):
    if "user" not in request.session:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return request.session["user"]

# Главная страница (редирект на регистрацию)
@router.get("/", response_class=HTMLResponse)
async def root(request: Request, templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))):
    return redirect_with_flash(request, "/register", "Добро пожаловать! Для продолжения, нужно зарегистрироваться.")

# Страница регистрации (постоянный пароль)
@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request, templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))):
    return templates.TemplateResponse("register.html", {"request": request, "messages": get_flashed_messages(request)})

@router.post("/register", response_class=HTMLResponse)
async def register_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    approve_password: str = Form(...),
    db_url: str = Depends(get_db_url)
):
    try:
        data = RegisterModel(username=username, password=password, approve_password=approve_password)
        response = register(db_url, data.username, data.password, is_temporary=False)
        return redirect_with_flash(request, "/login", response["message"], "success")
    except (UserExistsError, ValueError) as e:
        return redirect_with_flash(request, "/register", str(e.detail if hasattr(e, 'detail') else e), "danger")

# Страница регистрации (временный пароль)
@router.get("/register/temporary", response_class=HTMLResponse)
async def register_temp_page(request: Request, templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))):
    return templates.TemplateResponse("register_temp.html", {"request": request, "messages": get_flashed_messages(request)})

@router.post("/register/temporary", response_class=HTMLResponse)
async def register_temp_submit(
    request: Request,
    username: str = Form(...),
    temporary_password: str = Form(...),
    approve_password: str = Form(...),
    db_url: str = Depends(get_db_url)
):
    try:
        data = RegisterTemporaryModel(username=username, temporary_password=temporary_password, approve_password=approve_password)
        response = register(db_url, data.username, data.temporary_password, is_temporary=True)
        return redirect_with_flash(request, "/login", response.message, "success")
    except (UserExistsError, TemporaryPasswordExpiredError, ValueError) as e:
        return redirect_with_flash(request, "/register/temporary", str(e.detail if hasattr(e, 'detail') else e), "danger")

# Страница входа
@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request, templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))):
    return templates.TemplateResponse("login.html", {"request": request, "messages": get_flashed_messages(request)})

@router.post("/login", response_class=HTMLResponse)
async def login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db_url: str = Depends(get_db_url)
):
    try:
        data = LoginModel(username=username, password=password)
        response = login_in(db_url, data.username, data.password)
        request.session["user"] = username  # Сохраняем пользователя в сессии
        print(f"Session before redirect: {request.session}")
        return redirect_with_flash(request, "/dashboard", response["message"], "success")
    except (InvalidCredentialsError, TemporaryPasswordExpiredError) as e:
        return redirect_with_flash(request, "/login", str(e.detail), "danger")

# Общая страница (Dashboard) после авторизации
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboard_page(
    request: Request,
    current_user: str = Depends(get_current_user),
    templates: Jinja2Templates = Depends(lambda: Jinja2Templates(directory="frontend/templates"))
):
    return templates.TemplateResponse("dashboard.html", {"request": request, "messages": get_flashed_messages(request), "username": current_user})

# Выход (Logout)
@router.get("/logout", response_class=HTMLResponse)
async def logout(request: Request):
    request.session.pop("user", None)  # Удаляем пользователя из сессии
    return redirect_with_flash(request, "/login", "Успешный выход", "success")