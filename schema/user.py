from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel


class UserDB(SQLModel, table=True):
    username: str
    password: str
    

class NewUserDB(UserDB, table=True):
    id: UUID
    email: str
    phone_number: str
    created_at: datetime = datetime.now()