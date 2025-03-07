import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

from fastapi import FastAPI, Request, Depends
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from backend.routes.auth import router as auth_router
from backend.routes.mortgage import router as mortgage_router
from backend.exceptions import UserExistsError, InvalidCredentialsError, TemporaryPasswordExpiredError
from backend.utils.session import redirect_with_flash
from starlette.responses import Response

app = FastAPI()


app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

@app.middleware("http")
async def add_session(request: Request, call_next):
    # Загружаем сессию из cookie, если она есть
    session_data = request.cookies.get("session", "{}")
    try:
        request.scope["session"] = json.loads(session_data)
    except json.JSONDecodeError:
        request.scope["session"] = {}


    response = await call_next(request)


    if isinstance(response, Response):
        session_data = json.dumps(request.scope["session"])
        response.set_cookie("session", session_data, httponly=True)
    return response


app.include_router(auth_router)
app.include_router(mortgage_router)


@app.exception_handler(UserExistsError)
async def user_exists_exception_handler(request: Request, exc: UserExistsError):
    if request.headers.get("accept") == "text/html":
        return redirect_with_flash(request, request.url.path, exc.detail, "danger")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail}, headers=exc.headers)

@app.exception_handler(InvalidCredentialsError)
async def invalid_credentials_exception_handler(request: Request, exc: InvalidCredentialsError):
    if request.headers.get("accept") == "text/html":
        return redirect_with_flash(request, request.url.path, exc.detail, "danger")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail}, headers=exc.headers)

@app.exception_handler(TemporaryPasswordExpiredError)
async def temporary_password_expired_exception_handler(request: Request, exc: TemporaryPasswordExpiredError):
    if request.headers.get("accept") == "text/html":
        return redirect_with_flash(request, request.url.path, exc.detail, "danger")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail}, headers=exc.headers)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001, app_dir="..", env_file="../config.env")