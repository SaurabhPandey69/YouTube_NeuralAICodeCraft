"""
PYTHON LIST METHODS: INSERT, REMOVE, POP, CLEAR, DEL
NeuralAICodeCraft - Complete Guide

Topics Covered:
1. insert() - Add at specific position
2. Replacing Elements
3. remove() - Remove by value
4. pop() - Remove and return by index
5. clear() - Remove all elements
6. del - Delete elements or entire list
7. Difference Between Methods
"""

print("=" * 70)
print("🐍 PYTHON LIST METHODS - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: insert() METHOD
# ============================================

print("\n📚 PART 1: insert() METHOD")
print("-" * 50)

print("""
SYNTAX: list.insert(index, element)

WHAT IT DOES:
- Inserts element at the specified position
- Shifts elements to the right
- Index can be negative (inserts from end)
- Returns None (modifies in-place)
""")

# 1.1 Basic Insert
print("\n1.1 Basic Insert:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry']
print(f"Original: {fruits}")
fruits.insert(1, 'blueberry')
print(f"After insert(1, 'blueberry'): {fruits}")

# 1.2 Insert at Beginning
print("\n1.2 Insert at Beginning:")
print("-" * 30)

numbers = [2, 3, 4, 5]
print(f"Original: {numbers}")
numbers.insert(0, 1)
print(f"After insert(0, 1): {numbers}")

# 1.3 Insert at End
print("\n1.3 Insert at End (Using len()):")
print("-" * 30)

colors = ['red', 'green', 'blue']
print(f"Original: {colors}")
colors.insert(len(colors), 'yellow')
print(f"After insert(len(colors), 'yellow'): {colors}")

# 1.4 Insert with Negative Index
print("\n1.4 Insert with Negative Index:")
print("-" * 30)

letters = ['a', 'b', 'd', 'e']
print(f"Original: {letters}")
letters.insert(-2, 'c')  # Insert at second-last position
print(f"After insert(-2, 'c'): {letters}")

# 1.5 Insert at Out of Range Index
print("\n1.5 Insert at Out of Range Index:")
print("-" * 30)

names = ['Alice', 'Bob']
print(f"Original: {names}")
names.insert(10, 'Charlie')  # Index beyond list length
print(f"After insert(10, 'Charlie'): {names}")  # Appends at end

names.insert(-10, 'David')  # Negative index beyond list length
print(f"After insert(-10, 'David'): {names}")  # Inserts at beginning

print("\n💡 TIP: insert() with index >= len() appends to end")
print("  insert() with negative index < -len() inserts at beginning")

# ============================================
# PART 2: REPLACING ELEMENTS
# ============================================

print("\n✏️ PART 2: REPLACING ELEMENTS")
print("-" * 50)

print("""
Replacing elements is done by direct assignment:
- list[index] = new_value
- Replaces element at that position
- No method call needed!
""")

# 2.1 Replace by Index
print("\n2.1 Replace by Index:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Original: {fruits}")
fruits[1] = 'blueberry'
print(f"After fruits[1] = 'blueberry': {fruits}")
fruits[-1] = 'dragonfruit'
print(f"After fruits[-1] = 'dragonfruit': {fruits}")

# 2.2 Replace with Slice
print("\n2.2 Replace with Slice (Multiple Elements):")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6]
print(f"Original: {numbers}")
numbers[1:4] = [10, 20, 30]
print(f"After numbers[1:4] = [10, 20, 30]: {numbers}")

# 2.3 Replace with Different Length
print("\n2.3 Replace with Different Length Slice:")
print("-" * 30)

letters = ['a', 'b', 'c', 'd', 'e']
print(f"Original: {letters}")
letters[1:3] = ['x', 'y', 'z', 'w']  # Expanding
print(f"After letters[1:3] = ['x','y','z','w']: {letters}")

letters[2:5] = ['m']  # Shrinking
print(f"After letters[2:5] = ['m']: {letters}")

# ============================================
# PART 3: remove() METHOD
# ============================================

print("\n🗑️ PART 3: remove() METHOD")
print("-" * 50)

print("""
SYNTAX: list.remove(element)

WHAT IT DOES:
- Removes the FIRST occurrence of the specified value
- Raises ValueError if element not found
- Returns None (modifies in-place)
""")

# 3.1 Basic Remove
print("\n3.1 Basic Remove:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'banana', 'date']
print(f"Original: {fruits}")
fruits.remove('banana')  # Removes first 'banana'
print(f"After remove('banana'): {fruits}")

# 3.2 Remove with Duplicates
print("\n3.2 Remove with Duplicates:")
print("-" * 30)

numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {numbers}")

# Remove all 2's
while 2 in numbers:
    numbers.remove(2)
print(f"After removing all 2's: {numbers}")

# 3.3 ValueError Handling
print("\n3.3 ValueError Handling:")
print("-" * 30)

colors = ['red', 'green', 'blue']
print(f"Original: {colors}")

try:
    colors.remove('yellow')  # Not in list
except ValueError as e:
    print(f"❌ Error: {e}")

# Safe removal
def safe_remove(lst, element):
    """Remove element safely (no error if not found)"""
    try:
        lst.remove(element)
        return True
    except ValueError:
        return False

print(f"\nSafe removal:")
print(f"remove('yellow') → {safe_remove(colors, 'yellow')}")
print(f"Colors after safe removal: {colors}")

# ============================================
# PART 4: pop() METHOD
# ============================================

print("\n📤 PART 4: pop() METHOD")
print("-" * 50)

print("""
SYNTAX: list.pop(index)

WHAT IT DOES:
- Removes and RETURNS element at specified index
- If no index given, removes and returns LAST element
- Raises IndexError if index out of range
- Returns the removed element
""")

# 4.1 Basic Pop
print("\n4.1 Basic Pop (Last Element):")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Original: {fruits}")
removed = fruits.pop()
print(f"After pop(): {fruits}")
print(f"Removed element: {removed}")

# 4.2 Pop by Index
print("\n4.2 Pop by Index:")
print("-" * 30)

numbers = [10, 20, 30, 40, 50]
print(f"Original: {numbers}")
removed = numbers.pop(2)
print(f"After pop(2): {numbers}")
print(f"Removed element: {removed}")

# 4.3 Pop with Negative Index
print("\n4.3 Pop with Negative Index:")
print("-" * 30)

letters = ['a', 'b', 'c', 'd', 'e']
print(f"Original: {letters}")
removed = letters.pop(-2)
print(f"After pop(-2): {letters}")
print(f"Removed element: {removed}")

# 4.4 IndexError Handling
print("\n4.4 IndexError Handling:")
print("-" * 30)

empty_list = []
try:
    empty_list.pop()
except IndexError as e:
    print(f"❌ Error: {e}")

# 4.5 Using Pop in a Loop
print("\n4.5 Using Pop in a Loop:")
print("-" * 30)

stack = [1, 2, 3, 4, 5]
print(f"Original stack: {stack}")
print("Popping all elements:")
while stack:
    element = stack.pop()
    print(f"  Popped: {element}, Remaining: {stack}")

# ============================================
# PART 5: clear() METHOD
# ============================================

print("\n🧹 PART 5: clear() METHOD")
print("-" * 50)

print("""
SYNTAX: list.clear()

WHAT IT DOES:
- Removes ALL elements from the list
- List becomes empty []
- Returns None (modifies in-place)
- Faster than assigning [] (reuses memory)
""")

# 5.1 Basic Clear
print("\n5.1 Basic Clear:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Original: {fruits}")
print(f"ID before clear: {id(fruits)}")
fruits.clear()
print(f"After clear(): {fruits}")
print(f"ID after clear: {id(fruits)}")  # Same ID - list reused!

# 5.2 clear() vs [] Assignment
print("\n5.2 clear() vs [] Assignment:")
print("-" * 30)

# Using clear()
list1 = [1, 2, 3]
list1_id = id(list1)
list1.clear()
print(f"clear() - Same object? {id(list1) == list1_id}")  # True

# Using [] assignment
list2 = [1, 2, 3]
list2_id = id(list2)
list2 = []
print(f"[] assignment - Same object? {id(list2) == list2_id}")  # False

print("\n💡 TIP: Use clear() to keep the same list object")
print("  Use [] assignment when you want to create a new list")

# ============================================
# PART 6: del STATEMENT
# ============================================

print("\n🗡️ PART 6: del STATEMENT")
print("-" * 50)

print("""
SYNTAX: del list[index]
        del list[start:end]
        del list  (delete entire list)

WHAT IT DOES:
- Removes element(s) by index or slice
- Can delete entire list object
- Does NOT return removed elements
- Raises IndexError if index out of range
""")

# 6.1 Delete by Index
print("\n6.1 Delete by Index:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
del fruits[1]
print(f"After del fruits[1]: {fruits}")

# 6.2 Delete by Slice
print("\n6.2 Delete by Slice:")
print("-" * 30)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original: {numbers}")
del numbers[2:6]
print(f"After del numbers[2:6]: {numbers}")

# Delete from beginning
numbers = [0, 1, 2, 3, 4, 5]
print(f"\nOriginal: {numbers}")
del numbers[:2]
print(f"After del numbers[:2]: {numbers}")

# Delete from end
numbers = [0, 1, 2, 3, 4, 5]
del numbers[-2:]
print(f"After del numbers[-2:]: {numbers}")

# 6.3 Delete Entire List
print("\n6.3 Delete Entire List:")
print("-" * 30)

my_list = [1, 2, 3]
print(f"Before del: {my_list}")
del my_list
# print(my_list)  # This would raise NameError - list no longer exists!
print("After del: list variable no longer exists!")

# 6.4 del vs remove vs pop
print("\n6.4 del vs remove vs pop - Visual Comparison:")
print("-" * 30)

# del
list_del = [1, 2, 3, 4]
print(f"del list_del[1] → {list_del}")
del list_del[1]
print(f"  Result: {list_del}")

# remove
list_remove = [1, 2, 3, 4]
print(f"list_remove.remove(3) → {list_remove}")
list_remove.remove(3)
print(f"  Result: {list_remove}")

# pop
list_pop = [1, 2, 3, 4]
popped = list_pop.pop(1)
print(f"list_pop.pop(1) → {list_pop}")
print(f"  Popped: {popped}, Result: {list_pop}")

# ============================================
# PART 7: COMPARISON TABLE
# ============================================

print("\n📊 PART 7: METHOD COMPARISON")
print("-" * 50)

print("""
┌─────────────┬──────────────┬──────────────┬──────────────────┐
│  METHOD     │  REMOVES BY  │  RETURNS     │  ERROR           │
├─────────────┼──────────────┼──────────────┼──────────────────┤
│  remove(x)  │  Value       │  None        │  ValueError      │
│  pop(i)     │  Index       │  Element     │  IndexError      │
│  del list[i]│  Index       │  Nothing     │  IndexError      │
│  clear()    │  All         │  None        │  None            │
└─────────────┴──────────────┴──────────────┴──────────────────┘

┌─────────────┬──────────────────────────────────────────────┐
│  METHOD     │  USE CASE                                    │
├─────────────┼──────────────────────────────────────────────┤
│  insert()   │  Add element at specific position            │
│  assign     │  Replace element at specific position        │
│  remove()   │  Delete by value (first occurrence)          │
│  pop()      │  Get and remove element (use the value)      │
│  clear()    │  Empty the list (keep the same object)       │
│  del        │  Delete by index/slice or entire list        │
└─────────────┴──────────────────────────────────────────────┘
""")

# ============================================
# PART 8: PERFORMANCE COMPARISON
# ============================================

print("\n⚡ PART 8: PERFORMANCE COMPARISON")
print("-" * 50)

import time

def time_method(method, *args):
    """Time a method execution"""
    start = time.time()
    method(*args)
    return time.time() - start

# Create test lists
size = 10000
test_list = list(range(size))

print(f"Testing with list of {size} elements:\n")

# insert at beginning (slow)
start = time.time()
test_list.insert(0, -1)
insert_time = time.time() - start
print(f"insert(0, -1): {insert_time:.6f}s (O(n) - shifts all elements)")

# insert at end (fast)
test_list = list(range(size))
start = time.time()
test_list.insert(size, -1)
insert_end_time = time.time() - start
print(f"insert(len, -1): {insert_end_time:.6f}s (O(1) - appends)")

# remove from beginning (slow)
test_list = list(range(size))
start = time.time()
test_list.remove(0)
remove_time = time.time() - start
print(f"remove(0): {remove_time:.6f}s (O(n) - shifts all elements)")

# pop from end (fast)
test_list = list(range(size))
start = time.time()
test_list.pop()
pop_time = time.time() - start
print(f"pop(): {pop_time:.6f}s (O(1))")

# ============================================
# PART 9: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 9: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Insert Practice
Insert 99 at position 3 in [1, 2, 3, 4, 5]

🎯 EXERCISE 2: Replace Practice
Replace 'banana' with 'mango' in ['apple', 'banana', 'cherry']

🎯 EXERCISE 3: Remove Practice
Remove all occurrences of 2 from [1, 2, 3, 2, 4, 2, 5]

🎯 EXERCISE 4: Pop Practice
Pop the middle element from [10, 20, 30, 40, 50]

🎯 EXERCISE 5: Clear vs Del
Explain the difference between clear() and del

🎯 CHALLENGE: Combine Methods
Write a program that uses insert, remove, pop, and clear on the same list
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Insert:")
lst1 = [1, 2, 3, 4, 5]
lst1.insert(3, 99)
print(f"  [1,2,3,4,5].insert(3,99) → {lst1}")

# Exercise 2
print("\nEx2 - Replace:")
lst2 = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(lst2):
    if fruit == 'banana':
        lst2[i] = 'mango'
print(f"  Replace 'banana' → {lst2}")

# Exercise 3
print("\nEx3 - Remove all 2's:")
lst3 = [1, 2, 3, 2, 4, 2, 5]
while 2 in lst3:
    lst3.remove(2)
print(f"  After removing all 2's: {lst3}")

# Exercise 4
print("\nEx4 - Pop Middle:")
lst4 = [10, 20, 30, 40, 50]
middle_idx = len(lst4) // 2
removed = lst4.pop(middle_idx)
print(f"  Popped middle element: {removed}")
print(f"  Remaining list: {lst4}")

# Exercise 5
print("\nEx5 - clear() vs del:")
print("""
  clear() → Removes all elements but keeps the list object
  del → Deletes the entire list variable (no longer exists)

  Example:
  lst = [1, 2, 3]
  lst.clear() → lst is empty but exists []
  del lst → lst no longer exists (NameError)
""")

# Challenge
print("\nChallenge - Combined Methods:")
combined = [1, 2, 3]
print(f"  Original: {combined}")
combined.insert(1, 99)
print(f"  After insert(1,99): {combined}")
combined.remove(99)
print(f"  After remove(99): {combined}")
popped = combined.pop(1)
print(f"  After pop(1): {combined} (removed: {popped})")
combined.clear()
print(f"  After clear(): {combined}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST METHODS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    INSERTION                                │
├─────────────────────────────────────────────────────────────┤
│  list.insert(i, x)  → Insert x at index i                  │
│  list[i] = x        → Replace element at index i           │
│  list[i:j] = [x,y]  → Replace slice with new elements      │
├─────────────────────────────────────────────────────────────┤
│                    REMOVAL                                  │
├─────────────────────────────────────────────────────────────┤
│  list.remove(x)     → Remove first occurrence of x         │
│  list.pop(i)        → Remove and return element at i       │
│  del list[i]        → Remove element at i                  │
│  del list[i:j]      → Remove slice                         │
│  list.clear()       → Remove all elements                  │
│  del list           → Delete entire list                   │
├─────────────────────────────────────────────────────────────┤
│                    PERFORMANCE (O notation)                │
├─────────────────────────────────────────────────────────────┤
│  insert(0, x)       → O(n) ⚠️ Slow                       │
│  insert(len, x)     → O(1) ✅ Fast                       │
│  remove(x)          → O(n) ⚠️ Slow (searches)            │
│  pop()              → O(1) ✅ Fast                       │
│  pop(i)             → O(n) ⚠️ Slow (if not end)          │
│  del list[i]        → O(n) ⚠️ Slow (if not end)          │
│  clear()            → O(n) ✅ Fast                        │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Comprehensions - Python's Most Powerful Feature
""")