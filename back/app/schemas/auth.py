from pydantic import BaseModel, EmailStr
import enum

class UserRole(str, enum.Enum):
    ADMIN = "admin"
    USER = "user"
    MODERATOR = "moderator"

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: EmailStr | None = None


class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    is_active: bool | None = None


class UserInDB(User):
    hashed_password: str