from core.db import Base, engine
from db.models.user import User

def create_table():
    Base.metadata.create_all(bind=engine)

