from app.common.status import StatusCode
import json

# ================================================================================ #

class APIResponse():
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


class SuccessResponse(APIResponse):
    def __init__(self, msg: str = "SuccessResponse", data= None):
        super().__init__(
            status=StatusCode.SUCCESS,
            msg= "✅ "+msg,
            error=None,
            data=data
        )

class FailResponse(APIResponse):
    def __init__(self, msg: str = "FailResponse", data= None):
        super().__init__(
            status=StatusCode.SUCCESS,
            msg= "🛑 "+msg,
            error=None,
            data=data
        )