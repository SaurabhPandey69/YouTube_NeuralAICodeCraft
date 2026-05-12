"""
PYTHON INPUT AND OUTPUT FUNCTIONS
NeuralAICodeCraft - Complete Guide to print() and input()

Topics Covered:
1. print() function (basics to advanced)
2. input() function (user interaction)
3. Formatted output (f-strings, format(), %)
4. Escape sequences & special characters
5. Real-world examples
"""

print("=" * 70)
print("🐍 PYTHON INPUT AND OUTPUT FUNCTIONS")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: THE print() FUNCTION
# ============================================

print("\n📺 PART 1: THE print() FUNCTION")
print("-" * 50)

# 1.1 Basic Printing
print("\n1.1 Basic Printing:")
print("-" * 30)

print("Hello World!")  # String
print(42)              # Integer
print(3.14159)         # Float
print(True)            # Boolean
print([1, 2, 3])       # List
print({"name": "John"}) # Dictionary

# 1.2 Printing Multiple Items
print("\n1.2 Printing Multiple Items:")
print("-" * 30)

print("Hello", "World", "from", "Python")
print(1, 2, 3, 4, 5)
print("Age:", 25, "City:", "New York")

# 1.3 The sep Parameter (Separator)
print("\n1.3 The sep Parameter:")
print("-" * 30)

print("apple", "banana", "cherry", sep=", ")
print("apple", "banana", "cherry", sep=" | ")
print("apple", "banana", "cherry", sep="\n")  # New line separator
print("1", "2", "3", sep=" + ")  # Custom separator

# Real-world examples with sep
print("Date:", "2024", "01", "15", sep="-")
print("Time:", "14", "30", "00", sep=":")

# 1.4 The end Parameter
print("\n1.4 The end Parameter:")
print("-" * 30)

print("Hello", end=" ")
print("World")
print("First line", end=" --- ")
print("Second line")

# Multiple prints without newline
for i in range(5):
    print(i, end=" ")
print()  # New line after loop

# Custom end character
print("Loading", end="...")
print("Done!")

# 1.5 Combining sep and end
print("\n1.5 Combining sep and end:")
print("-" * 30)

print("A", "B", "C", sep=" → ", end=" ✓\n")
print("1", "2", "3", sep=" + ", end=" = 6\n")

# 1.6 The file Parameter (Print to File)
print("\n1.6 The file Parameter (Print to File):")
print("-" * 30)

# Print to a file instead of console
with open("output.txt", "w") as f:
    print("This goes to a file", file=f)
    print("Another line in the file", file=f)
print("✅ Check 'output.txt' file created!")

# 1.7 flush Parameter (Force output)
print("\n1.7 flush Parameter (Real-time output):")
print("-" * 30)

import time
print("Processing", end="", flush=True)
for i in range(3):
    time.sleep(0.5)
    print(".", end="", flush=True)
print(" Done!")

# ============================================
# PART 2: ESCAPE SEQUENCES
# ============================================

print("\n🔧 PART 2: ESCAPE SEQUENCES")
print("-" * 50)

print("""
Common Escape Sequences:
\\n - New line
\\t - Tab (4 spaces)
\\\\ - Backslash
\\" - Double quote
\\' - Single quote
\\r - Carriage return
\\b - Backspace
""")

# 2.1 New Line and Tab
print("\n2.1 New Line and Tab:")
print("-" * 30)

print("Line 1\nLine 2\nLine 3")
print("Column1\tColumn2\tColumn3")
print("Name:\tJohn\nAge:\t25\nCity:\tNYC")

# 2.2 Quotes inside Strings
print("\n2.2 Quotes inside Strings:")
print("-" * 30)

print("He said, \"Python is awesome!\"")
print('It\'s a beautiful day')
print("C:\\Users\\John\\Documents")  # Raw backslashes

# 2.3 Raw Strings (ignore escape sequences)
print("\n2.3 Raw Strings (r''):")
print("-" * 30)

normal_string = "C:\\Users\\John"
raw_string = r"C:\Users\John"
print(f"Normal string: {normal_string}")
print(f"Raw string: {raw_string}")

file_path = r"C:\Program Files\Python\Scripts"
print(f"File path: {file_path}")

# 2.4 Multi-line Strings (Triple Quotes)
print("\n2.4 Multi-line Strings (Triple Quotes):")
print("-" * 30)

multi_line = """
This is a multi-line string.
It can span multiple lines.
No need for \\n characters!
"""
print(multi_line)

# For docstrings (function documentation)
def greet(name):
    """
    Greets a person by name.
    
    Parameters:
    name (str): The person's name
    
    Returns:
    str: Greeting message
    """
    return f"Hello, {name}!"

print(greet.__doc__)

# ============================================
# PART 3: THE input() FUNCTION
# ============================================

print("\n⌨️ PART 3: THE input() FUNCTION")
print("-" * 50)

# Note: For demonstration, we'll use pre-defined values
# In actual interactive mode, these would prompt for user input

print("\n3.1 Basic Input (Simulated):")
print("-" * 30)

# In a real interactive session, you would run:
# name = input("Enter your name: ")

# For this script, we'll simulate input
def simulate_input(prompt, value):
    """Simulate user input for demonstration"""
    print(f"{prompt}{value}")
    return value

# Example 1: String input
print("\nExample 1: Getting user's name")
name = simulate_input("Enter your name: ", "John Doe")
print(f"Hello, {name}!")

# Example 2: Numeric input
print("\nExample 2: Getting user's age")
age_str = simulate_input("Enter your age: ", "25")
age = int(age_str)  # Convert string to integer
print(f"Next year, you will be {age + 1} years old!")

# Example 3: Float input
print("\nExample 3: Getting user's height")
height_str = simulate_input("Enter your height in meters: ", "1.75")
height = float(height_str)
print(f"Your height is {height}m")

# 3.2 Type Conversion with input()
print("\n3.2 Type Conversion with input():")
print("-" * 30)

# input() always returns a string - convert as needed
print("Common type conversions:")
print("  int(input())  → Converts to integer")
print("  float(input())→ Converts to float")
print("  str(input())  → Stays as string (default)")
print("  bool(input()) → Converts to boolean (careful!)")

# Boolean conversion example
print("\n⚠️ Note: bool(\"false\") returns True (non-empty string)!")
print("  Use: user_input.lower() == 'true' for boolean input")

# 3.3 Complete Input Example
print("\n3.3 Complete User Profile Input:")
print("-" * 30)

# Simulating user input
user_data = {
    'name': simulate_input("Enter name: ", "Alice Johnson"),
    'age': int(simulate_input("Enter age: ", "28")),
    'height': float(simulate_input("Enter height (m): ", "1.68")),
    'city': simulate_input("Enter city: ", "San Francisco"),
    'is_student': simulate_input("Are you a student? (yes/no): ", "yes").lower() == 'yes'
}

print("\n📋 User Profile:")
print(f"  Name: {user_data['name']}")
print(f"  Age: {user_data['age']}")
print(f"  Height: {user_data['height']}m")
print(f"  City: {user_data['city']}")
print(f"  Student: {user_data['is_student']}")

# 3.4 Input Validation (Basic)
print("\n3.4 Input Validation Example:")
print("-" * 30)

def get_valid_age(prompt):
    """Get and validate age input"""
    age_str = simulate_input(prompt, "25")
    try:
        age = int(age_str)
        if 0 <= age <= 120:
            return age
        else:
            print("  Invalid age! Must be between 0 and 120.")
            return 0
    except ValueError:
        print("  Invalid input! Please enter a number.")
        return 0

age = get_valid_age("Enter your age: ")
print(f"✅ Valid age: {age}")

# ============================================
# PART 4: FORMATTED OUTPUT
# ============================================

print("\n🎨 PART 4: FORMATTED OUTPUT (3 Ways)")
print("-" * 50)

name = "Alice"
age = 25
height = 1.68
score = 95.5

# 4.1 Method 1: f-strings (Python 3.6+ - RECOMMENDED)
print("\n4.1 f-strings (Modern & Fast):")
print("-" * 30)

print(f"Name: {name}")
print(f"Age: {age}, Next year: {age + 1}")
print(f"Height: {height:.2f}m")  # 2 decimal places
print(f"Score: {score:.1%}")      # Percentage
print(f"Name: {name:<10} Age: {age:>5}")  # Left/Right alignment

# Complex expressions in f-strings
print(f"Sum of 5 and 3: {5 + 3}")
print(f"Name uppercase: {name.upper()}")
print(f"Is adult: {'Yes' if age >= 18 else 'No'}")

# 4.2 Method 2: .format() method
print("\n4.2 .format() Method (Flexible):")
print("-" * 30)

print("Name: {}".format(name))
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}, Name again: {0}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Formatting with .format()
print("Height: {:.2f}m".format(height))
print("Score: {:.1%}".format(score))
print("Number: {:,}".format(1000000))  # Thousand separator
print("Hex: {:X}".format(255))          # Hexadecimal

# 4.3 Method 3: % formatting (Legacy - C style)
print("\n4.3 % Formatting (Legacy Style):")
print("-" * 30)

print("Name: %s" % name)
print("Name: %s, Age: %d" % (name, age))
print("Height: %.2fm" % height)
print("Score: %.1f%%" % score)

print("""
Format Specifiers:
%s - String
%d - Integer
%f - Float
%.2f - Float with 2 decimals
%x - Hexadecimal
%% - Percent sign
""")

# 4.4 Comparison of Methods
print("\n4.4 Comparison - All Three Methods:")
print("-" * 30)

product = "Laptop"
price = 999.99
quantity = int(3)

# Debug type checks
print(f"[DEBUG] quantity type: {type(quantity)}")  # <class 'int'>
print(f"[DEBUG] product type: {type(product)}")    # <class 'str'>
print(f"[DEBUG] price type: {type(price)}")        # <class 'float'>

# Method 1: f-string (Best for readability - Python 3.6+)
print(f"f-string: {quantity} x {product} = ${price * quantity:.2f}")

# Method 2: .format() (Good for Python 3.x before 3.6)
print(".format(): {} x {} = ${:.2f}".format(quantity, product, price * quantity))

# Method 3: % formatting (Old-style, still works)
# Option A: Calculate total first (cleaner)
#total = price * quantity
#print("% formatting: %d x %s = $%.2f" % (quantity), product, total)

# Option B: Calculate inline
#print("% formatting: %d x %s = $%.2f" % (quantity), product, price * quantity)


# ============================================
# PART 5: SPECIAL PRINTING TECHNIQUES
# ============================================

print("\n✨ PART 5: SPECIAL PRINTING TECHNIQUES")
print("-" * 50)

# 5.1 Pretty Printing with pprint
print("\n5.1 Pretty Printing (pprint):")
print("-" * 30)

from pprint import pprint

complex_data = {
    "name": "Python Course",
    "topics": ["Variables", "Data Types", "Functions", "Classes"],
    "metadata": {
        "duration": "20 hours",
        "level": "Beginner",
        "rating": 4.8
    },
    "students": [
        {"name": "John", "score": 95},
        {"name": "Jane", "score": 98},
        {"name": "Bob", "score": 87}
    ]
}

print("Regular print():")
print(complex_data)

print("\nPretty print (pprint):")
pprint(complex_data, indent=2, width=80)

# 5.2 Progress Bar Simulation
print("\n5.2 Simple Progress Bar:")
print("-" * 30)

def progress_bar(percent, width=30):
    """Display a simple progress bar"""
    filled = int(width * percent / 100)
    bar = "█" * filled + "░" * (width - filled)
    print(f"\rProgress: |{bar}| {percent:.1f}%", end="", flush=True)

# Simulate progress
for i in range(0, 101, 10):
    progress_bar(i)
    time.sleep(0.2)
print("\n✅ Complete!")

# 5.3 Table Formatting
print("\n5.3 Simple Table Formatting:")
print("-" * 30)

# Header
print(f"{'Name':<15} {'Age':<5} {'City':<15} {'Score':<8}")
print("-" * 50)

# Data rows
students = [
    ("Alice Johnson", 25, "New York", 95.5),
    ("Bob Smith", 22, "Los Angeles", 87.0),
    ("Charlie Brown", 23, "Chicago", 92.3),
    ("Diana Prince", 24, "Boston", 98.7)
]

for name, age, city, score in students:
    print(f"{name:<15} {age:<5} {city:<15} {score:<8.1f}")

# 5.4 Clearing Screen (Cross-platform)
print("\n5.4 Screen Clearing (Simulated):")
print("-" * 30)

import os
import platform

def clear_screen():
    """Clear terminal screen"""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
    print("🧹 Screen cleared! (Simulated)")

print("This would clear the screen in terminal")
# clear_screen()  # Uncomment to actually clear screen

# ============================================
# PART 6: COMPLETE REAL-WORLD EXAMPLE
# ============================================

print("\n🏪 PART 6: REAL-WORLD EXAMPLE - Shopping Cart Program")
print("-" * 50)

class ShoppingCart:
    """Simple shopping cart with input/output"""
    
    def __init__(self):
        self.items = []
        self.prices = []
    
    def add_item(self):
        """Add an item to the cart"""
        print("\n➕ Add Item to Cart")
        print("-" * 30)
        
        # Simulated input for demo
        item = simulate_input("  Item name: ", "Laptop")
        price = float(simulate_input("  Price: $", "999.99"))
        quantity = int(simulate_input("  Quantity: ", "1"))
        
        self.items.append(item)
        self.prices.append(price * quantity)
        
        print(f"\n✅ Added {quantity}x {item} (${price * quantity:.2f})")
    
    def display_receipt(self):
        """Display formatted receipt"""
        print("\n" + "=" * 50)
        print(f"{'RECEIPT':^50}")
        print("=" * 50)
        
        if not self.items:
            print("  Cart is empty!")
            return
        
        # Header
        print(f"{'Item':<25} {'Price':>10} {'Unit':>10}")
        print("-" * 50)
        
        # Items
        total = 0
        for item, price in zip(self.items, self.prices):
            print(f"{item:<25} ${price:>9.2f}")
            total += price
        
        print("-" * 50)
        print(f"{'TOTAL':<25} ${total:>9.2f}")
        print("=" * 50)
        print(f"Thank you for shopping! {'🎉':^10}")
    
    def run(self):
        """Run the shopping cart program"""
        print("\n🛒 Welcome to NeuralAICodeCraft Store!")
        
        while True:
            print("\nOptions:")
            print("  1. Add item")
            print("  2. View receipt")
            print("  3. Exit")
            
            choice = simulate_input("\nChoose option: ", "1")
            
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.display_receipt()
            elif choice == "3":
                print("\n👋 Thanks for visiting!")
                break
            else:
                print("Invalid option!")

# Run the shopping cart (commented for demo)
# cart = ShoppingCart()
# cart.run()

# ============================================
# PART 7: COMMON MISTAKES & BEST PRACTICES
# ============================================

print("\n⚠️ PART 7: COMMON MISTAKES & BEST PRACTICES")
print("-" * 50)

print(r'''
❌ COMMON MISTAKES:

1. Forgetting to convert input() type
   age = input("Enter age: ")  # Returns string
   print(age + 5)  # TypeError!
   
   ✅ Fix: age = int(input("Enter age: "))

2. Using + to concatenate different types
   print("Age: " + age)  # Error if age is int
   
   ✅ Fix: print(f"Age: {age}")

3. Forgetting escape sequences
   path = "C:\Users\John"  # \U is escape!
   
   ✅ Fix: path = r"C:\Users\John"

4. Not using descriptive prompts
   input()  # User doesn't know what to enter
   
   ✅ Fix: name = input("Enter your name: ")

5. Assuming input() returns correct type
   is_true = bool(input("Enter True/False: "))  # Always True!
   
   ✅ Fix: is_true = input().lower() == 'true'

✨ BEST PRACTICES:

1. ✅ Always use descriptive prompts in input()
2. ✅ Use f-strings for formatting (Python 3.6+)
3. ✅ Validate and convert user input
4. ✅ Use meaningful variable names
5. ✅ Add error handling for type conversion
6. ✅ Use sep and end for clean output
7. ✅ Use triple quotes for multi-line strings
8. ✅ Use raw strings for file paths (r'...')
''')

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
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    print() FUNCTION                         │
├─────────────────────────────────────────────────────────────┤
│ print(value1, value2, ...)           → Basic printing       │
│ print(..., sep=', ')                  → Custom separator     │
│ print(..., end='\\n')                 → Custom ending        │
│ print(..., file=file_object)          → Print to file        │
│ print(..., flush=True)                → Force output         │
├─────────────────────────────────────────────────────────────┤
│                    input() FUNCTION                         │
├─────────────────────────────────────────────────────────────┤
│ name = input()                       → Get string input      │
│ name = input("Prompt: ")             → With prompt           │
│ age = int(input())                   → Convert to integer    │
│ height = float(input())              → Convert to float      │
├─────────────────────────────────────────────────────────────┤
│                FORMATTED OUTPUT                             │
├─────────────────────────────────────────────────────────────┤
│ f"Hello {name}"                      → f-string ✅ Modern    │
│ "Hello {}".format(name)              → .format() ✅ Flexible │
│ "Hello %s" % name                    → % formatting ⚠️ Legacy│
├─────────────────────────────────────────────────────────────┤
│                ESCAPE SEQUENCES                             │
├─────────────────────────────────────────────────────────────┤
│ \\n - New line      \\t - Tab        \\\\ - Backslash          │
│ \\" - Double quote  \\' - Single quote r'' - Raw string      │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: File Handling (Reading and Writing Files)
""")

