from sqlalchemy import Column, Integer, String
from models.database import Base

class User(Base):
    __tablename__ = "users"
    
    pin = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    department = Column(String, index=True)
