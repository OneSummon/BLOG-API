from typing import Annotated
from fastapi import Depends

from app.database.models import Comment, Post, User
from app.schemas.users import UserProfileSchema
from app.validate.validate import get_existing_comment, get_existing_post, get_existing_user
from app.validate.schema import ExstCommentSchema, ExstPostSchema
from app.security import get_current_user

from app.security import CurrentUser


VerifyUserDep = Annotated[User, Depends(get_current_user)]

ExstPostDep = Annotated[Post, Depends(get_existing_post)]

ExstCommentDep = Annotated[Comment, Depends(get_existing_comment)]

ExstUserDep = Annotated[User, Depends(get_existing_user)]