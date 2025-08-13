def count_vowels():
    s = input("Enter the string: ")
    vowels = 'aeiouAEIOU'
    vowel_count = {}
    total = 0

    for char in s:
        if char in vowels:
            key = char.lower()
            vowel_count[key] = vowel_count.get(key, 0) + 1
            total += 1

    if total == 0:
        print("The number of vowels present in given string are : 0 vowels")
        return

    details = []
    for v in 'aeiou':
        if v in vowel_count:
            count = vowel_count[v]
            details.append(f"{count}{v}'s" if count > 1 else f"{count}{v}")

    print(f"The number of vowels present in given string are : {total} vowels({', '.join(details)})")

count_vowels()