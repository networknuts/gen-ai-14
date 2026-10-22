from dotenv import load_dotenv
import os 
import requests 
import json 

# STEP 1: LOAD THE DOT ENV FILE
load_dotenv()

# STEP 2: ASK FOR CUSTOMER QUERY
human_query = input("Enter your query: ")

# STEP 3: DECLARE THE OPENAI API KEY
MY_OPENAI_API_KEY = os.getenv("MY_OPENAI_API_KEY")

# STEP 4: SET THE OPENAI URL
OPENAI_URL = "https://api.openai.com/v1/responses"

# STEP 5: SET THE HEADERS
OPENAI_HEADERS = {"Content-Type": "application/json","Authorization": f"Bearer {MY_OPENAI_API_KEY}"}

# STEP 6: SET THE DATA / PAYLOAD
OPENAI_DATA = {"model":"gpt-6-luna","input": human_query}

# STEP 7: MAKE THE CONNECTION
response = requests.post(OPENAI_URL,headers=OPENAI_HEADERS,data=json.dumps(OPENAI_DATA))

human_response = response.json()['output'][1]['content'][0]['text']

print(human_response)