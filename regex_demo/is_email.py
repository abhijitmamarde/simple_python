import re

valid_email = "myemail.123@gmail.com"
invalid_email1 = "myemail.123@gmail"
invalid_email2 = "myemail.123"

def is_valid_email(email):
    email = email.lower()
    pattern = r"[\w.-]+@[\w.-]+\.\w+"
    result = re.match(pattern, email)
    if result:
        print("Valid email")
    else:
        print("Invalid email")

is_valid_email(valid_email)
is_valid_email(invalid_email1)
is_valid_email(invalid_email2)