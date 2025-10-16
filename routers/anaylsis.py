from fastapi import APIRouter

router = APIRouter()

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