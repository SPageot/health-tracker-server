from fastapi import APIRouter, Request
from schema.journal import Journal
from security.ratelimit import limiter
from db.sql import engine
from sqlmodel import Session, select
from fastapi.exceptions import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
import uuid
router = APIRouter()


#Get All Journal Entries
@router.get("/user/{user_id}", tags=["journal"])
@limiter.limit("5/minute")
def get_journal_entry(request: Request, user_id: uuid.UUID):
    with Session(engine) as session:
        statement = select(Journal).where(Journal.user_id == user_id)
        results = session.exec(statement).all()
        return results

#Get Journal Entry
@router.get("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def get_journal_entry(request: Request, journal_id: uuid.UUID):
    with Session(engine) as session:
        statement = select(Journal).where(Journal.id == journal_id)
        results = session.exec(statement).all()
        return results

#Add Journal Entry
@router.post("/entry", tags=["journal"])
@limiter.limit("5/minute")
def add_journal_entry(request: Request, entry: Journal):
    with Session(engine) as session:
        for key in entry:
            value = key[1]
            if value == "" or value is None:
                raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail=f"Missing required field: {key}")
    with Session(engine) as session:
        session.add(Journal(**dict(entry)))
        session.commit()
    return {"message":"Entry Saved!"}

#Delete Journal Entry
@router.delete("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def delete_journal_entry(request: Request, journal_id: uuid.UUID):
    with Session(engine) as session:
        item = session.get(Journal, journal_id)
        if item is None:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Journal entry not found")
        session.delete(item)
        session.commit()
    return {"message": "User deleted successfully"}

#Update Journal Entry
@router.put("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def update_journal_entry(request: Request, journal_id: int, entry: Journal):
    with Session(engine) as session:
        item = session.get(Journal, journal_id)
        print(item)
        if item is None:
            raise HTTPException(status_code=HTTP_400_BAD_REQUEST, detail="Journal entry not found")
        item.sqlmodel_update(entry)
        session.commit()
    return session