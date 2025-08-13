def count_vowels_in_string():
    s = input("Enter the string: ")
    vowels = 'aeiouAEIOU'
    vowel_counts = {}
    total = 0
    for ch in s:
        if ch in vowels:
            total += 1
            ch_lower = ch.lower()
            if ch_lower in vowel_counts:
                vowel_counts[ch_lower] += 1
            else:
                vowel_counts[ch_lower] = 1
    if total == 0:
        print("The number of vowels present in given string are : 0 vowels")
        return
    # Prepare the breakdown string
    breakdown = []
    for v in 'aeiou':
        if v in vowel_counts:
            count = vowel_counts[v]
            if count == 1:
                breakdown.append(f"1{v}")
            else:
                breakdown.append(f"{count}{v}’s")
    breakdown_str = ','.join(breakdown)
    print(f"The number of vowels present in given string are : {total}vowels({breakdown_str})")

count_vowels_in_string()
