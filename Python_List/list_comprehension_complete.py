"""
LIST COMPREHENSION IN PYTHON - COMPLETE GUIDE
NeuralAICodeCraft - Master Pythonic List Creation

Topics Covered:
1. Basic List Comprehension
2. For Loop vs List Comprehension
3. Conditional Statements
4. Nested List Comprehensions
5. Multiple Iterators
6. Real-World Examples
"""

print("=" * 70)
print("🐍 LIST COMPREHENSION IN PYTHON - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: WHAT IS LIST COMPREHENSION?
# ============================================

print("\n📚 PART 1: WHAT IS LIST COMPREHENSION?")
print("-" * 50)

print("""
List comprehension is a CONCISE way to create lists in Python.

SYNTAX:
    [expression for item in iterable]

BENEFITS:
├── More concise (1 line vs multiple lines)
├── Faster than traditional loops (optimized in C)
├── More readable (once you understand it)
└── Considered "Pythonic" - the Python way!
""")

# 1.1 Basic Example
print("\n1.1 Basic Example - Squares of numbers:")
print("-" * 30)

# Traditional for loop
squares_for = []
for i in range(1, 6):
    squares_for.append(i ** 2)
print(f"  For loop: {squares_for}")

# List comprehension
squares_comp = [i ** 2 for i in range(1, 6)]
print(f"  List comprehension: {squares_comp}")

# 1.2 Transforming Data
print("\n1.2 Transforming Data - Convert to uppercase:")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date"]

# For loop
uppercase_for = []
for fruit in fruits:
    uppercase_for.append(fruit.upper())
print(f"  For loop: {uppercase_for}")

# List comprehension
uppercase_comp = [fruit.upper() for fruit in fruits]
print(f"  List comprehension: {uppercase_comp}")

# 1.3 Creating from Range
print("\n1.3 Creating from Range:")
print("-" * 30)

even_numbers = [x for x in range(2, 21, 2)]
print(f"  Even numbers 2-20: {even_numbers}")

# ============================================
# PART 2: FOR LOOP vs LIST COMPREHENSION
# ============================================

print("\n⚖️ PART 2: FOR LOOP vs LIST COMPREHENSION")
print("-" * 50)

# 2.1 Code Length Comparison
print("\n2.1 Code Length Comparison:")
print("-" * 30)

print("  For loop (5 lines):")
print("    result = []")
print("    for i in range(10):")
print("        result.append(i ** 2)")
print("    print(result)")

print("\n  List comprehension (1 line):")
print("    result = [i ** 2 for i in range(10)]")

# 2.2 Performance Comparison
print("\n2.2 Performance Comparison:")
print("-" * 30)

import time

def time_for_loop(n):
    """Time traditional for loop"""
    start = time.time()
    result = []
    for i in range(n):
        result.append(i ** 2)
    return time.time() - start

def time_comprehension(n):
    """Time list comprehension"""
    start = time.time()
    result = [i ** 2 for i in range(n)]
    return time.time() - start

n = 1000000
for_time = time_for_loop(n)
comp_time = time_comprehension(n)

print(f"  For loop ({n} elements): {for_time:.4f}s")
print(f"  List comprehension ({n} elements): {comp_time:.4f}s")
print(f"  List comprehension is {for_time/comp_time:.1f}x faster!")

# 2.3 Readability Comparison
print("\n2.3 Readability Comparison:")
print("-" * 30)

# For loop (very readable, good for complex logic)
print("  For loop (readable):")
names = ["alice", "bob", "charlie", "diana"]
capitalized = []
for name in names:
    capitalized.append(name.capitalize())
print(f"    {capitalized}")

# List comprehension (concise)
print("  List comprehension (concise):")
capitalized_comp = [name.capitalize() for name in names]
print(f"    {capitalized_comp}")

print("\n💡 TIP: Use comprehension for simple transformations, for loops for complex logic!")

# ============================================
# PART 3: CONDITIONAL STATEMENTS (if filter)
# ============================================

print("\n🔀 PART 3: CONDITIONAL STATEMENTS - if FILTER")
print("-" * 50)

print("""
SYNTAX:
    [expression for item in iterable if condition]

This filters items - only includes items where condition is True
""")

# 3.1 Basic if filter
print("\n3.1 Filtering Even Numbers:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For loop with if
even_for = []
for num in numbers:
    if num % 2 == 0:
        even_for.append(num)
print(f"  For loop: {even_for}")

# List comprehension with if
even_comp = [num for num in numbers if num % 2 == 0]
print(f"  List comprehension: {even_comp}")

# 3.2 Filtering Strings by Length
print("\n3.2 Filtering Strings by Length:")
print("-" * 30)

words = ["hello", "world", "python", "is", "amazing", "fun"]

# Words with length > 3
long_words = [word for word in words if len(word) > 3]
print(f"  Words with length > 3: {long_words}")

# 3.3 Multiple Conditions
print("\n3.3 Multiple Conditions (and):")
print("-" * 30)

numbers = list(range(1, 21))

# Numbers that are even AND divisible by 3
filtered = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
print(f"  Even and divisible by 3: {filtered}")

# 3.4 Complex Filtering
print("\n3.4 Complex Filtering - Custom Function:")
print("-" * 30)

def is_prime(n):
    """Check if number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [num for num in range(1, 51) if is_prime(num)]
print(f"  Prime numbers 1-50: {primes}")

# ============================================
# PART 4: if-else IN EXPRESSION
# ============================================

print("\n🔄 PART 4: if-else IN EXPRESSION")
print("-" * 50)

print("""
SYNTAX:
    [expression_if_true if condition else expression_if_false for item in iterable]

This transforms items - applies conditional expression
NOTE: Condition goes BEFORE the for loop!
""")

# 4.1 Basic if-else
print("\n4.1 Even/Odd Transformation:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# For loop with if-else
result_for = []
for num in numbers:
    if num % 2 == 0:
        result_for.append("even")
    else:
        result_for.append("odd")
print(f"  For loop: {result_for}")

# List comprehension with if-else
result_comp = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(f"  List comprehension: {result_comp}")

# 4.2 if-else with Different Values
print("\n4.2 if-else with Different Values:")
print("-" * 30)

numbers = [-5, -3, 0, 2, 4, 7, -2, 8]

# Classify numbers
classification = ["positive" if num > 0 else "negative" if num < 0 else "zero" for num in numbers]
print(f"  Classification: {classification}")

# 4.3 if-else with Math Operations
print("\n4.3 if-else with Math Operations:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square if even, cube if odd
transformed = [num ** 2 if num % 2 == 0 else num ** 3 for num in numbers]
print(f"  Even→Square, Odd→Cube: {transformed}")

# 4.4 if-else vs if filter (Important!)
print("\n4.4 if-else vs if filter - Understanding the Difference:")
print("-" * 30)

print("  if filter (keeps/excludes items):")
filtered = [num for num in range(1, 11) if num % 2 == 0]
print(f"    [num for num in range(10) if num % 2 == 0] → {filtered}")

print("\n  if-else in expression (transforms all items):")
transformed = ["even" if num % 2 == 0 else "odd" for num in range(1, 11)]
print(f"    ['even' if num % 2 == 0 else 'odd' for num in range(10)] → {transformed}")

# ============================================
# PART 5: NESTED LIST COMPREHENSIONS
# ============================================

print("\n📦 PART 5: NESTED LIST COMPREHENSIONS")
print("-" * 50)

print("""
Nested list comprehensions are like nested for loops.
Used for creating lists from lists of lists (matrices).
""")

# 5.1 Basic Nested Comprehension
print("\n5.1 Flattening a Matrix:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# For loop
flat_for = []
for row in matrix:
    for num in row:
        flat_for.append(num)
print(f"  For loop flatten: {flat_for}")

# List comprehension
flat_comp = [num for row in matrix for num in row]
print(f"  List comprehension flatten: {flat_comp}")

# 5.2 Creating Matrix with Comprehensions
print("\n5.2 Creating a Matrix:")
print("-" * 30)

# 3x3 matrix with zeros
matrix_zero = [[0 for _ in range(3)] for _ in range(3)]
print(f"  3x3 zero matrix: {matrix_zero}")

# Multiplication table
mult_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("  5x5 Multiplication table:")
for row in mult_table:
    print(f"    {row}")

# 5.3 Filtering in Nested Comprehension
print("\n5.3 Filtering in Nested Comprehension:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten even numbers only
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(f"  Even numbers flattened: {even_flat}")

# 5.4 Transform in Nested Comprehension
print("\n5.4 Transform in Nested Comprehension:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Square each element
squared_matrix = [[num ** 2 for num in row] for row in matrix]
print(f"  Squared matrix:")
for row in squared_matrix:
    print(f"    {row}")

# ============================================
# PART 6: MULTIPLE ITERATORS
# ============================================

print("\n🔗 PART 6: MULTIPLE ITERATORS")
print("-" * 50)

print("""
SYNTAX:
    [expression for item1 in iterable1 for item2 in iterable2]

Creates a cartesian product of two iterables.
""")

# 6.1 Cartesian Product
print("\n6.1 Cartesian Product:")
print("-" * 30)

colors = ["red", "blue"]
sizes = ["S", "M", "L"]

# For loop
combinations_for = []
for color in colors:
    for size in sizes:
        combinations_for.append((color, size))
print(f"  For loop: {combinations_for}")

# List comprehension
combinations_comp = [(color, size) for color in colors for size in sizes]
print(f"  List comprehension: {combinations_comp}")

# 6.2 Coordinates
print("\n6.2 Creating Coordinates:")
print("-" * 30)

coordinates = [(x, y) for x in range(3) for y in range(3)]
print(f"  All coordinates 0-2: {coordinates}")

# ============================================
# PART 7: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 7: REAL-WORLD EXAMPLES")
print("-" * 30)

# 7.1 Data Processing
print("\n7.1 Data Processing - Extract Emails:")
print("-" * 30)

data = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@work.com"},
    {"name": "Charlie", "email": "charlie@test.org"},
]

emails = [person["email"] for person in data]
print(f"  Emails: {emails}")

# 7.2 Text Processing
print("\n7.2 Text Processing - Word Lengths:")
print("-" * 30)

sentence = "Python list comprehension is powerful and elegant"
words = sentence.split()
word_lengths = [len(word) for word in words]
word_info = [(word, len(word)) for word in words]

print(f"  Sentence: {sentence}")
print(f"  Word lengths: {word_lengths}")
print(f"  Word info: {word_info[:3]}...")

# 7.3 Data Cleaning
print("\n7.3 Data Cleaning - Remove Empty Strings:")
print("-" * 30)

data_with_empty = ["Python", "", "list", None, "comprehension", " ", "is", None, "great"]
cleaned = [item for item in data_with_empty if item and str(item).strip()]
print(f"  Original: {data_with_empty}")
print(f"  Cleaned: {cleaned}")

# 7.4 Grades Processing
print("\n7.4 Grades Processing:")
print("-" * 30)

grades = [85, 92, 78, 65, 90, 55, 88, 70, 95, 60]

# Pass/Fail
status = ["Pass" if grade >= 60 else "Fail" for grade in grades]
print(f"  Grades: {grades}")
print(f"  Status: {status}")

# Above average
average = sum(grades) / len(grades)
above_avg = [grade for grade in grades if grade >= average]
print(f"  Average: {average:.1f}")
print(f"  Above average: {above_avg}")

# Letter grades
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

letter_grades = [get_grade(grade) for grade in grades]
print(f"  Letter grades: {letter_grades}")

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Squares of Even Numbers
Create a list of squares of even numbers from 1 to 20.

🎯 EXERCISE 2: String Transformation
Convert a list of strings to uppercase and add "!" at the end.

🎯 EXERCISE 3: Filter and Transform
From a list of numbers, keep only numbers > 10 and multiply them by 2.

🎯 EXERCISE 4: Nested Comprehension
Create a 4x4 multiplication table using nested list comprehension.

🎯 EXERCISE 5: Palindrome Filter
From a list of words, keep only palindromes.

🎯 CHALLENGE: Matrix Transpose
Transpose a 3x3 matrix using nested list comprehension.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Squares of Even Numbers:")
squares_even = [x ** 2 for x in range(1, 21) if x % 2 == 0]
print(f"  {squares_even}")

# Exercise 2
print("\nEx2 - String Transformation:")
words = ["hello", "world", "python"]
transformed = [word.upper() + "!" for word in words]
print(f"  {transformed}")

# Exercise 3
print("\nEx3 - Filter and Transform:")
numbers = [5, 12, 8, 20, 3, 15, 7]
filtered = [num * 2 for num in numbers if num > 10]
print(f"  Original: {numbers}")
print(f"  Filtered & doubled: {filtered}")

# Exercise 4
print("\nEx4 - Multiplication Table:")
table = [[i * j for j in range(1, 5)] for i in range(1, 5)]
print("  Table:")
for row in table:
    print(f"    {row}")

# Exercise 5
print("\nEx5 - Palindrome Filter:")
words = ["racecar", "hello", "level", "world", "radar", "python"]
palindromes = [word for word in words if word == word[::-1]]
print(f"  Original: {words}")
print(f"  Palindromes: {palindromes}")

# Challenge
print("\nChallenge - Matrix Transpose:")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("  Original Matrix:")
for row in matrix:
    print(f"    {row}")

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("  Transposed Matrix:")
for row in transpose:
    print(f"    {row}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST COMPREHENSION MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    BASIC SYNTAX                             │
├─────────────────────────────────────────────────────────────┤
│  [expression for item in iterable]                         │
│  Example: [x**2 for x in range(10)]                        │
├─────────────────────────────────────────────────────────────┤
│                    WITH CONDITION (filter)                  │
├─────────────────────────────────────────────────────────────┤
│  [expression for item in iterable if condition]            │
│  Example: [x for x in range(20) if x % 2 == 0]            │
├─────────────────────────────────────────────────────────────┤
│                    WITH if-else (transform)                 │
├─────────────────────────────────────────────────────────────┤
│  [expr_if_true if condition else expr_if_false for item]   │
│  Example: ['even' if x%2==0 else 'odd' for x in range(10)] │
├─────────────────────────────────────────────────────────────┤
│                    NESTED COMPREHENSION                     │
├─────────────────────────────────────────────────────────────┤
│  [expr for item1 in iter1 for item2 in iter2]             │
│  Example: [num for row in matrix for num in row]          │
├─────────────────────────────────────────────────────────────┤
│                    KEY POINTS                               │
├─────────────────────────────────────────────────────────────┤
│  ✅ More concise than loops                                │
│  ✅ Faster than loops (optimized in C)                    │
│  ✅ More Pythonic                                          │
│  ⚠️ Use for simple transformations                         │
│  ⚠️ Avoid for complex logic (use for loops)               │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Dictionary & Set Comprehensions
""")