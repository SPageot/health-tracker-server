from uuid import UUID
from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str
    password: str
    

class NewUser(User):
    email: str
    phone_number: str
    created_at: datetime = datetime.now()

class UserDetails(BaseModel):
    id: UUID
    username: str
    password: str
    email: str
    phone_number: str
    
