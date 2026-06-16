from sqlalchemy.orm import Session
from models.repo import Repo
from models.repo_analysis import RepoAnalysis
def get_repo(db: Session, repo_id: int):
    return db.query(Repo).filter(Repo.id == repo_id).first()
def get_repo_by_full_name(db: Session, full_name: str):
    return db.query(Repo).filter(Repo.full_name == full_name).first()
def create_repo(db: Session, repo: Repo):
    db.add(repo)
    db.commit()
    db.refresh(repo)
    return repo
def update_repo(db: Session, repo: Repo):
    db.merge(repo)
    db.commit()
    db.refresh(repo)
    return repo
def delete_repo(db: Session, repo: Repo):
    db.delete(repo)
    db.commit()
    return repo
def get_repos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Repo).offset(skip).limit(limit).all()   
def get_repo_analyses(db: Session, repo_id: int):
    repo = db.query(Repo).filter(Repo.id == repo_id).first()
    return repo.analyses if repo else None  
def create_repo_analysis(db: Session, analysis: RepoAnalysis):
    db.add(analysis)
    db.commit()
    db.refresh(analysis)
    return analysis
def get_repo_analysis(db: Session, analysis_id: int):
    return db.query(RepoAnalysis).filter(RepoAnalysis.id == analysis_id).first()
def delete_repo_analysis(db: Session, analysis: RepoAnalysis):
    db.delete(analysis)
    db.commit()
    return analysis
def get_repo_analyses_by_repo_id(db: Session, repo_id: int):
    return db.query(RepoAnalysis).filter(RepoAnalysis.repo_id == repo_id).all()
def get_repo_analyses_by_user_id(db: Session, user_id: int):
    return db.query(RepoAnalysis).join(Repo).filter(Repo.owner_id == user_id).all()
def get_latest_repo_analysis_by_repo_id(db: Session, repo_id: int):
    return db.query(RepoAnalysis).filter(RepoAnalysis.repo_id == repo_id).order_by(RepoAnalysis.generated_at.desc()).first()
def get_latest_repo_analysis_by_user_id(db: Session, user_id: int):
    return db.query(RepoAnalysis).join(Repo).filter(Repo.owner_id == user_id).order_by(RepoAnalysis.generated_at.desc()).first()
def get_repo_analysis_count_by_repo_id(db: Session, repo_id: int):
    return db.query(RepoAnalysis).filter(RepoAnalysis.repo_id == repo_id).count()
def get_repo_analysis_count_by_user_id(db: Session, user_id: int):
    return db.query(RepoAnalysis).join(Repo).filter(Repo.owner_id == user_id).count()
def get_repo_analysis_summary_by_repo_id(db: Session, repo_id: int):    
    analyses = db.query(RepoAnalysis).filter(RepoAnalysis.repo_id == repo_id).all()
    if not analyses:
        return None
    summary = {
        "repo_id": repo_id,
        "total_analyses": len(analyses),
        "average_code_quality_score": sum(a.code_quality_score for a in analyses) / len(analyses),
        "average_security_score": sum(a.security_score for a in analyses) / len(analyses),
        "average_maintainability_score": sum(a.maintainability_score for a in analyses) / len(analyses),
        "average_overall_score": sum(a.overall_score for a in analyses) / len(analyses),
    }
    return summary
def get_repo_analysis_summary_by_user_id(db: Session, user_id: int):
    analyses = db.query(RepoAnalysis).join(Repo).filter(Repo.owner_id == user_id).all()
    if not analyses:
        return None
    summary = {
        "user_id": user_id,
        "total_analyses": len(analyses),
        "average_code_quality_score": sum(a.code_quality_score for a in analyses) / len(analyses),
        "average_security_score": sum(a.security_score for a in analyses) / len(analyses),
        "average_maintainability_score": sum(a.maintainability_score for a in analyses) / len(analyses),
        "average_overall_score": sum(a.overall_score for a in analyses) / len(analyses),
    }
    return summary
