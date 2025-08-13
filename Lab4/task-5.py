filename = "task5.txt"
try:
    with open(filename, "r") as f:
        lines = f.readlines()
        print(len(lines))
except FileNotFoundError:
    print(f"File '{filename}' 3 lines of text ")
