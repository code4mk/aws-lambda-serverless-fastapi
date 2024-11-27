from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# Pydantic model for creating a new user
class UserCreateSchema(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(..., min_length=8)


# Pydantic model for updating user data
class UserUpdateSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
