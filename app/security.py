from datetime import datetime, timedelta
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from app.core.session_dep import SessionDep
from app.crud.users import get_user
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


class CurrentUser(BaseModel):
    id: int
    role: str
    
    
#hashing----------------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


#create-access-token----------------------------------------------
SECRET_KEY=SECRET_KEY
ALGORITHM=ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES=ACCESS_TOKEN_EXPIRE_MINUTES

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")
async def get_current_user(session: SessionDep, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        user_id = payload.get("sub")
        role = payload.get("role")
        
        if not user_id or not role:
            raise HTTPException(status_code=401)
        
        if role not in ["user", "admin"]:
            raise HTTPException(status_code=403)
        
        user = await get_user(user_id, session)
        if not user:
            raise HTTPException(status_code=401)
        
        return user
        
    except JWTError:
        raise HTTPException(status_code=401)