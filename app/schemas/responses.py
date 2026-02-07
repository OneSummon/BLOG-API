from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AuthorResponseSchema(BaseModel):
    id: int
    username: str
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)


class PostResponseSchema(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    author_id: int
    author: Optional[AuthorResponseSchema] = None
    
    model_config = ConfigDict(from_attributes=True)


class CommentResponseSchema(BaseModel):
    id: int
    text: str
    post_id: int
    author_id: int
    created_at: datetime
    author: Optional[AuthorResponseSchema] = None
    
    model_config = ConfigDict(from_attributes=True)