items = {
    "movies":{
        "avengers": "action",
        "titanic": "romance",
        "inception": "sci-fi",
        "the godfather": "crime"
    },
    "books": {
        "harry potter": "fantasy",
        "the great gatsby": "classic",
        "to kill a mockingbird": "historical fiction",
        "1984": "dystopian"
    },
    "products": {
        "iphone": "electronics",
        "nike shoes": "footwear",
        "samsung tv": "electronics",
        "adidas hoodie": "clothing"
    }
}
print("Categories: movies, books, products")
category = input("Enter a category: ").strip().lower()
if category in items:
    print("Available types:")
    types = set(items[category].values())
    for t in types:
        print("- " + t)
    preferences = input("Enter your prefered type: ").strip().lower()
    print("Recommended items:")
    found = False
    for item, item_type in items[category].items():
        if item_type.lower() == preferences.lower():
                print("- " + item)
                found = True
        if not found:
            print("No items found for the selected type.")
else:
    print("Invalid category. Please choose from movies, books, or products.")