from openai import OpenAI 
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv 

load_dotenv()

customer_query = "what is python?"

client = OpenAI()
response = client.responses.create(
    model="gpt-6-luna",
    input=customer_query
)
print(response.output_text)

print("="*50)

llm = ChatOpenAI(model="gpt-6-luna")
response = llm.invoke(customer_query)
print(response.content)