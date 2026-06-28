"""
FOR LOOP WITH else, enumerate() & NESTED LOOPS
NeuralAICodeCraft - Complete Guide

Topics Covered:
1. for loop with else
2. enumerate() Function
3. Nested For Loops
"""

print("=" * 70)
print("🐍 FOR LOOP WITH else, enumerate() & NESTED LOOPS")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: FOR LOOP WITH else
# ============================================

print("\n📚 PART 1: FOR LOOP WITH else")
print("-" * 50)

print("""
else with for loop executes ONLY when:
├── Loop completes ALL iterations
├── No break statement was encountered
└── NOT executed if break occurs

Common Use Case: Search with "not found" condition
""")

# 1.1 Basic else (no break)
print("\n1.1 Basic else (no break):")
print("-" * 30)

print("Loop completes normally:")
for i in range(1, 6):
    print(f"  {i}")
else:
    print("  ✅ Loop completed normally!")

# 1.2 else with break (does NOT execute)
print("\n1.2 else with break (not executed):")
print("-" * 30)

print("Loop with break at 3:")
for i in range(1, 6):
    if i == 3:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")
else:
    print("  ❌ This else will NOT execute")

print("  ✅ Loop exited with break")

# 1.3 else with continue (else executes)
print("\n1.3 else with continue (else executes):")
print("-" * 30)

print("Loop with continue at 3:")
for i in range(1, 6):
    if i == 3:
        print(f"  Skipping {i}")
        continue
    print(f"  {i}")
else:
    print("  ✅ Else executes because no break!")

# 1.4 Practical: Prime Number Check
print("\n1.4 Practical: Prime Number Check:")
print("-" * 30)

def is_prime(n):
    """Check if number is prime using for-else"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"  {n} is divisible by {i}")
            return False
    else:
        print(f"  ✅ {n} is PRIME!")
        return True

# Test numbers
test_numbers = [2, 7, 12, 17, 25, 29]
for num in test_numbers:
    is_prime(num)

# 1.5 Practical: Search with "not found"
print("\n1.5 Practical: Search with 'not found':")
print("-" * 30)

def find_element(lst, target):
    """Search for element using for-else"""
    for item in lst:
        if item == target:
            print(f"  ✅ Found '{target}'!")
            return True
    else:
        print(f"  ❌ '{target}' not found")
        return False

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

find_element(fruits, "cherry")
find_element(fruits, "mango")

# 1.6 else with nested loops
print("\n1.6 else with Nested Loops:")
print("-" * 30)

print("Breaking outer loop:")
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            print(f"  Breaking at i={i}, j={j}")
            break
        print(f"  i={i}, j={j}")
    else:
        print(f"  Inner loop completed for i={i}")
print("  Outer loop completed")

print("\n💡 TIP: else attaches to the innermost loop!")

# ============================================
# PART 2: enumerate() FUNCTION
# ============================================

print("\n🔢 PART 2: enumerate() FUNCTION")
print("-" * 50)

print("""
enumerate() adds a counter to an iterable.
- Returns tuples of (index, value)
- Syntax: enumerate(iterable, start=0)
- Default start is 0
- Lazy evaluation - yields values one by one
""")

# 2.1 Basic enumerate
print("\n2.1 Basic enumerate (default start=0):")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date"]

print("Using enumerate:")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# 2.2 Custom start index
print("\n2.2 Custom start index (start=1):")
print("-" * 30)

print("Starting from 1:")
for index, fruit in enumerate(fruits, start=1):
    print(f"  {index}: {fruit}")

# 2.3 enumerate vs manual counter
print("\n2.3 enumerate vs Manual Counter:")
print("-" * 30)

colors = ["red", "green", "blue", "yellow"]

print("Manual counter:")
index = 0
for color in colors:
    print(f"  {index}: {color}")
    index += 1

print("\nenumerate() - cleaner!")
for index, color in enumerate(colors):
    print(f"  {index}: {color}")

# 2.4 Converting enumerate to list
print("\n2.4 enumerate() to list:")
print("-" * 30)

fruits = ["apple", "banana", "cherry"]
enum_list = list(enumerate(fruits))
print(f"  list(enumerate(fruits)) → {enum_list}")

# 2.5 enumerate with start and step (custom logic)
print("\n2.5 Custom Counter with enumerate:")
print("-" * 30)

def enumerate_custom(iterable, start=0, step=1):
    """Custom enumerate with step"""
    for item in iterable:
        yield start, item
        start += step

for index, fruit in enumerate_custom(fruits, start=1, step=2):
    print(f"  {index}: {fruit}")

# 2.6 Real-world: Creating dictionaries
print("\n2.6 enumerate() to create dictionaries:")
print("-" * 30)

names = ["Alice", "Bob", "Charlie", "Diana"]

# Create dictionary with employee IDs
employees = {index + 100: name for index, name in enumerate(names)}
print(f"  Employee dictionary: {employees}")

# 2.7 enumerate with string
print("\n2.7 enumerate() with strings:")
print("-" * 30)

word = "Python"
for index, char in enumerate(word):
    print(f"  Position {index}: '{char}'")

# ============================================
# PART 3: NESTED FOR LOOPS
# ============================================

print("\n🔀 PART 3: NESTED FOR LOOPS")
print("-" * 50)

print("""
Nested loops are loops inside loops.
- Inner loop completes all iterations for each outer loop iteration
- Outer loop controls the inner loop's repetitions
- Used for: patterns, matrices, combinations
""")

# 3.1 Basic Nested Loop
print("\n3.1 Basic Nested Loop:")
print("-" * 30)

print("Outer loop (i) × Inner loop (j):")
for i in range(1, 4):
    print(f"  i={i}")
    for j in range(1, 4):
        print(f"    j={j}")
    print("  ---")

# 3.2 Multiplication Table
print("\n3.2 Multiplication Table (5x5):")
print("-" * 30)

print("  Multiplication Table:")
print("    " + " ".join(f"{j:3}" for j in range(1, 6)))
for i in range(1, 6):
    print(f"  {i}  " + " ".join(f"{i*j:3}" for j in range(1, 6)))

# 3.3 Creating Patterns
print("\n3.3 Creating Patterns with Nested Loops:")
print("-" * 30)

print("  Right Triangle Pattern:")
for i in range(1, 6):
    print("    " + "* " * i)

print("\n  Number Pattern:")
for i in range(1, 6):
    print("    " + " ".join(str(i) for _ in range(i)))

print("\n  Floyd's Triangle:")
num = 1
for i in range(1, 6):
    for j in range(i):
        print(f"    {num:2}", end=" ")
        num += 1
    print()

# 3.4 Matrix Operations
print("\n3.4 Matrix Operations:")
print("-" * 30)

# Create a 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Matrix:")
for row in matrix:
    print(f"    {row}")

# Sum of all elements
total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total += matrix[i][j]
print(f"  Sum of all elements: {total}")

# Matrix transpose
print("\n  Matrix Transpose:")
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
for row in transpose:
    print(f"    {row}")

# 3.5 enumerate() with Nested Loops
print("\n3.5 enumerate() in Nested Loops:")
print("-" * 30)

grid = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H', 'I']
]

print("  Grid with positions:")
for i, row in enumerate(grid):
    for j, value in enumerate(row):
        print(f"    grid[{i}][{j}] = '{value}'")

# 3.6 Simulating enumerate() with Nested Loops
print("\n3.6 Simulating enumerate() with Nested Loops:")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date"]

print("  Using nested loop to simulate enumerate:")
for i in range(len(fruits)):
    print(f"    {i}: {fruits[i]}")

print("\n  Using enumerate (cleaner way):")
for i, fruit in enumerate(fruits):
    print(f"    {i}: {fruit}")

# ============================================
# PART 4: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 4: REAL-WORLD EXAMPLES")
print("-" * 50)

# 4.1 Student Grades
print("\n4.1 Student Grades Manager:")
print("-" * 30)

students = [
    {"name": "Alice", "scores": [85, 90, 78]},
    {"name": "Bob", "scores": [92, 88, 95]},
    {"name": "Charlie", "scores": [70, 75, 80]}
]

for student in students:
    avg = sum(student["scores"]) / len(student["scores"])
    print(f"  {student['name']}: {avg:.1f}")
else:
    print("  ✅ All grades calculated!")

# 4.2 CSV Data Processing
print("\n4.2 CSV Data Processing:")
print("-" * 30)

csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

print("  Processing CSV:")
for i, row in enumerate(csv_data):
    if i == 0:
        print(f"    Header: {row}")
    else:
        print(f"    Row {i}: Name={row[0]}, Age={row[1]}, City={row[2]}")

# 4.3 To-Do List with Nested Loops
print("\n4.3 To-Do List Manager:")
print("-" * 30)

todo_list = [
    ["Morning", "Wake up", "Exercise", "Breakfast"],
    ["Work", "Check email", "Code", "Meeting"],
    ["Evening", "Dinner", "Read", "Sleep"]
]

for category, tasks in enumerate(todo_list):
    print(f"  Category {category + 1}:")
    for i, task in enumerate(tasks, start=1):
        print(f"    {i}. {task}")

# ============================================
# PART 5: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 5: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: For-else
Use for-else to check if a number is prime.

🎯 EXERCISE 2: enumerate()
Use enumerate to print "Index 0: apple, Index 1: banana" etc.

🎯 EXERCISE 3: Nested Loops
Create a 3x3 multiplication table.

🎯 EXERCISE 4: enumerate with Custom Start
Print employee list with IDs starting from 101.

🎯 EXERCISE 5: Nested Loop Pattern
Create a diamond pattern using nested loops.

🎯 CHALLENGE: Shopping Cart
Use nested loops and enumerate to process a shopping cart with items and prices.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Prime Checker:")
def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True

for num in [2, 7, 12, 17]:
    print(f"  {num} is prime? {is_prime_num(num)}")

# Exercise 2
print("\nEx2 - enumerate() with fruits:")
fruits = ["apple", "banana", "cherry", "date"]
for i, fruit in enumerate(fruits):
    print(f"  Index {i}: {fruit}")

# Exercise 3
print("\nEx3 - Multiplication Table:")
for i in range(1, 4):
    row = [i * j for j in range(1, 4)]
    print(f"  {row}")

# Exercise 4
print("\nEx4 - Employee IDs:")
employees = ["Alice", "Bob", "Charlie"]
for emp_id, name in enumerate(employees, start=101):
    print(f"  ID {emp_id}: {name}")

# Exercise 5
print("\nEx5 - Diamond Pattern:")
n = 3
for i in range(1, n + 1):
    print("  " + " " * (n - i) + "* " * i)
for i in range(n - 1, 0, -1):
    print("  " + " " * (n - i) + "* " * i)

# Challenge
print("\nChallenge - Shopping Cart:")
cart = [
    ("Laptop", 999.99, 1),
    ("Mouse", 29.99, 2),
    ("Keyboard", 79.99, 1)
]

total = 0
for i, (item, price, qty) in enumerate(cart, start=1):
    subtotal = price * qty
    total += subtotal
    print(f"  {i}. {item}: ${price} × {qty} = ${subtotal:.2f}")
print(f"  Total: ${total:.2f}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ FOR LOOP, else, enumerate() & NESTED LOOPS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    FOR LOOP WITH else                       │
├─────────────────────────────────────────────────────────────┤
│  for item in iterable:                                     │
│      if condition:                                         │
│          break                                             │
│  else:                                                     │
│      # Runs only if NO break occurred                      │
│      print("Loop completed normally!")                     │
├─────────────────────────────────────────────────────────────┤
│                    enumerate() FUNCTION                     │
├─────────────────────────────────────────────────────────────┤
│  enumerate(iterable)           → (0, item), (1, item)...   │
│  enumerate(iterable, start=1)  → (1, item), (2, item)...   │
│  for i, item in enumerate(list):                           │
│      print(i, item)                                        │
├─────────────────────────────────────────────────────────────┤
│                    NESTED LOOPS                             │
├─────────────────────────────────────────────────────────────┤
│  for i in range(3):                                        │
│      for j in range(3):                                    │
│          print(i, j)    # Inner loop runs 9 times          │
│                                                             │
│  Use for: Patterns, Matrices, Combinations                 │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: While Loop & Infinite Loops
""")