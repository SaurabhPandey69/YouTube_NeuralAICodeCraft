"""
VALUEERROR FLOAT TO INT & LIST MODIFICATION METHODS
NeuralAICodeCraft - Complete Guide

Topics Covered:
1. ValueError in Float to Int Conversion
2. Correct Conversion Methods
3. Lists are Mutable Objects
4. append() vs extend()
5. Modifying Operators (+=, *=, del)
"""

import math

print("=" * 70)
print("🐍 VALUEERROR FLOAT TO INT & LIST MODIFICATION")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: VALUEERROR EXPLAINED
# ============================================

print("\n📚 PART 1: VALUEERROR EXPLAINED")
print("-" * 50)

print("""
ValueError occurs when a function receives an argument of the right type 
but inappropriate value.

COMMON SCENARIO: Converting string "3.14" to integer
- int("3.14") → ValueError!
- int("3") → ✅ Works (3)
- float("3.14") → ✅ Works (3.14)
""")

# 1.1 Demonstrating ValueError
print("\n1.1 Demonstrating ValueError:")
print("-" * 30)

# This works
print(f"int('42') → {int('42')}")

# This fails
try:
    result = int("3.14")
    print(f"int('3.14') → {result}")
except ValueError as e:
    print(f"❌ int('3.14') → ValueError: {e}")

# Float conversion works
print(f"float('3.14') → {float('3.14')}")

# 1.2 Why This Happens
print("\n1.2 Why This Happens:")
print("-" * 30)

print("""
int('3.14') fails because:
├── int() expects a string containing ONLY digits (0-9)
├── It CANNOT handle decimal points
├── It CANNOT handle negative signs (except at start)
└── It CANNOT handle fractions

SOLUTION: Convert to float first, then to int!
""")

# ============================================
# PART 2: CORRECT CONVERSION METHODS
# ============================================

print("\n🎯 PART 2: CORRECT CONVERSION METHODS")
print("-" * 50)

print("""
METHODS TO CONVERT FLOAT STRING TO INTEGER:

1. Two-step conversion: int(float("3.14"))
2. Rounding: int(float("3.14")) → 3 (truncates)
3. math.floor() → rounds down
4. math.ceil() → rounds up
5. round() → rounds to nearest
""")

# 2.1 Basic Conversion
print("\n2.1 Basic Conversion (int(float())):")
print("-" * 30)

float_str = "3.14"
result = int(float(float_str))
print(f"  int(float('3.14')) → {result}")

# 2.2 Floor vs Ceil vs Round
print("\n2.2 Floor vs Ceil vs Round:")
print("-" * 30)

values = ["3.1", "3.5", "3.9", "-3.1", "-3.5", "-3.9"]

print(f"{'Value':<8} {'int(float)':<12} {'floor()':<12} {'ceil()':<12} {'round()':<12}")
print("-" * 60)

for val in values:
    num = float(val)
    int_conv = int(num)
    floor_val = math.floor(num)
    ceil_val = math.ceil(num)
    round_val = round(num)
    print(f"{val:<8} {int_conv:<12} {floor_val:<12} {ceil_val:<12} {round_val:<12}")

print("\n📌 KEY DIFFERENCES:")
print("  int() → Truncates toward zero")
print("  floor() → Rounds down (toward -∞)")
print("  ceil() → Rounds up (toward +∞)")
print("  round() → Rounds to nearest (banker's rounding)")

# 2.3 Practical Example
print("\n2.3 Practical Example: User Input:")
print("-" * 30)

def get_valid_integer(user_input):
    """Safely convert user input to integer"""
    try:
        # Try direct conversion first
        return int(user_input)
    except ValueError:
        try:
            # Try float conversion
            return int(float(user_input))
        except ValueError:
            return None

test_inputs = ["42", "3.14", "2.7", "abc", "-5.9", "100.0"]

print("  Testing user input conversion:")
for inp in test_inputs:
    result = get_valid_integer(inp)
    print(f"    '{inp}' → {result}")

# ============================================
# PART 3: LISTS ARE MUTABLE OBJECTS
# ============================================

print("\n📋 PART 3: LISTS ARE MUTABLE OBJECTS")
print("-" * 50)

print("""
MUTABLE: Can be changed after creation.
- Lists can be modified in-place
- No new object is created
- Memory efficient!

IMMUTABLE: Cannot be changed after creation.
- Strings, tuples, integers, floats
- Modifications create new objects
""")

# 3.1 Demonstrating Mutability
print("\n3.1 Demonstrating Mutability:")
print("-" * 30)

my_list = [1, 2, 3]
print(f"Original list: {my_list}")
print(f"ID before modification: {id(my_list)}")

my_list.append(4)
print(f"After append: {my_list}")
print(f"ID after modification: {id(my_list)}")
print(f"Same object? {id(my_list) == id(my_list)}")  # True - same object!

# 3.2 Immutable Comparison
print("\n3.2 Immutable Objects (Strings):")
print("-" * 30)

my_str = "Hello"
print(f"Original string: {my_str}")
print(f"ID before: {id(my_str)}")

my_str = my_str + " World"
print(f"After concatenation: {my_str}")
print(f"ID after: {id(my_str)}")
print(f"Same object? {id(my_str) == id(my_str)}")  # New object!

# ============================================
# PART 4: append() vs extend()
# ============================================

print("\n⚖️ PART 4: append() vs extend() - THE CRITICAL DIFFERENCE")
print("-" * 50)

print("""
KEY DIFFERENCE:
- append() adds the object ITSELF → Nested list
- extend() adds the ELEMENTS → Flattened list
""")

# 4.1 Demonstration
print("\n4.1 append() vs extend() Demonstration:")
print("-" * 30)

# Using append()
list_a = [1, 2, 3]
list_a.append([4, 5, 6])
print(f"append([4,5,6]) → {list_a}")  # [1, 2, 3, [4, 5, 6]]

# Using extend()
list_b = [1, 2, 3]
list_b.extend([4, 5, 6])
print(f"extend([4,5,6]) → {list_b}")  # [1, 2, 3, 4, 5, 6]

# 4.2 Visual Comparison
print("\n4.2 Visual Comparison:")
print("-" * 30)

print("""
┌─────────────────────────────────────────────────────────────┐
│  Original List: [1, 2, 3]                                  │
├─────────────────────────────────────────────────────────────┤
│  append([4, 5])   → [1, 2, 3, [4, 5]]  # Whole list added  │
│  extend([4, 5])   → [1, 2, 3, 4, 5]    # Elements added    │
└─────────────────────────────────────────────────────────────┘
""")

# 4.3 Different Types
print("\n4.3 append vs extend - Different Types:")
print("-" * 30)

my_list = [1, 2, 3]
my_list_append = my_list.copy()
my_list_extend = my_list.copy()

# Append tuple
my_list_append.append((4, 5))
print(f"append((4,5)) → {my_list_append}")

# Extend tuple
my_list_extend.extend((4, 5))
print(f"extend((4,5)) → {my_list_extend}")

# Append string
list_append_str = [1, 2, 3]
list_append_str.append("ABC")
print(f"\nappend('ABC') → {list_append_str}")

# Extend string
list_extend_str = [1, 2, 3]
list_extend_str.extend("ABC")
print(f"extend('ABC') → {list_extend_str}")

# ============================================
# PART 5: MODIFYING OPERATORS
# ============================================

print("\n🔧 PART 5: MODIFYING OPERATORS (+=, *=, del)")
print("-" * 50)

# 5.1 += Operator (extends in-place)
print("\n5.1 += Operator (in-place extend):")
print("-" * 30)

my_list = [1, 2, 3]
print(f"Before: {my_list}")
print(f"ID before: {id(my_list)}")

my_list += [4, 5]
print(f"After += [4,5]: {my_list}")
print(f"ID after: {id(my_list)}")
print(f"Same object? {id(my_list) == id(my_list)}")  # True

# 5.2 *= Operator (repeats in-place)
print("\n5.2 *= Operator (in-place repeat):")
print("-" * 30)

my_list = [1, 2]
print(f"Before: {my_list}")
print(f"ID before: {id(my_list)}")

my_list *= 3
print(f"After *= 3: {my_list}")
print(f"ID after: {id(my_list)}")

# 5.3 del (remove elements)
print("\n5.3 del - Remove Elements:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Before: {fruits}")

del fruits[1]  # Remove banana
print(f"After del fruits[1]: {fruits}")

del fruits[1:3]  # Remove cherry and date
print(f"After del fruits[1:3]: {fruits}")

# 5.4 append vs +=
print("\n5.4 append vs += (Important Difference):")
print("-" * 30)

print("""
append() adds a single element (can be any object)
+= extends the list with elements from an iterable

These are NOT the same!
""")

list1 = [1, 2, 3]
list1.append([4, 5])
print(f"append([4,5]) → {list1}")

list2 = [1, 2, 3]
list2 += [4, 5]
print(f"+= [4,5] → {list2}")

# ============================================
# PART 6: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 6: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Fix ValueError
Convert "3.14" to integer correctly.

🎯 EXERCISE 2: append vs extend
Explain what happens with append(['a','b']) vs extend(['a','b'])

🎯 EXERCISE 3: += Operator
Use += to extend a list with another list.

🎯 EXERCISE 4: del Operator
Remove elements from a list using del.

🎯 EXERCISE 5: Type Conversion
Create a function that safely converts any string to integer.

🎯 CHALLENGE: Mixed Types
Combine append, extend, += on the same list and track changes.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Fix ValueError:")
value = "3.14"
print(f"  int(float('3.14')) → {int(float(value))}")

# Exercise 2
print("\nEx2 - append vs extend:")
append_demo = [1, 2, 3]
append_demo.append(['a', 'b'])
print(f"  append(['a','b']) → {append_demo}")

extend_demo = [1, 2, 3]
extend_demo.extend(['a', 'b'])
print(f"  extend(['a','b']) → {extend_demo}")

# Exercise 3
print("\nEx3 - += Operator:")
list3 = [10, 20, 30]
list3 += [40, 50]
print(f"  += [40,50] → {list3}")

# Exercise 4
print("\nEx4 - del Operator:")
fruits = ['apple', 'banana', 'cherry', 'date']
del fruits[-1]
print(f"  del fruits[-1] → {fruits}")

# Exercise 5
print("\nEx5 - Safe Conversion:")
def safe_int(value):
    try:
        return int(value)
    except ValueError:
        try:
            return int(float(value))
        except ValueError:
            return None

test_values = ["42", "3.14", "2.7", "abc"]
for val in test_values:
    print(f"  safe_int('{val}') → {safe_int(val)}")

# Challenge
print("\nChallenge - Mixed Methods:")
mixed = [1, 2]
mixed.append([3, 4])
mixed.extend([5, 6])
mixed += [7, 8]
print(f"  Mixed list: {mixed}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ VALUEERROR & LIST METHODS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│              FLOAT TO INT CONVERSION                        │
├─────────────────────────────────────────────────────────────┤
│  int("3.14")      → ❌ ValueError                          │
│  int(float("3.14")) → 3 (truncates)                       │
│  math.floor(3.14) → 3 (rounds down)                       │
│  math.ceil(3.14)  → 4 (rounds up)                         │
│  round(3.14)      → 3 (nearest)                           │
├─────────────────────────────────────────────────────────────┤
│              LIST MODIFICATION                              │
├─────────────────────────────────────────────────────────────┤
│  append(x)        → Adds x as a single element             │
│  extend(iter)     → Adds elements from iterable            │
│  += [x,y]         → In-place extend                       │
│  *= n             → In-place repeat                       │
│  del list[start]  → Remove elements                       │
├─────────────────────────────────────────────────────────────┤
│              MUTABLE vs IMMUTABLE                          │
├─────────────────────────────────────────────────────────────┤
│  ✅ Lists are MUTABLE (changed in-place)                   │
│  ❌ Strings are IMMUTABLE (new object on change)           │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Methods - insert(), remove(), pop(), clear()
""")