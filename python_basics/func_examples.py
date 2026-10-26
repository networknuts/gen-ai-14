def say_hello():
    print("hello world")
    print("hello ai")

def say_goodbye():
    print("bye world")
    print("bye ai")

def greeting(username):
    print(f"hello {username}, how are you?")

def add_together(n1=0,n2=0):
    return(n1+n2)

def ai_input(user_name,user_request):
    return {
        "name": user_name,
        "query": user_request
    }

customer_name = input("Enter your name: ")
customer_query = input("Enter your query: ")

result = ai_input(customer_name,customer_query)
print(result)