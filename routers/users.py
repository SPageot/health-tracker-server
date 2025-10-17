from fastapi import APIRouter
from ..models.usermodels import User, NewUser

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
def get_user(user_id: int):
    return {"message": "Hello, World!"}

#Login User
@router.post("/login-user",tags=["users"])
def login_user(user: User):
    return {"message": "Hello, World!"}

#Register User
@router.post("/register-user", tags=["users"])
def register_user(new_user: NewUser):
    return {"message": "Hello, World!"}

#Delete User
@router.delete("/{user_id}", tags=["users"])
def delete_user(user_id: int):
    return {"message": "Hello, World!"}

#Update User
@router.put("/{user_id}", tags=["users"])
def update_user(user: User):
    return {"message": "Hello, World!"}