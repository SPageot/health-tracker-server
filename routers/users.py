from fastapi import APIRouter

router = APIRouter()

#Login User
@router.post("/login-user")
def login_user(username: str, password: str):
    return {"message": "Hello, World!"}

#Register User
@router.post("/register-user")
def register_user(username: str, password: str):
    return {"message": "Hello, World!"}

#Delete User
@router.delete("/delete-user")
def delete_user(username: str):
    return {"message": "Hello, World!"}

#Update User
@router.put("/update-user")
def update_user(username: str, password: str):
    return {"message": "Hello, World!"}