from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from db.database import Base
from sqlalchemy.orm import relationship
class Repo(Base):
    __tablename__ = "repos"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    full_name = Column(String, unique=True, index=True)
    description = Column(String)
    html_url = Column(String)
    stargazers_count = Column(Integer)
    forks_count = Column(Integer)
    language = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    last_commit_at = Column(DateTime)
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="repos")
    analyses = relationship("RepoAnalysis", back_populates="repo")