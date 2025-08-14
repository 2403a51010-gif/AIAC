import csv

def calculate_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

filename = input("Enter the CSV filename: ")

try:
    with open(filename, newline='Student.csv') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip header row if present
        print(f"{'Name':<15}{'Total':<10}{'Average':<10}{'Grade':<6}")
        print("-" * 41)
        for row in reader:
            name = row[0]
            try:
                marks = list(map(float, row[1:4]))
            except ValueError:
                print(f"Invalid marks for {name}. Skipping.")
                continue
            total = sum(marks)
            average = total / 3
            grade = calculate_grade(average)
            print(f"{name:<15}{total:<10.2f}{average:<10.2f}{grade:<6}")
except FileNotFoundError:
    print("File not found. Please check the filename and try again.")
