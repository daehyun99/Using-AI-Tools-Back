import json
from fastapi import Depends, Request, Response
from app.services.utils import log_response 

from app.database.conn import db


async def log_response_middleware(request: Request, call_next) -> Response:
    # correlation_id = getattr(request.state, "correlation_id", "unknown")
    response = await call_next(request)
    body = b"".join([chunk async for chunk in response.body_iterator])

    async def regenerate_body(body: bytes):
        yield body
    response.body_iterator = regenerate_body(body)

    try:
        data = json.loads(body)
    except Exception:
        data = {"raw": body.decode("utf-8", errors="replace")}
    
    # 간단한 메시지 설정
    msg = "Response logged from middleware"
    
    session = next(db.session())

    # 상태 코드에 따라 성공/에러로 구분하여 로깅
    if response.status_code < 400:
        log_response(
            session= session,
            correlation_id="unknown",
            msg=msg,
            status=response.status_code,
            result_data=data,
            error=None
        )
    else:
        log_response(
            session= session,
            correlation_id="unknown",
            msg=msg,
            status=response.status_code,
            result_data=None,
            error=data
        )
    
    # 원래의 응답 반환
    return response