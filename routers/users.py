from fastapi import APIRouter

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
def get_users(user_id: int):
    return {"message": "Hello, World!"}

#Login User
@router.post("/login-user",tags=["users"])
def login_user(username: str, password: str):
    return {"message": "Hello, World!"}

#Register User
@router.post("/register-user", tags=["users"])
def register_user(username: str, password: str):
    return {"message": "Hello, World!"}

#Delete User
@router.delete("/delete-user", tags=["users"])
def delete_user(username: str):
    return {"message": "Hello, World!"}

#Update User
@router.put("/update-user", tags=["users"])
def update_user(username: str, password: str):
    return {"message": "Hello, World!"}