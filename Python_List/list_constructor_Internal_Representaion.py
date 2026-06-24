"""
LIST CONSTRUCTOR & RANGE - PART 2: INTERNAL REPRESENTATION
NeuralAICodeCraft - Deep Dive into How Lists Work

Topics Covered:
1. list() is a Type, Not a Function
2. range() is a Type, Not a Function
3. Internal Representation of Lists
4. list() vs [] - Performance Comparison
5. range() Internal Representation
"""

import sys
import time
from dis import dis

print("=" * 70)
print("🐍 LIST CONSTRUCTOR & RANGE - PART 2")
print("NeuralAICodeCraft - Internal Representation Deep Dive")
print("=" * 70)

# ============================================
# PART 1: LIST() IS A TYPE, NOT A FUNCTION
# ============================================

print("\n📚 PART 1: list() is a TYPE, Not a Function")
print("-" * 50)

print("""
Technically, `list` is a **type** (a class), not a function. [citation:1]

But in Python, calling a type looks exactly like calling a function!
This is a beautiful design choice - everything is consistent.
""")

# Demonstrating list is a type
print(f"  type(list): {type(list)}")  # <class 'type'>
print(f"  type(list()): {type(list())}")  # <class 'list'>
print(f"  isinstance([], list): {isinstance([], list)}")  # True

print("""
High Church Python: "list() is a call to a type, not a function!" [citation:1]
Vernacular Python: "Just call list() to make a list, it works!"

For practical purposes, treat it like a function - that's what Python expects! [citation:3]
""")

# ============================================
# PART 2: RANGE() IS A TYPE, NOT A FUNCTION
# ============================================

print("\n📚 PART 2: range() is a TYPE, Not a Function")
print("-" * 50)

print("""
Just like list, range is actually a **type** (a class).
It's an immutable sequence type that generates numbers on demand. [citation:1]
""")

print(f"  type(range): {type(range)}")  # <class 'type'>
print(f"  type(range(5)): {type(range(5))}")  # <class 'range'>

print("""
Why this matters:
- In Python 2, range() returned a list (function call)
- In Python 3, range() returns a range object (type call)
- This was a major improvement for memory efficiency!
""")

# ============================================
# PART 3: INTERNAL REPRESENTATION OF LISTS
# ============================================

print("\n🗂️ PART 3: INTERNAL REPRESENTATION OF LISTS")
print("-" * 50)

print("""
How Python stores lists in memory:

1. List stores POINTERS to objects, not the objects themselves
2. The internal struct is called PyListObject
3. Contains: ob_item (pointer array), allocated, and ob_size
4. Over-allocates space for efficient appends
""")

# 3.1 List Memory Layout
print("\n3.1 List Memory Layout:")
print("-" * 30)

my_list = [1, 2, 3, 4, 5]
print(f"  List: {my_list}")
print(f"  Length: {len(my_list)}")
print(f"  Memory size: {sys.getsizeof(my_list)} bytes")

print("\n  Visual representation:")
print("  ┌─────────────────────────────────────────────────────────┐")
print("  │  PyListObject                                          │")
print("  │  ├── ob_size: 5        (number of elements)            │")
print("  │  ├── allocated: 8      (capacity including overalloc)  │")
print("  │  └── ob_item: [ptr0, ptr1, ptr2, ptr3, ptr4, ...]     │")
print("  │              │    │    │    │    │                     │")
print("  │              ▼    ▼    ▼    ▼    ▼                     │")
print("  │          ┌────┬────┬────┬────┬────┐                   │")
print("  │          │int1│int2│int3│int4│int5│  (actual objects) │")
print("  │          └────┴────┴────┴────┴────┘                   │")
print("  └─────────────────────────────────────────────────────────┘")

# 3.2 Memory Growth with Append
print("\n3.2 Memory Growth with append():")
print("-" * 30)

def list_growth():
    """Show how list memory grows when appending"""
    lst = []
    for i in range(20):
        print(f"  Length: {len(lst):2}, Size: {sys.getsizeof(lst):3} bytes")
        lst.append(i)

print("  Memory growth as list grows:")
list_growth()

# 3.3 Objects Are Stored Separately
print("\n3.3 Objects Are Stored Separately:")
print("-" * 30)

a = 1000
b = 2000
my_list = [a, b]
print(f"  List: {my_list}")
print(f"  List memory: {sys.getsizeof(my_list)} bytes")
print(f"  a memory: {sys.getsizeof(a)} bytes")
print(f"  b memory: {sys.getsizeof(b)} bytes")
print("  Total objects: a, b, and the list pointers")
print("  Total memory: list + a + b")

# ============================================
# PART 4: list() vs [] - PERFORMANCE
# ============================================

print("\n⚡ PART 4: list() vs [] - Performance Differences")
print("-" * 50)

print("""
`[]` (literal) and `list()` (constructor) have different bytecode:
- `[]` → BUILD_LIST (fast, direct) [citation:5]
- `list()` → LOAD_GLOBAL + CALL_FUNCTION (slower, function lookup) [citation:5]
""")

print("\n4.1 Bytecode Comparison:")
print("-" * 30)

def literal_list():
    return []

def constructor_list():
    return list()

print("  literal_list() bytecode:")
dis(literal_list)

print("\n  constructor_list() bytecode:")
dis(constructor_list)

print("""
  Differences:
  ┌─────────────────────────────────────────────────────────────┐
  │  [] literal:    BUILD_LIST  (1 instruction)                │
  │  list():        LOAD_GLOBAL + CALL_FUNCTION (2+ instructions) │
  └─────────────────────────────────────────────────────────────┘
  `[]` is slightly faster because it doesn't need to look up `list`!
""")

# 4.2 Performance Comparison
print("\n4.2 Performance Comparison:")
print("-" * 30)

def time_constructor(n=1000000):
    """Time list() constructor"""
    start = time.time()
    for _ in range(n):
        _ = list()
    return time.time() - start

def time_literal(n=1000000):
    """Time [] literal"""
    start = time.time()
    for _ in range(n):
        _ = []
    return time.time() - start

n = 500000
literal_time = time_literal(n)
constructor_time = time_constructor(n)

print(f"  [] literal ({n} iterations): {literal_time:.4f}s")
print(f"  list() constructor ({n} iterations): {constructor_time:.4f}s")
print(f"  [] is {constructor_time / literal_time:.2f}x faster!")

print("\n📊 RECOMMENDATIONS:")
print("  ✅ Use [] for empty lists (faster, cleaner)")
print("  ✅ Use list() when converting from another iterable")
print("  ✅ Use list() when you need a list from range, string, tuple")

# ============================================
# PART 5: RANGE INTERNAL REPRESENTATION
# ============================================

print("\n🔢 PART 5: range() Internal Representation")
print("-" * 50)

print("""
range object internally stores:
├── start: starting value
├── stop: ending value (exclusive)
├── step: step value
└── length: computed from start, stop, step

It generates values on demand (lazy evaluation)!
""")

# 5.1 Range Attributes
print("\n5.1 Range Attributes:")
print("-" * 30)

r = range(5, 50, 3)
print(f"  range(5, 50, 3)")
print(f"  start: {r.start}")
print(f"  stop: {r.stop}")
print(f"  step: {r.step}")
print(f"  length: {len(r)}")
print(f"  Memory size: {sys.getsizeof(r)} bytes")

# 5.2 Range vs List Memory
print("\n5.2 Range vs List Memory Comparison:")
print("-" * 30)

for n in [10, 100, 1000, 10000, 100000]:
    range_obj = range(n)
    list_obj = list(range_obj)
    range_size = sys.getsizeof(range_obj)
    list_size = sys.getsizeof(list_obj)
    print(f"  n={n:6}: range={range_size:4} bytes, list={list_size:6} bytes, ratio={list_size/range_size:.0f}x")

# 5.3 Range Indexing (Lazy)
print("\n5.3 Range Indexing - Values Generated on Demand:")
print("-" * 30)

r = range(10)
print(f"  range(10): {r}")
print(f"  r[0]: {r[0]} (computed when accessed)")
print(f"  r[5]: {r[5]} (computed when accessed)")
print(f"  r[-1]: {r[-1]} (computed when accessed)")

# ============================================
# PART 6: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 6: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Type Check
Check the type of list and range - what do you observe?

🎯 EXERCISE 2: Memory Comparison
Compare memory of a list vs range for n=1000000.

🎯 EXERCISE 3: Bytecode Analysis
Use dis() to analyze the bytecode of [] and list().

🎯 EXERCISE 4: List Growth
Monitor memory growth as a list grows with append().

🎯 EXERCISE 5: Range Attributes
Explore the start, stop, step, and length of different ranges.

🎯 CHALLENGE: Performance Benchmark
Write a program that benchmarks [] vs list() for different sizes.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Type Check:")
print(f"  type(list): {type(list)}")
print(f"  type(range): {type(range)}")

# Exercise 2
print("\nEx2 - Memory Comparison:")
r = range(1000000)
l = list(r)
print(f"  range(1000000): {sys.getsizeof(r)} bytes")
print(f"  list(range(1000000)): {sys.getsizeof(l):,} bytes")

# Exercise 3
print("\nEx3 - Bytecode Analysis:")
print("  Use: dis([])  # Not directly possible in code")
print("  See the output in the console above.")

# Exercise 4
print("\nEx4 - List Growth:")
def show_growth():
    lst = []
    for i in range(10):
        print(f"    len={len(lst)}: {sys.getsizeof(lst)} bytes")
        lst.append(i)
show_growth()

# Exercise 5
print("\nEx5 - Range Attributes:")
r1 = range(1, 20, 3)
print(f"  range(1,20,3): start={r1.start}, stop={r1.stop}, step={r1.step}, len={len(r1)}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST CONSTRUCTOR & RANGE PART 2 - MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    list() vs []                             │
├─────────────────────────────────────────────────────────────┤
│  Feature          │  [] Literal     │  list() Constructor  │
├───────────────────┼─────────────────┼──────────────────────┤
│  Bytecode         │  BUILD_LIST     │  LOAD_GLOBAL + CALL  │
│  Speed            │  Faster         │  Slightly Slower    │
│  Use case         │  Empty/new list │  Convert iterable    │
│  Readability      │  Clean          │  Explicit            │
├─────────────────────────────────────────────────────────────┤
│                    RANGE INTERNAL STORAGE                   │
├─────────────────────────────────────────────────────────────┤
│  start: 0         │  stop: 10      │  step: 1            │
│  Values generated on demand (lazy evaluation)             │
│  Memory: ~48 bytes regardless of range size               │
├─────────────────────────────────────────────────────────────┤
│                    LIST INTERNAL STORAGE                   │
├─────────────────────────────────────────────────────────────┤
│  Stores POINTERS to objects, not objects themselves       │
│  Over-allocates capacity for efficient append()           │
│  Memory grows dynamically                                  │
│  Each element is a pointer to a Python object             │
└─────────────────────────────────────────────────────────────┘
""")