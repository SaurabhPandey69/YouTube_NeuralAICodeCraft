"""
LIST CONSTRUCTOR FUNCTION & RANGE ITERABLE - COMPLETE GUIDE
NeuralAICodeCraft - Master list() constructor and range() function

Topics Covered:
1. The list() Constructor Function
2. The range() Function
3. Range is NOT a List!
4. Iterables vs Iterators
5. Converting Range to Iterator
6. Performance & Memory Efficiency
"""

print("=" * 70)
print("🐍 LIST CONSTRUCTOR & RANGE ITERABLE - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: THE list() CONSTRUCTOR
# ============================================

print("\n📦 PART 1: THE list() CONSTRUCTOR")
print("-" * 50)

print("""
list() is a built-in function that creates a new list from ANY iterable.
It converts strings, tuples, ranges, and other iterables into lists. [citation:2]
""")

# 1.1 Creating Empty List
print("\n1.1 Empty List:")
print("-" * 30)

empty1 = []
empty2 = list()
print(f"  [] → {empty1}")
print(f"  list() → {empty2}")

# 1.2 From Strings (each character becomes an element)
print("\n1.2 From Strings:")
print("-" * 30)

string = "Python"
char_list = list(string)
print(f"  list('Python') → {char_list}")  # ['P', 'y', 't', 'h', 'o', 'n'] [citation:4]

# 1.3 From Tuples
print("\n1.3 From Tuples:")
print("-" * 30)

tuple_data = (1, 2, 3, 4)
tuple_to_list = list(tuple_data)
print(f"  list((1,2,3,4)) → {tuple_to_list}")  # [1, 2, 3, 4] [citation:3]

# 1.4 From Range
print("\n1.4 From Range:")
print("-" * 30)

range_to_list = list(range(5))
print(f"  list(range(5)) → {range_to_list}")  # [0, 1, 2, 3, 4] [citation:6]

# 1.5 From Dictionary (keys only)
print("\n1.5 From Dictionary (keys only):")
print("-" * 30)

dict_data = {"a": 1, "b": 2, "c": 3}
dict_keys = list(dict_data)
dict_values = list(dict_data.values())
print(f"  list(dict) → {dict_keys}")  # ['a', 'b', 'c']
print(f"  list(dict.values()) → {dict_values}")  # [1, 2, 3]

# ============================================
# PART 2: THE range() FUNCTION
# ============================================

print("\n🔢 PART 2: THE range() FUNCTION")
print("-" * 50)

print("""
range() creates a sequence of numbers WITHOUT storing them all in memory. [citation:9]
It's a LAZY sequence - numbers are generated on demand! [citation:8]
""")

# 2.1 One Argument: range(stop)
print("\n2.1 range(stop) - Count from 0 to stop-1:")
print("-" * 30)

r1 = range(5)
print(f"  range(5) → {list(r1)}")  # [0, 1, 2, 3, 4] [citation:10]

# 2.2 Two Arguments: range(start, stop)
print("\n2.2 range(start, stop) - Count from start to stop-1:")
print("-" * 30)

r2 = range(2, 7)
print(f"  range(2, 7) → {list(r2)}")  # [2, 3, 4, 5, 6] [citation:10]

# 2.3 Three Arguments: range(start, stop, step)
print("\n2.3 range(start, stop, step) - Count with step:")
print("-" * 30)

r3 = range(1, 10, 2)
print(f"  range(1, 10, 2) → {list(r3)}")  # [1, 3, 5, 7, 9] [citation:9]

# 2.4 Negative Step (counting backwards)
print("\n2.4 Negative Step - Counting Backwards:")
print("-" * 30)

r4 = range(10, 0, -1)
print(f"  range(10, 0, -1) → {list(r4)}")  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] [citation:11]

# 2.5 Empty Range
print("\n2.5 Empty Range:")
print("-" * 30)

r_empty = range(5, 2)
print(f"  range(5, 2) → {list(r_empty)}")  # [] [citation:10]

# ============================================
# PART 3: RANGE IS NOT A LIST!
# ============================================

print("\n🔑 PART 3: RANGE IS NOT A LIST! (IMPORTANT CONCEPT)")
print("-" * 50)

print("""
range() does NOT create a list. It creates a range object that produces numbers when needed. [citation:8]
This is called LAZY EVALUATION - numbers are generated on demand, not stored in memory. [citation:9]
""")

r = range(5)
print(f"  range(5) object: {r}")
print(f"  Type: {type(r)}")
print(f"  Is it a list? {isinstance(r, list)}")  # False
print(f"  Is it iterable? {hasattr(r, '__iter__')}")  # True
print(f"  Is it an iterator? {hasattr(r, '__next__')}")  # False [citation:13]

print("\n📊 Memory Comparison:")
import sys

range_obj = range(1_000_000)
list_obj = list(range(1_000_000))

print(f"  range(1,000,000) size: {sys.getsizeof(range_obj)} bytes")
print(f"  list(range(1,000,000)) size: {sys.getsizeof(list_obj):,} bytes")
print(f"  Range is {sys.getsizeof(list_obj) // sys.getsizeof(range_obj)}x smaller!")

print("\n✅ KEY INSIGHT: range is MEMORY-EFFICIENT!")
print("  It doesn't store all values. It generates them when needed.") [citation:5]

# ============================================
# PART 4: ITERABLES vs ITERATORS
# ============================================

print("\n🔄 PART 4: ITERABLES vs ITERATORS")
print("-" * 50)

print("""
ITERABLE: An object that can be iterated over (has __iter__())
ITERATOR: An object that remembers its position (has __iter__() AND __next__()) [citation:13]

range is an ITERABLE, not an ITERATOR! [citation:14]
""")

r = range(5)
print(f"  range(5) object: {r}")
print(f"  Has __iter__? {hasattr(r, '__iter__')}")   # True
print(f"  Has __next__? {hasattr(r, '__next__')}")   # False [citation:14]

# 4.1 Getting an Iterator from Range
print("\n4.1 Creating an Iterator from Range:")
print("-" * 30)

it = iter(r)  # Gets an iterator from the range object [citation:13]
print(f"  iterator object: {it}")
print(f"  Has __iter__? {hasattr(it, '__iter__')}")   # True
print(f"  Has __next__? {hasattr(it, '__next__')}")   # True

# 4.2 Using next() with Iterator
print("\n4.2 Using next() to get values:")
print("-" * 30)

it = iter(range(3))
print(f"  next(it) → {next(it)}")  # 0
print(f"  next(it) → {next(it)}")  # 1
print(f"  next(it) → {next(it)}")  # 2

# 4.3 StopIteration
print("\n4.3 StopIteration - When exhausted:")
print("-" * 30)

it = iter(range(2))
print(f"  {next(it)}")
print(f"  {next(it)}")
try:
    print(f"  {next(it)}")  # This raises StopIteration
except StopIteration:
    print("  ⚠️ StopIteration: No more values!")

# 4.4 Iterables Return Fresh Iterators
print("\n4.4 Iterables Return NEW Iterators Each Time:")
print("-" * 30)

r = range(3)
it1 = iter(r)
it2 = iter(r)

print(f"  Range object: {r}")
print(f"  iter1: {it1}")
print(f"  iter2: {it2}")
print(f"  Are they the same object? {it1 is it2}")  # False - fresh iterators!

# Each iterator remembers its own position
print(f"  next(it1) → {next(it1)}")  # 0
print(f"  next(it2) → {next(it2)}")  # 0 (starts from beginning)
print(f"  next(it1) → {next(it1)}")  # 1 (continues from where it left off)

# ============================================
# PART 5: FOR LOOP WITH RANGE (Behind the Scenes)
# ============================================

print("\n🔧 PART 5: FOR LOOP WITH RANGE - Behind the Scenes")
print("-" * 50)

print("""
When you write: for i in range(5):
Python does this:
1. Calls iter(range(5)) to get an iterator
2. Repeatedly calls next(iterator) until StopIteration [citation:14]
""")

print("\n5.1 Manual for-loop implementation:")
print("-" * 30)

r = range(5)
it = iter(r)

print("  Manual iteration:")
while True:
    try:
        value = next(it)
        print(f"    {value}")
    except StopIteration:
        print("  ✅ Iteration complete!")
        break

print("\n5.2 Same thing with for loop (Python does it automatically):")
for i in range(5):
    print(f"    {i}")

# ============================================
# PART 6: RANGE PROPERTIES
# ============================================

print("\n🔍 PART 6: RANGE PROPERTIES")
print("-" * 50)

r = range(5, 50, 3)
print(f"  Range: {r}")
print(f"  start: {r.start}")
print(f"  stop: {r.stop}")
print(f"  step: {r.step}")
print(f"  length: {len(r)}")
print(f"  index of 14: {r.index(14)}")
print(f"  Contains 20? {20 in r}")
print(f"  Contains 15? {15 in r}")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Convert String to List
Convert "Hello World" to a list of characters.

🎯 EXERCISE 2: Range to List
Create a list of even numbers from 0 to 20 using range.

🎯 EXERCISE 3: Reverse Range
Create a countdown from 10 to 1 using range and list().

🎯 EXERCISE 4: Manual Iteration
Iterate through range(4) manually using iter() and next().

🎯 EXERCISE 5: Memory Comparison
Compare memory of range(1000000) vs list(range(1000000)).

🎯 CHALLENGE: Custom Iterator
Create a range object, get its iterator, and explain why range itself isn't an iterator.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
text = "Hello World"
char_list = list(text)
print(f"Ex1 - Character list: {char_list}")

# Exercise 2
evens = list(range(0, 21, 2))
print(f"Ex2 - Even numbers 0-20: {evens}")

# Exercise 3
countdown = list(range(10, 0, -1))
print(f"Ex3 - Countdown: {countdown}")

# Exercise 4
print("Ex4 - Manual iteration:")
it = iter(range(4))
for _ in range(4):
    print(f"  next(it) → {next(it)}")

# Exercise 5
print(f"Ex5 - Memory:")
r = range(1000000)
l = list(r)
print(f"  range(1,000,000): {sys.getsizeof(r)} bytes")
print(f"  list(range(...)): {sys.getsizeof(l):,} bytes")

# Challenge
print("Ex6 - Challenge:")
r = range(5)
it = iter(r)
print(f"  range object: {r}")
print(f"  Is range an iterator? {hasattr(r, '__next__')}")  # False
print(f"  Is iterator an iterator? {hasattr(it, '__next__')}")  # True
print("  ✅ Range is an ITERABLE, not an ITERATOR!")
print("  It produces fresh iterators when needed.")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST CONSTRUCTOR & RANGE ITERABLE MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    list() CONSTRUCTOR                       │
├─────────────────────────────────────────────────────────────┤
│  list()               → [] (empty list)                    │
│  list("abc")          → ['a','b','c']      [citation:4]    │
│  list((1,2,3))        → [1,2,3]            [citation:3]    │
│  list(range(5))       → [0,1,2,3,4]        [citation:6]    │
├─────────────────────────────────────────────────────────────┤
│                    range() FUNCTION                         │
├─────────────────────────────────────────────────────────────┤
│  range(5)             → 0,1,2,3,4 (stop)                   │
│  range(2,7)           → 2,3,4,5,6 (start, stop)           │
│  range(1,10,2)        → 1,3,5,7,9 (start, stop, step)     │
│  range(10,0,-1)       → 10,9,8,7,6,5,4,3,2,1 (negative)  │
├─────────────────────────────────────────────────────────────┤
│                    ITERABLE vs ITERATOR                     │
├─────────────────────────────────────────────────────────────┤
│  Iterable: Can be iterated over (has __iter__)             │
│  Iterator: Remembers position (has __iter__ and __next__)  │
│  range:       ITERABLE (not an iterator)  [citation:14]    │
│  range_iterator: ITERATOR (produced by iter(range))        │
├─────────────────────────────────────────────────────────────┤
│                    KEY INSIGHTS                             │
├─────────────────────────────────────────────────────────────┤
│  ✅ range is LAZY: numbers generated on demand [citation:8] │
│  ✅ range is MEMORY-EFFICIENT [citation:5]                  │
│  ✅ range is an ITERABLE, not a list [citation:13]          │
│  ✅ Use list(range()) when you need a real list [citation:9]│
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Comprehensions - Python's Most Powerful List Creation Tool
""")