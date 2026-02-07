from datetime import datetime
from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(15), unique=True, index=True)
    hashed_password: Mapped[str]
    role: Mapped[str]
    created_at: Mapped[datetime]
    description: Mapped[str] = mapped_column(nullable=True)
    date_of_birth: Mapped[datetime] = mapped_column(nullable=True)
    
    posts: Mapped[list["Post"]] = relationship(
        back_populates="author", 
        cascade="all, delete-orphan"
    )
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="author", 
        cascade="all, delete-orphan"
    )
    likes: Mapped[list["Like"]] = relationship(
        back_populates="author",
        cascade="all, delete-orphan"
    )


class Post(Base):
    __tablename__ = "posts"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    is_published: Mapped[bool] = mapped_column(default=True)
    
    author: Mapped["User"] = relationship(
        back_populates="posts",
    )
    comments: Mapped[list["Comment"]] = relationship(
        back_populates="post",
        cascade="all, delete-orphan"
    )
    likes: Mapped[list["Like"]] = relationship(
        back_populates="post",
        cascade="all, delete-orphan"
    )
    

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    created_at: Mapped[datetime]
    updated_at: Mapped[datetime]
    
    post: Mapped["Post"] = relationship(
        back_populates="comments",
    )
    author: Mapped["User"] = relationship(
        back_populates="comments",
    )
    

class Like(Base):
    __tablename__ = "likes"
    
    __table_args__ = (
        UniqueConstraint("author_id", "post_id", name="uq_user_post_like"),
    )
    
    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), nullable=False)
    created_at: Mapped[datetime]
    
    author: Mapped["User"] = relationship(
        back_populates="likes",
    )
    post: Mapped["Post"] = relationship(
        back_populates="likes",
    )