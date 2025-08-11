# Example input-output prompt:
# Input: Enter numbers separated by spaces: 5 2 9 1 7
# Output: Sorted numbers in descending order: 9 7 5 2 1

def sort_descending(numbers):
    return sorted(numbers, reverse=True)

user_input = input("Enter numbers separated by spaces: ")
numbers = list(map(int, user_input.strip().split()))
sorted_numbers = sort_descending(numbers)
print("Sorted numbers in descending order:", ' '.join(map(str, sorted_numbers)))
