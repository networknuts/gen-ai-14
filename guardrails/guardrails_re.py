import re 

USER_INPUT = """
Hi, my name is aryan and my email is ARyan@example.com.
Please draft an email from me to my employer at info@EXample.com 
asking for 10 days of work from home.
"""

normalized_prompt = USER_INPUT.strip().lower()

sanitized_prompt = re.sub(r"\w+@\w+\.\w+","<EMAIL_ADDRESS>",normalized_prompt)
print(sanitized_prompt)