from datetime import datetime
from uuid import UUID
import uuid
from sqlmodel import Field, SQLModel, table


class UserDB(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    password: str
    

class Users(SQLModel, table=True):
    id: UUID | None = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str
    password: str
    email: str = Field(default="", index=True)
    phone_number: str = Field(default="", index=True)
    created_at: datetime = Field(default=datetime.now(), index=True)

