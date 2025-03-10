from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    # id: int
    username: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    
    class Config:
        from_attributes = True

class UserWithHashedPass(User):
    hashed_password: str