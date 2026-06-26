"""
PYTHON list.clear() & OBJECT CACHING/INTERNING
NeuralAICodeCraft - Complete Guide

Topics Covered:
1. list.clear() Method
2. How clear() Works Under the Hood
3. clear() vs del list[:] vs list = []
4. Object Caching (Small Integers)
5. String Interning
6. Why Lists Create New Objects
"""

import sys
import time

print("=" * 70)
print("🐍 PYTHON list.clear() & OBJECT CACHING")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: list.clear() BASICS
# ============================================

print("\n📚 PART 1: list.clear() METHOD")
print("-" * 50)

print("""
SYNTAX: my_list.clear()

WHAT IT DOES:
- Removes ALL elements from the list
- List becomes empty []
- Returns None (modifies in-place)
- Affects ALL references to the list
""")

# 1.1 Basic Usage
print("\n1.1 Basic Usage:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Before: {fruits}")
fruits.clear()
print(f"After clear(): {fruits}")

# 1.2 All References are Affected
print("\n1.2 All References Are Affected:")
print("-" * 30)

original = [1, 2, 3, 4, 5]
reference = original  # Both point to same list

print(f"Original: {original}")
print(f"Reference: {reference}")
print(f"Same object? {original is reference}")  # True

original.clear()

print(f"\nAfter original.clear():")
print(f"Original: {original}")   # Empty!
print(f"Reference: {reference}") # Also empty!

print("\n✅ clear() modifies the list IN-PLACE!")
print("  All variables referencing the list see the change.")

# ============================================
# PART 2: HOW clear() WORKS UNDER THE HOOD
# ============================================

print("\n🔧 PART 2: HOW clear() WORKS UNDER THE HOOD (CPython)")
print("-" * 50)

print("""
CPython's list.clear() implementation:

static int
_list_clear(PyListObject *a)
{
    Py_ssize_t i;
    PyObject **item = a->ob_item;
    if (item != NULL) {
        // First: make the list EMPTY
        i = Py_SIZE(a);
        Py_SIZE(a) = 0;      // Set length to 0
        a->ob_item = NULL;    // Clear pointer array
        a->allocated = 0;     // Reset allocation
        
        // THEN: decrement reference counts
        while (--i >= 0) {
            Py_XDECREF(item[i]);  // Decrement refcount for each element
        }
        PyMem_FREE(item);     // Free the memory block
    }
    return 0;
}

KEY INSIGHTS:
├── Makes the list empty FIRST (so no recursive issues)
├── Then decrements reference counts for each element
├── Time Complexity: O(n) where n is list length [citation:1][citation:3]
└── If refcount reaches 0, object is freed immediately
""")

# 2.1 Measuring clear() Time Complexity
print("\n2.1 Time Complexity Demonstration:")
print("-" * 30)

def time_clear(size):
    """Time how long clear() takes for a list of given size"""
    lst = [None] * size
    start = time.time()
    lst.clear()
    return time.time() - start

print("  Time to clear lists of different sizes:")
print(f"  {'Size':<12} {'Time (seconds)':<15}")
print("  " + "-" * 30)

for size in [100000, 500000, 1000000, 5000000]:
    t = time_clear(size)
    print(f"  {size:<12} {t:.6f}")

print("\n  ⏱️ clear() scales linearly with list size - O(n)!")

# ============================================
# PART 3: clear() vs del list[:] vs list = []
# ============================================

print("\n⚖️ PART 3: clear() vs del list[:] vs list = []")
print("-" * 50)

print("""
Three ways to "clear" a list:

1. my_list.clear()      → In-place clear (affects all references)
2. del my_list[:]       → In-place clear (affects all references) 
3. my_list = []         → Creates NEW list (doesn't affect other references) [citation:7]
""")

# 3.1 clear() vs del list[:]
print("\n3.1 clear() vs del list[:]:")
print("-" * 30)

print("  Both are IN-PLACE - they modify the original list object.")
print("  Both affect ALL references to the list.\n")

lst1 = [1, 2, 3]
ref1 = lst1
lst1.clear()
print(f"  clear() → lst1: {lst1}, ref1: {ref1}")

lst2 = [1, 2, 3]
ref2 = lst2
del lst2[:]
print(f"  del lst2[:] → lst2: {lst2}, ref2: {ref2}")

# 3.2 Assignment to []
print("\n3.2 assignment to []:")
print("-" * 30)

lst3 = [1, 2, 3]
ref3 = lst3
print(f"  Before: lst3: {lst3}, ref3: {ref3}")
print(f"  Same object? {lst3 is ref3}")  # True

lst3 = []  # Reassigns to NEW list!

print(f"\n  After lst3 = []:")
print(f"  lst3: {lst3}")    # Empty list
print(f"  ref3: {ref3}")    # Still [1, 2, 3]!
print(f"  Same object? {lst3 is ref3}")  # False

print("\n📌 KEY DIFFERENCE:")
print("  clear() and del modify the EXISTING list")
print("  = [] creates a NEW list (old one may be garbage collected)")

# ============================================
# PART 4: OBJECT CACHING (Small Integers)
# ============================================

print("\n💾 PART 4: OBJECT CACHING - SMALL INTEGERS")
print("-" * 50)

print("""
PYTHON CACHES SMALL INTEGERS (-5 to 256)

- Integers in this range are pre-created
- All references to these values point to the SAME object
- This is a PERFORMANCE optimization [citation:13]
- Larger integers create NEW objects each time
""")

# 4.1 Small Integer Caching
print("\n4.1 Small Integer Caching (-5 to 256):")
print("-" * 30)

# Small integers - cached
a = 100
b = 100
print(f"  a = 100, b = 100")
print(f"  Same object? {a is b}")  # True!
print(f"  ID of a: {id(a)}")
print(f"  ID of b: {id(b)}")

# 4.2 Large Integers - NOT Cached
print("\n4.2 Large Integers (Not Cached):")
print("-" * 30)

c = 1000
d = 1000
print(f"  c = 1000, d = 1000")
print(f"  Same object? {c is d}")  # False! (New objects each time)
print(f"  ID of c: {id(c)}")
print(f"  ID of d: {id(d)}")

# 4.3 Caching Range
print("\n4.3 Caching Range (-5 to 256):")
print("-" * 30)

for num in [-10, -5, 0, 100, 256, 257, 1000]:
    x = num
    y = num
    same = x is y
    print(f"  {num:4} → Same object? {same} {'✅ CACHED' if same else '❌ NEW'}")

print("\n📌 Python caches integers -5 to 256 for performance!")

# ============================================
# PART 5: STRING INTERNING
# ============================================

print("\n📝 PART 5: STRING INTERNING")
print("-" * 50)

print("""
STRING INTERNING:
- Certain strings are cached and reused
- String literals are automatically interned
- Only strings matching identifier rules: letters, digits, underscore [citation:13]
- Long or complex strings create new objects
""")

# 5.1 Simple Strings - Interned
print("\n5.1 Simple Strings (Interned):")
print("-" * 30)

s1 = "hello"
s2 = "hello"
print(f"  s1 = 'hello', s2 = 'hello'")
print(f"  Same object? {s1 is s2}")  # True!

# 5.2 Complex Strings - Not Interned
print("\n5.2 Complex Strings (Not Interned):")
print("-" * 30)

s3 = "Hello World with spaces"
s4 = "Hello World with spaces"
print(f"  s3 = 'Hello World with spaces'")
print(f"  s4 = 'Hello World with spaces'")
print(f"  Same object? {s3 is s4}")  # False!

# 5.3 Using sys.intern()
print("\n5.3 Forcing Interning with sys.intern():")
print("-" * 30)

import sys
s5 = sys.intern("This is a long string!")
s6 = sys.intern("This is a long string!")
print(f"  After sys.intern()")
print(f"  Same object? {s5 is s6}")  # True!

print("\n📌 String interning saves memory for repeated strings!")

# ============================================
# PART 6: LISTS CREATE NEW OBJECTS
# ============================================

print("\n📋 PART 6: LISTS ALWAYS CREATE NEW OBJECTS")
print("-" * 50)

print("""
Unlike small integers and some strings, LIST LITERALS ALWAYS CREATE NEW OBJECTS.

WHY?
- Lists are MUTABLE
- If they were shared, modifying one would affect all references
- Python creates a new list object for each list literal

TRY THIS:
- [1,2,3] is [1,2,3] → False (different objects!)
- (1,2,3) is (1,2,3) → True (tuples are immutable!)
""")

# 6.1 Lists vs Tuples
print("\n6.1 Lists vs Tuples Comparison:")
print("-" * 30)

# Lists always create new objects
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(f"  list1 = [1,2,3], list2 = [1,2,3]")
print(f"  Same object? {list1 is list2}")  # False!
print(f"  ID list1: {id(list1)}")
print(f"  ID list2: {id(list2)}")

# Tuples may be cached
tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)
print(f"\n  tuple1 = (1,2,3), tuple2 = (1,2,3)")
print(f"  Same object? {tuple1 is tuple2}")  # True! (Tuples are immutable)

# 6.2 Lists with Cached Integers
print("\n6.2 Lists Contain References to Cached Objects:")
print("-" * 30)

# List contains references to cached integers
list_a = [100, 200, 300]
list_b = [100, 200, 300]

print(f"  list_a[0] is list_b[0]? {list_a[0] is list_b[0]}")  # True!
print(f"  list_a is list_b? {list_a is list_b}")  # False!

print("\n📌 The LIST objects are different, but the INTEGERS inside are shared!")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: clear() References
Create a list, assign it to another variable, clear it.
What happens to both variables?

🎯 EXERCISE 2: clear() vs []
Create a list, assign it to another variable, then use = [].
What happens to both variables?

🎯 EXERCISE 3: Integer Caching
Check if 255 is 255 and 257 is 257. Explain.

🎯 EXERCISE 4: String Interning
Test if "hello" is "hello" vs "hello world" is "hello world"

🎯 EXERCISE 5: List Identity
Check if [1,2,3] is [1,2,3] and explain why.

🎯 CHALLENGE: Memory Optimization
Write a function that demonstrates the memory saved by interning.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - clear() References:")
lst = [1, 2, 3]
ref = lst
lst.clear()
print(f"  lst: {lst}, ref: {ref} (Both empty!)")

# Exercise 2
print("\nEx2 - clear() vs []:")
lst = [1, 2, 3]
ref = lst
lst = []
print(f"  lst: {lst}, ref: {ref} (ref unchanged!)")

# Exercise 3
print("\nEx3 - Integer Caching:")
print(f"  255 is 255? {255 is 255}")  # True
print(f"  257 is 257? {257 is 257}")  # False

# Exercise 4
print("\nEx4 - String Interning:")
print(f"  'hello' is 'hello'? {'hello' is 'hello'}")  # True
print(f"  'hello world' is 'hello world'? {'hello world' is 'hello world'}")  # False

# Exercise 5
print("\nEx5 - List Identity:")
print(f"  [1,2,3] is [1,2,3]? {[1,2,3] is [1,2,3]}")  # False
print("  Lists always create new objects!")

# Challenge
print("\nChallenge - Interning Memory:")
def intern_demo():
    import sys
    print("  Without interning:")
    s1 = "This is a very long string that will be repeated many times"
    s2 = "This is a very long string that will be repeated many times"
    print(f"    Same object? {s1 is s2}")
    print(f"    Memory used: {sys.getsizeof(s1) + sys.getsizeof(s2)} bytes")
    
    print("\n  With interning:")
    s3 = sys.intern("This is a very long string that will be repeated many times")
    s4 = sys.intern("This is a very long string that will be repeated many times")
    print(f"    Same object? {s3 is s4}")
    print(f"    Memory used: {sys.getsizeof(s3)} bytes (shared!)")

intern_demo()

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST.CLEAR() & CACHING MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    CLEARING LISTS                           │
├─────────────────────────────────────────────────────────────┤
│  my_list.clear()   → In-place clear, affects all refs      │
│  del my_list[:]    → In-place clear, affects all refs      │
│  my_list = []      → New list, doesn't affect other refs   │
│  clear() is O(n) in CPython [citation:1][citation:3]       │
├─────────────────────────────────────────────────────────────┤
│                    OBJECT CACHING                           │
├─────────────────────────────────────────────────────────────┤
│  Small ints (-5 to 256) are CACHED [citation:13]           │
│  String literals may be INTERNED [citation:13]             │
│  Lists ALWAYS create NEW objects                           │
│  Tuples may be CACHED (immutable)                          │
├─────────────────────────────────────────────────────────────┤
│                    WHEN TO USE WHAT                         │
├─────────────────────────────────────────────────────────────┤
│  Use clear() when:                                          │
│  ├── Need to affect ALL references                         │
│  ├── Want to reuse the same list object                    │
│  └── Memory efficiency matters                             │
│                                                             │
│  Use = [] when:                                             │
│  ├── Only current variable needs empty list                │
│  ├── Other references should keep old data                 │
│  └── Want to create a new list object                      │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Comprehensions - Python's Most Powerful Feature
""")