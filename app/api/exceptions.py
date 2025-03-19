from app.common.status import StatusCode, Service, DetailCode
import json

# ================================================================================ #

class APIException(Exception):
    def __init__(self, status: int, msg: str, error= None, data= None):
        self.status = status
        self.msg = msg
        self.error = error
        self.data = data

    def to_dict(self):
        return {
            "status": self.status,
            "msg": self.msg,
            "error": self.error,
            "data": self.data,
        }
    def __str__(self):
        return json.dumps(self.to_dict(), indent= 4, ensure_ascii= False)

# ================================================================================ #


class ErrorResponse(APIException):
    def __init__(self, msg: str = f"🛑 ErrorResponse", ex: Exception = None):
        error_code = f"{StatusCode.TEMP_ERROR}{Service.DEFAULT}{DetailCode.Unknown_Error}"
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
        error_code = f"{StatusCode.SERVER_ERROR}{Service.VIDEO}{DetailCode.Unknown_Error}"
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
        error_code = f"{StatusCode.SERVER_ERROR}{Service.FILE}{DetailCode.Unknown_Error}"
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