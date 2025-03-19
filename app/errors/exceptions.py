from app.common.status import StatusCode, Service, DetailCode

from app.common.response import APIException


class ErrorResponse_LLM(APIException):
    def __init__(self, msg: str = f"🛑 ErrorResponse_LLM", ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{Service.LLM}{DetailCode.Unknown_Error}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }
        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=msg,
            error=error_detail,
            data=None
        )


class ErrorResponse_Video(APIException):
    def __init__(self, msg: str = f"🛑 ErrorResponse_Video", ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{Service.Video}{DetailCode.Unknown_Error}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }
        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=msg,
            error=error_detail,
            data=None
        )


class ErrorResponse_File(APIException):
    def __init__(self, msg: str = f"🛑 ErrorResponse_File", ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{Service.Video}{DetailCode.Unknown_Error}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }
        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=msg,
            error=error_detail,
            data=None
        )