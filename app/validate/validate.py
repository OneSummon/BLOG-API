from fastapi import HTTPException
from app.crud.comments import get_comment
from app.crud.posts import get_post
from app.crud.users import get_user
from app.database.models import Post, User
from app.schemas.users import UserProfileSchema
from app.validate.schema import ExstCommentSchema, ExstPostSchema


from app.core.session_dep import SessionDep


async def get_existing_post(post_id: int, session: SessionDep) -> Post:
    post = await get_post(post_id, session)
    
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return post


async def get_existing_comment(comment_id: int, session: SessionDep):
    exst_comment = await get_comment(comment_id, session)
    
    if not exst_comment:
        raise HTTPException(status_code=404)
    
    return exst_comment


async def get_existing_user(user_id: int, session: SessionDep) -> User:
    existing_user = await get_user(user_id, session)
    
    if not existing_user:
        raise HTTPException(status_code=404)
    
    return existing_user