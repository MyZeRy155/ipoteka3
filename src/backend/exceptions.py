from fastapi import HTTPException, status

class UserExistsError(HTTPException):
    def __init__(self, detail: str = "Пользователь с таким username уже существует"):
        super().__init__(
            status_code=status.HTTP_409_CONFLICT,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )


class InvalidCredentialsError(HTTPException):
    def __init__(self, detail: str = "Неверное имя пользователя или пароль"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )


class TemporaryPasswordExpiredError(HTTPException):
    def __init__(self, detail: str = "Временный пароль истек (более 30 дней)"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )

class UserNotFoundError(HTTPException):
    def __init__(self, detail: str = "Пользователь с таким username не найден"):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )