"""
PYTHON list() CONSTRUCTOR - COMPLETE GUIDE
NeuralAICodeCraft - Convert Any Iterable to a List

Topics Covered:
1. list() Basics
2. Converting Strings to Lists
3. Converting Tuples to Lists
4. Converting Range to Lists
5. Converting Dictionaries to Lists
6. Converting Sets to Lists
7. list() vs [] Comparison
8. Real-World Examples
"""

import time
import sys

print("=" * 70)
print("🐍 PYTHON list() CONSTRUCTOR - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: list() BASICS
# ============================================

print("\n📚 PART 1: list() BASICS")
print("-" * 50)

print("""
SYNTAX: list(iterable)

WHAT IT DOES:
├── Creates a new list from an iterable
├── Converts any iterable to a list
├── Returns a new list object
├── The original iterable is unchanged

list() can also create an empty list:
├── list() → empty list []
├── [] → empty list (faster)
""")

# 1.1 Empty List
print("\n1.1 Creating Empty Lists:")
print("-" * 30)

empty1 = list()
empty2 = []

print(f"list() → {empty1}")
print(f"[] → {empty2}")
print(f"Same object? {empty1 is empty2}")  # False

# 1.2 Type Check
print("\n1.2 Type Check:")
print("-" * 30)

my_list = list()
print(f"type(list()) → {type(my_list)}")

# ============================================
# PART 2: CONVERTING STRINGS TO LISTS
# ============================================

print("\n📝 PART 2: CONVERTING STRINGS TO LISTS")
print("-" * 50)

print("""
list(string) → Converts each character to a list element
- Each character becomes an item
- Spaces are preserved
- Special characters become items
""")

# 2.1 Basic String Conversion
print("\n2.1 Basic String Conversion:")
print("-" * 30)

word = "Python"
char_list = list(word)
print(f"list('Python') → {char_list}")

# 2.2 String with Spaces
print("\n2.2 String with Spaces:")
print("-" * 30)

sentence = "Hello World"
chars = list(sentence)
print(f"list('Hello World') → {chars}")
print(f"Length: {len(chars)}")

# 2.3 String with Special Characters
print("\n2.3 String with Special Characters:")
print("-" * 30)

special = "Python@2024!"
special_list = list(special)
print(f"list('Python@2024!') → {special_list}")

# 2.4 Multi-line String
print("\n2.4 Multi-line String:")
print("-" * 30)

multiline = "Line1\nLine2\nLine3"
multiline_list = list(multiline)
print(f"Multi-line string → {multiline_list[:20]}...")

# ============================================
# PART 3: CONVERTING TUPLES TO LISTS
# ============================================

print("\n📦 PART 3: CONVERTING TUPLES TO LISTS")
print("-" * 50)

print("""
list(tuple) → Converts tuple to a list
- Creates a mutable version of the tuple
- Elements remain the same
- Original tuple is unchanged
""")

# 3.1 Basic Tuple Conversion
print("\n3.1 Basic Tuple Conversion:")
print("-" * 30)

my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(f"Tuple: {my_tuple}")
print(f"List: {my_list}")
print(f"Type of tuple: {type(my_tuple)}")
print(f"Type of list: {type(my_list)}")

# 3.2 Mixed Tuple
print("\n3.2 Mixed Tuple:")
print("-" * 30)

mixed_tuple = (1, "Hello", 3.14, True)
mixed_list = list(mixed_tuple)
print(f"Mixed tuple: {mixed_tuple}")
print(f"Mixed list: {mixed_list}")

# 3.3 Nested Tuple
print("\n3.3 Nested Tuple:")
print("-" * 30)

nested_tuple = (1, (2, 3), (4, 5, 6))
nested_list = list(nested_tuple)
print(f"Nested tuple: {nested_tuple}")
print(f"Nested list: {nested_list}")
print("Note: Nested tuples remain as tuples!")

# ============================================
# PART 4: CONVERTING RANGE TO LISTS
# ============================================

print("\n🔢 PART 4: CONVERTING RANGE TO LISTS")
print("-" * 50)

print("""
list(range()) → Converts range to a list
- Creates a list with all values
- Memory efficient: range is lazy, list is eager
- Useful for debugging range objects
""")

# 4.1 Basic Range Conversion
print("\n4.1 Basic Range Conversion:")
print("-" * 30)

r = range(5)
r_list = list(r)
print(f"range(5) → {r}")
print(f"list(range(5)) → {r_list}")

# 4.2 Range with Start and Stop
print("\n4.2 Range with Start and Stop:")
print("-" * 30)

r = range(2, 7)
r_list = list(r)
print(f"range(2, 7) → {list(r)}")

# 4.3 Range with Step
print("\n4.3 Range with Step:")
print("-" * 30)

r = range(1, 10, 2)
r_list = list(r)
print(f"range(1, 10, 2) → {r_list}")

# 4.4 Descending Range
print("\n4.4 Descending Range:")
print("-" * 30)

r = range(10, 0, -1)
r_list = list(r)
print(f"range(10, 0, -1) → {r_list}")

# 4.5 Memory Comparison
print("\n4.5 Memory Comparison:")
print("-" * 30)

print("Memory for range vs list:")
large_range = range(1000000)
large_list = list(large_range)

print(f"  range(1,000,000) size: {sys.getsizeof(large_range)} bytes")
print(f"  list(range(1,000,000)) size: {sys.getsizeof(large_list):,} bytes")

print("  ✅ range is MEMORY EFFICIENT!")

# ============================================
# PART 5: CONVERTING DICTIONARIES TO LISTS
# ============================================

print("\n📖 PART 5: CONVERTING DICTIONARIES TO LISTS")
print("-" * 50)

print("""
list(dict) → Converts KEYS to a list
- Only keys are included
- Values are NOT included
- Use dict.values() to get values
- Use dict.items() for key-value pairs
""")

# 5.1 Basic Dictionary Conversion (Keys)
print("\n5.1 Dictionary Keys to List:")
print("-" * 30)

person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}
keys_list = list(person)
print(f"Dictionary: {person}")
print(f"list(dict) → {keys_list}")

# 5.2 Dictionary Values to List
print("\n5.2 Dictionary Values to List:")
print("-" * 30)

values_list = list(person.values())
print(f"list(dict.values()) → {values_list}")

# 5.3 Dictionary Items to List
print("\n5.3 Dictionary Items to List:")
print("-" * 30)

items_list = list(person.items())
print(f"list(dict.items()) → {items_list}")

# 5.4 Empty Dictionary
print("\n5.4 Empty Dictionary:")
print("-" * 30)

empty_dict = {}
print(f"list(empty_dict) → {list(empty_dict)}")

# ============================================
# PART 6: CONVERTING SETS TO LISTS
# ============================================

print("\n🎯 PART 6: CONVERTING SETS TO LISTS")
print("-" * 50)

print("""
list(set) → Converts set to a list
- Order may vary (sets are unordered)
- Useful for sorting set elements
- Duplicates are removed (set property)
""")

# 6.1 Basic Set Conversion
print("\n6.1 Basic Set Conversion:")
print("-" * 30)

my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print(f"Set: {my_set}")
print(f"List: {my_list}")

# 6.2 Set with Duplicates
print("\n6.2 Set with Duplicates:")
print("-" * 30)

data = [1, 2, 2, 3, 3, 4, 5, 5]
unique_set = set(data)
unique_list = list(unique_set)
print(f"Original with duplicates: {data}")
print(f"Set (unique): {unique_set}")
print(f"List from set: {unique_list}")

# 6.3 Sorting Set
print("\n6.3 Sorting Set Elements:")
print("-" * 30)

unordered_set = {5, 2, 8, 1, 9}
sorted_list = sorted(list(unordered_set))
print(f"Original set: {unordered_set}")
print(f"Sorted list: {sorted_list}")

# ============================================
# PART 7: CONVERTING OTHER ITERABLES
# ============================================

print("\n🔄 PART 7: CONVERTING OTHER ITERABLES")
print("-" * 50)

# 7.1 Converting from File (Simulated)
print("\n7.1 File Lines to List:")
print("-" * 30)

# Simulate file content
file_content = "Line1\nLine2\nLine3\nLine4"
lines = file_content.split('\n')
print(f"Lines from file: {lines}")

# 7.2 Converting Generators
print("\n7.2 Generator to List:")
print("-" * 30)

def square_numbers(n):
    for i in range(n):
        yield i ** 2

gen = square_numbers(5)
gen_list = list(gen)
print(f"Generator values: {gen_list}")

# 7.3 Converting Map Object
print("\n7.3 Map Object to List:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
map_obj = map(lambda x: x ** 2, numbers)
map_list = list(map_obj)
print(f"Map object to list: {map_list}")

# 7.4 Converting Zip Object
print("\n7.4 Zip Object to List:")
print("-" * 30)

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]
zip_obj = zip(names, scores)
zip_list = list(zip_obj)
print(f"Zip object to list: {zip_list}")

# ============================================
# PART 8: list() vs [] - Performance Comparison
# ============================================

print("\n⚡ PART 8: list() vs [] - Performance Comparison")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  list()             │  []                  │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Speed          │  Slower             │  Faster              │
│  Readability    │  Explicit           │  Concise             │
│  Use case       │  Convert iterables  │  Create new lists    │
│  Empty list     │  list()             │  []                  │
│  With data      │  list(range(5))     │  [1, 2, 3, 4, 5]    │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 8.1 Performance Test
print("\n8.1 Performance Test:")
print("-" * 30)

n = 1000000

# Using []
start = time.time()
for _ in range(100):
    lst = []
    for i in range(n):
        lst.append(i)
list_time = time.time() - start

# Using list() with range
start = time.time()
for _ in range(100):
    lst = list(range(n))
range_time = time.time() - start

print(f"Creating {n} elements using [] + loop: {list_time:.4f}s")
print(f"Creating {n} elements using list(range()): {range_time:.4f}s")
print(f"list(range()) is {list_time/range_time:.2f}x faster!")

# 8.2 Bytecode Comparison
print("\n8.2 Bytecode Comparison:")
print("-" * 30)

print("""
DISASSEMBLY ANALYSIS:

def use_list():
    return list()

def use_brackets():
    return []

Bytecode:
- [] → BUILD_LIST (single instruction)
- list() → LOAD_GLOBAL + CALL_FUNCTION (multiple instructions)

RESULT: [] is faster for empty lists!
""")

# ============================================
# PART 9: PRACTICAL EXAMPLES
# ============================================

print("\n🚀 PART 9: PRACTICAL EXAMPLES")
print("-" * 30)

# 9.1 Character Counter
print("\n9.1 Character Counter:")
print("-" * 30)

text = "hello world"
chars = list(text)
unique_chars = list(set(chars))
print(f"Text: {text}")
print(f"Characters: {chars}")
print(f"Unique characters: {unique_chars}")

# 9.2 Creating Number List
print("\n9.2 Creating Number List:")
print("-" * 30)

# Even numbers
evens = list(range(0, 20, 2))
print(f"Even numbers: {evens}")

# Squares
squares = list(x ** 2 for x in range(10))
print(f"Squares: {squares}")

# 9.3 Reading CSV (Simulated)
print("\n9.3 CSV Data to List:")
print("-" * 30)

csv_data = "name,age,city\nAlice,25,NYC\nBob,30,LA"
lines = csv_data.split('\n')
header = lines[0].split(',')
rows = [line.split(',') for line in lines[1:]]

print(f"Header: {header}")
print(f"Data rows: {rows}")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: String to List
Convert "Programming" to a list of characters.

🎯 EXERCISE 2: Range to List
Convert range(1, 20, 3) to a list.

🎯 EXERCISE 3: Tuple to List
Convert (5, 10, 15, 20) to a list.

🎯 EXERCISE 4: Dict Keys to List
Convert {'a': 1, 'b': 2, 'c': 3} to a list of keys.

🎯 EXERCISE 5: Set to List
Convert {3, 1, 4, 1, 5} to a sorted list.

🎯 CHALLENGE: Combined Conversion
Convert a dictionary's values to a list and sort them.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - String to List:")
print(f"  list('Programming') → {list('Programming')}")

# Exercise 2
print("\nEx2 - Range to List:")
print(f"  list(range(1, 20, 3)) → {list(range(1, 20, 3))}")

# Exercise 3
print("\nEx3 - Tuple to List:")
print(f"  list((5, 10, 15, 20)) → {list((5, 10, 15, 20))}")

# Exercise 4
print("\nEx4 - Dict Keys:")
d = {'a': 1, 'b': 2, 'c': 3}
print(f"  list({'a': 1, 'b': 2, 'c': 3}) → {list(d)}")

# Exercise 5
print("\nEx5 - Set to Sorted List:")
s = {3, 1, 4, 1, 5}
print(f"  sorted(list({s})) → {sorted(list(s))}")

# Challenge
print("\nChallenge - Dict Values:")
data = {'Math': 85, 'Science': 92, 'English': 78}
values = list(data.values())
sorted_values = sorted(values)
print(f"  Values: {values}")
print(f"  Sorted: {sorted_values}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ list() CONSTRUCTOR MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    list() CONVERSIONS                       │
├─────────────────────────────────────────────────────────────┤
│  list()                → [] (empty list)                   │
│  list("abc")           → ['a','b','c']                    │
│  list((1,2,3))         → [1, 2, 3]                        │
│  list(range(5))        → [0, 1, 2, 3, 4]                  │
│  list({'a':1, 'b':2})  → ['a', 'b'] (keys)               │
│  list({1,2,3})         → [1, 2, 3] (order may vary)      │
│  list(dict.values())   → [1, 2, 3] (values)               │
│  list(dict.items())    → [('a',1), ('b',2)]               │
├─────────────────────────────────────────────────────────────┤
│                    WHEN TO USE                              │
├─────────────────────────────────────────────────────────────┤
│  ✅ Use list() for:                                        │
│     - Converting iterables to lists                       │
│     - Creating lists from range()                         │
│     - When you need a list from any iterable              │
│                                                             │
│  ✅ Use [] for:                                             │
│     - Creating empty lists                                 │
│     - Creating lists with known values                    │
│     - Best performance                                     │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python List Methods - Complete Guide
""")