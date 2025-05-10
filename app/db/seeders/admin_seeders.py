# from motor.motor_asyncio import AsyncIOMotorClient
from app.db.database import admin_collection
from app.core.security import hash_password
import datetime

async def seed_admin():
    admin_data = [
        {
            "name": "Super Admin",
            "email": "superadmin@monago.com",
            "password": hash_password("monago-superadmin"),
            "role": "superadmin",
            "permissions": ["manage_plans", "view_reports"],
            "is_active": True,
            "created_at": datetime.datetime.utcnow().isoformat(),
            "updated_at": datetime.datetime.utcnow().isoformat()
        },
    ]

    if admin_collection.count_documents({}) == 0:
        admin_collection.insert_many(admin_data)