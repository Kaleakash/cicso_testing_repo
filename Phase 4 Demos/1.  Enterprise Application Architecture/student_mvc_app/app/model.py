from typing import Optional

from pydantic import BaseModel, ConfigDict, EmailStr, Field
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class Student(Base):
    """Model: persistent entity."""

    __tablename__ = "students"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    age: Mapped[int]
    course: Mapped[str] = mapped_column(String(100))


class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    email: EmailStr
    age: int = Field(ge=1, le=120)
    course: str = Field(min_length=1, max_length=100)


class StudentUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(default=None, ge=1, le=120)
    course: Optional[str] = Field(default=None, min_length=1, max_length=100)


class StudentResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: EmailStr
    age: int
    course: str
