import pymongo
from config import MONGO_URL

try:
    client = pymongo.MongoClient(MONGO_URL)
    if client: print("Connected successfully!")
except:
    print("Could not connect to MongoDB")

db = client.tambangla
users_collection = db["users"]