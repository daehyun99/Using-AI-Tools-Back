from app.common.status import StatusCode, Service, DetailCode

from app.common.response import APIResponse


class FailLoadLLM(APIResponse):
    def __init__(self, ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{Service.LLM}{DetailCode.Not_Found}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }
        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=f"🛑 LLM 모델 로드 실패",
            error=error_detail,
            data=None
        )


class FailDownloadVideo(APIResponse):
    def __init__(self, ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{'2'.zfill()}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }

        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=f"🛑 영상 다운로드 실패",
            error=error_detail,
            data=None
        )


class FailDeleteVideo(APIResponse):
    def __init__(self, ex: Exception = None):
        error_code = f"{StatusCode.SERVER_ERROR}{'2'.zfill()}"
        error_detail = {
            "code": error_code,
            "ex" : str(ex) if ex else None
        }

        super().__init__(
            status=StatusCode.SERVER_ERROR,
            msg=f"🛑 영상 삭제 실패",
            error=error_detail,
            data=None
        )

