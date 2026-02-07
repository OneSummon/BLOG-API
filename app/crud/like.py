from datetime import datetime
from sqlalchemy import delete, select
from app.database.models import Like
from app.core.session_dep import SessionDep



async def is_post_liked(user_id: int, post_id: int, session: SessionDep) -> bool:
    exst_user_like = await session.scalar(select(Like).where(Like.author_id == user_id, Like.post_id == post_id))
    
    if exst_user_like:
        return True
    return False


async def set_like(post_id: int, author_id: int, session: SessionDep):
    new_like = Like(
        author_id=author_id,
        post_id=post_id,
        created_at=datetime.now(),
    )
    
    session.add(new_like)
    await session.commit()
    await session.refresh(new_like)
    
    return new_like


async def delete_like(post_id: int, author_id: int, session: SessionDep):
    await session.execute(delete(Like).where(Like.author_id == author_id, Like.post_id == post_id))
    await session.commit()
 