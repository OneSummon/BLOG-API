from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.users import UserProfileSchema
from app.schemas.users import UserAuthorSchema


class PostDataSchema(BaseModel):
    title: str
    content: str


class PostSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    author_id: Optional[int] = None
    author: Optional[UserAuthorSchema] = None
    
    model_config = ConfigDict(from_attributes=True)