from fastapi import APIRouter, Request
from security.ratelimit import limiter
from sqlmodel import Session, select
from db.sql import engine
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from schema.user import Users
import uuid

router = APIRouter()

@router.get("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
async def get_user(request:Request, user_id: uuid.UUID):
   with Session(engine) as session:
        statement = select(Users).where(Users.id == user_id)
        results = session.exec(statement).all()
        return results

#Login User
#TODO:ADD AUTH TOKEN
@router.post("/login-user",tags=["users"])
@limiter.limit("5/minute")
async def login_user(request:Request, user: Users):
    with Session(engine) as session:
        statement = select(Users).where(Users.username == user.username and Users.password == user.password)
        results = session.exec(statement).all()
        return results

#Register User
@router.post("/register-user", tags=["users"])
@limiter.limit("5/minute")
async def register_user(request:Request, new_user: Users):
    with Session(engine) as session:
        print(type(new_user))
        for key in new_user:
            value = key[1]
            print(value)
            if value == "" or value is None:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Missing required field: {key}")
    with Session(engine) as session:
        session.add(Users(**dict(new_user)))
        session.commit()
    return new_user

#Delete User
@router.delete("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
async def delete_user(request:Request, user_id: uuid.UUID):
    with Session(engine) as session:
        item = session.get(Users, user_id)
        if item is None:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="User not found")
        session.delete(item)
        session.commit()
    return {"message": "User deleted successfully"}

#Update User
@router.put("/{user_id}", tags=["users"])
@limiter.limit("5/minute")
def update_user(request:Request,user_id:uuid.UUID, user: Users):
    with Session(engine) as session:
        item = session.get(Users, user_id)
        print(item)
        if item is None:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="User not found")
        item.sqlmodel_update(user)
        session.commit()
    return session