from fastapi import APIRouter, Request
from ..security.ratelimit import limiter
from ..models.usermodels import User, NewUser

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
def get_user(request:Request, user_id: int):
    return {"message": "Hello, World!"}

#Login User
@router.post("/login-user",tags=["users"])
@limiter.limit("5/minute")
def login_user(request:Request, user: User):
    return {"message": "Hello, World!"}

#Register User
@router.post("/register-user", tags=["users"])
@limiter.limit("5/minute")
def register_user(request:Request, new_user: NewUser):
    return {"message": "Hello, World!"}

#Delete User
@router.delete("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
def delete_user(request:Request, user_id: int):
    return {"message": "Hello, World!"}

#Update User
@router.put("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
def update_user(request:Request, user: User):
    return {"message": "Hello, World!"}