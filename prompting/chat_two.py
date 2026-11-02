from dotenv import load_dotenv
from openai import OpenAI 

# STEP 1: LOAD THE .ENV FILE
load_dotenv()

prompt_file = open("few_shot_prompt.txt","r")
system_prompt = prompt_file.read()
prompt_file.close()

# STEP 2: ASK FOR CUSTOMER QUERY
query = input("Enter your question: ")

# STEP 3: MAKE THE LLM REQUEST
client = OpenAI()
response = client.responses.create(
    model="gpt-6-luna",
    instructions=system_prompt,
    input=query
)

# STEP 4: PRINTING RESPONSE
print(response.output_text)