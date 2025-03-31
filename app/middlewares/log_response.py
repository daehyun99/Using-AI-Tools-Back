import json
from fastapi import Request, Response
# from app.api.log import log_response 



async def log_response_middleware(request: Request, call_next) -> Response:
    # correlation_id = getattr(request.state, "correlation_id", "unknown")
    ...


from app.common.logger import logger
import time
async def test_middleware(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"✅ middleware test. : {response}")
    return response
