"""
PYTHON LISTS INTRODUCTION (PART 1)
NeuralAICodeCraft - Complete Guide to List Basics

Topics Covered:
1. What are Lists?
2. Creating Lists
3. Accessing List Elements (Indexing)
4. Lists are Ordered
5. Lists are Heterogeneous
6. Lists are Mutable
7. Common Operations (append, len, +)
8. Iterating Through Lists
"""

print("=" * 70)
print("🐍 PYTHON LISTS INTRODUCTION (PART 1)")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: WHAT ARE LISTS?
# ============================================

print("\n📚 PART 1: WHAT ARE LISTS?")
print("-" * 50)

print("""
A list is a collection of items (elements) stored in a single variable.

Think of a list like a container that can hold multiple values:
- A list of student names
- A list of test scores
- A list of shopping items

KEY CHARACTERISTICS:
├── Ordered - Items have a specific order [citation:3][citation:5]
├── Heterogeneous - Can hold different types [citation:5][citation:6]
├── Mutable - Can be changed after creation [citation:3][citation:6]
└── Dynamic - Can grow or shrink [citation:5]
""")

# Example: Without lists (individual variables)
print("\n❌ WITHOUT LISTS (Individual Variables):")
student1 = "Alice"
student2 = "Bob"
student3 = "Charlie"
# ... This gets messy with many students

print("✅ WITH LISTS:")
students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"  Students: {students}")

# ============================================
# PART 2: CREATING LISTS
# ============================================

print("\n📦 PART 2: CREATING LISTS")
print("-" * 50)

print("\n2.1 Empty List:")
empty_list1 = []
empty_list2 = list()
print(f"  Method 1: {empty_list1}")
print(f"  Method 2: {empty_list2}")

print("\n2.2 List with Values:")
fruits = ["apple", "banana", "cherry"]  # Strings
numbers = [10, 20, 30, 40]             # Integers
mixed = [1, "Hello", 3.14, True]       # Mixed types
nested = [[1, 2], [3, 4]]              # List inside list

print(f"  Fruits: {fruits}")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed}")
print(f"  Nested list: {nested}")

print("\n2.3 List from String:")
chars = list("Python")
print(f"  list('Python'): {chars}")

# ============================================
# PART 3: ACCESSING LIST ELEMENTS
# ============================================

print("\n🔍 PART 3: ACCESSING LIST ELEMENTS (INDEXING)")
print("-" * 50)

print("""
IMPORTANT: Indexing starts at 0!
- First item → index 0
- Second item → index 1
- Third item → index 2
- And so on... [citation:1][citation:2]
""")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"  List: {fruits}")

print("\n3.1 Positive Indexing:")
print(f"  fruits[0] → {fruits[0]}  # First item")
print(f"  fruits[1] → {fruits[1]}  # Second item")
print(f"  fruits[2] → {fruits[2]}  # Third item")
print(f"  fruits[3] → {fruits[3]}  # Fourth item")
print(f"  fruits[4] → {fruits[4]}  # Fifth item")

print("\n3.2 Negative Indexing (count from end):")
print(f"  fruits[-1] → {fruits[-1]}  # Last item")
print(f"  fruits[-2] → {fruits[-2]}  # Second last")
print(f"  fruits[-3] → {fruits[-3]}  # Third last")

print("\n3.3 Accessing Individual Items:")
# Individual item access
print(f"  My favorite fruit is {fruits[0]}!")
print(f"  My second favorite is {fruits[1]}!")

# ============================================
# PART 4: LISTS ARE ORDERED
# ============================================

print("\n📋 PART 4: LISTS ARE ORDERED")
print("-" * 50)

print("""
Lists preserve the order in which items are added [citation:3][citation:5].
The order matters! ['a','b','c'] is NOT the same as ['c','b','a'].
""")

list_a = ["apple", "banana", "cherry"]
list_b = ["cherry", "banana", "apple"]

print(f"  List A: {list_a}")
print(f"  List B: {list_b}")
print(f"  Are they equal? {list_a == list_b}")  # False - order matters!

# ============================================
# PART 5: LISTS ARE HETEROGENEOUS
# ============================================

print("\n🎨 PART 5: LISTS ARE HETEROGENEOUS")
print("-" * 50)

print("""
Lists can hold different types of data [citation:5][citation:6]:
- Integers
- Strings
- Floats
- Booleans
- Other lists
- Any Python object!
""")

mixed_list = [42, "Python", 3.14, True, [1, 2, 3]]
print(f"  Mixed list: {mixed_list}")
print(f"  Index 0 (int): {mixed_list[0]} → {type(mixed_list[0])}")
print(f"  Index 1 (str): {mixed_list[1]} → {type(mixed_list[1])}")
print(f"  Index 2 (float): {mixed_list[2]} → {type(mixed_list[2])}")
print(f"  Index 3 (bool): {mixed_list[3]} → {type(mixed_list[3])}")
print(f"  Index 4 (list): {mixed_list[4]} → {type(mixed_list[4])}")

# ============================================
# PART 6: LISTS ARE MUTABLE
# ============================================

print("\n✏️ PART 6: LISTS ARE MUTABLE")
print("-" * 50)

print("""
Lists can be changed after creation [citation:3][citation:6]:
- Modify existing elements
- Add new elements
- Remove elements
""")

fruits = ["apple", "banana", "cherry"]
print(f"  Original: {fruits}")

# Modify an element
fruits[1] = "blueberry"
print(f"  After fruits[1] = 'blueberry': {fruits}")

# Add new element
fruits.append("date")
print(f"  After append('date'): {fruits}")

# Remove element
fruits.remove("cherry")
print(f"  After remove('cherry'): {fruits}")

print("\n⚠️ Important: Strings are IMMUTABLE, but lists are MUTABLE!")
print("  String: name = 'Alice'; name[0] = 'B' ❌ (Error!)")
print("  List:   names = ['Alice']; names[0] = 'Bob' ✅ (Works!)")

# ============================================
# PART 7: COMMON LIST OPERATIONS
# ============================================

print("\n🔧 PART 7: COMMON LIST OPERATIONS")
print("-" * 50)

# 7.1 Append
print("\n7.1 append() - Add item to end:")
fruits = ["apple", "banana", "cherry"]
print(f"  Before: {fruits}")
fruits.append("date")
print(f"  After append('date'): {fruits}")

# 7.2 Len
print("\n7.2 len() - Get list length:")
numbers = [10, 20, 30, 40, 50]
print(f"  List: {numbers}")
print(f"  Length: {len(numbers)}")

# 7.3 Concatenation (+)
print("\n7.3 Concatenation (+) - Combine lists:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"  {list1} + {list2} = {combined}")

# 7.4 Repetition (*)
print("\n7.4 Repetition (*) - Repeat list:")
original = [1, 2]
repeated = original * 3
print(f"  {original} * 3 = {repeated}")

# 7.5 Membership (in)
print("\n7.5 Membership (in) - Check if item exists:")
fruits = ["apple", "banana", "cherry"]
print(f"  List: {fruits}")
print(f"  'banana' in fruits? {'banana' in fruits}")
print(f"  'grape' in fruits? {'grape' in fruits}")

# ============================================
# PART 8: ITERATING THROUGH LISTS
# ============================================

print("\n🔄 PART 8: ITERATING THROUGH LISTS")
print("-" * 50)

print("\n8.1 Using for loop (Pythonic way):")
fruits = ["apple", "banana", "cherry", "date"]
print("  Fruits:")
for fruit in fruits:
    print(f"    {fruit}")

print("\n8.2 Using for loop with index:")
print("  Fruits with positions:")
for i in range(len(fruits)):
    print(f"    Index {i}: {fruits[i]}")

# ============================================
# PART 9: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 9: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Create a List
Create a list called 'colors' with 5 colors.

🎯 EXERCISE 2: Access Elements
From the colors list:
- Print the first color
- Print the last color
- Print the middle color

🎯 EXERCISE 3: Modify List
Change the second color to something else.

🎯 EXERCISE 4: Add and Remove
Add a new color to the end, then remove the first color.

🎯 EXERCISE 5: Iteration
Print all colors with 'I like ' before each one.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
colors = ["red", "blue", "green", "yellow", "purple"]
print(f"Ex1 - Colors: {colors}")

# Exercise 2
print(f"Ex2 - First: {colors[0]}, Last: {colors[-1]}, Middle: {colors[2]}")

# Exercise 3
colors[1] = "cyan"
print(f"Ex3 - After change: {colors}")

# Exercise 4
colors.append("orange")
colors.remove("red")
print(f"Ex4 - After add/remove: {colors}")

# Exercise 5
print("Ex5 - Iteration:")
for color in colors:
    print(f"  I like {color}!")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ PYTHON LISTS INTRODUCTION (PART 1) COMPLETE!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    CREATING LISTS                           │
├─────────────────────────────────────────────────────────────┤
│  []                    → Empty list                         │
│  [1, 2, 3]             → List with values                   │
│  list("abc")           → ['a','b','c']                      │
├─────────────────────────────────────────────────────────────┤
│                    ACCESSING ELEMENTS                       │
├─────────────────────────────────────────────────────────────┤
│  my_list[0]            → First element [citation:1]          │
│  my_list[-1]           → Last element [citation:7]          │
│  my_list[1] = 99       → Modify element [citation:1]        │
├─────────────────────────────────────────────────────────────┤
│                    KEY CHARACTERISTICS                      │
├─────────────────────────────────────────────────────────────┤
│  ✅ Ordered            → Items have a specific order        │
│  ✅ Heterogeneous      → Can mix data types [citation:5]     │
│  ✅ Mutable            → Can be changed [citation:3]         │
│  ✅ Dynamic            → Can grow/shrink [citation:5]        │
├─────────────────────────────────────────────────────────────┤
│                    COMMON OPERATIONS                        │
├─────────────────────────────────────────────────────────────┤
│  append(x)             → Add x to end [citation:1]          │
│  len(my_list)          → Get length [citation:7]            │
│  list1 + list2         → Concatenate lists [citation:2]      │
│  x in my_list          → Check membership                   │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python Lists Part 2 - Slicing & List Methods
""")