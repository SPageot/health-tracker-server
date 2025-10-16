from fastapi import APIRouter

router = APIRouter()

#Get Journal Entries
@router.get("/journal")
def read_root():
    return {"message": "Hello, World!"}
#Add Journal Entry
@router.post("/journal")
def read_root():
    return {"message": "Hello, World!"}

#Delete Journal Entry
@router.delete("/journal")
def read_root():
    return {"message": "Hello, World!"}

#Update Journal Entry
@router.put("/journal")
def read_root():
    return {"message": "Hello, World!"}
