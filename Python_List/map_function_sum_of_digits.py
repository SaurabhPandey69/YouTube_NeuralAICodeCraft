"""
PYTHON map() FUNCTION - SUM OF DIGITS PROBLEM WALKTHROUGH
NeuralAICodeCraft - Complete Guide to map() Function

Topics Covered:
1. Sum of Digits Problem
2. For Loop Solution
3. List Comprehension Solution
4. map() Function Solution
5. Map Iterator Object
6. Converting Map to List
7. Performance Comparison
"""

import time

print("=" * 70)
print("🐍 PYTHON map() FUNCTION - SUM OF DIGITS COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: SUM OF DIGITS PROBLEM
# ============================================

print("\n📚 PART 1: SUM OF DIGITS PROBLEM")
print("-" * 50)

print("""
PROBLEM: Sum of Digits of Each Number from 10 to n

Definition: Sum of digits of a number is the sum of its individual digits.

Examples:
- 123 → 1 + 2 + 3 = 6
- 456 → 4 + 5 + 6 = 15
- 789 → 7 + 8 + 9 = 24

Task: Calculate sum of digits for all numbers from 10 to n
""")


def sum_of_digits(num):
    """Calculate sum of digits of a number"""
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total


print("\nTesting sum_of_digits function:")
test_numbers = [123, 456, 789, 1010]
for num in test_numbers:
    result = sum_of_digits(num)
    print(f"  sum_of_digits({num}) = {result}")

# ============================================
# PART 2: FOR LOOP SOLUTION
# ============================================

print("\n🔄 PART 2: FOR LOOP SOLUTION")
print("-" * 50)

print("""
APPROACH: Using a for loop with function calls

PROS:
├── Simple and readable
├── Easy to debug
├── Good for beginners

CONS:
├── Verbose (multiple lines)
├── Slower for large data
└── Not Pythonic
""")


def sum_of_digits_loop(n):
    """Calculate sum of digits for numbers 10 to n using for loop"""
    results = []
    for num in range(10, n + 1):
        digit_sum = sum_of_digits(num)
        results.append(digit_sum)
    return results


# Test the function
print("Testing sum_of_digits_loop(20):")
result_loop = sum_of_digits_loop(20)
print(f"  Results: {result_loop}")

print("\nStep-by-step execution:")
print("  Number → Sum of Digits")
print("  " + "-" * 25)
for i, num in enumerate(range(10, 21), 10):
    digit_sum = sum_of_digits(i)
    print(f"  {i:4} → {digit_sum:3}")

# ============================================
# PART 3: LIST COMPREHENSION SOLUTION
# ============================================

print("\n⚡ PART 3: LIST COMPREHENSION SOLUTION")
print("-" * 50)

print("""
APPROACH: Using list comprehension

PROS:
├── Concise (single line)
├── Pythonic
├── Fast

CONS:
├── Less readable for complex logic
├── Harder to debug
└── Not suitable for very complex operations
""")


def sum_of_digits_comp(n):
    """Calculate sum of digits for numbers 10 to n using list comprehension"""
    return [sum_of_digits(num) for num in range(10, n + 1)]


# Test the function
print("Testing sum_of_digits_comp(20):")
result_comp = sum_of_digits_comp(20)
print(f"  Results: {result_comp}")

print("\nComparison with for loop:")
print(f"  For loop result: {result_loop}")
print(f"  Comprehension result: {result_comp}")
print(f"  Same result? {result_loop == result_comp}")

# ============================================
# PART 4: map() FUNCTION BASICS
# ============================================

print("\n🔧 PART 4: map() FUNCTION BASICS")
print("-" * 50)

print("""
WHAT IS map()?
├── Built-in Python function
├── Applies a function to every item in an iterable
├── Returns a MAP OBJECT (iterator)
├── Lazy evaluation (values computed on demand)
└── More efficient than loops for large data

SYNTAX: map(function, iterable1, iterable2, ...)

PARAMETERS:
├── function: The function to apply
├── iterable: The iterable to process
└── Returns: Map object (iterator)
""")

# 4.1 Basic map() Example
print("\n4.1 Basic map() Example:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]


def square(x):
    return x ** 2


map_obj = map(square, numbers)
print(f"Original list: {numbers}")
print(f"map object: {map_obj}")
print(f"Type: {type(map_obj)}")

# Convert to list to see results
result_list = list(map_obj)
print(f"Result as list: {result_list}")

print("\n⚠️ IMPORTANT: map object can only be iterated ONCE!")
print("  After converting to list, the map object is exhausted.")


# 4.2 map() with Lambda
print("\n4.2 map() with Lambda:")
print("-" * 30)

# Using lambda (inline function)
squares = list(map(lambda x: x ** 2, numbers))
print(f"Using lambda: {squares}")

# 4.3 map() with Built-in Functions
print("\n4.3 map() with Built-in Functions:")
print("-" * 30)

# Convert strings to integers
str_nums = ["1", "2", "3", "4", "5"]
int_nums = list(map(int, str_nums))
print(f"Strings to ints: {int_nums}")

# Convert to uppercase
words = ["hello", "world", "python"]
upper_words = list(map(str.upper, words))
print(f"Uppercase: {upper_words}")

# 4.4 map() with Multiple Iterables
print("\n4.4 map() with Multiple Iterables:")
print("-" * 30)

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

# Add corresponding elements
sums = list(map(lambda x, y: x + y, list1, list2))
print(f"list1: {list1}")
print(f"list2: {list2}")
print(f"Sum: {sums}")

# Multiple operations
products = list(map(lambda x, y: x * y, list1, list2))
print(f"Product: {products}")

# ============================================
# PART 5: map() SOLUTION FOR SUM OF DIGITS
# ============================================

print("\n🎯 PART 5: map() SOLUTION FOR SUM OF DIGITS")
print("-" * 50)

print("""
APPROACH: Using map() function

PROS:
├── Clean and functional
├── Lazy evaluation
├── Memory efficient
├── Fast for large data

CONS:
├── Slightly less readable for beginners
├── Map object needs conversion
└── One-time use (iterator)
""")


def sum_of_digits_map(n):
    """Calculate sum of digits for numbers 10 to n using map()"""
    return list(map(sum_of_digits, range(10, n + 1)))


# Test the function
print("Testing sum_of_digits_map(20):")
result_map = sum_of_digits_map(20)
print(f"  Results: {result_map}")

print("\nComparison of all methods (n=20):")
print(f"  For loop result: {result_loop}")
print(f"  Comprehension result: {result_comp}")
print(f"  map() result: {result_map}")
print(f"  All methods produce same result? {result_loop == result_comp == result_map}")

# ============================================
# PART 6: MAP ITERATOR OBJECT - DEEP DIVE
# ============================================

print("\n🔍 PART 6: MAP ITERATOR OBJECT - DEEP DIVE")
print("-" * 50)

print("""
WHAT IS A MAP ITERATOR?
├── A lazy iterator that computes values on demand
├── Does NOT store all values in memory
├── Can be iterated only once
├── Supports next() function
└── Raises StopIteration when exhausted
""")

# 6.1 Creating and Iterating
print("\n6.1 Creating and Iterating:")
print("-" * 30)

my_map = map(lambda x: x ** 2, [1, 2, 3, 4, 5])

print("Manual iteration with next():")
print(f"  next(my_map) → {next(my_map)}")
print(f"  next(my_map) → {next(my_map)}")
print(f"  next(my_map) → {next(my_map)}")
print(f"  next(my_map) → {next(my_map)}")
print(f"  next(my_map) → {next(my_map)}")

# 6.2 Exhausting the Map
print("\n6.2 Exhausting the Map (StopIteration):")
print("-" * 30)

my_map = map(lambda x: x ** 2, [1, 2])
print(f"  next(my_map) → {next(my_map)}")
print(f"  next(my_map) → {next(my_map)}")
try:
    print(f"  next(my_map) → {next(my_map)}")  # This will raise StopIteration
except StopIteration:
    print("  ⚠️ StopIteration! Map is exhausted.")

# 6.3 Converting Map to Different Types
print("\n6.3 Converting Map to Different Types:")
print("-" * 30)

original_map = map(lambda x: x ** 2, [1, 2, 3, 4, 5])

# Convert to list
list_result = list(original_map)
print(f"  As list: {list_result}")

# Map is now exhausted
print(f"  Map is exhausted: {list(original_map)}")  # Empty list

print("\n💡 TIP: Convert map to list/tuple/set immediately if you need reuse!")

# 6.4 map() with Lazy Evaluation
print("\n6.4 Lazy Evaluation (Values computed on demand):")
print("-" * 30)


def expensive_function(x):
    print(f"  Computing for {x}...")
    return x ** 2


print("Creating map (no computation yet):")
my_lazy_map = map(expensive_function, [1, 2, 3])

print("\nNow iterating (computation happens):")
for value in my_lazy_map:
    print(f"  Got: {value}")

print("\n✅ Values are computed ONLY when needed!")

# ============================================
# PART 7: PERFORMANCE COMPARISON
# ============================================

print("\n⚡ PART 7: PERFORMANCE COMPARISON")
print("-" * 50)

print("""
PERFORMANCE SUMMARY:
├── For Loop: Slowest (Python-level iteration)
├── List Comprehension: Fast (optimized C-level)
└── map(): Fastest (C-level, lazy)
""")


def performance_test(n):
    """Test performance of all three methods"""
    # For loop
    start = time.time()
    result_loop = []
    for num in range(10, n + 1):
        result_loop.append(sum_of_digits(num))
    loop_time = time.time() - start

    # List comprehension
    start = time.time()
    result_comp = [sum_of_digits(num) for num in range(10, n + 1)]
    comp_time = time.time() - start

    # map()
    start = time.time()
    result_map = list(map(sum_of_digits, range(10, n + 1)))
    map_time = time.time() - start

    # Verify all methods produce same result
    same = result_loop == result_comp == result_map

    return {
        'n': n,
        'loop_time': loop_time,
        'comp_time': comp_time,
        'map_time': map_time,
        'same_result': same
    }


# Test with different sizes
print("\nPerformance Test Results:")
print("-" * 50)
print(f"{'n':<10} {'Loop (s)':<12} {'Comp (s)':<12} {'map() (s)':<12} {'Fastest'}")
print("-" * 60)

for n in [1000, 10000, 50000]:
    results = performance_test(n)
    fastest = min(results['loop_time'], results['comp_time'], results['map_time'])
    if fastest == results['map_time']:
        fastest_name = "map()"
    elif fastest == results['comp_time']:
        fastest_name = "Comp"
    else:
        fastest_name = "Loop"

    print(f"{n:<10} {results['loop_time']:<12.4f} {results['comp_time']:<12.4f} {results['map_time']:<12.4f} {fastest_name}")

print("\n✅ All methods produce identical results!")

# ============================================
# PART 8: ADVANCED map() TECHNIQUES
# ============================================

print("\n🚀 PART 8: ADVANCED map() TECHNIQUES")
print("-" * 50)

# 8.1 map() with Multiple Functions
print("\n8.1 map() with Multiple Functions:")
print("-" * 30)

data = [1, 2, 3, 4, 5]
operations = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x + 10]

for op in operations:
    result = list(map(op, data))
    print(f"  {op.__name__ if hasattr(op, '__name__') else 'op'}: {result}")

# 8.2 Chaining map() with filter()
print("\n8.2 Chaining map() with filter():")
print("-" * 30)

numbers = range(1, 21)

# Filter even numbers, then square them
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"  Squares of even numbers 1-20: {result}")

# 8.3 map() with zip()
print("\n8.3 map() with zip():")
print("-" * 30)

names = ['Alice', 'Bob', 'Charlie', 'David']
ages = [25, 30, 35, 28]

# Combine name and age into formatted string
formatted = list(map(lambda n, a: f"{n} ({a} years)", names, ages))
for person in formatted:
    print(f"  {person}")

# 8.4 map() with enumerate()
print("\n8.4 map() with enumerate():")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']

# Get index and value
result = list(map(lambda x: f"{x[0]}: {x[1]}", enumerate(fruits)))
print(f"  Indexed fruits: {result}")

# ============================================
# PART 9: COMMON MISTAKES WITH map()
# ============================================

print("\n⚠️ PART 9: COMMON MISTAKES WITH map()")
print("-" * 50)

# 9.1 Forgetting to Convert map()
print("\n9.1 Mistake #1: Forgetting to Convert map()")
print("-" * 30)

print("""
❌ WRONG:
    result = map(sum_of_digits, range(10, 21))
    print(result)  # Prints: <map object at 0x...>

✅ CORRECT:
    result = list(map(sum_of_digits, range(10, 21)))
    print(result)  # Prints: [1, 2, 3, ...]
""")

# 9.2 Reusing map() Object
print("\n9.2 Mistake #2: Reusing map() Object")
print("-" * 30)

print("""
❌ WRONG:
    my_map = map(lambda x: x ** 2, [1, 2, 3])
    print(list(my_map))  # [1, 4, 9]
    print(list(my_map))  # [] (map is exhausted!)

✅ CORRECT:
    my_list = list(map(lambda x: x ** 2, [1, 2, 3]))
    print(my_list)  # [1, 4, 9]
    print(my_list)  # [1, 4, 9] (list can be reused)
""")

# 9.3 Using map() with Function That Has Side Effects
print("\n9.3 Mistake #3: Function with Side Effects")
print("-" * 30)


def side_effect(x):
    print(f"  Processing {x}...")
    return x ** 2


print("⚠️ map() executes function lazily, so side effects occur when iterating:")
my_map = map(side_effect, [1, 2, 3])
print("  map created (no output yet)")
print("  Now iterating:")
for value in my_map:
    print(f"    Got: {value}")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Sum of Digits from 1 to 100
Use map() to calculate sum of digits for numbers 1 to 100.

🎯 EXERCISE 2: Sum of Squares of Digits
Create a function that calculates sum of squares of digits using map().

🎯 EXERCISE 3: Multiple Iterables
Use map() with three lists: [1,2,3], [4,5,6], [7,8,9] to add them.

🎯 EXERCISE 4: String Transformation
Use map() to convert a list of strings to title case.

🎯 EXERCISE 5: map() with filter
Find squares of even numbers from 1 to 30 using map() and filter().

🎯 CHALLENGE: Performance Test
Test performance of map() vs comprehension for n=1000000.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Sum of Digits 1-100:")
result1 = list(map(sum_of_digits, range(1, 101)))
print(f"  First 10 results: {result1[:10]}...")

# Exercise 2
print("\nEx2 - Sum of Squares of Digits:")


def sum_squares_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** 2
        num //= 10
    return total


result2 = list(map(sum_squares_digits, range(10, 31)))
print(f"  Sum of squares of digits (10-30): {result2}")

# Exercise 3
print("\nEx3 - Adding Three Lists:")
a = [1, 2, 3, 4, 5]
b = [10, 20, 30, 40, 50]
c = [100, 200, 300, 400, 500]
result3 = list(map(lambda x, y, z: x + y + z, a, b, c))
print(f"  Sum: {result3}")

# Exercise 4
print("\nEx4 - String to Title Case:")
names = ['alice', 'bob', 'charlie', 'david']
result4 = list(map(str.title, names))
print(f"  Title case: {result4}")

# Exercise 5
print("\nEx5 - Squares of Even Numbers:")
result5 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(1, 31))))
print(f"  Squares of evens: {result5}")

# Challenge
print("\nChallenge - Performance Test (n=1000000):")
print("  Try: result = list(map(sum_of_digits, range(1, 1000001)))")
print("  vs: result = [sum_of_digits(x) for x in range(1, 1000001)]")
print("  map() will be faster due to C-level iteration!")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ map() FUNCTION & SUM OF DIGITS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    map() FUNCTION                           │
├─────────────────────────────────────────────────────────────┤
│  map(function, iterable)  → Creates map object            │
│  list(map(...))           → Converts to list              │
│  tuple(map(...))          → Converts to tuple             │
│  set(map(...))            → Converts to set               │
├─────────────────────────────────────────────────────────────┤
│                    map() with Lambdas                       │
├─────────────────────────────────────────────────────────────┤
│  map(lambda x: x**2, [1,2,3]) → [1,4,9]                   │
│  map(lambda x,y: x+y, [1,2], [3,4]) → [4,6]               │
│  map(str.upper, ['a','b']) → ['A','B']                    │
├─────────────────────────────────────────────────────────────┤
│                SUM OF DIGITS SOLUTIONS                      │
├─────────────────────────────────────────────────────────────┤
│  For Loop:      Traditional, readable                     │
│  Comprehension: Pythonic, concise                         │
│  map():         Fastest, memory efficient                 │
├─────────────────────────────────────────────────────────────┤
│                    KEY RULES                               │
├─────────────────────────────────────────────────────────────┤
│  ✅ map() returns an iterator (lazy)                      │
│  ✅ Convert map to list/tuple/set to see results          │
│  ✅ map object can be iterated only ONCE                 │
│  ✅ map() executes function in C → Faster                │
│  ✅ Use map() for simple transformations                  │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: filter() Function Explained
""")