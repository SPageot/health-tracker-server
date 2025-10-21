from sqlmodel import SQLModel, create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:St%40nley1985@localhost:5432/self-care-journal"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)