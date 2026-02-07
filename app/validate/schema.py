from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ConfigDict

from app.schemas.like import LikeSchema


class ExstPostSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    likes: Optional[List[LikeSchema]] = None
    
    model_config = ConfigDict(from_attributes=True)


class ExstCommentSchema(BaseModel):
    id: int