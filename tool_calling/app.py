from dotenv import load_dotenv
from openai import OpenAI 
import os 
import requests 

# SETUP THE ENVIRONMENT
load_dotenv()
client = OpenAI()
f = open("weather_tool_description.txt","r")
weather_tool_description = f.read()
f.close()

# CREATE THE TOOL / FUNCTION
def get_weather(zipcode):
    country_code = "in"
    openweathermap_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country_code}&appid={openweathermap_api_key}"
    response = requests.get(url)
    result = response.json()
    return result 

# TOOL SCHEMA / TOOL BLUEPRINT
openai_tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": weather_tool_description,
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "zipcode": {
                    "type": "string",
                    "description": "the zipcode of the location to get the weather of."
                },
            },
            "required": ["zipcode"],
        },
    }
]

human_query = input("Enter your query: ")

response = client.responses.create(
    model="gpt-6-luna",
    input=human_query,
    tools=openai_tools
)

print(response.output)