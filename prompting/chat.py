from dotenv import load_dotenv
from openai import OpenAI 

# STEP 1: LOAD THE .ENV FILE
load_dotenv()
#SYSTEM_INFO = "you are a cloud ai assistant. you will only answer queries related to the cloud, if the user is asking for anything else, you will refuse to answer the query."

# STEP 2: ASK FOR CUSTOMER QUERY
query = input("Enter your question: ")

# STEP 3: MAKE THE LLM REQUEST
client = OpenAI()
response = client.responses.create(
    model="gpt-6-luna",
    #instructions=SYSTEM_INFO,
    input=query
)

# STEP 4: PRINTING RESPONSE
print(response.output_text)