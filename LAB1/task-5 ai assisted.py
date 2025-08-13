def word_frequency(text):
	words = text.split()
	freq = {}
	for word in words:
		word = word.lower().strip('.,!?')
		freq[word] = freq.get(word, 0) + 1
	return freq

# Sample input from console
input_text = input("Enter a string: ")
result = word_frequency(input_text)
print(result)

# Example:
# Input: "Hello world! Hello Python."
# Output: {'hello': 2, 'world': 1, 'python': 1}