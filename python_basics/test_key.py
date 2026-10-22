import os 
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("ABC")
print(api_key)