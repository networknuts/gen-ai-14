from langchain_openai import ChatOpenAI 
from langgraph.graph import StateGraph, START, END 
from dotenv import load_dotenv
from typing import TypedDict
import json 

# SETUP THE ENVIRONMENT
load_dotenv()
llm_developer = ChatOpenAI(model="gpt-6-luna")
llm_qa = ChatOpenAI(model="gpt-6.1-terra")

MAX_RETRIES = 3

# STEP 1: DEFINE THE STATE
class CodingState(TypedDict):
    user_request: str 
    code: str 
    rating: int
    retries: int 
    feedback: str 
    status: str 

# STEP 2: CREATING THE NODES

# NODE 1: DEVELOPER NODE
def developer_node(state: CodingState):
    prompt = f"""
    Write code for the following user requirement:
    {state['user_request']}

    If feedback is provided, improve the previous version of the code.
    Previous code:
    {state['code']}

    Feedback: 
    {state['feedback']}

    Only return the code, no markdown.
    """
    response = llm_developer.invoke(prompt).content.strip()
    return {
        "code": response,
        "feedback": ""
    }

# NODE 2: JUDGE CODE
def judge_node(state: CodingState):
    prompt = f"""
    Review the given code on the following parameters:
    - Error handling
    - Modern coding practices
    - Scalability
    - Readability of the code
    - Vulnerabilities in the code
    - Does the code contain comments for developers to understand important steps

    Return the output in the following dict format:
    {{
        "rating": integer value between 1-10 which is a rating of the overall code,
        "feedback": string value with clear explanation on improvements to make to the code
    }}

    Code:
    {state['code']}
    """
    response = llm_qa.invoke(prompt).content.strip()
    result = json.loads(response)
    return {
        "rating": int(result['rating']),
        "feedback": result['feedback']
    }

# NODE 3: APPROVAL NODE
def status_success(state: CodingState):
    return {"status": "passed"}

# NODE 3: FAILURE NODE
def status_failure(state: CodingState):
    return {"status": "failed"}

# NODE 4: INCREMENTAL RETRY LOGIC NODE
def incremental_retry(state: CodingState):
    return {"retries": state['retries']+1}

# NODE 5: CHECK RATING AND RETRIES
def check_rating(state: CodingState):
    if state['rating'] >= 8:
        return "approved"
    elif state['retries'] >= MAX_RETRIES:
        return "failed"
    else:
        return "retry"


# STEP 3: BUILDING THE RELATIONSHIP BETWEEN NODES

graph = StateGraph(CodingState)

graph.add_node("developer",developer_node)
graph.add_node("qa",judge_node)
graph.add_node("approval",status_success)
graph.add_node("failure",status_failure)
graph.add_node("retry",incremental_retry)

graph.set_entry_point("developer")
graph.add_edge("developer","qa")
graph.add_conditional_edges(
    "qa",
    check_rating,
    {
        "approved": "approval",
        "failed": "failure",
        "retry": "retry"
    }
)
graph.add_edge("approval",END)
graph.add_edge("failure",END)
graph.add_edge("retry","developer")

# STEP 4: COMPILE THE AGENT
agent = graph.compile()

# STEP 5: RUNNING THE AGENT
user_request = input("Enter idea to create code for: ")

result = agent.invoke({
    "user_request": user_request,
    "code": "",
    "rating": 0,
    "feedback": "",
    "retries": 0,
    "status": "running"
})

print("RAW RESULT")
print(result)

print("\nAGENT OUTPUT\n")
print("GENERATED CODE")
print(result['code'])
print("FEEDBACK")
print(result['feedback'])
print("STATUS")
print(result['status'])
print("RATING")
print(result['rating'])
print("RETRIES USED")
print(result['retries'])