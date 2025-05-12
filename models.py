from pydantic import BaseModel, EmailStr, Field
from typing import Optional
import uuid # For user ID if not directly from Supabase UUID

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6)

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class TokenData(BaseModel):
    access_token: str
    refresh_token: Optional[str] = None
    token_type: str = "bearer"
    expires_in: Optional[int] = None
    # Supabase might also return user data along with token

class UserResponse(BaseModel):
    id: uuid.UUID # Supabase user IDs are UUIDs
    email: EmailStr
    created_at: Optional[str] = None # Supabase provides this as ISO string
    # Add other fields from Supabase user object as needed, e.g., last_sign_in_at

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "email": "user@example.com",
                "created_at": "2023-10-26T10:00:00Z"
            }
        }
