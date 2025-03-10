from fastapi import APIRouter, Depends , status
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException

from src.auth.schema import User, UserWithHashedPass

#fake data to login user
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakesecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakesecret2",
        "disabled": True,
    },
}


user_router = APIRouter()

# Simulates password hashing by appending "fakehashed" to the original password. 
def fake_hash_password(password: str):
    return "fake" + password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/token")

# def fake_decode_token(token):
#     return User(
#         username=token + "randomPass", email="rohan@bohra.com", is_verified=True
#     )


#fetch a user from the fake database
def get_user(Exampledb, username: str):
    if username in Exampledb:
        user_dict = Exampledb[username]
        return UserWithHashedPass(**user_dict)
    
#This function pretends to decode a token and return the user.
# In a real app, we would use JWT (JSON Web Tokens) instead.
def fake_decode_token(token):
    user = get_user(fake_users_db, token)
    return user 


#Extracts the token from the request header using Depends(oauth2_scheme).
# Decodes the token to get the user (fake_decode_token(token)).
# If the user does not exist, it raises a 401 Unauthorized error.
# If the user exists, it returns the user object.
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"})
    return user

async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@user_router.post("/token")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_dict = fake_users_db.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    user = UserWithHashedPass(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if hashed_password != user.hashed_password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.username, "token_type": "bearer"}

@user_router.get("/users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_active_user)]):    
    return current_user
