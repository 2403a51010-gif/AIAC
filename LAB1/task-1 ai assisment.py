# Function to compare three numbers and return the largest one
def max_of_three(a, b, c):
	return max(a, b, c)

# Take three inputs from the console
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find and print the largest number
largest = max_of_three(num1, num2, num3)
print("The largest number is:", largest)