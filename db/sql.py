from sqlmodel import SQLModel, create_engine
from config import settings

engine = create_engine(settings.db_url, echo=True)

SQLModel.metadata.create_all(engine)