from fastapi import APIRouter
from app.core.session_dep import SessionDep
from app.deps import ExstUserDep, VerifyUserDep

from app.crud.users import delete_user, get_users, update_user
from app.schemas.users import DataUpdateSchema, UserProfileSchema

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile")
async def profile(user: VerifyUserDep):
    profile_info = UserProfileSchema(
        username=user.username,
        description=user.description,
        date_of_birth=user.date_of_birth,
        created_at=user.created_at,
        posts=user.posts,
    )
    
    return profile_info


@router.put("/profile/update")
async def profile_update(data_update: DataUpdateSchema,user: VerifyUserDep, session: SessionDep):
    
    upd_user = await update_user(
        user.id,
        session,
        data_update.description,
        data_update.date_of_birth,
    )
    
    return upd_user


@router.delete("/profile/delete")
async def profile_delete(user: VerifyUserDep, session: SessionDep):
    await delete_user(user.id, session)
    return {"success delete": True}


@router.get("/get_all", response_model=list[UserProfileSchema])
async def get_all_users(session: SessionDep):
    all_users = await get_users(session)
    
    return all_users
    

@router.get("/{user_id}")
async def get_user_by_id(profile: ExstUserDep):
    
    find_user_profile = UserProfileSchema(
        username=profile.username,
        created_at=profile.created_at,
        posts=profile.posts
    )
    
    return find_user_profile