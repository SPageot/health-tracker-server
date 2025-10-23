from fastapi import APIRouter, Request
from security.ratelimit import limiter

router = APIRouter();

#Get Advice
@router.get("/advice", tags=['analysis'])
@limiter.limit("5/minute")
def get_advice(request:Request):
    return {"message": "Hello, World!"}

#Get Mood Analysis with sentimental analysis From Journal Entries
@router.get("/mood", tags=['analysis'])
@limiter.limit("5/minute")
def get_mood_analysis(request:Request):
    return {"message": "Hello, World!"}

# Get Stress Analysis from journal entries
@router.get("/stress", tags=['analysis'])
@limiter.limit("5/minute")
def get_stress_analysis(request: Request):
    return {"message": "Hello, World!"}