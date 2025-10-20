from fastapi import APIRouter

router = APIRouter();


#Get Advice
@router.get("/advice", tags=['analysis'])
def get_advice():
    return {"message": "Hello, World!"}

#Get Mood Analysis with sentimental analysis From Journal Entries
@router.get("/mood", tags=['analysis'])
def get_mood_analysis():
    return {"message": "Hello, World!"}

# Get Stress Analysis from journal entries
@router.get("/stress", tags=['analysis'])
def get_stress_analysis():
    return {"message": "Hello, World!"}