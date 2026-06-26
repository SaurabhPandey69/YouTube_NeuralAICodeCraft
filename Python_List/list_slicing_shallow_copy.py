"""
PYTHON LIST SLICING & SHALLOW COPY - COMPLETE GUIDE
NeuralAICodeCraft - Understanding Shallow vs Deep Copy

Topics Covered:
1. Slicing Basics
2. Slicing Creates a New List
3. Shallow Copy Explained
4. Slicing vs copy() vs list()
5. Nested List Pitfalls
6. Deep Copy Solution
"""

import copy

print("=" * 70)
print("🐍 LIST SLICING & SHALLOW COPY - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: SLICING BASICS
# ============================================

print("\n📚 PART 1: SLICING BASICS")
print("-" * 50)

print("""
SYNTAX: list[start:end:step]

WHAT IT DOES:
- Extracts a portion of the list
- Returns a NEW list
- Original list remains unchanged
- Creates a SHALLOW COPY
""")

# 1.1 Basic Slicing
print("\n1.1 Basic Slicing:")
print("-" * 30)

original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {original}")

# Different slices
print(f"\noriginal[2:7]  → {original[2:7]}")    # [2, 3, 4, 5, 6]
print(f"original[:5]   → {original[:5]}")       # [0, 1, 2, 3, 4]
print(f"original[5:]   → {original[5:]}")       # [5, 6, 7, 8, 9]
print(f"original[::2]  → {original[::2]}")      # [0, 2, 4, 6, 8]
print(f"original[::-1] → {original[::-1]}")     # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print(f"\nOriginal unchanged: {original}")

# 1.2 Slicing Creates a New Object
print("\n1.2 Slicing Creates a NEW Object:")
print("-" * 30)

my_list = [1, 2, 3, 4, 5]
sliced = my_list[1:4]

print(f"Original: {my_list}")
print(f"Sliced: {sliced}")
print(f"Same object? {my_list is sliced}")  # False
print(f"ID of original: {id(my_list)}")
print(f"ID of sliced: {id(sliced)}")

# ============================================
# PART 2: SLICING = SHALLOW COPY
# ============================================

print("\n🔍 PART 2: SLICING CREATES A SHALLOW COPY")
print("-" * 50)

print("""
SHALLOW COPY:
- Creates a NEW list object
- Copies REFERENCES to the original elements
- Does NOT copy nested objects
- Nested objects are SHARED
""")

# 2.1 Simple List - Shallow Copy
print("\n2.1 Simple List (No Nested Objects):")
print("-" * 30)

original = [1, 2, 3, 4, 5]
sliced = original[:]  # Creates a shallow copy

print(f"Original: {original}")
print(f"Sliced: {sliced}")
print(f"Same object? {original is sliced}")  # False

print("\nModifying the sliced copy:")
sliced[0] = 99
sliced[1] = 88

print(f"Original: {original}")  # Unchanged!
print(f"Sliced: {sliced}")      # Changed!

print("\n✅ For simple lists, slicing creates an independent copy.")

# 2.2 Visual Representation
print("\n2.2 Visual Representation of Shallow Copy:")
print("-" * 30)

print("""
┌─────────────────────────────────────────────────────────────┐
│                    SHALLOW COPY                             │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  original = [1, 2, 3, 4, 5]                               │
│               │  │  │  │  │                                │
│               ▼  ▼  ▼  ▼  ▼                                │
│             [1] [2] [3] [4] [5]                           │
│               ▲  ▲  ▲  ▲  ▲                                │
│               │  │  │  │  │                                │
│  sliced = original[:]                                    │
│                                                             │
│  Different list, but elements point to the SAME objects!   │
└─────────────────────────────────────────────────────────────┘
""")

# ============================================
# PART 3: NESTED LISTS - THE PITFALL
# ============================================

print("\n⚠️ PART 3: NESTED LISTS - THE PITFALL")
print("-" * 50)

print("""
CRITICAL INSIGHT:
- Slicing copies REFERENCES to nested objects
- Nested lists are SHARED between original and copy
- Modifying nested list affects BOTH!
""")

# 3.1 Nested List Demonstration
print("\n3.1 Nested List Demonstration:")
print("-" * 30)

original_nested = [1, 2, [3, 4, 5], 6]
sliced_nested = original_nested[:]  # Shallow copy

print(f"Original: {original_nested}")
print(f"Sliced: {sliced_nested}")
print(f"Same object? {original_nested is sliced_nested}")  # False

# Check nested list object IDs
print(f"\nNested list ID (original): {id(original_nested[2])}")
print(f"Nested list ID (sliced): {id(sliced_nested[2])}")
print(f"Same nested object? {original_nested[2] is sliced_nested[2]}")  # True!

# 3.2 Modifying Nested List
print("\n3.2 Modifying Nested List:")
print("-" * 30)

print("Modifying nested list in the slice...")
sliced_nested[2][0] = 99
sliced_nested[2][1] = 88

print(f"Original: {original_nested}")  # ALSO changed!
print(f"Sliced: {sliced_nested}")      # Changed!

print("\n⚠️ WARNING: The nested list is SHARED!")
print("  Changes to nested objects affect BOTH lists.")

# 3.3 Visual Representation
print("\n3.3 Visual Representation of Nested List Sharing:")
print("-" * 30)

print("""
┌─────────────────────────────────────────────────────────────┐
│              SHALLOW COPY WITH NESTED LIST                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  original = [1, 2, [3, 4, 5], 6]                          │
│               │  │    ▲       │                             │
│               ▼  ▼    │       ▼                             │
│             [1] [2]  [3,4,5]  [6]                          │
│               ▲  ▲    ▲       ▲                             │
│               │  │    │       │                             │
│  sliced = original[:]                                     │
│                                                             │
│  Nested list is SHARED between both lists!                 │
└─────────────────────────────────────────────────────────────┘
""")

# ============================================
# PART 4: SLICING vs copy() vs list()
# ============================================

print("\n⚖️ PART 4: SLICING vs copy() vs list()")
print("-" * 50)

print("""
ALL THREE create SHALLOW copies:
1. slicing: my_list[:]
2. copy(): my_list.copy()
3. constructor: list(my_list)

They all behave the SAME way with nested lists.
""")

# 4.1 Comparison
print("\n4.1 Comparison of Copy Methods:")
print("-" * 30)

original = [1, 2, [3, 4]]

# Method 1: Slicing
slice_copy = original[:]

# Method 2: copy()
method_copy = original.copy()

# Method 3: list()
list_copy = list(original)

print(f"Original: {original}")
print(f"Slice copy: {slice_copy}")
print(f"copy() copy: {method_copy}")
print(f"list() copy: {list_copy}")

print("\nAll three create SHALLOW copies!")
print(f"Original nested ID: {id(original[2])}")
print(f"Slice nested ID: {id(slice_copy[2])}")
print(f"copy() nested ID: {id(method_copy[2])}")
print(f"list() nested ID: {id(list_copy[2])}")
print(f"All share the SAME nested object?")

# 4.2 Modifying All Copies
print("\n4.2 Modifying Nested in All Copies:")
print("-" * 30)

original = [1, 2, [3, 4]]
slice_copy = original[:]
method_copy = original.copy()
list_copy = list(original)

slice_copy[2][0] = 99
method_copy[2][1] = 88
list_copy[2][0] = 77

print(f"Original: {original}")  # All changes reflected!
print(f"Slice copy: {slice_copy}")
print(f"copy() copy: {method_copy}")
print(f"list() copy: {list_copy}")

# ============================================
# PART 5: DEEP COPY SOLUTION
# ============================================

print("\n🔬 PART 5: DEEP COPY SOLUTION")
print("-" * 50)

print("""
DEEP COPY:
- Creates a COMPLETE independent copy
- Recursively copies ALL nested objects
- No sharing between original and copy
- Use: copy.deepcopy()
""")

# 5.1 Deep Copy Demonstration
print("\n5.1 Deep Copy Demonstration:")
print("-" * 30)

import copy

original_deep = [1, 2, [3, 4, 5], 6]
deep_copy = copy.deepcopy(original_deep)

print(f"Original: {original_deep}")
print(f"Deep copy: {deep_copy}")

# Check nested list IDs
print(f"\nNested list ID (original): {id(original_deep[2])}")
print(f"Nested list ID (deep copy): {id(deep_copy[2])}")
print(f"Same object? {original_deep[2] is deep_copy[2]}")  # False!

# 5.2 Modifying Deep Copy
print("\n5.2 Modifying Deep Copy:")
print("-" * 30)

deep_copy[2][0] = 99
deep_copy[2][1] = 88

print(f"Original: {original_deep}")  # Unchanged!
print(f"Deep copy: {deep_copy}")     # Changed!

print("\n✅ Deep copy is COMPLETELY independent!")

# ============================================
# PART 6: SHALLOW vs DEEP COPY - SUMMARY
# ============================================

print("\n📊 PART 6: SHALLOW vs DEEP COPY - SUMMARY")
print("-" * 50)

# 6.1 Comparison Table
print("\n6.1 Comparison Table:")
print("-" * 30)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  SHALLOW COPY       │  DEEP COPY           │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Creates        │  New top-level list │  New top-level list  │
│  Nested objects │  SHARED             │  NEW (recursive)     │
│  Performance    │  Fast               │  Slower              │
│  Memory         │  Less               │  More                │
│  Independent    │  Partially          │  COMPLETELY          │
│  Methods        │  slicing, copy()    │  copy.deepcopy()     │
│  Use when       │  Simple lists       │  Nested structures   │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 6.2 When to Use Each
print("\n6.2 When to Use Each:")
print("-" * 30)

print("""
USE SHALLOW COPY (slicing, copy(), list()) when:
├── List contains only IMMUTABLE objects (int, str, tuple)
├── You want a new list but don't need to modify nested objects
├── Performance matters (shallow copy is faster)
└── You need multiple independent views of the same data

USE DEEP COPY (copy.deepcopy()) when:
├── List contains MUTABLE nested objects (lists, dicts, sets)
├── You need to modify nested objects independently
├── You want complete isolation from the original
└── Working with complex nested structures
""")

# ============================================
# PART 7: PRACTICAL EXAMPLES
# ============================================

print("\n🚀 PART 7: PRACTICAL EXAMPLES")
print("-" * 30)

# 7.1 Safe Function with Slicing
print("\n7.1 Safe Function (Using Slicing):")
print("-" * 30)

def safe_process(data):
    """Process data without modifying original"""
    # Create a slice to avoid modifying original
    working_copy = data[:]
    
    # Modify the copy
    for i in range(len(working_copy)):
        if isinstance(working_copy[i], int):
            working_copy[i] *= 2
    
    return working_copy

original = [1, 2, 3, 4, 5]
result = safe_process(original)

print(f"Original: {original}")  # Unchanged!
print(f"Result: {result}")

# 7.2 Matrix Operations
print("\n7.2 Matrix Operations:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Shallow copy of matrix (shares rows!)
shallow_matrix = matrix[:]

# Deep copy of matrix
deep_matrix = copy.deepcopy(matrix)

# Modify shallow copy
shallow_matrix[0][0] = 99
print(f"Original matrix: {matrix[0]}")    # Changed! (shallow copy shared)
print(f"Shallow copy: {shallow_matrix[0]}")  # Changed!
print(f"Deep copy: {deep_matrix[0]}")        # Unchanged!

print("\n💡 For matrices, use deepcopy() to create independent copies!")

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Slice Copy
Create a slice of [1, 2, 3, 4, 5] and verify it's a new object.

🎯 EXERCISE 2: Nested List Copy
Slice a list with nested list [1, [2, 3], 4] and modify nested.

🎯 EXERCISE 3: copy() vs deepcopy()
Compare behavior of copy() and deepcopy() with nested lists.

🎯 EXERCISE 4: Matrix Copy
Create a 3x3 matrix and copy it using different methods.

🎯 CHALLENGE: Safe Function
Write a function that removes an element from a list without modifying original.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Slice Copy:")
lst = [1, 2, 3, 4, 5]
sliced = lst[:]
print(f"  Original: {lst}, Sliced: {sliced}")
print(f"  Same object? {lst is sliced}")  # False

# Exercise 2
print("\nEx2 - Nested List Copy:")
lst = [1, [2, 3], 4]
sliced = lst[:]
sliced[1][0] = 99
print(f"  Original: {lst}")    # Changed!
print(f"  Sliced: {sliced}")

# Exercise 3
print("\nEx3 - copy() vs deepcopy():")
lst = [1, [2, 3], 4]
shallow = lst.copy()
deep = copy.deepcopy(lst)
shallow[1][0] = 99
deep[1][1] = 88
print(f"  Original: {lst}")    # Changed by shallow
print(f"  Shallow: {shallow}")
print(f"  Deep: {deep}")

# Exercise 4
print("\nEx4 - Matrix Copy:")
matrix = [[1, 2], [3, 4]]
shallow_matrix = matrix[:]
deep_matrix = copy.deepcopy(matrix)
shallow_matrix[0][0] = 99
print(f"  Original: {matrix[0]}")
print(f"  Shallow: {shallow_matrix[0]}")
print(f"  Deep: {deep_matrix[0]}")

# Challenge
print("\nChallenge - Safe Function:")
def remove_safe(lst, index):
    """Remove element without modifying original"""
    copy = lst[:]
    copy.pop(index)
    return copy

original = [1, 2, 3, 4, 5]
result = remove_safe(original, 2)
print(f"  Original: {original}")
print(f"  Result: {result}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST SLICING & SHALLOW COPY MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    SLICING SYNTAX                           │
├─────────────────────────────────────────────────────────────┤
│  list[start:end]     → Elements from start to end-1        │
│  list[:]             → SHALLOW COPY of entire list         │
│  list[::2]           → Every second element                │
│  list[::-1]          → Reverse list                        │
├─────────────────────────────────────────────────────────────┤
│                    SHALLOW COPY METHODS                     │
├─────────────────────────────────────────────────────────────┤
│  new = old[:]        → Slicing                             │
│  new = old.copy()    → copy() method                      │
│  new = list(old)     → Constructor                         │
│  new = copy.copy(old)→ copy module                        │
├─────────────────────────────────────────────────────────────┤
│                    DEEP COPY                                │
├─────────────────────────────────────────────────────────────┤
│  new = copy.deepcopy(old) → Complete independent copy      │
├─────────────────────────────────────────────────────────────┤
│                    KEY RULES                                │
├─────────────────────────────────────────────────────────────┤
│  ✅ Slicing creates a SHALLOW copy                         │
│  ✅ New list object is created                             │
│  ✅ Nested objects are SHARED                             │
│  ✅ Modifying nested affects BOTH                         │
│  ✅ Use deepcopy() for complete independence              │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python List Comprehensions - Complete Guide
""")