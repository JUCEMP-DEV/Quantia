from fastapi import HTTPException
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    if not password:
        raise HTTPException(
            status_code=400,
            detail="La contrasena es obligatoria.",
        )

    if len(password.encode("utf-8")) > 72:
        raise HTTPException(
            status_code=400,
            detail="La contrasena no puede superar 72 bytes.",
        )

    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not plain_password or not hashed_password:
        return False

    if len(plain_password.encode("utf-8")) > 72:
        return False

    return pwd_context.verify(plain_password, hashed_password)
