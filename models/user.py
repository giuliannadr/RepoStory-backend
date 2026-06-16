from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from db.database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    github_username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    avatar_url = Column(String)
    location = Column(String)
    hashed_password = Column(String, nullable=True)
    created_at = Column(DateTime)
    last_analyzed_at = Column(DateTime)
    repos = relationship("Repo", back_populates="owner")