from fastapi import APIRouter, HTTPException
from app.core.session_dep import SessionDep
from app.crud.comments import create_comment, delete_comment, get_comments, update_comment
from app.schemas.comments import CommentDataSchema, CommentSchema, UpdCommentData
from app.schemas.responses import CommentResponseSchema
from app.deps import ExstCommentDep, ExstPostDep, VerifyUserDep


router = APIRouter(prefix="/posts/{post_id}/comments", tags=["Comments"])


@router.post("/", response_model=CommentSchema)
async def create(commentData: CommentDataSchema, user: VerifyUserDep, session: SessionDep, post: ExstPostDep):
    new_comment = await create_comment(commentData.text, post.id, user.id, session)
    
    return new_comment


@router.get("/", response_model=list[CommentResponseSchema])
async def get_comments_post(session: SessionDep, post: ExstPostDep, limit: int = 20, offset: int = 0):
    all_comments = await get_comments(
        post.id,
        session,
        limit,
        offset,
    )
    
    return all_comments


@router.put("/{comment_id}")
async def update(updCommentData: UpdCommentData, user: VerifyUserDep, comment: ExstCommentDep, session: SessionDep, post: ExstPostDep):
    if comment.author_id != user.id:
        raise HTTPException(status_code=403)
    
    updt_comment = await update_comment(updCommentData.text, comment.id, session)
    
    return updt_comment


@router.delete("/{comment_id}")
async def delete(user: VerifyUserDep, comment: ExstCommentDep, session: SessionDep, post: ExstPostDep):
    if comment.author_id != user.id:
        raise HTTPException(status_code=403)
    
    if comment.post_id != post.id:
        raise HTTPException(status_code=404)
    
    await delete_comment(comment.id, session)
    
    return {"success": True}