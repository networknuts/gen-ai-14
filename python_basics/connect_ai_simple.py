from dotenv import load_dotenv
import os 
from openai import OpenAI 

# STEP 1: LOAD THE .ENV FILE 
load_dotenv()
user_input = input("Enter your question: ")

# STEP 2: DEFINE THE OPENAI VARIABLE
client = OpenAI()

# STEP 3: MAKE THE LLM REQUEST
response = client.responses.create(
    model="gpt-6-luna",
    input=user_input
)

# STEP 4: PRINT THE OUTPUT
print(response.json())