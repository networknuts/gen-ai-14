from dotenv import load_dotenv
import os

load_dotenv()

my_var_one = os.getenv("OPENWEATHERMAP_API_KEY")
my_var_two = os.getenv("MY_SERVER_PASSWORD")

print(my_var_one)
print(my_var_two)