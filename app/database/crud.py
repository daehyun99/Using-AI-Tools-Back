from app.database.schema import USERS, SERVICE_USAGE
from sqlalchemy.orm import Session

# ========================
# USERS - CREATE
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

# USERS - READ
def read_user_by_email(session: Session, email: str):
    """ DB 조회 """
    user = session.query(USERS).filter(USERS.email == email).first()
    return user

def read_user_by_uuid(session: Session, uuid: str):
    """ DB 조회 """
    user = session.query(USERS).filter(USERS.uuid == uuid).first()
    return user

# USERS - UPDATE
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

# USERS - DELETE
def delete_user(session: Session, email: str):
    """ DB 삭제 """
    ...

# ========================
# SERVICE_USAGE
def create_service_usage(session: Session, uuid: str, correlation_id: str):
    """ DB 저장 """
    service_usage = SERVICE_USAGE(
        uuid= uuid,
        correlation_id= correlation_id
    )
    session.add(service_usage)
    session.commit()
