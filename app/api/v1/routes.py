from fastapi import APIRouter

from app.api.v1.endpoints import (
        message_navigator,
    recognize_handler,
    feedback_handler,   
)



router = APIRouter()


router.include_router(message_navigator.router, prefix="/navigator-advance", tags=["Message Navigator"])
router.include_router(feedback_handler.router, prefix="/feedback", tags=["Feedback"])
