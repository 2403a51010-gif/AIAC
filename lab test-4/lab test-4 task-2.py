import random
import statistics
import csv
import os

# Step 1️⃣: Generate random numeric dataset
def generate_data(rows=100, cols=3, outlier_fraction=0.05, seed=42):
    random.seed(seed)
    data = []

    for _ in range(rows):
        row = [random.gauss(50, 10 + 5 * i) for i in range(cols)]  # normal-like distribution
        data.append(row)

    # Inject outliers randomly
    n_outliers = int(rows * outlier_fraction)
    for _ in range(n_outliers):
        r = random.randint(0, rows - 1)
        c = random.randint(0, cols - 1)
        data[r][c] += random.choice([1, -1]) * random.uniform(60, 100)

    return data


# Step 2️⃣: Remove outliers using Z-score
def remove_outliers_zscore(data, threshold=3.0):
    cols = list(zip(*data))
    means = [statistics.mean(col) for col in cols]
    stds = [statistics.pstdev(col) or 1 for col in cols]  # avoid div-by-zero

    cleaned = []
    removed = 0

    for row in data:
        keep = True
        for i, val in enumerate(row):
            z = abs((val - means[i]) / stds[i])
            if z > threshold:
                keep = False
                break
        if keep:
            cleaned.append(row)
        else:
            removed += 1

    return cleaned, removed


# Step 3️⃣: Save data to CSV
def save_csv(data, filepath):
    os.makedirs(os.path.dirname(filepath) or ".", exist_ok=True)
    header = [f"feature_{i+1}" for i in range(len(data[0]))]
    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(data)


# Step 4️⃣: Main function to tie it all together
def main():
    print("🔢 Generating random dataset...")
    data = generate_data(rows=1000, cols=3, outlier_fraction=0.02)

    print("💾 Saving original data...")
    save_csv(data, "original_data.csv")

    print("🧹 Removing outliers using Z-score method...")
    cleaned, removed = remove_outliers_zscore(data, threshold=3.0)
    save_csv(cleaned, "cleaned_data.csv")

    print("\n✅ Process complete!")
    print(f"Total rows generated: {len(data)}")
    print(f"Outliers removed: {removed}")
    print(f"Rows kept: {len(cleaned)}")
    print("📂 Files saved as 'original_data.csv' and 'cleaned_data.csv'.")


# Step 5️⃣: Run
if __name__ == "__main__":
    main()
