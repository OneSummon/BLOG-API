from datetime import datetime
from sqlalchemy import delete, select, update
from sqlalchemy.orm import selectinload
from app.database.models import User
from app.core.session_dep import SessionDep


async def get_user(user_id: int, session: SessionDep):
    return await session.scalar(select(User).where(User.id == user_id).options(selectinload(User.posts)))


async def get_users(session: SessionDep):
    return await session.scalars(select(User).options(selectinload(User.posts)))


async def update_user(user_id: int, session: SessionDep, new_description: str = None, new_date_of_birth: datetime = None):
    upd_user = await session.scalar(select(User).where(User.id == user_id))
    
    if new_description:
        await session.execute(update(User).where(User.id == user_id).values(description=new_description))
        
    if new_date_of_birth:
        await session.execute(update(User).where(User.id == user_id).values(date_of_birth=new_date_of_birth))
        
        
    await session.commit()
    await session.refresh(upd_user)
    
    return upd_user


async def delete_user(user_id: int, session: SessionDep):
    await session.execute(delete(User).where(User.id == user_id))
    await session.commit()