from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from db.repositories.repo_repository import get_repo_by_full_name, get_latest_repo_analysis_by_repo_id, create_repo_analysis, create_repo
from services.github_service import get_repo_stats, get_repo_commits
from services.ai_service import generate_repo_story
from models.repo import Repo
from models.repo_analysis import RepoAnalysis
from models.user import User

def get_or_create_analysis(db: Session, User: User, Repo: Repo):
    existing_analysis = get_latest_repo_analysis_by_repo_id(db, Repo.id)
    if existing_analysis and existing_analysis.generated_at > datetime.utcnow() - timedelta(hours=24):
        return existing_analysis
    repo_stats = get_repo_stats(User.github_username, Repo.name)
    commits = get_repo_commits(User.github_username, Repo.name)
    story = generate_repo_story(repo_stats, commits)
    analysis = RepoAnalysis(
        repo_id=Repo.id,
        authors=repo_stats["authors"],
        duration_weeks=repo_stats["duration_weeks"],
        commit_frequency=repo_stats["commit_frequency"],
        story=story,
        generated_at=datetime.utcnow(),
        total_commits=repo_stats["total_commits"],
        code_quality_score=None,  # Placeholder for actual code quality score
        security_score=None,  # Placeholder for actual security score
        maintainability_score=None,  # Placeholder for actual maintainability score
        overall_score=None  # Placeholder for actual overall score
    )
    return create_repo_analysis(db, analysis) 