from pydantic import BaseModel
from typing import Any, Optional
from enum import Enum

class ResponseCode(Enum):
    SUCCESS = (0, "Success")
    NOT_FOUND = (404, "Resource not found")
    SERVER_ERROR = (500, "Internal server error")
    VALIDATION_ERROR = (422, "Validation error")
    UNAUTHORIZED = (401, "Unauthorized")
    FORBIDDEN = (403, "Forbidden")

    def __init__(self, code, message):
        self.code = code
        self.message = message

class ResponseModel(BaseModel):
    code: int
    msg: str
    data: Optional[Any] = None

    @classmethod
    def from_code(cls, response_code: ResponseCode, data: Any = None):
        return cls(code=response_code.code, msg=response_code.message, data=data)