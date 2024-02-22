import re

def is_valid_email(email):
    # Define a simple email validation pattern
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Use the pattern to match the email
    match = email_pattern.match(email)

    # Check if the email is valid
    if match:
        return True
    else:
        return False

# Example usage:
email_to_check = input("Enter an email address: ")

if is_valid_email(email_to_check):
    print("The email address is valid.")
else:
    print("The email address is not valid.")
