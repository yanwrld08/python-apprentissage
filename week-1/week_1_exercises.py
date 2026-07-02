"""
Week 1 Exercises: Language Basics

These exercises cover:
- Variables and types
- Arithmetic operations
- String manipulation
- Type conversion
- print() and f-strings
"""

# ===== Exercise 1: Variables and Basic Math =====
print("=== Exercise 1: Variables and Basic Math ===")

# TODO: Create variables for your age, height (in cm), and weight (in kg)
# Then calculate your BMI: weight / (height_in_meters ** 2)

age = 20
height_cm = 180
weight_kg = 75

height_m = height_cm / 100
bmi = weight_kg / (height_m ** 2)

print(f"Age: {age}, Height: {height_cm} cm, Weight: {weight_kg} kg")
print(f"BMI: {bmi:.2f}")


# ===== Exercise 2: Type Conversion =====
print("\n=== Exercise 2: Type Conversion ===")

# TODO: Convert between types
number_str = "42"
number_int = int(number_str)
number_float = float(number_int)

print(f"String: {number_str} (type: {type(number_str).__name__})")
print(f"Int: {number_int} (type: {type(number_int).__name__})")
print(f"Float: {number_float} (type: {type(number_float).__name__})")


# ===== Exercise 3: String Formatting =====
print("\n=== Exercise 3: String Formatting ===")

name = "Alice"
score = 95.5
attempts = 3

# Using f-strings
print(f"Player: {name}, Score: {score:.1f}, Attempts: {attempts}")

# Using .format()
print("Player: {}, Score: {:.1f}, Attempts: {}".format(name, score, attempts))


# ===== Exercise 4: Simple Calculation =====
print("\n=== Exercise 4: Simple Calculation ===")

# TODO: Calculate the total cost of items with tax
price_item1 = 19.99
price_item2 = 15.50
quantity_item1 = 2
quantity_item2 = 3
tax_rate = 0.08  # 8%

subtotal = (price_item1 * quantity_item1) + (price_item2 * quantity_item2)
tax = subtotal * tax_rate
total = subtotal + tax

print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total: ${total:.2f}")


# ===== Exercise 5: String Methods =====
print("\n=== Exercise 5: String Methods ===")

text = "  hello world  "

print(f"Original: '{text}'")
print(f"Upper: '{text.upper()}'")
print(f"Lower: '{text.lower()}'")
print(f"Stripped: '{text.strip()}'")
print(f"Title: '{text.title()}'")
print(f"Replaced: '{text.replace('world', 'Python')}'")


# ===== Exercise 6: Input and Processing =====
print("\n=== Exercise 6: Input and Processing ===")

# Uncomment to use interactive input
# user_name = input("What's your name? ")
# user_age = int(input("How old are you? "))
# print(f"Hello {user_name}! In 10 years, you'll be {user_age + 10}.")

# For testing, we'll use hardcoded values
user_name = "Bob"
user_age = 25
print(f"Hello {user_name}! In 10 years, you'll be {user_age + 10}.")