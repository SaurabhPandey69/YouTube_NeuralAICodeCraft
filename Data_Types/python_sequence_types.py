"""
PYTHON SEQUENCE TYPES: LISTS, TUPLES & RANGES
NeuralAICodeCraft - Complete Guide with Examples

Topics Covered:
1. Lists (Mutable Sequences)
2. Tuples (Immutable Sequences)
3. Ranges (Lazy Sequences)
4. Common Sequence Operations
"""

print("=" * 70)
print("🐍 PYTHON SEQUENCE TYPES: LISTS, TUPLES & RANGES")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: LISTS (Mutable Sequences)
# ============================================

print("\n📋 PART 1: LISTS - MUTABLE SEQUENCES")
print("-" * 50)

# 1.1 Creating Lists
print("\n1.1 Creating Lists:")
print("-" * 30)

empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
nested = [[1, 2], [3, 4], [5, 6]]
list_from_range = list(range(10))
list_from_string = list("Python")

print(f"  Empty list: {empty_list}")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed}")
print(f"  Nested list: {nested}")
print(f"  From range: {list_from_range}")
print(f"  From string: {list_from_string}")

# 1.2 Accessing Elements
print("\n1.2 Accessing Elements:")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"  Fruits: {fruits}")
print(f"  First fruit (index 0): {fruits[0]}")
print(f"  Last fruit (index -1): {fruits[-1]}")
print(f"  Slicing [1:4]: {fruits[1:4]}")
print(f"  Slicing [::2] (every other): {fruits[::2]}")
print(f"  Reverse [::-1]: {fruits[::-1]}")

# 1.3 List Methods
print("\n1.3 List Methods:")
print("-" * 30)

# Append (add to end)
shopping = []
shopping.append("milk")
shopping.append("eggs")
shopping.append("bread")
print(f"  After append: {shopping}")

# Extend (add multiple items)
shopping.extend(["butter", "cheese", "juice"])
print(f"  After extend: {shopping}")

# Insert (at specific position)
shopping.insert(1, "yogurt")
print(f"  After insert at index 1: {shopping}")

# Remove (first occurrence)
shopping.remove("butter")
print(f"  After remove 'butter': {shopping}")

# Pop (remove and return)
popped = shopping.pop()
print(f"  Popped item: {popped}")
print(f"  After pop: {shopping}")

# Pop at index
popped_index = shopping.pop(1)
print(f"  Popped at index 1: {popped_index}")
print(f"  After pop index 1: {shopping}")

# Sort
numbers_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers_list.sort()
print(f"  Sorted list: {numbers_list}")

# Sort descending
numbers_list.sort(reverse=True)
print(f"  Sorted descending: {numbers_list}")

# Reverse
fruits = ["apple", "banana", "cherry"]
fruits.reverse()
print(f"  Reversed list: {fruits}")

# Index (find position)
position = fruits.index("banana")
print(f"  Index of 'banana': {position}")

# Count occurrences
numbers = [1, 2, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(f"  Count of 2: {count}")

# Clear
shopping.clear()
print(f"  After clear: {shopping}")

# 1.4 List Comprehensions
print("\n1.4 List Comprehensions (Pythonic way):")
print("-" * 30)

# Square numbers
squares = [x**2 for x in range(10)]
print(f"  Squares: {squares}")

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"  Evens: {evens}")

# Nested list comprehension
matrix = [[j for j in range(3)] for i in range(3)]
print(f"  Matrix: {matrix}")

# Conditional with else
parity = ["even" if x % 2 == 0 else "odd" for x in range(10)]
print(f"  Parity: {parity}")

# 1.5 Nested Lists (Matrices)
print("\n1.5 Nested Lists (Matrices):")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"  Matrix:")
for row in matrix:
    print(f"    {row}")

print(f"  Element at [1][1]: {matrix[1][1]}")
print(f"  Row 2: {matrix[1]}")
print(f"  Column 1: {[row[0] for row in matrix]}")

# 1.6 List Performance Considerations
print("\n1.6 List Performance Notes:")
print("-" * 30)
print("""
  ✅ Fast for: Indexing, appending (amortized O(1))
  ⚠️ Slow for: Inserting at beginning, searching (O(n))
  💡 Tip: Use deque from collections for frequent left-side operations
  💡 Tip: Use array module for homogeneous numeric data
""")

# ============================================
# PART 2: TUPLES (Immutable Sequences)
# ============================================

print("\n📦 PART 2: TUPLES - IMMUTABLE SEQUENCES")
print("-" * 50)

# 2.1 Creating Tuples
print("\n2.1 Creating Tuples:")
print("-" * 30)

empty_tuple = ()
single_item = (1,)  # Note the comma!
numbers = (1, 2, 3, 4, 5)
mixed = (1, "hello", 3.14, True)
nested = ((1, 2), (3, 4), (5, 6))
tuple_from_list = tuple([1, 2, 3])
tuple_from_string = tuple("Python")

print(f"  Empty tuple: {empty_tuple}")
print(f"  Single item tuple: {single_item} (type: {type(single_item)})")
print(f"  Numbers: {numbers}")
print(f"  Mixed types: {mixed}")
print(f"  Nested tuple: {nested}")
print(f"  From list: {tuple_from_list}")
print(f"  From string: {tuple_from_string}")

# 2.2 Tuple Immutability
print("\n2.2 Tuple Immutability (Cannot Change):")
print("-" * 30)

coordinates = (10, 20)
print(f"  Original tuple: {coordinates}")
print(f"  Access first element: {coordinates[0]}")
print("  Trying to modify...")
try:
    coordinates[0] = 99
except TypeError as e:
    print(f"  ❌ Error: {e}")

# 2.3 Tuple Methods (limited)
print("\n2.3 Tuple Methods:")
print("-" * 30)

colors = ("red", "green", "blue", "green", "yellow")
print(f"  Tuple: {colors}")
print(f"  Count of 'green': {colors.count('green')}")
print(f"  Index of 'blue': {colors.index('blue')}")

# 2.4 Tuple Unpacking
print("\n2.4 Tuple Unpacking:")
print("-" * 30)

# Basic unpacking
point = (10, 20)
x, y = point
print(f"  Point: {point} → x={x}, y={y}")

# Swapping variables
a, b = 5, 10
print(f"  Before swap: a={a}, b={b}")
a, b = b, a
print(f"  After swap: a={a}, b={b}")

# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print(f"  Numbers: {numbers}")
print(f"  First: {first}, Middle: {middle}, Last: {last}")

# Ignoring values
person = ("John", 30, "Engineer", "New York")
name, age, *rest = person
print(f"  Name: {name}, Age: {age}, Rest: {rest}")

# 2.5 Named Tuples
print("\n2.5 Named Tuples (Enhanced Readability):")
print("-" * 30)

from collections import namedtuple

# Define named tuple
Person = namedtuple('Person', ['name', 'age', 'city', 'profession'])

# Create instances
person1 = Person(name="Alice", age=28, city="New York", profession="Engineer")
person2 = Person("Bob", 32, "San Francisco", "Designer")

print(f"  Person 1: {person1}")
print(f"  Person 1.name: {person1.name}")
print(f"  Person 1.age: {person1.age}")
print(f"  Person 2: {person2}")

# Named tuple methods
print(f"  As dictionary: {person1._asdict()}")
print(f"  Fields: {person1._fields}")

# 2.6 When to Use Tuples vs Lists
print("\n2.6 Tuples vs Lists: When to Use What?")
print("-" * 30)

print("""
  ✅ USE TUPLES WHEN:
  ├── Data should not change (constants, configuration)
  ├── Dictionary keys (tuples are hashable)
  ├── Function returns multiple values
  ├── Performance matters (tuples are slightly faster)
  └── Data has a fixed structure (like database records)

  ✅ USE LISTS WHEN:
  ├── Data needs to change (add, remove, modify)
  ├── Unknown number of elements
  ├── Need list-specific methods
  └── Working with dynamic collections
""")

# 2.7 Tuples as Dictionary Keys
print("\n2.7 Tuples as Dictionary Keys (Lists cannot be keys):")
print("-" * 30)

# Valid - tuple as key
locations = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
    (41.8781, -87.6298): "Chicago"
}
print(f"  Location at (40.7128, -74.0060): {locations[(40.7128, -74.0060)]}")

# Invalid - list as key (uncomment to see error)
try:
    invalid_dict = {[1, 2]: "value"}
except TypeError as e:
    print(f"  ❌ List as key error: {e}")

# ============================================
# PART 3: RANGES (Lazy Sequences)
# ============================================

print("\n🎯 PART 3: RANGES - MEMORY-EFFICIENT SEQUENCES")
print("-" * 50)

# 3.1 Creating Ranges
print("\n3.1 Creating Ranges:")
print("-" * 30)

# Single argument (stop)
range1 = range(10)
print(f"  range(10): {list(range1)}")

# Two arguments (start, stop)
range2 = range(5, 15)
print(f"  range(5, 15): {list(range2)}")

# Three arguments (start, stop, step)
range3 = range(0, 20, 2)
print(f"  range(0, 20, 2): {list(range3)}")

# Negative step
range4 = range(10, 0, -1)
print(f"  range(10, 0, -1): {list(range4)}")

# 3.2 Range Properties
print("\n3.2 Range Properties:")
print("-" * 30)

r = range(1, 100, 3)
print(f"  Range: {r}")
print(f"  Start: {r.start}")
print(f"  Stop: {r.stop}")
print(f"  Step: {r.step}")
print(f"  Length: {len(r)}")
print(f"  Index 0: {r[0]}")
print(f"  Index 10: {r[10]}")
print(f"  Last element: {r[-1]}")
print(f"  Memory size: {r.__sizeof__()} bytes (vs {len(r)*28} bytes for list)")

# 3.3 Memory Efficiency Demonstration
print("\n3.3 Memory Efficiency (Lazy Evaluation):")
print("-" * 30)

import sys

# Create large list vs range
large_list = list(range(1_000_000))
large_range = range(1_000_000)

print(f"  List of 1M numbers: {sys.getsizeof(large_list):,} bytes")
print(f"  Range of 1M numbers: {sys.getsizeof(large_range):,} bytes")
print(f"  Memory saved: {(sys.getsizeof(large_list) - sys.getsizeof(large_range)):,} bytes ({(sys.getsizeof(large_list)/sys.getsizeof(large_range)):.0f}x smaller)")

# 3.4 Range Operations
print("\n3.4 Range Operations:")
print("-" * 30)

r = range(10, 30, 3)
print(f"  Range: {list(r)}")

# Membership testing
print(f"  15 in range? {15 in r}")
print(f"  16 in range? {16 in r}")

# Slicing ranges
print(f"  Slice [2:5]: {list(r[2:5])}")
print(f"  Slice [::2]: {list(r[::2])}")

# Converting to list
print(f"  As list: {list(r)}")
print(f"  As tuple: {tuple(r)}")

# 3.5 Practical Uses of Ranges
print("\n3.5 Practical Uses of Ranges:")
print("-" * 30)

# For loops
print("  Even numbers from 0 to 10:")
for i in range(0, 11, 2):
    print(f"    {i}")

# Index-based iteration
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"\n  Index-based iteration:")
for i in range(len(fruits)):
    print(f"    {i}: {fruits[i]}")

# Creating sequences
even_numbers = list(range(0, 20, 2))
odd_numbers = list(range(1, 20, 2))
print(f"  Even numbers: {even_numbers}")
print(f"  Odd numbers: {odd_numbers}")

# Reverse iteration
print(f"  Numbers 10 to 1: {list(range(10, 0, -1))}")

# ============================================
# PART 4: COMMON SEQUENCE OPERATIONS
# ============================================

print("\n🔧 PART 4: COMMON SEQUENCE OPERATIONS")
print("-" * 50)

# 4.1 Operations on All Sequences
print("\n4.1 Operations on All Sequences:")
print("-" * 30)

seq_list = [1, 2, 3, 4, 5]
seq_tuple = (1, 2, 3, 4, 5)
seq_range = range(1, 6)

print(f"  List: {seq_list}")
print(f"  Tuple: {seq_tuple}")
print(f"  Range: {list(seq_range)}")

# Length
print(f"  Length (list): {len(seq_list)}")
print(f"  Length (tuple): {len(seq_tuple)}")
print(f"  Length (range): {len(seq_range)}")

# Min, Max, Sum
print(f"  Min: {min(seq_list)}")
print(f"  Max: {max(seq_list)}")
print(f"  Sum: {sum(seq_list)}")

# Membership
print(f"  3 in list? {3 in seq_list}")
print(f"  10 in list? {10 in seq_list}")

# Concatenation
list_concat = seq_list + [6, 7, 8]
tuple_concat = seq_tuple + (6, 7, 8)
print(f"  List concatenation: {list_concat}")
print(f"  Tuple concatenation: {tuple_concat}")

# Repetition
list_repeat = seq_list * 2
tuple_repeat = seq_tuple * 2
print(f"  List repetition: {list_repeat}")
print(f"  Tuple repetition: {tuple_repeat}")

# 4.2 Slicing Techniques
print("\n4.2 Advanced Slicing Techniques:")
print("-" * 30)

items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"  Original: {items}")

# Basic slicing
print(f"  [2:5]: {items[2:5]}")
print(f"  [:5]: {items[:5]}")
print(f"  [5:]: {items[5:]}")
print(f"  [::2]: {items[::2]}")
print(f"  [1::2]: {items[1::2]}")
print(f"  [::-1]: {items[::-1]} (reverse)")

# Slicing with negative indices
print(f"  [-3:]: {items[-3:]}")
print(f"  [:-3]: {items[:-3]}")
print(f"  [-5:-2]: {items[-5:-2]}")

# 4.3 Iteration Techniques
print("\n4.3 Iteration Techniques:")
print("-" * 30)

# Enumerate (get index and value)
colors = ["red", "green", "blue"]
print("  Using enumerate:")
for i, color in enumerate(colors):
    print(f"    {i}: {color}")

# Zip (iterate multiple sequences)
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["NYC", "LA", "Chicago"]

print("\n  Using zip:")
for name, age, city in zip(names, ages, cities):
    print(f"    {name} is {age} from {city}")

# Sorted
unsorted = [3, 1, 4, 1, 5, 9, 2]
print(f"  Unsorted: {unsorted}")
print(f"  Sorted: {sorted(unsorted)}")
print(f"  Sorted reverse: {sorted(unsorted, reverse=True)}")
print(f"  Original unchanged: {unsorted}")

# Reversed
print(f"  Reversed: {list(reversed(unsorted))}")

# ============================================
# PART 5: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 5: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: List Comprehension
Create a list of squares of all odd numbers from 1 to 20.

Solution:
odd_squares = [x**2 for x in range(1, 21) if x % 2 == 1]
print(odd_squares)

🎯 EXERCISE 2: Tuple Unpacking
Given a tuple (name, age, city, profession, salary), unpack all values.

Solution:
person = ("John", 30, "NYC", "Engineer", 75000)
name, age, city, profession, salary = person

🎯 EXERCISE 3: Range Usage
Create a range that generates numbers: 100, 95, 90, ... , 0

Solution:
descending = range(100, -1, -5)
print(list(descending))

🎯 EXERCISE 4: List Methods
Write a program that:
1. Creates an empty list
2. Adds 5 numbers using append
3. Inserts a number at position 2
4. Removes the last element
5. Sorts the list
6. Reverses the list

🎯 EXERCISE 5: Named Tuple
Create a named tuple 'Book' with fields: title, author, year, genre
Create 3 book instances and print them

🎯 CHALLENGE: Matrix Operations
Create a 5x5 matrix using nested list comprehension
Calculate the sum of all elements
Find the maximum element in each row
""")

# Solutions
print("\n💡 SOLUTIONS:")
print("-" * 30)

# Exercise 1
odd_squares = [x**2 for x in range(1, 21) if x % 2 == 1]
print(f"  Ex1 - Odd squares: {odd_squares}")

# Exercise 2
person = ("John", 30, "NYC", "Engineer", 75000)
name, age, city, profession, salary = person
print(f"  Ex2 - Unpacked: {name}, {age}, {city}, {profession}, {salary}")

# Exercise 3
descending = range(100, -1, -5)
print(f"  Ex3 - Descending: {list(descending)}")

# Exercise 4
lst = []
lst.extend([10, 20, 30, 40, 50])
lst.insert(2, 25)
lst.pop()
lst.sort()
lst.reverse()
print(f"  Ex4 - Final list: {lst}")

# Exercise 5
from collections import namedtuple
Book = namedtuple('Book', ['title', 'author', 'year', 'genre'])
books = [
    Book("1984", "George Orwell", 1949, "Dystopian"),
    Book("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
]
print(f"  Ex5 - Books:")
for book in books:
    print(f"    {book.title} by {book.author} ({book.year})")

# Challenge
matrix = [[i*5 + j for j in range(5)] for i in range(5)]
print(f"  Challenge - 5x5 Matrix:")
for row in matrix:
    print(f"    {row}")
print(f"    Sum of all elements: {sum(sum(row) for row in matrix)}")
print(f"    Max in each row: {[max(row) for row in matrix]}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ SEQUENCE TYPES MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE:

┌─────────────┬──────────────┬─────────────┬──────────────┐
│   FEATURE   │    LIST      │    TUPLE    │    RANGE     │
├─────────────┼──────────────┼─────────────┼──────────────┤
│ Mutability  │ ✅ Mutable   │ ❌ Immutable│ ❌ Immutable │
│ Dynamic     │ ✅ Dynamic   │ ❌ Fixed    │ ❌ Fixed     │
│ Memory      │ High         │ Low         │ Very Low     │
│ Speed       │ Medium       │ Fast        │ Fast (lazy)  │
│ Hashable    │ ❌ No        │ ✅ Yes      │ ✅ Yes       │
│ Use Case    │ Collections  │ Constants   │ Loops/Large  │
└─────────────┴──────────────┴─────────────┴──────────────┘

NEXT VIDEO: Dictionaries, Sets, Frozenset & Binary Types!
""")