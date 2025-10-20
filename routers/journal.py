from fastapi import APIRouter, Request
from ..models.journalmodels import JournalEntry
from ..security.ratelimit import limiter
router = APIRouter()


#Get All Journal Entries
@router.get("/", tags=["journal"])
@limiter.limit("5/minute")
def get_all_journal_entries(request: Request):
    return {"message": "Hello, World!!!"}

#Get Journal Entry
@router.get("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def get_journal_entry(request: Request, journal_id: int):
    return {"message": "Hello, World!"}

#Add Journal Entry
@router.post("/entry", tags=["journal"])
@limiter.limit("5/minute")
def add_journal_entry(request: Request, entry: JournalEntry):
    return {"message": "Hello, World!"}

#Delete Journal Entry
@router.delete("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def delete_journal_entry(request: Request, journal_id: int):
    return {"message": "Hello, World!"}

#Update Journal Entry
@router.put("/{journal_id}", tags=["journal"])
@limiter.limit("5/minute")
def update_journal_entry(request: Request, journal_id: int, entry: JournalEntry):
    return {"message": "Hello, World!"}