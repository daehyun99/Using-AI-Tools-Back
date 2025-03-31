import uuid

def generate_metadata():
    return str(uuid.uuid4())

from app.database.schema import temps
from app.api.response import SuccessResponse

from sqlalchemy.orm import Session
import json


def logging_request(session: Session, correlation_id: str, msg: str, metadata: dict):
    log = temps(
        log_type="REQUEST",
        correlation_id=correlation_id,
        msg=msg,
        data=metadata  # 요청의 경우 data 필드에 metadata 기록
    )
    session.add(log)
    session.commit()

def logging_response(session: Session, correlation_id: str, obj: SuccessResponse):
    """ DB에 로깅 + Response 반환"""
    log = temps(
        layer = "PRESENTATION",
        log_type="RESPONSE",
        correlation_id="correlation_id",
        status=obj.status,
        msg=obj.msg,
        data=obj.data,
        error=obj.error,
    )
    session.add(log)
    session.commit()
    return obj
