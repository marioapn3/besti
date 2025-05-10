from typing import List, Optional
from fastapi import HTTPException


class CustomHTTPException(HTTPException):
    def __init__(
        self,
        status: int,
        message_id : str,
        message_en : str,
        type_: Optional[str] = None,
        detail: Optional[str] = None,
        validation_problems: Optional[List[str]] = None,
    ):
        super().__init__(status_code=status, detail=detail)
        self.type_ = type_
        self.message_id = message_id
        self.message_en = message_en
        self.status = status
        self.detail = detail
        self.validation_problems = validation_problems or []
        