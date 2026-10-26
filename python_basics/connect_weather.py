import requests
from dotenv import load_dotenv
import os 

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
COUNTRY_CODE = input("Enter your country code: ")
ZIP_CODE = input("Enter your zip code: ")

OPENWEATHERMAP_URL = f"https://api.openweathermap.org/data/2.5/weather?zip={ZIP_CODE},{COUNTRY_CODE}&appid={OPENWEATHERMAP_API_KEY}"

response = requests.get(OPENWEATHERMAP_URL)

if response.status_code == 200:
    print("Connection success")
    print(response.json())
else:
    print("Connection failure")
    print(f"Error: {response.json()['message']}")