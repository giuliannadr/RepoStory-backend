from sqlalchemy.orm import Session
from models.user import User
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()
def get_user_by_github_username(db: Session, github_username: str):
    return db.query(User).filter(User.github_username == github_username).first()
def create_user(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
def update_user(db: Session, user: User):
    db.merge(user)
    db.commit()
    db.refresh(user)
    return user
def delete_user(db: Session, user: User):
    db.delete(user)
    db.commit()
    return user
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()
def get_user_repos(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user.repos if user else None
def get_user_analyses(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        analyses = []
        for repo in user.repos:
            analyses.extend(repo.analyses)
        return analyses
    return None
def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()
def update_last_analyzed(db: Session, user: User):
    user.last_analyzed_at = datetime.utcnow()
    db.commit()
    db.refresh(user)
    return user
