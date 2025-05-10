from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import CustomHTTPException


async def custom_http_exception_handler(request: Request, exc: CustomHTTPException):
    return JSONResponse(
        status_code=exc.status,
        content={
            "response_code": exc.status,
            "status" : False,
            "message" : {
                "ID" : exc.message_id,
                "EN" : exc.message_en
            },
        },
    )


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    validation_errors = [
        f"{error['loc'][-1]}: {error['msg']}" for error in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content={
            "response_code": 422,    
            "status" : False,
            "message": {
                "ID" : "Terjadi kesalahan saat memvalidasi permintaan Anda",
                "EN" :  "There was an error validating your request",
            },
            "validation_problems": validation_errors,
        },
    )