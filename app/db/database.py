from pymongo import MongoClient
from app.core.config import settings  # Import settings from your configuration file
from pymongo import ASCENDING
from motor.motor_asyncio import AsyncIOMotorClient

# MongoDB Connection
client = MongoClient(settings.MONGODB_URL)
# clientMotor 
clientmotor = AsyncIOMotorClient(settings.MONGODB_URL)
db = client[settings.DATABASE_NAME]
dbMotor = clientmotor[settings.DATABASE_NAME]

sessions_collection = db["sessions"] # _id, user_id, created_at, updated_at
messages_collection = db["messages"] # _id, session_id, role, content, created_at, updated_at


# Automated Index Creation
def create_indexes():
    sessions_collection.create_index('_id')
    messages_collection.create_index([('session_id', ASCENDING), ('created_at', ASCENDING)])



create_indexes()
