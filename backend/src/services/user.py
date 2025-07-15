from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from ..models.user import UserInDB
from ..config.settings import settings
from ..config.database import get_db
from ..services.database import get_user_by_username

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v3/auth/token")

def get_user(username: str, db: Session):
    db_user = get_user_by_username(db, username)
    if db_user:
        return UserInDB(
            id=db_user.id,
            username=db_user.username,
            hashed_password=db_user.hashed_password,
            role=db_user.role
        )
    return None

async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username, db)
    if user is None:
        raise credentials_exception
    return user