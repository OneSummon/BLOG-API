from datetime import datetime
from pydantic import BaseModel, ConfigDict

class LikeSchema(BaseModel):
    id: int
    author_id: int
    post_id: int
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)