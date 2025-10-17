from fastapi import APIRouter
from ..models.journalmodels import JournalEntry
router = APIRouter()


#Get All Journal Entries
@router.get("/", tags=["journal"])
def get_all_journal_entries():
    return {"message": "Hello, World!!!"}

#Get Journal Entry
@router.get("/{journal_id}", tags=["journal"])
def get_journal_entry(journal_id: int):
    return {"message": "Hello, World!"}

#Add Journal Entry
@router.post("/entry", tags=["journal"])
def add_journal_entry(entry: JournalEntry):
    return {"message": "Hello, World!"}

#Delete Journal Entry
@router.delete("/{journal_id}", tags=["journal"])
def delete_journal_entry(journal_id: int):
    return {"message": "Hello, World!"}

#Update Journal Entry
@router.put("/{journal_id}", tags=["journal"])
def update_journal_entry(journal_id: int, entry: JournalEntry):
    return {"message": "Hello, World!"}

#Get Advice
@router.get("/advice")
def get_advice():
    return {"message": "Hello, World!"}

#Get Mood Analysis with sentimental analysis From Journal Entries
@router.get("/mood-analysis")
def get_mood_analysis():
    return {"message": "Hello, World!"}

# Get Stress Analysis from journal entries
@router.get("/stress-analysis")
def get_stress_analysis():
    return {"message": "Hello, World!"}
