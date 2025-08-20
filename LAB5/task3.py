import random

# Sample product categories and products
products = {
    "soap": ["Dove Soap", "Lux Soap", "Pears Soap"],
    "mobile": ["iPhone 14", "Samsung Galaxy S23", "OnePlus 11"],
    "toys": ["Lego Set", "Barbie Doll", "Hot Wheels Car"],
    "games": ["Chess Board", "Monopoly", "Scrabble"]
}

# Simple recommendation logic based on user history
def recommend(history):
    recommendations = []
    for item in history:
        item = item.lower()
        if item in products:
            recommendations.extend(products[item])
    # If no match, suggest random products
    if not recommendations:
        all_products = [p for plist in products.values() for p in plist]
        recommendations = random.sample(all_products, 3)
    return recommendations

def main():
    print("Enter your search history (comma separated, e.g. soap,mobile,toys):")
    user_input = input().strip()
    history = [h.strip() for h in user_input.split(",") if h.strip()]
    recs = recommend(history)
    print("\nRecommended products for you:")
    for r in recs:
        print("-", r)

if __name__ == "__main__":
    main()