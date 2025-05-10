from fastapi import HTTPException, status
from app.services.admin_service import AdminService
from loguru import logger

def check_permission(email: str, required_permission: str):
    admin = AdminService.get_admin_by_email(email)
    if not admin:
        logger.error("admin_not_found email: " + email)
        raise ValueError("admin_not_found")
    
    if required_permission not in admin.get("permissions", []):
        logger.error("permission_denied email: " + email)
        logger.error("Permission admin : " + str(admin.get("permissions", [])))
        logger.error("Permission required : " + required_permission)
        raise ValueError("permission_denied")
