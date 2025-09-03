def validate_email(email):
    # Check exactly one '@'
    if email.count('@') != 1:
        print("Invalid input")
        return
    
    # Check first and last character (must be alphanumeric)
    if not (email[0].isalnum() and email[-1].isalnum()):
        print("Invalid input")
        return
    
    print("Valid email")

# Take user input
email_input = input("Enter your email: ")
validate_email(email_input)
