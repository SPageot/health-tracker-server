from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    username: str = ""
    password: str = ""
    

class NewUser(User):
    email: str
    phone_number: str
    created_at: datetime = datetime.now()
    
