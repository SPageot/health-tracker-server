from pydantic import BaseModel
from datetime import datetime

class JournalEntry(BaseModel):
   id: int | None = None
   date: datetime = datetime.now()
   content: str = ""
   created_at: datetime = datetime.now()