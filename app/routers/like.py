from fastapi import APIRouter
from app.core.session_dep import SessionDep
from app.deps import ExstPostDep, VerifyUserDep

from app.crud.like import delete_like, is_post_liked, set_like


router = APIRouter(prefix="/posts/{post_id}/like", tags=["Like"])


@router.post("/")
async def create_like(user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    new_like = await set_like(post.id, user.id, session)
    
    return new_like


@router.delete("/")
async def remove_like(user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    await delete_like(post.id, user.id, session)
    
    return {"success": True}


@router.get("/check")
async def is_like(user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    check_answer = await is_post_liked(user.id, post.id, session)
    
    return {"liked": check_answer}


@router.get("/counts")
async def count_likes(post: ExstPostDep):
    return {"count": len(post.likes)}