from functools import wraps
from typing import Annotated, Union
from fastapi.responses import JSONResponse
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import jwt
from fastapi import Depends, Header, Request, HTTPException
from app.exceptions.custom_exceptions import CustomHTTPException

from app.core.security import decode_token


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = False):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise CustomHTTPException(
                    type_="/unauthorized",
                    status=403,
                    message_en="Invalid authentication scheme.",
                    message_id="Autentikasi Scheme Tidak Valid.",
                )
            payload = self.verify_jwt(credentials.credentials)
            if payload is None:
                raise CustomHTTPException(
                    type_="/unauthorized",
                    status=403,
                    message_en="Invalid token or expired token.",
                    message_id="Token Tidak Valid atau Telah Kadaluarsa.",
                )
            request.state.jwtData = payload
            return credentials.credentials
        else:
            raise CustomHTTPException(
                type_="/unauthorized",
                status=403,
                message_en="Unauthorized",
                message_id="Tidak Diizinkan.",
            )

    def verify_jwt(self, jwtoken: str):
        try:
            payload = decode_token(jwtoken)
            return payload
        except:
            return None