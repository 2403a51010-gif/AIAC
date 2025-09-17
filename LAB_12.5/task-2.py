import csv, json, time, bisect

def load_csv(filename):
    with open(filename, newline='', encoding="utf-8") as f:
        return [{"title": row["title"], "author": row["author"]} for row in csv.DictReader(f)]

def load_json(filename):
    with open(filename, encoding="utf-8") as f:
        return json.load(f)

def linear_search(data, keyword):
    keyword = keyword.lower()
    return [entry for entry in data if keyword in entry["title"].lower() or keyword in entry["author"].lower()]

def binary_search(data, keyword):
    titles = [entry["title"].lower() for entry in data]
    sorted_data = sorted(data, key=lambda x: x["title"].lower())
    keyword = keyword.lower()
    idx = bisect.bisect_left(titles, keyword)
    results = []
    while idx < len(sorted_data) and keyword in sorted_data[idx]["title"].lower():
        results.append(sorted_data[idx])
        idx += 1
    return results

def build_hash_index(data):
    index = {}
    for entry in data:
        for word in entry["title"].lower().split() + entry["author"].lower().split():
            if word not in index:
                index[word] = []
            index[word].append(entry)
    return index

def hash_search(index, keyword):
    return index.get(keyword.lower(), [])

def benchmark(search_func, *args):
    start = time.time()
    result = search_func(*args)
    elapsed = time.time() - start
    return result, elapsed

def main():
    data = [
        {"title": "Deep Learning for NLP", "author": "Ian Goodfellow"},
        {"title": "Quantum Computing Advances", "author": "John Preskill"},
        {"title": "AI in Healthcare", "author": "Andrew Ng"},
        {"title": "Graph Neural Networks", "author": "Thomas Kipf"},
        {"title": "Blockchain for Security", "author": "Satoshi Nakamoto"}
    ]
    hash_index = build_hash_index(data)
    keyword = input("Enter search keyword: ")
    results_lin, t_lin = benchmark(linear_search, data, keyword)
    results_bin, t_bin = benchmark(binary_search, data, keyword)
    results_hash, t_hash = benchmark(hash_search, hash_index, keyword)
    print(f"\nResults (Linear Search, {t_lin:.6f}s): {results_lin}")
    print(f"Results (Binary Search, {t_bin:.6f}s): {results_bin}")
    print(f"Results (Hash Search, {t_hash:.6f}s): {results_hash}")

if __name__ == "__main__":
    main()
