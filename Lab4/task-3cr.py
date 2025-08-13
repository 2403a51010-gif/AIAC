def format_full_name():
    name = input("Enter your name: ").strip()
    parts = name.split()
    if len(parts) < 2:
        print("Please enter both first and last name.")
        return
    first_name = parts[0]
    last_name = parts[-1].capitalize()
    print(f"{first_name} is the first name")
    print(f"{last_name} is the last name")

format_full_name()
