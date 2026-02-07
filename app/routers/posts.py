from fastapi import APIRouter, HTTPException
from app.core.session_dep import SessionDep
from app.deps import ExstPostDep, VerifyUserDep

from app.schemas.posts import PostDataSchema, PostSchema
from app.schemas.responses import AuthorResponseSchema, PostResponseSchema
from app.crud.posts import create_post, delete_post, get_posts, update_post

router = APIRouter(prefix="/posts", tags=["Posts"])


@router.post("/create")
async def create(post_data: PostDataSchema, user: VerifyUserDep, session: SessionDep):
    new_post = await create_post(
        post_data.title,
        post_data.content,
        user.id,
        session
    )
    
    return new_post


@router.get("/get-all", response_model=list[PostResponseSchema])
async def get_all_posts(session: SessionDep, limit: int = 20, offset: int = 0):
    all_posts = await get_posts(session, limit, offset)
    
    return all_posts


@router.put("/update/{post_id}")
async def update(update_data: PostDataSchema,user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    if post.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not your post")
    
    upd_post = await update_post(
        post.id,
        session,
        update_data.title,
        update_data.content,
    )
    
    return PostSchema(
        id=upd_post.id,
        title=upd_post.title,
        content=upd_post.content,
        created_at=upd_post.created_at,
        updated_at=upd_post.updated_at,
    )


@router.delete("/delete/{post_id}")
async def delete(user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    if post.author_id != user.id:
        raise HTTPException(status_code=403, detail="Not your post")
    
    await delete_post(post.id, session)
    
    return {"success": True}


@router.get("/{post_id}")
async def get_post_by_id(post: ExstPostDep):
    
    return PostResponseSchema(
        id=post.id,
        title=post.title,
        content=post.content,
        created_at=post.created_at,
        updated_at=post.updated_at,
        author_id=post.author_id,
        author=AuthorResponseSchema(
            id=post.author.id,
            username=post.author.username,
            created_at=post.author.created_at
        ) if post.author else None
    )