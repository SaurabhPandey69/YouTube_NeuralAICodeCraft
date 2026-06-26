"""
PYTHON COPY() METHOD - COMPLETE GUIDE
NeuralAICodeCraft - The Right Way to Copy Lists

Topics Covered:
1. The Aliasing Problem (Assignment doesn't copy)
2. The copy() Method
3. Shallow Copy Explained
4. Alternative Methods (Slicing, Constructor)
5. copy() vs deepcopy()
"""

import copy

print("=" * 70)
print("🐍 PYTHON COPY() METHOD - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: THE ALIASING PROBLEM
# ============================================

print("\n📚 PART 1: THE ALIASING PROBLEM")
print("-" * 50)

print("""
When you assign one list to another using =, you don't create a copy.
Both variables reference the SAME list object. [citation:1][citation:2]

This is called ALIASING - two names for the same object.
""")

# 1.1 Demonstrating Aliasing
print("\n1.1 Aliasing Demonstration:")
print("-" * 30)

original = [1, 2, 3]
aliased = original  # This creates an alias, not a copy! [citation:2]

print(f"Original list: {original}")
print(f"Aliased list: {aliased}")
print(f"Same object? {original is aliased}")  # True!
print(f"ID of original: {id(original)}")
print(f"ID of aliased: {id(aliased)}")

# 1.2 Modifying the Aliased List
print("\n1.2 Modifying the Aliased List:")
print("-" * 30)

print("Now modifying aliased list...")
aliased.append(4)
aliased[0] = 99

print(f"Original list: {original}")  # ALSO changed! [citation:2]
print(f"Aliased list: {aliased}")

print("\n⚠️ WARNING: Changes to one affect the other because they're the SAME object!")
print("  This is called a SIDE EFFECT and often leads to bugs.")

# ============================================
# PART 2: THE copy() METHOD
# ============================================

print("\n📋 PART 2: THE copy() METHOD")
print("-" * 50)

print("""
SYNTAX: new_list = old_list.copy()

WHAT IT DOES:
- Creates a SHALLOW copy of the list [citation:1][citation:6]
- New list object with same elements [citation:1]
- Original list remains unchanged
- Also called a 'shallow copy' [citation:8]
""")

# 2.1 Basic copy()
print("\n2.1 Basic copy() Demonstration:")
print("-" * 30)

original = [1, 2, 3]
copied = original.copy()  # Creates a true copy [citation:1]

print(f"Original list: {original}")
print(f"Copied list: {copied}")
print(f"Same object? {original is copied}")  # False! Different objects

# 2.2 Modifying Copied List
print("\n2.2 Modifying the Copied List:")
print("-" * 30)

copied.append(4)
copied[0] = 99

print(f"Original list: {original}")  # Unchanged! [citation:1]
print(f"Copied list: {copied}")

print("\n✅ The copy() method creates an INDEPENDENT copy!")
print("  Changes to the copy don't affect the original.")

# 2.3 Copying Mixed Lists
print("\n2.3 Copying a Mixed List:")
print("-" * 30)

mixed = ['apple', 42, 3.14, True]
mixed_copy = mixed.copy()

print(f"Original mixed: {mixed}")
print(f"Copied mixed: {mixed_copy}")

# ============================================
# PART 3: SHALLOW COPY EXPLAINED
# ============================================

print("\n🔍 PART 3: SHALLOW COPY EXPLAINED")
print("-" * 50)

print("""
SHALLOW COPY creates a new list, but...
- Copies REFERENCES to the objects inside [citation:6][citation:8]
- Does NOT copy nested objects [citation:8][citation:11]
- Nested objects are SHARED between original and copy [citation:11]
""")

# 3.1 Shallow Copy with Nested List
print("\n3.1 Shallow Copy with Nested List:")
print("-" * 30)

original_nested = [1, 2, [3, 4, 5], 6]
copied_nested = original_nested.copy()

print(f"Original nested list: {original_nested}")
print(f"Copied nested list: {copied_nested}")

# Check nested list memory addresses
print(f"\nID of inner list in original: {id(original_nested[2])}")
print(f"ID of inner list in copy: {id(copied_nested[2])}")
print(f"Same inner list object? {original_nested[2] is copied_nested[2]}")  # True! [citation:8]

# 3.2 Modifying Nested List
print("\n3.2 Modifying Nested List in Copy:")
print("-" * 30)

print("Now modifying the nested list in the copy...")
copied_nested[2][0] = 99  # Modify nested list

print(f"Original nested list: {original_nested}")  # ALSO changed! [citation:8]
print(f"Copied nested list: {copied_nested}")

print("\n⚠️ IMPORTANT: copy() is SHALLOW!")
print("  Top-level elements are independent, but nested objects are SHARED.")

# 3.3 Adding vs Modifying
print("\n3.3 Adding vs Modifying - Important Difference:")
print("-" * 30)

# Adding to top level (independent)
original_nested.append(100)
print(f"Original after append: {original_nested}")
print(f"Copy after append: {copied_nested}")  # Unchanged!

# Modifying nested list (shared)
copied_nested[2][1] = 88
print(f"\nAfter modifying nested in copy:")
print(f"Original: {original_nested}")  # Changed!
print(f"Copy: {copied_nested}")  # Changed!

# ============================================
# PART 4: ALTERNATIVE COPYING METHODS
# ============================================

print("\n🔄 PART 4: ALTERNATIVE COPYING METHODS")
print("-" * 50)

print("""
There are multiple ways to copy lists:

1. copy() method → list.copy()
2. Slicing → list[:] [citation:1][citation:8]
3. Constructor → list(list) [citation:3][citation:12]
4. copy module → copy.copy(list) [citation:6]
""")

# 4.1 Slicing Method
print("\n4.1 Slicing Method:")
print("-" * 30)

original = [1, 2, 3]
sliced_copy = original[:]  # Creates shallow copy [citation:1]

print(f"Original: {original}")
print(f"Sliced copy: {sliced_copy}")
print(f"Same object? {original is sliced_copy}")  # False

# 4.2 Constructor Method
print("\n4.2 Constructor Method:")
print("-" * 30)

constructor_copy = list(original)  # Creates shallow copy [citation:3][citation:12]

print(f"Original: {original}")
print(f"Constructor copy: {constructor_copy}")
print(f"Same object? {original is constructor_copy}")  # False

# 4.3 copy.copy() from copy module
print("\n4.3 copy.copy() Method:")
print("-" * 30)

import copy
module_copy = copy.copy(original)  # Creates shallow copy [citation:6][citation:11]

print(f"Original: {original}")
print(f"copy.copy() copy: {module_copy}")
print(f"Same object? {original is module_copy}")  # False

# 4.4 Comparison of Methods
print("\n4.4 Comparison Summary:")
print("-" * 30)

print("""
┌─────────────────┬──────────────┬────────────────────────────┐
│  Method         │  Copy Type   │  Syntax                     │
├─────────────────┼──────────────┼────────────────────────────┤
│  .copy()        │  Shallow     │  new = old.copy()          │
│  Slicing        │  Shallow     │  new = old[:]              │
│  list()         │  Shallow     │  new = list(old)           │
│  copy.copy()    │  Shallow     │  new = copy.copy(old)      │
│  copy.deepcopy()│  Deep        │  new = copy.deepcopy(old)  │
└─────────────────┴──────────────┴────────────────────────────┘
""")

# ============================================
# PART 5: SHALLOW COPY vs DEEP COPY
# ============================================

print("\n🔬 PART 5: SHALLOW COPY vs DEEP COPY")
print("-" * 50)

print("""
SHALLOW COPY → Copies only top-level references
DEEP COPY → Recursively copies ALL nested objects [citation:6][citation:8]
""")

# 5.1 Creating Nested List
print("\n5.1 Creating Nested List:")
print("-" * 30)

nested = [1, [2, 3], [4, [5, 6]]]
print(f"Original nested: {nested}")

# 5.2 Shallow Copy
print("\n5.2 Shallow Copy:")
print("-" * 30)

shallow = nested.copy()
print(f"Shallow copy: {shallow}")
print(f"Same nested object? {nested[1] is shallow[1]}")  # True - shared!

# 5.3 Deep Copy
print("\n5.3 Deep Copy:")
print("-" * 30)

deep = copy.deepcopy(nested)
print(f"Deep copy: {deep}")
print(f"Same nested object? {nested[1] is deep[1]}")  # False - independent! [citation:8]

# 5.4 Modifying Deep Copy
print("\n5.4 Modifying Deep Copy:")
print("-" * 30)

nested[1][0] = 999  # Modify original
shallow[1][1] = 888  # Modify shallow
deep[2][0] = 777  # Modify deep

print(f"Original: {nested}")
print(f"Shallow copy: {shallow}")  # Shared nested changed!
print(f"Deep copy: {deep}")  # Independent! [citation:8]

print("\n📌 DEEP COPY creates a COMPLETELY independent copy!")

# ============================================
# PART 6: PRACTICAL EXAMPLES
# ============================================

print("\n🚀 PART 6: PRACTICAL EXAMPLES")
print("-" * 50)

# 6.1 Before and After
print("\n6.1 Before and After Snapshot:")
print("-" * 30)

tasks = ["email", "review", "deploy", "test"]
print(f"Original tasks: {tasks}")

# Create snapshot before modification [citation:9]
before = tasks.copy()
tasks.remove("review")
tasks.append("document")

print(f"After modification: {tasks}")
print(f"Snapshot (original): {before}")

# 6.2 Sorting Without Affecting Original
print("\n6.2 Sorting Without Affecting Original:")
print("-" * 30)

scores = [85, 92, 78, 95, 88]
print(f"Original scores: {scores}")

# Sort a copy, not the original [citation:9]
sorted_scores = sorted(scores.copy())  # sorted() returns a new list
# or: sorted_scores = sorted(scores)

print(f"Sorted copy: {sorted_scores}")
print(f"Original unchanged: {scores}")

# 6.3 Function Side Effects Prevention
print("\n6.3 Function Without Side Effects:")
print("-" * 30)

def add_item_safely(items, new_item):
    """Add item without modifying original list [citation:9]"""
    items = items.copy()  # Work on a copy
    items.append(new_item)
    return items

original_cart = ["apple", "banana"]
updated_cart = add_item_safely(original_cart, "cherry")

print(f"Original cart: {original_cart}")  # Unchanged!
print(f"Updated cart: {updated_cart}")

# 6.4 Copy with List Comprehension
print("\n6.4 Copy with Transformation:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers.copy()]  # Copy first, then transform

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Assignment vs copy()
Create a list [1,2,3]. Assign it to another variable and also copy it.
Modify both copies and observe what happens.

🎯 EXERCISE 2: Shallow Copy
Create a list with nested list: [1, [2,3], 4]
Copy it using copy() and modify the nested list.
What happens to the original?

🎯 EXERCISE 3: Multiple Methods
Copy a list using:
- copy()
- slicing
- list()
- copy.copy()
Compare the results.

🎯 EXERCISE 4: Deep Copy
Create a deeply nested list and copy it using deepcopy().
Verify that nested objects are independent.

🎯 CHALLENGE: Safe Function
Write a function that processes a list without modifying the original.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Assignment vs copy():")
lst = [1, 2, 3]
assigned = lst
copied = lst.copy()
assigned.append(4)
copied.append(5)
print(f"  Original: {lst}")
print(f"  Assigned (modified): {assigned}")
print(f"  Copied (modified): {copied}")

# Exercise 2
print("\nEx2 - Shallow Copy:")
nested = [1, [2, 3], 4]
shallow = nested.copy()
shallow[1][0] = 99
print(f"  Original: {nested}")  # Changed!
print(f"  Shallow copy: {shallow}")

# Exercise 3
print("\nEx3 - Multiple Methods:")
data = [1, 2, 3]
copy1 = data.copy()
copy2 = data[:]
copy3 = list(data)
copy4 = copy.copy(data)
print(f"  All methods work correctly!")

# Exercise 4
print("\nEx4 - Deep Copy:")
deep_nested = [1, [2, 3], [4, 5]]
deep_copy = copy.deepcopy(deep_nested)
deep_nested[1][0] = 99
print(f"  Original: {deep_nested}")
print(f"  Deep copy: {deep_copy}")  # Unchanged!

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ COPY() METHOD MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    COPYING LISTS                            │
├─────────────────────────────────────────────────────────────┤
│  = assignment    → ALIAS (same object) [citation:2]        │
│  .copy()         → SHALLOW copy [citation:1]              │
│  [:]             → SHALLOW copy [citation:1][citation:8]   │
│  list()          → SHALLOW copy [citation:3][citation:12]  │
│  copy.copy()     → SHALLOW copy [citation:11]              │
│  copy.deepcopy() → DEEP copy [citation:6][citation:8]      │
├─────────────────────────────────────────────────────────────┤
│                    WHEN TO USE WHAT                         │
├─────────────────────────────────────────────────────────────┤
│  USE copy() when:                                           │
│  ├── Need independent top-level list                      │
│  ├── No nested mutable objects                            │
│  └── Simple lists with immutable items                    │
│                                                             │
│  USE deepcopy() when:                                       │
│  ├── Lists with nested lists/dicts                         │
│  ├── Need complete independence [citation:8]               │
│  └── Modifying nested structures                        │
├─────────────────────────────────────────────────────────────┤
│                    KEY RULES                                │
├─────────────────────────────────────────────────────────────┤
│  ✅ = creates ALIAS, not copy                              │
│  ✅ copy() creates new list object [citation:1]            │
│  ✅ copy() is SHALLOW [citation:6]                        │
│  ✅ Nested objects are SHARED [citation:8]                │
│  ✅ deepcopy() is COMPLETE [citation:8]                   │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Comprehensions - Python's Most Powerful Feature
""")