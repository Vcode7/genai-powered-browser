"""MongoDB database configuration and connection (Render & Atlas compatible)"""
import os
import ssl
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import ASCENDING, DESCENDING

load_dotenv()

# MongoDB connection settings
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "lernova_db")

# Global variables
client: AsyncIOMotorClient = None
database = None


async def connect_to_mongo():
    """Connect to MongoDB (handles TLS 1.2 for Atlas/Render)"""
    global client, database
    try:
        # Enforce TLS 1.2 to prevent SSL handshake errors
        client = AsyncIOMotorClient(
            MONGODB_URL,
            tls=True,
            tlsAllowInvalidCertificates=False,
            ssl=True,
            ssl_cert_reqs=ssl.CERT_REQUIRED,
            ssl_version=ssl.PROTOCOL_TLSv1_2,
        )
        database = client[DATABASE_NAME]

        await create_indexes()
        print(f"✅ Connected to MongoDB: {DATABASE_NAME}")
    except Exception as e:
        print(f"❌ Error connecting to MongoDB: {e}")
        raise


async def close_mongo_connection():
    """Close MongoDB connection"""
    global client
    if client:
        client.close()
        print("✅ MongoDB connection closed")


async def create_indexes():
    """Create database indexes for better performance"""
    try:
        # Bookmarks
        await database.bookmarks.create_index([("user_id", ASCENDING), ("url", ASCENDING)], unique=True)
        await database.bookmarks.create_index([("created_at", DESCENDING)])

        # History
        await database.history.create_index([("user_id", ASCENDING), ("visited_at", DESCENDING)])
        await database.history.create_index([("url", ASCENDING)])

        # Settings
        await database.settings.create_index([("user_id", ASCENDING)], unique=True)

        # Focus sessions
        await database.focus_sessions.create_index([("user_id", ASCENDING), ("active", ASCENDING)])
        await database.focus_sessions.create_index([("created_at", DESCENDING)])

        print("✅ Database indexes created")
    except Exception as e:
        print(f"⚠️ Error creating indexes: {e}")


def get_database():
    """Return MongoDB database instance"""
    return database
