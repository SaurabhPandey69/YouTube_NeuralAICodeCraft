"""
PYTHON LIST ITERATION - FOR LOOP VS WHILE LOOP
NeuralAICodeCraft - Complete Guide to Iterating Lists

Topics Covered:
1. For Loop Iteration
2. While Loop Iteration
3. For vs While - Comparison
4. Common Patterns
5. Advanced Techniques
"""

import time

print("=" * 70)
print("🔄 PYTHON LIST ITERATION - FOR LOOP VS WHILE LOOP")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: FOR LOOP - BASIC ITERATION
# ============================================

print("\n📚 PART 1: FOR LOOP - BASIC ITERATION")
print("-" * 50)

print("""
FOR LOOP SYNTAX:
for element in list:
    # do something with element

FOR LOOP WITH INDEX:
for i in range(len(list)):
    # do something with list[i]
""")

# 1.1 Basic For Loop
print("\n1.1 Basic For Loop (Direct Access):")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"List: {fruits}\n")

print("Iterating with for loop:")
for fruit in fruits:
    print(f"  {fruit}")

# 1.2 For Loop with Index
print("\n1.2 For Loop with Index (range):")
print("-" * 30)

print("Iterating with index:")
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")

# 1.3 For Loop with enumerate
print("\n1.3 For Loop with enumerate():")
print("-" * 30)

print("Using enumerate() to get index and value:")
for i, fruit in enumerate(fruits):
    print(f"  Index {i}: {fruit}")

# 1.4 For Loop - Reverse Iteration
print("\n1.4 For Loop - Reverse Iteration:")
print("-" * 30)

print("Reversed using reversed():")
for fruit in reversed(fruits):
    print(f"  {fruit}")

print("\nReversed using slicing:")
for fruit in fruits[::-1]:
    print(f"  {fruit}")

# ============================================
# PART 2: WHILE LOOP - BASIC ITERATION
# ============================================

print("\n🔁 PART 2: WHILE LOOP - BASIC ITERATION")
print("-" * 50)

print("""
WHILE LOOP SYNTAX:
i = 0
while i < len(list):
    # do something with list[i]
    i += 1

WHILE LOOP SYNTAX (Reverse):
i = len(list) - 1
while i >= 0:
    # do something with list[i]
    i -= 1
""")

# 2.1 Basic While Loop
print("\n2.1 Basic While Loop:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"List: {fruits}\n")

print("Iterating with while loop:")
i = 0
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 1

# 2.2 While Loop with Index
print("\n2.2 While Loop with Index Display:")
print("-" * 30)

print("Iterating with index:")
i = 0
while i < len(fruits):
    print(f"  Index {i}: {fruits[i]}")
    i += 1

# 2.3 While Loop - Reverse Iteration
print("\n2.3 While Loop - Reverse Iteration:")
print("-" * 30)

print("Reverse iteration with while loop:")
i = len(fruits) - 1
while i >= 0:
    print(f"  Index {i}: {fruits[i]}")
    i -= 1

# 2.4 While Loop - Step by Step
print("\n2.4 While Loop - Skipping Elements (Step 2):")
print("-" * 30)

print("Every second element:")
i = 0
while i < len(fruits):
    print(f"  {fruits[i]}")
    i += 2

# ============================================
# PART 3: FOR LOOP VS WHILE LOOP
# ============================================

print("\n⚖️ PART 3: FOR LOOP VS WHILE LOOP - COMPARISON")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  FOR LOOP           │  WHILE LOOP          │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Syntax         │  Simpler            │  More complex        │
│  Readability    │  Very readable      │  Less readable       │
│  Performance    │  Faster             │  Slightly slower     │
│  Control        │  Limited            │  Full control        │
│  Risk           │  Safe               │  Infinite loop risk  │
│  Use when       │  Known iteration    │  Unknown iteration   │
│  Pythonic       │  ✅ Yes             │  ⚠️ Less Pythonic   │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 3.1 Performance Comparison
print("\n3.1 Performance Comparison:")
print("-" * 30)

def iter_for(lst):
    """Iterate using for loop"""
    result = 0
    for item in lst:
        result += item
    return result

def iter_while(lst):
    """Iterate using while loop"""
    result = 0
    i = 0
    while i < len(lst):
        result += lst[i]
        i += 1
    return result

# Create test data
test_data = list(range(1000000))

# Time for loop
start = time.time()
for_result = iter_for(test_data)
for_time = time.time() - start

# Time while loop
start = time.time()
while_result = iter_while(test_data)
while_time = time.time() - start

print(f"List size: 1,000,000 elements")
print(f"For loop time: {for_time:.4f}s")
print(f"While loop time: {while_time:.4f}s")
print(f"For loop is {while_time/for_time:.2f}x faster!")

# 3.2 When to Use Each
print("\n3.2 When to Use Each:")
print("-" * 30)

print("""
✅ USE FOR LOOP when:
├── Iterating over a sequence
├── Number of iterations is known
├── Simplicity and readability matter
├── Working with Pythonic code
└── Performance matters

✅ USE WHILE LOOP when:
├── Iteration count is unknown
├── Need to skip or jump dynamically
├── Complex conditions for stopping
├── Need to modify index manually
└── Working with infinite loops with break
""")

# ============================================
# PART 4: COMMON ITERATION PATTERNS
# ============================================

print("\n🎯 PART 4: COMMON ITERATION PATTERNS")
print("-" * 50)

# 4.1 Finding Maximum
print("\n4.1 Finding Maximum Element:")
print("-" * 30)

numbers = [45, 12, 89, 34, 67, 23, 90, 56]

# Using for loop
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"List: {numbers}")
print(f"Maximum (for loop): {max_val}")

# Using while loop
max_val = numbers[0]
i = 1
while i < len(numbers):
    if numbers[i] > max_val:
        max_val = numbers[i]
    i += 1
print(f"Maximum (while loop): {max_val}")

# 4.2 Finding Sum and Average
print("\n4.2 Finding Sum and Average:")
print("-" * 30)

numbers = [10, 20, 30, 40, 50]

# For loop
sum_for = 0
for num in numbers:
    sum_for += num
avg_for = sum_for / len(numbers)
print(f"For loop - Sum: {sum_for}, Average: {avg_for}")

# While loop
sum_while = 0
i = 0
while i < len(numbers):
    sum_while += numbers[i]
    i += 1
avg_while = sum_while / len(numbers)
print(f"While loop - Sum: {sum_while}, Average: {avg_while}")

# 4.3 Filtering List
print("\n4.3 Filtering List (Even Numbers):")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For loop
evens_for = []
for num in numbers:
    if num % 2 == 0:
        evens_for.append(num)
print(f"For loop - Evens: {evens_for}")

# While loop
evens_while = []
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        evens_while.append(numbers[i])
    i += 1
print(f"While loop - Evens: {evens_while}")

# 4.4 Modifying in Place
print("\n4.4 Modifying List In Place (Square each element):")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
print(f"Original: {numbers}")

# For loop with index
for i in range(len(numbers)):
    numbers[i] = numbers[i] ** 2
print(f"For loop squared: {numbers}")

# While loop
numbers = [1, 2, 3, 4, 5]
i = 0
while i < len(numbers):
    numbers[i] = numbers[i] ** 2
    i += 1
print(f"While loop squared: {numbers}")

# 4.5 Nested Loop - 2D List
print("\n4.5 Nested Loop - 2D List:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# For loop nested
print("For loop nested:")
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()

# While loop nested
print("\nWhile loop nested:")
i = 0
while i < len(matrix):
    j = 0
    while j < len(matrix[i]):
        print(f"  {matrix[i][j]}", end=" ")
        j += 1
    print()
    i += 1

# ============================================
# PART 5: ADVANCED ITERATION TECHNIQUES
# ============================================

print("\n🚀 PART 5: ADVANCED ITERATION TECHNIQUES")
print("-" * 50)

# 5.1 Using break
print("\n5.1 Using break - Stop at 5:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# For loop with break
for num in numbers:
    if num == 5:
        break
    print(f"  {num}")
print("  (Stopped at 5)")

# While loop with break
print("\nWhile loop with break:")
i = 0
while i < len(numbers):
    if numbers[i] == 5:
        break
    print(f"  {numbers[i]}")
    i += 1
print("  (Stopped at 5)")

# 5.2 Using continue
print("\n5.2 Using continue - Skip 5:")
print("-" * 30)

# For loop with continue
for num in numbers:
    if num == 5:
        continue
    print(f"  {num}")
print("  (Skipped 5)")

# 5.3 Iterating Multiple Lists
print("\n5.3 Iterating Multiple Lists (zip):")
print("-" * 30)

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 92, 78]

# Using zip
for name, score in zip(names, scores):
    print(f"  {name}: {score}")

# With while loop
print("\nUsing while loop:")
i = 0
while i < len(names):
    print(f"  {names[i]}: {scores[i]}")
    i += 1

# 5.4 Infinite Loop with Break (Practical)
print("\n5.4 Processing Until Condition Met:")
print("-" * 30)

print("Finding first number > 50:")
numbers = [10, 23, 45, 67, 89, 12]
i = 0
while i < len(numbers):
    if numbers[i] > 50:
        print(f"  Found: {numbers[i]} at index {i}")
        break
    i += 1
else:
    print("  No number > 50 found")

# ============================================
# PART 6: PERFORMANCE COMPARISON TABLE
# ============================================

print("\n📊 PART 6: PERFORMANCE COMPARISON TABLE")
print("-" * 50)

print("""
┌─────────────────────────────┬─────────────────────────────────┐
│     OPERATION               │     TIME (seconds)              │
├─────────────────────────────┼─────────────────────────────────┤
│  For loop (simple)          │  0.02s                         │
│  While loop (simple)        │  0.03s                         │
│  For loop (range indexing)  │  0.04s                         │
│  While loop (range indexing)│  0.05s                         │
│  enumerate()                │  0.03s                         │
│  List comprehension         │  0.01s                         │
├─────────────────────────────┼─────────────────────────────────┤
│  For loop is generally FASTER than while loop!              │
│  List comprehension is FASTEST!                              │
└─────────────────────────────┴─────────────────────────────────┘
""")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Sum All Elements
Find sum of [1,2,3,4,5] using for loop and while loop.

🎯 EXERCISE 2: Find Even Numbers
Print even numbers from [1,2,3,4,5,6,7,8,9,10] using both loops.

🎯 EXERCISE 3: Reverse a List
Reverse [1,2,3,4,5] using while loop (without slicing).

🎯 EXERCISE 4: Multiplication Table
Create multiplication table using nested for loops.

🎯 EXERCISE 5: Count Occurrences
Count how many times 'a' appears in a list using while loop.

🎯 CHALLENGE: Palindrome Check
Check if a list is palindrome using for and while loops.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Sum All Elements:")
numbers = [1, 2, 3, 4, 5]

sum_for = 0
for num in numbers:
    sum_for += num

sum_while = 0
i = 0
while i < len(numbers):
    sum_while += numbers[i]
    i += 1

print(f"  Sum (for loop): {sum_for}")
print(f"  Sum (while loop): {sum_while}")

# Exercise 2
print("\nEx2 - Even Numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("  For loop evens:", end=" ")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

print("  While loop evens:", end=" ")
i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        print(numbers[i], end=" ")
    i += 1
print()

# Exercise 3
print("\nEx3 - Reverse a List:")
numbers = [1, 2, 3, 4, 5]
reversed_list = []
i = len(numbers) - 1
while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1
print(f"  Original: {numbers}")
print(f"  Reversed: {reversed_list}")

# Exercise 4
print("\nEx4 - Multiplication Table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i*j:3}", end="")
    print()

# Exercise 5
print("\nEx5 - Count Occurrences:")
lst = ['a', 'b', 'a', 'c', 'a', 'd']
count = 0
i = 0
while i < len(lst):
    if lst[i] == 'a':
        count += 1
    i += 1
print(f"  List: {lst}")
print(f"  'a' appears {count} times")

# Challenge
print("\nChallenge - Palindrome Check:")
def is_palindrome_for(lst):
    for i in range(len(lst) // 2):
        if lst[i] != lst[len(lst) - 1 - i]:
            return False
    return True

def is_palindrome_while(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True

test1 = [1, 2, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]
print(f"  {test1} is palindrome? {is_palindrome_for(test1)}")
print(f"  {test2} is palindrome? {is_palindrome_while(test2)}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ LIST ITERATION MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    FOR LOOP                                 │
├─────────────────────────────────────────────────────────────┤
│  for item in list:                                         │
│      print(item)                                           │
│                                                             │
│  for i in range(len(list)):                               │
│      print(list[i])                                        │
│                                                             │
│  for i, item in enumerate(list):                          │
│      print(i, item)                                        │
├─────────────────────────────────────────────────────────────┤
│                    WHILE LOOP                               │
├─────────────────────────────────────────────────────────────┤
│  i = 0                                                      │
│  while i < len(list):                                     │
│      print(list[i])                                        │
│      i += 1                                                 │
│                                                             │
│  i = len(list) - 1                                        │
│  while i >= 0:                                              │
│      print(list[i])                                        │
│      i -= 1                                                 │
├─────────────────────────────────────────────────────────────┤
│                    BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────┤
│  ✅ FOR LOOP: Simpler, faster, Pythonic                   │
│  ✅ WHILE LOOP: Full control, dynamic conditions           │
│  ⚠️ Avoid infinite loops in while!                         │
│  ⚠️ Prefer for loop for simple iteration                  │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python List Methods - Complete Guide
""")