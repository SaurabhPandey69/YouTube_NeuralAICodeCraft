"""
PYTHON DICTIONARIES, SETS & BINARY TYPES
NeuralAICodeCraft - Complete Guide with Examples

Topics Covered:
1. Dictionaries (Mapping Type)
2. Sets & Frozenset (Set Types)
3. Boolean Type
4. Binary Types (Bytes, Bytearray, Memoryview)
"""

print("=" * 70)
print("🐍 PYTHON DICTIONARIES, SETS & BINARY TYPES")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: DICTIONARIES (Mapping Type)
# ============================================

print("\n📖 PART 1: DICTIONARIES - KEY-VALUE MAPPINGS")
print("-" * 50)

# 1.1 Creating Dictionaries
print("\n1.1 Creating Dictionaries:")
print("-" * 30)

# Different ways to create dicts
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
dict_constructor = dict(name="Bob", age=25, city="Los Angeles")
list_of_tuples = dict([("a", 1), ("b", 2), ("c", 3)])
dict_comprehension = {x: x**2 for x in range(5)}

print(f"  Empty dict: {empty_dict}")
print(f"  Person dict: {person}")
print(f"  Dict constructor: {dict_constructor}")
print(f"  From list of tuples: {list_of_tuples}")
print(f"  Dict comprehension: {dict_comprehension}")

# Mixed key types
mixed_dict = {
    "name": "John",
    1: "one",
    (1, 2): "tuple key",
    True: "boolean key"
}
print(f"  Mixed keys dict: {mixed_dict}")

# 1.2 Accessing and Modifying
print("\n1.2 Accessing and Modifying:")
print("-" * 30)

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"  Original: {person}")

# Access by key
print(f"  person['name']: {person['name']}")
print(f"  person.get('age'): {person.get('age')}")
print(f"  person.get('country', 'USA'): {person.get('country', 'USA')}")

# Adding new key-value
person["email"] = "alice@example.com"
print(f"  After adding email: {person}")

# Updating existing
person["age"] = 31
print(f"  After updating age: {person}")

# Update multiple values
person.update({"city": "San Francisco", "profession": "Engineer"})
print(f"  After update: {person}")

# 1.3 Dictionary Methods
print("\n1.3 Dictionary Methods:")
print("-" * 30)

sample = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1}
print(f"  Sample dict: {sample}")

# Keys, values, items
print(f"  keys(): {list(sample.keys())}")
print(f"  values(): {list(sample.values())}")
print(f"  items(): {list(sample.items())}")

# Get method (safe access)
print(f"  get('c'): {sample.get('c')}")
print(f"  get('z', 'Not Found'): {sample.get('z', 'Not Found')}")

# Pop and Popitem
popped_value = sample.pop('d')
print(f"  pop('d'): {popped_value}, dict now: {sample}")

popped_item = sample.popitem()
print(f"  popitem(): {popped_item}, dict now: {sample}")

# Update
sample.update({'f': 6, 'g': 7})
print(f"  update(): {sample}")

# Setdefault
value = sample.setdefault('h', 8)
print(f"  setdefault('h', 8): {value}, dict: {sample}")

# Copy
sample_copy = sample.copy()
print(f"  copy(): {sample_copy}")

# Clear
sample_copy.clear()
print(f"  clear(): {sample_copy}")

# 1.4 Dictionary Iteration
print("\n1.4 Dictionary Iteration:")
print("-" * 30)

scores = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 98}

print("  Iterating over keys:")
for key in scores:
    print(f"    {key}")

print("  Iterating over values:")
for value in scores.values():
    print(f"    {value}")

print("  Iterating over key-value pairs:")
for key, value in scores.items():
    print(f"    {key}: {value}")

# 1.5 Dictionary Comprehensions
print("\n1.5 Dictionary Comprehensions:")
print("-" * 30)

# Square numbers
squares = {x: x**2 for x in range(1, 6)}
print(f"  Squares: {squares}")

# Filter even numbers
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"  Even squares: {even_squares}")

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(f"  Original: {original}")
print(f"  Swapped: {swapped}")

# 1.6 Nested Dictionaries
print("\n1.6 Nested Dictionaries:")
print("-" * 30)

students = {
    "Alice": {
        "age": 25,
        "major": "Computer Science",
        "grades": [95, 88, 92]
    },
    "Bob": {
        "age": 24,
        "major": "Mathematics",
        "grades": [87, 91, 85]
    }
}

print(f"  Students dict: {students}")
print(f"  Alice's major: {students['Alice']['major']}")
print(f"  Bob's grades: {students['Bob']['grades']}")

# 1.7 Specialized Dictionaries
print("\n1.7 Specialized Dictionaries (collections module):")
print("-" * 30)

from collections import defaultdict, OrderedDict, Counter

# defaultdict
dd = defaultdict(int)
dd['a'] += 1
dd['b'] += 2
print(f"  defaultdict: {dd}")
print(f"  Missing key 'c': {dd['c']} (auto-initialized to 0)")

# OrderedDict (maintains insertion order - Python 3.7+ dicts do this by default)
od = OrderedDict()
od['first'] = 1
od['second'] = 2
od['third'] = 3
print(f"  OrderedDict: {od}")

# Counter
word_counter = Counter("hello world")
print(f"  Counter from string: {word_counter}")
print(f"  Most common: {word_counter.most_common(2)}")

# ============================================
# PART 2: SETS & FROZENSET
# ============================================

print("\n🎯 PART 2: SETS & FROZENSET - UNIQUE ELEMENTS")
print("-" * 50)

# 2.1 Creating Sets
print("\n2.1 Creating Sets:")
print("-" * 30)

empty_set = set()  # NOT {} (that's empty dict)
numbers = {1, 2, 3, 4, 5}
mixed = {1, "hello", 3.14, True}
set_from_list = set([1, 2, 2, 3, 3, 4])
set_comprehension = {x**2 for x in range(5)}

print(f"  Empty set: {empty_set}")
print(f"  Numbers set: {numbers}")
print(f"  Mixed set: {mixed}")
print(f"  Set from list (duplicates removed): {set_from_list}")
print(f"  Set comprehension: {set_comprehension}")

# 2.2 Set Properties (Uniqueness)
print("\n2.2 Set Properties (Automatic Uniqueness):")
print("-" * 30)

duplicates = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_set = set(duplicates)
print(f"  Original list with duplicates: {duplicates}")
print(f"  Set (duplicates removed): {unique_set}")
print(f"  Back to list: {list(unique_set)}")

# 2.3 Adding and Removing Elements
print("\n2.3 Adding and Removing Elements:")
print("-" * 30)

fruits = {"apple", "banana", "cherry"}
print(f"  Original set: {fruits}")

# Add
fruits.add("date")
print(f"  After add('date'): {fruits}")

# Update (add multiple)
fruits.update(["elderberry", "fig", "grape"])
print(f"  After update(): {fruits}")

# Remove (raises error if not found)
fruits.remove("banana")
print(f"  After remove('banana'): {fruits}")

# Discard (no error if not found)
fruits.discard("nonexistent")
print(f"  After discard('nonexistent'): {fruits}")

# Pop (removes arbitrary element)
popped = fruits.pop()
print(f"  Popped element: {popped}")
print(f"  After pop(): {fruits}")

# Clear
fruits.clear()
print(f"  After clear(): {fruits}")

# 2.4 Set Operations
print("\n2.4 Set Operations:")
print("-" * 30)

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"  Set A: {set_a}")
print(f"  Set B: {set_b}")

# Union (all elements from both)
union = set_a.union(set_b)
union_alt = set_a | set_b
print(f"  Union (A ∪ B): {union}")

# Intersection (common elements)
intersection = set_a.intersection(set_b)
intersection_alt = set_a & set_b
print(f"  Intersection (A ∩ B): {intersection}")

# Difference (elements in A but not in B)
difference = set_a.difference(set_b)
difference_alt = set_a - set_b
print(f"  Difference (A - B): {difference}")

# Symmetric Difference (elements in either, but not both)
sym_diff = set_a.symmetric_difference(set_b)
sym_diff_alt = set_a ^ set_b
print(f"  Symmetric Difference (A △ B): {sym_diff}")

# Subset and Superset
set_c = {1, 2, 3}
print(f"  Is {set_c} subset of {set_a}? {set_c.issubset(set_a)}")
print(f"  Is {set_a} superset of {set_c}? {set_a.issuperset(set_c)}")
print(f"  Are {set_a} and {set_b} disjoint? {set_a.isdisjoint(set_b)}")

# 2.5 Set Comprehensions
print("\n2.5 Set Comprehensions:")
print("-" * 30)

# Squares
squares_set = {x**2 for x in range(10)}
print(f"  Squares: {squares_set}")

# Even numbers
evens_set = {x for x in range(20) if x % 2 == 0}
print(f"  Evens: {evens_set}")

# Unique characters
text = "hello world"
unique_chars = {char for char in text if char != ' '}
print(f"  Unique chars in '{text}': {unique_chars}")

# 2.6 Frozenset (Immutable Set)
print("\n2.6 Frozenset (Immutable Version):")
print("-" * 30)

normal_set = {1, 2, 3}
frozen = frozenset([1, 2, 3, 3, 4, 4])

print(f"  Normal set: {normal_set}")
print(f"  Frozenset: {frozen}")

# Frozenset can be used as dictionary key
locations = {
    frozenset(["NY", "NJ"]): "Northeast",
    frozenset(["CA", "NV"]): "West Coast"
}
print(f"  Frozenset as dict key: {locations}")

# Trying to modify frozenset (will raise error)
try:
    frozen.add(5)
except AttributeError as e:
    print(f"  ❌ Cannot modify frozenset: {e}")

# 2.7 Practical Set Examples
print("\n2.7 Practical Examples:")
print("-" * 30)

# Finding common friends
user1_friends = {"Alice", "Bob", "Charlie", "David"}
user2_friends = {"Charlie", "David", "Eve", "Frank"}

common_friends = user1_friends & user2_friends
all_friends = user1_friends | user2_friends
unique_to_user1 = user1_friends - user2_friends

print(f"  User 1 friends: {user1_friends}")
print(f"  User 2 friends: {user2_friends}")
print(f"  Common friends: {common_friends}")
print(f"  All friends (unique): {all_friends}")
print(f"  Unique to User 1: {unique_to_user1}")

# ============================================
# PART 3: BOOLEAN TYPE
# ============================================

print("\n🔘 PART 3: BOOLEAN TYPE")
print("-" * 50)

# 3.1 Boolean Values
print("\n3.1 Boolean Values:")
print("-" * 30)

is_true = True
is_false = False

print(f"  True: {is_true}, type: {type(is_true)}")
print(f"  False: {is_false}, type: {type(is_false)}")

# Boolean operations
print(f"  True and True: {True and True}")
print(f"  True and False: {True and False}")
print(f"  True or False: {True or False}")
print(f"  not True: {not True}")
print(f"  not False: {not False}")

# 3.2 Truthy and Falsy Values
print("\n3.2 Truthy and Falsy Values:")
print("-" * 30)

falsy_values = [
    None, False, 0, 0.0, 0j,
    "", [], (), {}, set(), range(0)
]

print("  Falsy values (evaluate to False):")
for value in falsy_values:
    print(f"    bool({value}) = {bool(value)}")

truthy_values = [
    True, 1, -1, 1.5, "Hello", [1, 2], (1,), {"a": 1}, {1, 2}
]

print("\n  Truthy values (evaluate to True):")
for value in truthy_values:
    print(f"    bool({value}) = {bool(value)}")

# 3.3 Boolean in Conditions
print("\n3.3 Boolean in Conditions:")
print("-" * 30)

def check_value(value):
    if value:
        print(f"  '{value}' is TRUTHY")
    else:
        print(f"  '{value}' is FALSY")

check_value("Python")
check_value("")
check_value([1, 2, 3])
check_value([])
check_value(42)
check_value(0)

# 3.4 Boolean Functions
print("\n3.4 Boolean Functions:")
print("-" * 30)

# all() - returns True if all elements are truthy
print(f"  all([True, True, True]): {all([True, True, True])}")
print(f"  all([True, False, True]): {all([True, False, True])}")
print(f"  all([1, 2, 3]): {all([1, 2, 3])}")
print(f"  all([1, 0, 3]): {all([1, 0, 3])}")

# any() - returns True if any element is truthy
print(f"  any([False, False, False]): {any([False, False, False])}")
print(f"  any([False, True, False]): {any([False, True, False])}")
print(f"  any([0, 0, 0]): {any([0, 0, 0])}")
print(f"  any([0, 1, 0]): {any([0, 1, 0])}")

# ============================================
# PART 4: BINARY TYPES
# ============================================

print("\n💾 PART 4: BINARY TYPES (Bytes, Bytearray, Memoryview)")
print("-" * 50)

# 4.1 Bytes (Immutable)
print("\n4.1 Bytes - Immutable Binary Data:")
print("-" * 30)

# Creating bytes
bytes_literal = b'Hello World'
bytes_from_string = bytes("Python", 'utf-8')
bytes_from_list = bytes([65, 66, 67, 68])  # ASCII values
bytes_from_hex = bytes.fromhex('48656c6c6f')  # Hex to bytes

print(f"  Bytes literal: {bytes_literal}")
print(f"  From string: {bytes_from_string}")
print(f"  From list: {bytes_from_list}")
print(f"  From hex: {bytes_from_hex}")
print(f"  As string: {bytes_from_hex.decode('utf-8')}")

# Bytes operations
print(f"  Length: {len(bytes_literal)}")
print(f"  Index 0: {bytes_literal[0]}")
print(f"  Slice: {bytes_literal[0:5]}")

# 4.2 Bytearray (Mutable)
print("\n4.2 Bytearray - Mutable Binary Data:")
print("-" * 30)

# Creating bytearray
ba = bytearray(b'Hello')
print(f"  Original: {ba}")

# Modify
ba[0] = 74  # 'J' in ASCII
print(f"  After modification: {ba}")

# Append
ba.append(33)  # '!'
print(f"  After append: {ba}")

# Extend
ba.extend(b' World')
print(f"  After extend: {ba}")

# Convert to string
print(f"  As string: {ba.decode('utf-8')}")

# 4.3 Converting Between Types
print("\n4.3 Converting Between Types:")
print("-" * 30)

text = "Python Programming"

# String to bytes
text_bytes = text.encode('utf-8')
print(f"  String to bytes: {text_bytes}")

# Bytes to string
text_back = text_bytes.decode('utf-8')
print(f"  Bytes to string: {text_back}")

# String to bytearray
text_ba = bytearray(text, 'utf-8')
print(f"  String to bytearray: {text_ba}")

# Bytearray to string
text_from_ba = text_ba.decode('utf-8')
print(f"  Bytearray to string: {text_from_ba}")

# 4.4 Memoryview (Memory-efficient slicing)
print("\n4.4 Memoryview - Memory-Efficient Slicing:")
print("-" * 30)

data = bytearray(b'Hello World')
mv = memoryview(data)

print(f"  Original data: {data}")
print(f"  Memoryview: {mv}")
print(f"  Slice without copying: {mv[0:5]}")
print(f"  Memoryview to bytes: {mv.tobytes()}")

# Modify through memoryview
mv[0:5] = b'Jolly'
print(f"  After modification: {data}")

# 4.5 Working with Binary Files
print("\n4.5 Working with Binary Files:")
print("-" * 30)

# Writing binary data
with open('sample_binary.bin', 'wb') as f:
    f.write(b'Binary data written to file')
print("  ✅ Binary file written: 'sample_binary.bin'")

# Reading binary data
with open('sample_binary.bin', 'rb') as f:
    binary_data = f.read()
    print(f"  Read binary data: {binary_data}")
    print(f"  As string: {binary_data.decode('utf-8')}")

# 4.6 Practical Example: Image Processing Simulation
print("\n4.6 Practical Example: Simple Image Processing:")
print("-" * 30)

# Simulate image pixel data (RGB values)
image_data = bytearray([
    255, 0, 0,    # Red pixel
    0, 255, 0,    # Green pixel
    0, 0, 255,    # Blue pixel
    255, 255, 0,  # Yellow pixel
])

print(f"  Original image data (RGB): {list(image_data)}")

# Convert to grayscale simulation
def to_grayscale(pixel):
    """Simulate grayscale conversion"""
    return int(sum(pixel) / 3)

print("  Converting to grayscale...")
for i in range(0, len(image_data), 3):
    rgb = image_data[i:i+3]
    gray = to_grayscale(rgb)
    image_data[i:i+3] = [gray, gray, gray]

print(f"  Grayscale image data: {list(image_data)}")

# ============================================
# PART 5: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 5: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Word Frequency Counter
Write a function that takes a sentence and returns a dictionary with word frequencies.

Solution:
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

🎯 EXERCISE 2: Find Common Elements
Write a function that takes two lists and returns their common elements using sets.

Solution:
def find_common(list1, list2):
    return list(set(list1) & set(list2))

🎯 EXERCISE 3: Dictionary Merge
Write a function that merges two dictionaries (second overwrites first).

Solution:
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

🎯 EXERCISE 4: Remove Duplicates
Write a function that removes duplicates from a list while preserving order.

Solution:
def remove_duplicates_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

🎯 EXERCISE 5: Bytes to Hex Converter
Write a function that converts bytes to hex string.

Solution:
def bytes_to_hex(b):
    return b.hex()

🎯 CHALLENGE: URL Query Parser
Parse a URL query string into a dictionary.
Example: "name=John&age=25&city=NYC" → {'name': 'John', 'age': '25', 'city': 'NYC'}
""")

# Exercise Solutions
print("\n💡 SOLUTIONS:")
print("-" * 30)

# Exercise 1
def word_frequency(sentence):
    words = sentence.lower().split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(f"  Ex1 - Word frequency: {word_frequency('hello world hello python world')}")

# Exercise 2
def find_common(list1, list2):
    return list(set(list1) & set(list2))

print(f"  Ex2 - Common elements: {find_common([1,2,3,4], [3,4,5,6])}")

# Exercise 3
def merge_dicts(dict1, dict2):
    return {**dict1, **dict2}

print(f"  Ex3 - Merged dicts: {merge_dicts({'a':1, 'b':2}, {'b':3, 'c':4})}")

# Exercise 4
def remove_duplicates_preserve_order(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print(f"  Ex4 - Remove duplicates: {remove_duplicates_preserve_order([1,2,2,3,3,3,4])}")

# Exercise 5
def bytes_to_hex(b):
    return b.hex()

print(f"  Ex5 - Bytes to hex: {bytes_to_hex(b'Hello')}")

# Challenge
def parse_query_string(query):
    """Parse URL query string into dictionary"""
    params = {}
    if query:
        for pair in query.split('&'):
            if '=' in pair:
                key, value = pair.split('=', 1)
                params[key] = value
    return params

print(f"  Challenge - Query parser: {parse_query_string('name=John&age=25&city=NYC')}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ DICTIONARIES, SETS & BINARY TYPES MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    DICTIONARIES                             │
├─────────────────────────────────────────────────────────────┤
│ {key: value}              → Create dictionary               │
│ dict[key]                 → Access value                    │
│ dict.get(key, default)    → Safe access                     │
│ dict.keys(), values()     → Get keys/values                 │
│ dict.items()              → Get key-value pairs             │
│ dict.update(other)        → Merge dictionaries              │
│ {k:v for k,v in iterable} → Dict comprehension             │
├─────────────────────────────────────────────────────────────┤
│                        SETS                                 │
├─────────────────────────────────────────────────────────────┤
│ {1,2,3}                   → Create set                      │
│ set.add(x)                → Add element                     │
│ set.remove(x)             → Remove element (error if missing)│
│ set.discard(x)            → Remove element (no error)       │
│ set1 | set2               → Union                           │
│ set1 & set2               → Intersection                    │
│ set1 - set2               → Difference                      │
│ set1 ^ set2               → Symmetric difference            │
├─────────────────────────────────────────────────────────────┤
│                     BINARY TYPES                            │
├─────────────────────────────────────────────────────────────┤
│ b'text'                   → Bytes literal                   │
│ bytes([65,66,67])         → Create bytes from list          │
│ bytearray(b'text')        → Mutable bytearray               │
│ text.encode('utf-8')      → String to bytes                 │
│ bytes.decode('utf-8')     → Bytes to string                 │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Input and Output Functions (print() and input())
""")

# Clean up binary file
import os
if os.path.exists('sample_binary.bin'):
    os.remove('sample_binary.bin')
    print("\n🧹 Cleaned up temporary binary file.")
    