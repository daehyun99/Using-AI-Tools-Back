class StatusCode:
    SUCCESS = 200
    CLIENT_ERROR = 400
    SERVER_ERROR = 500


class Service:
    LLM = 1
    DATABASE = 2
    VIDEO = 3
    File = 4


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
