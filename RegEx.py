#RegEX example
import re

def validate_email(email_address):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$') #RegEx Pattern

    match = pattern.match(email_address)  #Matching with string

    if match: #Return True or False
        return True
    else:
        return False

input_email = input("Enter your email address- ") #Taking input from keyboard

if validate_email(input_email):
    print("Valid email.")
else:
    print("Invalid email.")
