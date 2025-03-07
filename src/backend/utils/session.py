from fastapi import Request
from starlette.responses import RedirectResponse

def flash(request: Request, message: str, category: str = "success"):
    if "_messages" not in request.session:
        request.session["_messages"] = []
    request.session["_messages"].append({"message": message, "category": category})

def get_flashed_messages(request: Request):
    messages = request.session.get("_messages", [])
    request.session["_messages"] = []
    return messages

def redirect_with_flash(request: Request, url: str, message: str, category: str = "info"):
    request.session.setdefault("flash_messages", []).append({"message": message, "category": category})
    return RedirectResponse(url, status_code=303)