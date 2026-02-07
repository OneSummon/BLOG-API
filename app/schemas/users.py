from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict


# Упрощенная схема для постов пользователя (без рекурсии)
class SimpleUserPostSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


# Основная схема для профиля (с постами)
class UserProfileSchema(BaseModel):
    username: str
    description: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    created_at: datetime
    posts: Optional[List[SimpleUserPostSchema]] = None
    
    model_config = ConfigDict(from_attributes=True)


# Упрощенная схема для автора в посте (без постов)
class UserAuthorSchema(BaseModel):
    id: int
    username: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)
    
class DataUpdateSchema(BaseModel):
    description: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    