import setup  # noqa: F401
from database import countries_collection
import requests

countries_api_url = 'https://restcountries.com/v3.1/all'
response = requests.get(countries_api_url)

if response.status_code == 200:
    countries_data = response.json()

    # Clear the collection if you don't want duplicates
    countries_collection.delete_many({})

    countries_collection.insert_many(countries_data)
    print(f"Inserted {len(countries_data)} records into the database.")
else:
    print("Failed to fetch countries data")
