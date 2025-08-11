
def factorial_for(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n = int(input("Enter a number to compute factorials from 1 to n: "))

print("\nThe factorials up to given :")
for i in range(1, n+1):
    print(f"{i}! = {factorial_for(i)}")






