# Wiki 참고 : https://github.com/daehyun99/Using-AI-Tools/wiki/error-codes

class StatusCode:
    TEMP_ERROR = 499 # 개발용 임시 에러
    SUCCESS = 200
    CLIENT_ERROR = 400
    SERVER_ERROR = 500
        

class Service:
    DEFAULT = 0 # 개발용 임시 서비스
    LLM = 1
    DATABASE = 2
    VIDEO = 3
    FILE = 4


class DetailCode:
    Unknown_Error = "001"
    Not_Found = "002"
    Invalid_Data = "003"
    Permission_Denied = "004"
    Authentication_Failed = "005"
    Timeout = "006"
    Unsupported_Format = "007"
    Rate_Limit_Exceeded = "008"
    Internal_System_Error = "009"
