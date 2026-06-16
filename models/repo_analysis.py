from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from db.database import Base
from sqlalchemy.orm import relationship
class RepoAnalysis(Base):
    __tablename__ = "repo_analyses"
    id = Column(Integer, primary_key=True, index=True)
    repo_id = Column(Integer, ForeignKey("repos.id"))
    authors = Column(String)
    duration_weeks = Column(Integer)
    commit_frequency = Column(Integer)
    story = Column(Text)
    generated_at = Column(DateTime)
    total_commits = Column(Integer)
    code_quality_score = Column(Integer)
    security_score = Column(Integer)
    maintainability_score = Column(Integer)
    overall_score = Column(Integer)
    repo = relationship("Repo", back_populates="analyses")