from langchain_openai import ChatOpenAI 
from langgraph.graph import StateGraph, START, END 
from dotenv import load_dotenv
from typing import TypedDict 

# SETUP THE AI ENVIRONMENT
load_dotenv()
llm = ChatOpenAI(model="gpt-6-luna")

# STEP 1: DEFINE THE STATE
class CodingState(TypedDict):
    user_request: str 
    code: str 
    rating: int

# STEP 2: CREATING THE NODES

# NODE 1: DEVELOPER NODE
def developer_node(state: CodingState):
    response = llm.invoke(
        f"""
        Write code for the following user requirement:
        {state['user_request']}

        Return the code in plain text format.
        """
    )
    return {
        "code": response.content
    }

# NODE 2: JUDGE CODE
def judge_node(state: CodingState):
    response = llm.invoke(
        f"""
        Review the given code on the following parameters:
        - Error handling
        - Modern coding practices
        - Scalability

        Provide a single rating between 1-10 after judging the code on the above parameters.

        Code:
        {state['code']}

        Important: Only return the rating in an integer format between 1-10
        """
    )
    return {
        "rating": response.content
    }

# STEP 3: BUILDING THE RELATIONSHIP BETWEEN NODES

graph = StateGraph(CodingState)

graph.add_node("developer",developer_node)
graph.add_node("qa",judge_node)

graph.add_edge(START,"developer")
graph.add_edge("developer","qa")
graph.add_edge("qa",END)

# STEP 4: COMPILE THE AGENT
whatever = graph.compile()

# STEP 5: RUNNING THE AGENT
user_request = input("Enter idea to create code for: ")

result = whatever.invoke({
    "user_request": user_request
})

print("\nAGENT OUTPUT\n")
print("GENERATED CODE")
print(result['code'])
print("RATING")
print(result['rating'])