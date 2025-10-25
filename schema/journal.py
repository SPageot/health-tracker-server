from datetime import datetime
from uuid import UUID
from sqlmodel import SQLModel, Field
import uuid

class Journal(SQLModel, table=True):
   id: UUID = Field(default_factory=uuid.uuid4, primary_key=True)
   user_id: UUID 
   content: str
   created_at: datetime = datetime.now()