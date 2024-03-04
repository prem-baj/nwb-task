from pymongo import MongoClient
from pymongo.server_api import ServerApi
import certifi
import os

username = os.getenv('MONGODB_USERNAME')
password = os.getenv('MONGODB_PASSWORD')
host = os.getenv('MONGODB_HOST')
app_name = os.getenv('MONGODB_APP_NAME')

# Connect to MongoDB
uri = f"mongodb+srv://{username}:{password}@{host}/nwb?retryWrites=true&w=majority&appName={app_name}"
client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())

db = client['nwb']
countries_collection = db['countries']
