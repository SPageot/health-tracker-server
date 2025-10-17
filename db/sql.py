from sqlmodel import SQLModel, create_engine

SQLALCHEMY_DATABASE_URL = ""

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)