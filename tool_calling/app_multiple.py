from dotenv import load_dotenv
from openai import OpenAI 
import os 
import requests 
import json

# SETUP THE ENVIRONMENT
load_dotenv()
client = OpenAI()

f = open("weather_tool_description.txt","r")
weather_tool_description = f.read()
f.close()

f = open("order_tool_description.txt","r")
order_tool_description = f.read()
f.close()

# CREATE TOOL - GET WEATHER
def get_weather(zipcode):
    country_code = "in"
    openweathermap_api_key = os.getenv("OPENWEATHERMAP_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{country_code}&appid={openweathermap_api_key}"
    response = requests.get(url)
    result = response.json()
    return result 

# CREATE TOOL - GET ORDER
def get_order(userid):
    url = f"http://localhost:8000/delivery/{userid}"
    response = requests.get(url)
    result = response.json()
    return result 

# TOOL SCHEMA / TOOL BLUEPRINT

#URL: https://developers.openai.com/api/docs/guides/function-calling?api-mode=responses
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
    },
    {
        "type": "function",
        "name": "get_order",
        "description": order_tool_description,
        "strict": False,
        "parameters": {
            "type": "object",
            "properties": {
                "userid": {
                    "type": "string",
                    "description": "The ID of the user to get the order data for."
                },
            },
            "required": ["userid"]
        }
    }
]

# ASK FOR CUSTOMER QUERY AND MAKE LLM CALL

human_query = input("Enter your query: ")

response = client.responses.create(
    model="gpt-6-luna",
    input=human_query,
    tools=openai_tools
)

# EXECUTE THE TOOL WHEN REQUIRED
function_output = []

for item in response.output:
    if item.type == "function_call": 
        arguments = json.loads(item.arguments) # str to dict 
        if item.name == "get_weather":
            result = get_weather(arguments['zipcode'])
            print("="*20,"RAW FUNCTION OUTPUT","="*20)
            print(result)
        elif item.name == "get_order":
            result = get_order(arguments['userid'])
            print("="*20,"RAW FUNCTION OUTPUT","="*20)
            print(result)
            
        function_output.append({
            "type": "function_call_output",
            "call_id": item.call_id,
            "output": json.dumps({"result": result}) #dict to str
        })

# SECOND LLM CALL
final_response = client.responses.create(
    model="gpt-6-luna",
    input=function_output,
    previous_response_id=response.id
)

print("="*20,"AI ENHANCED OUTPUT","="*20)
print(final_response.output_text)