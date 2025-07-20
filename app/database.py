from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

MONGODB_URI = os.getenv("MONGODB_URI")
MONGODB_DB_NAME = os.getenv("MONGODB_DB_NAME")

client = AsyncIOMotorClient(MONGODB_URI)
db = client[MONGODB_DB_NAME]
