from dotenv import load_dotenv
from openai import OpenAI 

# STEP 1: LOAD THE .ENV FILE
load_dotenv()

# STEP 2: ASK FOR CUSTOMER QUERY
query = input("Enter your question: ")

# STEP 3: MAKE THE LLM REQUEST
client = OpenAI()
response = client.responses.create(
    model="gpt-6-luna",
    input=[
        {
            "role": "user",
            "content": "hi, my name is jas."
        },
        {
            "role": "assistant",
            "content": "Hi Jas! Nice to meet you. How can I help?"
        },
        {
            "role": "user",
            "content": query
        }
    ]
)

# STEP 4: PRINTING RESPONSE
print(response.output_text)