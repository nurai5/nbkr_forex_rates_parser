from pymongo import ASCENDING
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")
is_local_mongodb = os.getenv("IS_LOCAL_MONGODB", "").lower() in ('true', '1', 't', 'y', 'yes')

if is_local_mongodb:
    client = MongoClient('mongodb', 27017)
else:
    client = MongoClient(uri, server_api=ServerApi('1'))

db = client.forex_rates

collection_name = db['NBKR_forex_rates']

collection_name.create_index(
    [
        ("base_currency", ASCENDING),
        ("target_currency", ASCENDING),
        ("date", ASCENDING)
    ],
    unique=True
)
