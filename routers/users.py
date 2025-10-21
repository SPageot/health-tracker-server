from fastapi import APIRouter, Request
from ..security.ratelimit import limiter
from ..models.usermodels import User, NewUser
from sqlmodel import Session, select
from db.sql import engine
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from ..schema.user import NewUserDB, UserDB
import uuid

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
async def get_user(request:Request, user_id: uuid.UUID):
   with Session(engine) as session:
        statement = select(NewUserDB).where(NewUserDB.id == user_id)
        results = session.exec(statement).all()
        return results

#Login User
#TODO:ADD AUTH TOKEN
@router.post("/login-user",tags=["users"])
@limiter.limit("5/minute")
async def login_user(request:Request, user: User):
    with Session(engine) as session:
        statement = select(UserDB).where(UserDB.username == user.username and UserDB.password == user.password)
        results = session.exec(statement).all()
        return results

#Register User
@router.post("/register-user", tags=["users"])
@limiter.limit("5/minute")
async def register_user(request:Request, new_user: NewUser):
    with Session(engine) as session:
        for key in new_user:
            value = new_user[key]
            if value == "" or value is None:
                if key == "id":
                    continue
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Missing required field: {key}")
    with Session(engine) as session:
        session.add(NewUser(**new_user))
        session.commit()
    return new_user

#Delete User
@router.delete("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
async def delete_user(request:Request, user_id: uuid.UUID):
    with Session(engine) as session:
        item = session.get(NewUserDB, user_id)
        if item is None:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="User not found")
        session.delete(item)
        session.commit()
    return {"message": "User deleted successfully"}

#Update User
@router.put("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
def update_user(request:Request, user: User):
    return {"message": "Hello, World!"}