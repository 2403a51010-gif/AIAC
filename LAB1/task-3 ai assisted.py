def factorial(n):
	if n == 0 or n == 1:
		return 1
	else:
		return n * factorial(n - 1)

# Take input from the console
num = int(input("Enter a number to calculate its factorial: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")