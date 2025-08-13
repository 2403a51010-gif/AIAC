file_path = r'c:\Users\admin\OneDrive\Desktop\task5.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        line_count = sum(1 for _ in f)
    print(f"Number of lines in the file: {line_count}")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")