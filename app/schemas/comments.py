from datetime import datetime
from pydantic import BaseModel


class CommentDataSchema(BaseModel):
    text: str

class CommentSchema(BaseModel):
    id: int
    text: str
    post_id: int
    author_id: int
    created_at: datetime
    

class UpdCommentData(BaseModel):
    text: str