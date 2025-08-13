def format_name(full_name):
    parts = full_name.strip().split()
    if len(parts) == 2:
        first, last = parts
        print(f"{first} is the first name")
        print(f"{last} is the last name")
    else:
        print("Please enter a name with exactly two words.")

format_name("rakesh reddy")
format_name("Varaprasad reddy")