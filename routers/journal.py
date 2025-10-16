from fastapi import APIRouter

router = APIRouter()


#Get All Journal Entries
@router.get("/", tags=["journal"])
def get_all_journal_entries():
    return {"message": "Hello, World!!!"}

#Get Journal Entry
@router.get("/{journal_id}", tags=["journal"])
def read_root():
    return {"message": "Hello, World!"}

#Add Journal Entry
@router.post("/entry", tags=["journal"])
def read_root():
    return {"message": "Hello, World!"}

#Delete Journal Entry
@router.delete("/{journal_id}", tags=["journal"])
def read_root():
    return {"message": "Hello, World!"}

#Update Journal Entry
@router.put("/{journal_id}", tags=["journal"])
def read_root():
    return {"message": "Hello, World!"}

#Get Advice
@router.get("/advice")
def read_root():
    return {"message": "Hello, World!"}

#Get Mood Analysis with sentimental analysis From Journal Entries
@router.get("/mood-analysis")
def read_root():
    return {"message": "Hello, World!"}

# Get Stress Analysis from journal entries
@router.get("/stress-analysis")
def read_root():
    return {"message": "Hello, World!"}
