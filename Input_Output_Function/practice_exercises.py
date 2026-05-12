# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Personal Information Form
Create a program that asks for:
- Full name
- Age
- Height
- Favorite color
Then prints a formatted profile.

🎯 EXERCISE 2: Simple Calculator
Take two numbers as input and print:
- Sum
- Difference
- Product
- Quotient
Format the output nicely.

🎯 EXERCISE 3: Temperature Converter
Ask user for temperature in Celsius
Convert to Fahrenheit: (C × 9/5) + 32
Print both with 2 decimal places.

🎯 EXERCISE 4: Multiplication Table
Ask user for a number
Print its multiplication table from 1 to 10
Use proper formatting (columns aligned)

🎯 EXERCISE 5: Shopping List
Create a program that:
- Asks for item names and prices
- Stores them in lists
- Prints a receipt with total
- Uses sep and end creatively

🎯 CHALLENGE: Quiz Program
Create a simple quiz with 3 questions:
- Ask questions using input()
- Validate answers
- Keep score
- Display final score with percentage
- Use colored output if possible
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1 Solution
print("\nEx1 - Profile Form:")
print("""
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height (m): "))
color = input("Enter favorite color: ")

print(f"\\n{'='*40}")
print(f"Profile: {name}")
print(f"Age: {age} (Next year: {age + 1})")
print(f"Height: {height:.2f}m")
print(f"Favorite Color: {color}")
print(f"{'='*40}")
""")

# Exercise 2 Solution
print("\nEx2 - Simple Calculator:")
print("""
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print(f"\\n{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b:.2f}")
""")

# Exercise 3 Solution
print("\nEx3 - Temperature Converter:")
print("""
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
""")

# Exercise 4 Solution
print("\nEx4 - Multiplication Table:")
print("""
num = int(input("Enter a number: "))

print(f"\\nMultiplication Table of {num}:")
print("-" * 20)
for i in range(1, 11):
    print(f"{num} × {i:2} = {num * i:3}")
""")

# Exercise 5 Solution
print("\nEx5 - Shopping List:")
print("""
items = []
prices = []
total = 0

while True:
    item = input("Enter item name (or 'done'): ")
    if item.lower() == 'done':
        break
    price = float(input(f"Enter price for {item}: $"))
    items.append(item)
    prices.append(price)
    total += price

print(f"\\n{'='*40}")
print(f"{'RECEIPT':^40}")
print(f"{'='*40}")
for item, price in zip(items, prices):
    print(f"{item:<25} ${price:>9.2f}")
print(f"{'-'*40}")
print(f"{'TOTAL':<25} ${total:>9.2f}")
print(f"{'='*40}")
""")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ PYTHON INPUT & OUTPUT MASTERED!")
print("=" * 70)


