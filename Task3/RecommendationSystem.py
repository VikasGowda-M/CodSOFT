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
while True:
    print("\nCategories: movies, books, products")
    category = input("Enter a category: ").strip().lower()
    if category not in items:
        print("Invalid category. Please choose from movies, books, or products.")
        continue
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
    again=input("Do you want to try again? (yes/no): ").strip().lower()
    if again != "yes":
        print("Thank you for using the recommendation system. Goodbye!")
        break
       