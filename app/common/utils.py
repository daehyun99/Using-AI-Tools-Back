from app.database.schema import SYSTEM_LOGS

from app.api.request import SuccessRequest
from app.api.response import SuccessResponse

from sqlalchemy.orm import Session
import json

import re
from uuid import uuid4

def generate_metadata():
    metadata = None
    while not metadata:
        metadata_candidate = f"{str(uuid4())[:-12]}{str(uuid4())}"
        metadata_check = True # DB에서 metadata 중복여부를 확인하는 코드로 수정 필요 (True -> DB에 중복 없음, False -> DB에 중복 있음)
        if metadata_check:
            metadata = metadata_candidate
    return metadata

def generate_id():
    id = None
    while not id:
        id_candidate = f"{str(uuid4())[:8]}{str(uuid4())[:8]}"
        id_check = True # DB에서 id 중복여부를 확인하는 코드로 수정 필요
        if id_check:
            id = id_candidate
    return id

def generate_pw():
    pw = None
    while not pw:
        pw_candidate = f"{str(uuid4())[:8]}{str(uuid4())[:8]}"
        pw_check = True # DB에서 pw 중복여부를 확인하는 코드로 수정 필요
        if pw_check:
            pw = pw_candidate
    return pw

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

    if re.match(pattern, email):
        return True
    else:
        return False
    

def logging_request(session: Session, layer: str, correlation_id: str, obj: SuccessRequest):
    """ DB에 로깅 """
    log = SYSTEM_LOGS(
        layer = layer,
        log_type="REQUEST",
        correlation_id=correlation_id,
        msg=obj.msg,
        data=obj.data,  # metadata
        error=obj.error
    )
    session.add(log)
    session.commit()

def logging_response(session: Session, layer: str, correlation_id: str, obj: SuccessResponse):
    """ DB에 로깅 + Response 반환"""
    log = SYSTEM_LOGS(
        layer = layer,
        log_type="RESPONSE",
        correlation_id=correlation_id,
        status=obj.status,
        msg=obj.msg,
        data=obj.data,
        error=obj.error,
    )
    session.add(log)
    session.commit()
    return obj
