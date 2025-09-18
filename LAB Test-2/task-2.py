def diff_lines(old, new):
    old_set = set(old)
    new_set = set(new)
    added = [line for line in new if line not in old_set]
    removed = [line for line in old if line not in new_set]
    return added, removed


# Input
old = input("Enter old list : ").split(',')
new = input("Enter new list : ").split(',')

# Output
added, removed = diff_lines(old, new)
print(f"added={added}, removed={removed}")
