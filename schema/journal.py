from datetime import datetime
from sqlmodel import SQLModel, table

class JournalEntryDB(SQLModel, table=True):
   id: int | None = None
   date: datetime = datetime.now()
   content: str
   created_at: datetime = datetime.now()