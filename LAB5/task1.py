import getpass
import hashlib

def anonymize_email(email):
    # Mask the email except the domain
    local, domain = email.split('@')
    return '*' * len(local) + '@' + domain

def anonymize_phone(phone):
    # Mask all but last 2 digits
    return '*' * (len(phone) - 2) + phone[-2:]

def anonymize_address(address):
    # Mask address except city (assuming last word is city)
    parts = address.split()
    if len(parts) > 1:
        return '*' * (len(address) - len(parts[-1])) + parts[-1]
    return '*' * len(address)

def hash_password(password):
    # Hash password for storage
    return hashlib.sha256(password.encode()).hexdigest()

def main():
    print("User Data Collection")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")

    # Anonymize sensitive data
    email_anon = anonymize_email(email)
    phone_anon = anonymize_phone(phone)
    address_anon = anonymize_address(address)

    # Create password for file protection
    password = getpass.getpass("Create a password to protect your data file: ")
    password_hash = hash_password(password)

    # Store data in a .txt file
    with open("userdata.txt", "w") as f:
        f.write("# User data (anonymized)\n")
        f.write(f"Name: {name}\n")
        f.write(f"Age: {age}\n")
        f.write(f"Email: {email_anon}\n")
        f.write(f"Phone: {phone_anon}\n")
        f.write(f"Address: {address_anon}\n")
        f.write("# Password hash for protection\n")
        f.write(f"PasswordHash: {password_hash}\n")

    print("Data collected and stored securely in 'userdata.txt'.")

if __name__ == "__main__":
    main()