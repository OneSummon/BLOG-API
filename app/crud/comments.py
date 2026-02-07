from datetime import datetime
from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload
from app.database.models import Comment
from app.core.session_dep import SessionDep


async def create_comment(text: str, post_id: int, author_id: int, session: SessionDep):
    new_comment = Comment(
        text=text,
        post_id=post_id,
        author_id=author_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    
    session.add(new_comment)
    await session.commit()
    await session.refresh(new_comment)
    
    return new_comment


async def get_comments(post_id: int, session: SessionDep, limit: int, offset: int):
    return await session.scalars(
        select(Comment)
        .where(Comment.post_id == post_id)
        .options(selectinload(Comment.author))
        .order_by(Comment.created_at.asc())
        .limit(limit)
        .offset(offset)
    )
    

async def get_comment(comment_id: int, session: SessionDep):
    return await session.scalar(select(Comment).where(Comment.id == comment_id))


async def update_comment(upd_text: str, comment_id: int, session: SessionDep):
    upd_comment = await session.scalar(select(Comment).where(Comment.id == comment_id))
    
    if upd_text:
        await session.execute(
            update(Comment)
            .where(Comment.id == comment_id)
            .values(text=upd_text,
                    updated_at=datetime.now())
            )
    
    await session.commit()
    await session.refresh(upd_comment)
    
    return upd_comment


async def delete_comment(comment_id: int, session: SessionDep):
    await session.execute(delete(Comment).where(Comment.id == comment_id))
    await session.commit()