def register_user():
    
    print("=== User Registration ===")
    user_details = {}
    username = input("Enter a username: ")
    while not username:
        print("Username cannot be empty.")
        username = input("Enter a username: ")
    password = input("Enter a password: ")
    while not password:
        print("Password cannot be empty.")
        password = input("Enter a password: ")

    user_details[username] = password
    print("Registration successful!\n")
    return user_details

def login_user(user_details):
    
    print("=== User Login ===")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in user_details and user_details[username] == password:
        print("Login successful! Welcome,", username)
    else:
        print("Login failed! Invalid username or password.")

users = register_user()
login_user(users)
