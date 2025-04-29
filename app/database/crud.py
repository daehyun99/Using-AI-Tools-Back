from app.database.schema import USERS
from sqlalchemy.orm import Session

def create_user(session: Session, uuid: str, email: str, password_hash: str, service_enabled: bool):
    """ DB에 저장 """
    user = USERS(
        uuid= uuid,
        email= email,
        password_hash= password_hash,
        service_enabled= True
    )
    session.add(user)
    session.commit()