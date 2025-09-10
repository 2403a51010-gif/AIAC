def process_scores(scores):
    avg = sum(scores) / len(scores)
    highest = max(scores)
    lowest = min(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)
scores = [85, 92, 78, 90, 88]
process_scores(scores)
