from app.database.schema import USERS
from sqlalchemy.orm import Session

def create_user(session: Session, uuid: str, email: str, password_hash: str, service_enabled: bool):
    """ DB 저장 """
    user = USERS(
        uuid= uuid,
        email= email,
        password_hash= password_hash,
        service_enabled= True
    )
    session.add(user)
    session.commit()

def read_user_by_email(session: Session, email: str):
    """ DB 조회 """
    user = session.query(USERS).filter(USERS.email == email).first()
    return user

def update_user(session: Session, email: str, password_hash: str, service_enabled: bool):
    """ DB 수정 """
    user = session.query(USERS).filter_by(email=email).first()

    if user:
        user.password_hash = password_hash
        user.service_enabled = service_enabled
        session.commit()
        return user
    else:
        ... # return 오류메시지 (로깅은 Auth.py에서)