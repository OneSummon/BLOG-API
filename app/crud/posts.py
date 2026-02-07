from datetime import datetime
from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload
from app.database.models import Post
from app.core.session_dep import SessionDep



async def create_post(title: str, content: str, author_id: int, session: SessionDep):
    new_post = Post(
        title=title,
        content=content,
        author_id=author_id,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        is_published=True,
    )
    
    session.add(new_post)
    await session.commit()
    await session.refresh(new_post)
    
    return new_post


async def get_posts(session: SessionDep, limit: int, offset: int):
    return await session.scalars(
        select(Post)
        .options(selectinload(Post.author))
        .order_by(Post.created_at.asc())
        .limit(limit)
        .offset(offset)
        )

async def get_post(post_id: int, session: SessionDep):
    return await session.scalar(select(Post).where(Post.id == post_id).options(selectinload(Post.author), selectinload(Post.likes)))


async def update_post(post_id: int, session: SessionDep, title: str = None, content: str = None):
    upd_post = await session.scalar(select(Post).where(Post.id == post_id))
    
    if title:
        await session.execute(update(Post).where(Post.id == post_id).values(title=title))
    
    if content:
        await session.execute(update(Post).where(Post.id == post_id).values(content=content))
    
    await session.execute(update(Post).where(Post.id == post_id).values(updated_at=datetime.now()))
    
    
    await session.commit()
    await session.refresh(upd_post)
    
    return upd_post


async def delete_post(post_id: int, session: SessionDep):
    await session.execute(delete(Post).where(Post.id == post_id))
    await session.commit()