"""
LIST SLICING IN PYTHON: COMPLETE GUIDE
NeuralAICodeCraft - Master [start:end:step]

Topics Covered:
1. Basic Slicing Syntax
2. Omitting Start and End
3. Negative Indexing
4. Step Parameter
5. Reversing Lists
6. Slicing for Modification
7. Copying Lists
8. Removing Elements with Slices
9. Advanced Slicing Techniques
"""

print("=" * 70)
print("🔪 LIST SLICING IN PYTHON - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: BASIC SLICING SYNTAX
# ============================================

print("\n📚 PART 1: BASIC SLICING SYNTAX")
print("-" * 50)

print("""
SYNTAX: list[start:end]
- start: index to begin (inclusive)
- end: index to stop (exclusive)
- Returns a NEW list
- Think of it like cutting between elements [citation:2]
""")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {my_list}")

# Basic slicing
print(f"\nmy_list[2:7]  → {my_list[2:7]}  # Elements from index 2 to 6")
print(f"my_list[3:6]  → {my_list[3:6]}  # Elements from index 3 to 5")
print(f"my_list[1:4]  → {my_list[1:4]}  # Elements from index 1 to 3")

# Understanding exclusive end
print("\nNOTE: The 'end' index is EXCLUDED!")
print(f"my_list[2:5] includes indices 2, 3, 4 → {my_list[2:5]}")

print("\n📌 TIP: Slice length = end - start")
print(f"  my_list[2:7] length = 7 - 2 = {len(my_list[2:7])}")

# ============================================
# PART 2: OMITTING START AND END
# ============================================

print("\n🎯 PART 2: OMITTING START AND END")
print("-" * 50)

print("""
- list[:end] → From beginning to end (exclusive)
- list[start:] → From start to end
- list[:] → Copy entire list [citation:2][citation:8]
""")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {my_list}")

print(f"\nmy_list[:5]   → {my_list[:5]}   # First 5 elements")
print(f"my_list[5:]   → {my_list[5:]}   # From index 5 to end")
print(f"my_list[:]    → {my_list[:]}    # Copy entire list")

# ============================================
# PART 3: NEGATIVE INDEXING
# ============================================

print("\n🔄 PART 3: NEGATIVE INDEXING")
print("-" * 50)

print("""
Negative indices count from the end of the list [citation:5]:
- -1 → Last element
- -2 → Second last
- Works with slicing: list[-3:] → Last 3 elements
""")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {my_list}")

print(f"\nmy_list[-1]     → {my_list[-1]}     # Last element")
print(f"my_list[-3:]    → {my_list[-3:]}    # Last 3 elements")
print(f"my_list[:-3]    → {my_list[:-3]}    # All except last 3")
print(f"my_list[-5:-2]  → {my_list[-5:-2]}  # Elements from -5 to -3")

print("\n📌 NOTE: The start index is inclusive, end is exclusive - works same for negative indices!")

# ============================================
# PART 4: STEP PARAMETER
# ============================================

print("\n⚡ PART 4: STEP PARAMETER [start:end:step]")
print("-" * 50)

print("""
- step: interval between indices [citation:2][citation:4]
- Default step is 1
- list[::2] → Every second element
""")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {my_list}")

print(f"\nmy_list[::2]   → {my_list[::2]}   # Every second element")
print(f"my_list[1::2]  → {my_list[1::2]}  # Every second starting at 1")
print(f"my_list[2:8:2] → {my_list[2:8:2]} # From 2 to 7, step 2")
print(f"my_list[::3]   → {my_list[::3]}   # Every third element")

print("\n💡 TIP: Step in slicing works like range(start, stop, step)! [citation:4]")

# ============================================
# PART 5: REVERSING A LIST
# ============================================

print("\n🔄 PART 5: REVERSING A LIST WITH [::-1]")
print("-" * 50)

print("""
- list[::-1] → Returns reversed list
- Python idiom for reversing [citation:2][citation:9]
""")

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {my_list}")
print(f"my_list[::-1] → {my_list[::-1]}  # Reversed")

# Reverse with step
print(f"\nmy_list[::-2]  → {my_list[::-2]}  # Reverse with every second element")
print(f"my_list[8:2:-1]→ {my_list[8:2:-1]} # Reverse from 8 to 3")

print("\n⚠️ IMPORTANT: With negative step, start > end to get elements [citation:2]")

# ============================================
# PART 6: SLICING FOR LIST MODIFICATION
# ============================================

print("\n✏️ PART 6: SLICING FOR LIST MODIFICATION")
print("-" * 50)

print("""
Lists are mutable - slices can be used on both sides of assignment! [citation:1]
""")

# 6.1 Replacing elements
print("\n6.1 Replacing Elements:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
fruits[1:3] = ['blueberry', 'coconut']
print(f"After fruits[1:3] = ['blueberry', 'coconut']: {fruits}")

# 6.2 Inserting elements (empty slice)
print("\n6.2 Inserting Elements (Empty Slice):")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
fruits[2:2] = ['blueberry', 'coconut']  # Insert at index 2 [citation:1]
print(f"After fruits[2:2] = ['blueberry', 'coconut']: {fruits}")

# 6.3 Removing elements (assign empty list)
print("\n6.3 Removing Elements (Assign Empty List):")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
fruits[1:3] = []  # Remove elements at index 1 and 2
print(f"After fruits[1:3] = []: {fruits}")

# 6.4 Expanding or shrinking with slices
print("\n6.4 Expanding/Shrinking with Slices:")
print("-" * 30)

words = ['We', 'belong', 'to', 'the', 'knights']
print(f"Original: {words}")
words[1:4] = ['are']
print(f"After words[1:4] = ['are']: {words}")  # Shrinks the list [citation:1]

words[1:2] = ['are', 'a', 'band', 'of']
print(f"After words[1:2] = ['are','a','band','of']: {words}")  # Expands the list [citation:1]

# ============================================
# PART 7: COPYING LISTS WITH [:]
# ============================================

print("\n📋 PART 7: COPYING LISTS WITH [:]")
print("-" * 50)

print("""
- list[:] creates a SHALLOW copy
- Changes to copy don't affect original
- Creates a new list object [citation:1]
""")

original = [1, 2, 3, 4, 5]
copy = original[:]

print(f"Original: {original}")
print(f"Copy: {copy}")

# Modify copy
copy[0] = 99
print(f"\nAfter modifying copy[0] = 99:")
print(f"Original: {original}  # Unchanged!")
print(f"Copy: {copy}")

print("\n🔑 KEY: original is copy? {original is copy}")  # False

# ============================================
# PART 8: REMOVING ELEMENTS WITH DEL
# ============================================

print("\n🗑️ PART 8: REMOVING ELEMENTS WITH del")
print("-" * 50)

print("""
- del list[start:end] removes slice [citation:1]
- Alternative to assigning empty list
""")

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
del fruits[1:3]
print(f"After del fruits[1:3]: {fruits}")

# Remove from beginning
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
del fruits[:2]
print(f"\nAfter del fruits[:2]: {fruits}")

# Remove from end
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
del fruits[-2:]
print(f"\nAfter del fruits[-2:]: {fruits}")

# ============================================
# PART 9: ADVANCED SLICING TECHNIQUES
# ============================================

print("\n🚀 PART 9: ADVANCED SLICING TECHNIQUES")
print("-" * 50)

# 9.1 Slicing with Step and Negative Indices
print("\n9.1 Step with Negative Indices:")
print("-" * 30)

nums = list(range(10))
print(f"List: {nums}")
print(f"nums[-4:-1]  → {nums[-4:-1]}  # From -4 to -2")
print(f"nums[-3:]    → {nums[-3:]}    # Last 3 elements")
print(f"nums[:-2]    → {nums[:-2]}    # All except last 2")

# 9.2 Out of Range Slicing (Safe!)
print("\n9.2 Out of Range Slicing (Safe!):")
print("-" * 30)

print(f"nums[:100]  → {nums[:100]}  # Clips to end")
print(f"nums[100:]  → {nums[100:]}  # Empty list")
print(f"nums[100:200]→ {nums[100:200]}  # Empty list")

print("\n📌 Python won't raise IndexError for slices out of range!")

# 9.3 Slicing with Reusable Slice Object
print("\n9.3 Reusable Slice Object (slice()):")
print("-" * 30)

my_slice = slice(2, 7, 2)
nums = list(range(10))
print(f"List: {nums}")
print(f"nums[my_slice] → {nums[my_slice]}")

# 9.4 List Comprehension with Slicing
print("\n9.4 List Comprehension + Slicing:")
print("-" * 30)

original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [x**2 for x in original[1::2]]
print(f"Original: {original}")
print(f"Square of every second element: {squared_evens}")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Extract Middle
Given list = [10, 20, 30, 40, 50, 60, 70]
Extract the middle 3 elements → [30, 40, 50]

🎯 EXERCISE 2: Reverse List
Reverse [1, 2, 3, 4, 5] using slicing → [5, 4, 3, 2, 1]

🎯 EXERCISE 3: Copy and Verify
Copy a list and verify changes don't affect original

🎯 EXERCISE 4: Every Third Element
Extract every third element from [1..20]

🎯 EXERCISE 5: Remove Middle
Remove the middle 3 elements from a 7-element list using del

🎯 EXERCISE 6: Insert Elements
Insert ['a','b'] at position 2 in [1,2,3,4]

🎯 CHALLENGE: Palindrome Check
Use slicing to check if a string is a palindrome
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
list1 = [10, 20, 30, 40, 50, 60, 70]
middle = list1[2:5]
print(f"\nEx1 - Middle 3: {middle}")

# Exercise 2
list2 = [1, 2, 3, 4, 5]
reversed_list = list2[::-1]
print(f"Ex2 - Reversed: {reversed_list}")

# Exercise 3
original = [1, 2, 3]
copy = original[:]
copy[0] = 99
print(f"Ex3 - Original: {original}, Copy: {copy}")

# Exercise 4
list4 = list(range(1, 21))
every_third = list4[2::3]
print(f"Ex4 - Every third: {every_third}")

# Exercise 5
list5 = [1, 2, 3, 4, 5, 6, 7]
del list5[2:5]
print(f"Ex5 - After removing middle: {list5}")

# Exercise 6
list6 = [1, 2, 3, 4]
list6[2:2] = ['a', 'b']
print(f"Ex6 - After insertion: {list6}")

# Challenge
def is_palindrome(text):
    return text == text[::-1]

print(f"Challenge - 'racecar' palindrome? {is_palindrome('racecar')}")
print(f"Challenge - 'python' palindrome? {is_palindrome('python')}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST SLICING MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    SLICING SYNTAX                           │
├─────────────────────────────────────────────────────────────┤
│  list[start:end]        → Elements from start to end-1     │
│  list[:end]             → First 'end' elements             │
│  list[start:]           → From 'start' to end              │
│  list[:]                → Copy entire list                 │
│  list[-3:]              → Last 3 elements                  │
│  list[:-3]              → All except last 3                │
│  list[::2]              → Every second element             │
│  list[::-1]             → Reverse list                     │
│  list[2:8:3]            → From 2 to 7, step 3              │
├─────────────────────────────────────────────────────────────┤
│                SLICING FOR MODIFICATION                     │
├─────────────────────────────────────────────────────────────┤
│  list[1:3] = ['a','b']  → Replace elements                 │
│  list[1:1] = ['a']      → Insert at position               │
│  list[1:3] = []         → Remove elements                  │
│  del list[1:3]          → Remove elements                  │
├─────────────────────────────────────────────────────────────┤
│                   KEY RULES                                 │
├─────────────────────────────────────────────────────────────┤
│  ✅ start is INCLUSIVE (included in result)                │
│  ✅ end is EXCLUSIVE (not included)                        │
│  ✅ Slices return NEW lists                                │
│  ✅ Negative indices count from end                        │
│  ✅ Step can be negative (reverse direction)               │
│  ⚠️ Out of range indices are safe (clip or empty)         │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Methods (append, extend, insert, remove, pop, sort)
""")