class Student:
	def __init__(self, name, roll_no, marks):
		self.name = name
		self.roll_no = roll_no
		self.marks = marks

	def display(self):
		print(f"Name: {self.name}, Roll No: {self.roll_no}, Marks: {self.marks}")

students = []
n = int(input("Enter number of students: "))
for i in range(n):
	name = input(f"Enter name of student {i+1}: ")
	roll_no = input(f"Enter roll number of student {i+1}: ")
	marks = float(input(f"Enter marks of student {i+1}: "))
	student = Student(name, roll_no, marks)
	students.append(student)

print("\nStudent Details:")
for student in students:
	student.display()