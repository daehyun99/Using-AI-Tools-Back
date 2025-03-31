from app.models import temps  # temps 모델 임포트 (temps 클래스)
from sqlalchemy.orm import Session
import json

def log_request(db: Session, correlation_id: str, msg: str, metadata: dict):
    log = temps(
        log_type="REQUEST",
        correlation_id=correlation_id,
        msg=msg,
        data=metadata  # 요청의 경우 data 필드에 metadata 기록
    )
    db.add(log)
    db.commit()


def log_response(db: Session, correlation_id: str, msg: str, status: str, result_data: dict = None, error: dict = None):
    log = temps(
        log_type="RESPONSE",
        correlation_id=correlation_id,
        status=status,
        msg=msg,
        data=result_data,  # 응답의 경우 data 필드에 실제 응답 데이터 기록
        error=error
    )
    db.add(log)
    db.commit()
