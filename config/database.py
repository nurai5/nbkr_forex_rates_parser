from pymongo import ASCENDING
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI")
# client = MongoClient(uri, server_api=ServerApi('1'))

# Create a new client and connect to the server
client = MongoClient('mongodb', 27017)

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
