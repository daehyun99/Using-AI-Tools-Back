
class StatusCode:
    HTTP_500 = 500
    HTTP_400 = 400
    HTTP_401 = 401
    HTTP_403 = 403
    HTTP_404 = 404
    HTTP_405 = 405

class APIException(Exception):
    status_code: int
    code: str
    msg: str
    detail: str

    def __init__(
            self,
            *args,
            status_code: int = StatusCode.HTTP_500,
            code: str = "000000",
            msg: str = None,
            detail: str = None,
            ex: Exception = None,
            ):
        self.status_code = status_code
        self.code = code
        self.msg = msg
        self.detail = detail
        super().__init__(ex)


class FailLoadLLM(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_500,
            msg=f"LLM 모델 로드 실패",
            code=f"{StatusCode.HTTP_500}{'1'.zfill(4)}",
            ex=ex,
        )
    def __str__(self):
        return f"{self.code} - {self.msg}"


class FailDownloadVideo(APIException):
    def __init__(self, ex: Exception = None):
        super().__init__(
            status_code=StatusCode.HTTP_500,
            msg=f"영상 다운로드 실패",
            code=f"{StatusCode.HTTP_500}{'2'.zfill(4)}",
            ex=ex,
        )
    def __str__(self):
        return f"{self.code} - {self.msg}"
    

