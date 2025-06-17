from urllib.request import Request
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from contextlib import asynccontextmanager
from app.api.v1.routes import router as api_router
import time
from app.core.logger_config import configure_logger
from app.exceptions.handlers import custom_http_exception_handler, validation_exception_handler
from app.exceptions.custom_exceptions import CustomHTTPException
from app.exceptions.schemas.custom_error_schema import CustomErrorSchema
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from fastapi.staticfiles import StaticFiles
from slowapi.middleware import SlowAPIMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from app.api.v1.endpoints.recognize_handler import load_clip_model, load_dataset


import os

is_production = os.getenv("ENVIRONMENT", "development").lower() == "production"
limiter = Limiter(key_func=get_remote_address)

configure_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown."""
    # load_clip_model()
    # load_dataset()
    yield



app = FastAPI(
    title="BESTI (Bot STI) API",
    version="1.0.0",
    description="API for managing BESTI (Bot STI) API platform.",
    docs_url=None if is_production else "/docs",  
    redoc_url=None if is_production else "/redoc" ,
    lifespan=lifespan,
    root_path="/besti-api"
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(SlowAPIMiddleware)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,  
    allow_methods=["*"],  
    allow_headers=["*"],  
    expose_headers=["Authorization"],  
)

app.add_exception_handler(CustomHTTPException, custom_http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)


# @app.options("/api/v1/auth/login")
# async def preflight_login():
#     headers = {
#         "Access-Control-Allow-Origin": "*",
#         "Access-Control-Allow-Methods": "POST, GET, OPTIONS",
#         "Access-Control-Allow-Headers": "Authorization, Content-Type",
#         "Access-Control-Allow-Credentials": "true",
#     }
#     return Response(status_code=200, headers=headers)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time() 
    response = await call_next(request)  
    process_time = time.time() - start_time  

    response.headers['X-Response-Time'] = f"{round(process_time * 1000, 2)} ms"

    return response


app.mount("/public", StaticFiles(directory="public"), name="public")
app.mount("/private", StaticFiles(directory="private"), name="private")

@app.get("/")
async def root():
    return {"message": "Welcome to BESTI (Bot STI) API."}

app.include_router(api_router, prefix="/api/v1")