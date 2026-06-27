"""
PYTHON FOR LOOP - COMPLETE SYNTAX & EXECUTION GUIDE
NeuralAICodeCraft - Master the For Loop

Topics Covered:
1. For Loop Basics
2. How Execution Works
3. Iterating over Iterables
4. range() with For Loop
5. break, continue, else
6. Nested For Loops
"""

print("=" * 70)
print("🔄 PYTHON FOR LOOP - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: FOR LOOP BASICS
# ============================================

print("\n📚 PART 1: FOR LOOP BASICS")
print("-" * 50)

print("""
WHAT IS A FOR LOOP?
├── Used to iterate over a sequence (iterable)
├── Executes code block for each item
├── Automatically stops when sequence ends
└── Cleaner than while loop for known sequences

SYNTAX:
for variable in iterable:
    # code block to execute
    # runs once for each item
""")

# 1.1 Basic For Loop
print("\n1.1 Basic For Loop:")
print("-" * 30)

print("Iterating over a list:")
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(f"  {fruit}")

print("\nIterating over a string:")
word = "Python"
for char in word:
    print(f"  {char}")

# ============================================
# PART 2: HOW EXECUTION WORKS
# ============================================

print("\n🔍 PART 2: HOW EXECUTION WORKS (Step-by-Step)")
print("-" * 50)

print("""
EXECUTION PROCESS:
1. Get the first item from the iterable
2. Assign it to the variable
3. Execute the code block
4. Get the next item
5. Repeat steps 2-4
6. Stop when no more items remain
""")

# 2.1 Step-by-Step Demonstration
print("\n2.1 Step-by-Step Execution:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry']
print("For loop execution:")
print("  Starting loop...")

for fruit in fruits:
    print(f"    Current item: '{fruit}'")
    print(f"    Executing code block...")

print("  Loop finished!")

# 2.2 Tracing with Range
print("\n2.2 Tracing with range():")
print("-" * 30)

print("for i in range(5):")
print("-" * 20)
for i in range(5):
    print(f"  i = {i}, loop body executes")
print("  Loop complete!")

print("\n  Execution steps:")
print("    i = 0 → execute body → increment")
print("    i = 1 → execute body → increment")
print("    i = 2 → execute body → increment")
print("    i = 3 → execute body → increment")
print("    i = 4 → execute body → increment")
print("    i = 5 → stop (5 is not less than 5)")

# 2.3 The Iteration Variable
print("\n2.3 The Iteration Variable:")
print("-" * 30)

print("The variable is re-assigned each iteration:")
numbers = [10, 20, 30]
for num in numbers:
    print(f"  num = {num} (id: {id(num)})")

# 2.4 Variable Persistence
print("\n2.4 Variable Persistence:")
print("-" * 30)

for i in range(3):
    print(f"  Inside loop: i = {i}")
print(f"After loop: i = {i} (still accessible!)")

# ============================================
# PART 3: ITERATING OVER ITERABLES
# ============================================

print("\n📦 PART 3: ITERATING OVER ITERABLES")
print("-" * 50)

# 3.1 Lists
print("\n3.1 Lists:")
print("-" * 30)

colors = ['red', 'green', 'blue', 'yellow']
print("Colors:")
for color in colors:
    print(f"  {color}")

# 3.2 Tuples
print("\n3.2 Tuples:")
print("-" * 30)

coordinates = (10, 20, 30, 40)
print("Coordinates:")
for coord in coordinates:
    print(f"  {coord}")

# 3.3 Strings
print("\n3.3 Strings:")
print("-" * 30)

word = "Hello"
print(f"Characters in '{word}':")
for char in word:
    print(f"  {char}")

# 3.4 Dictionaries
print("\n3.4 Dictionaries:")
print("-" * 30)

person = {'name': 'Alice', 'age': 25, 'city': 'NYC'}

print("Keys:")
for key in person:
    print(f"  {key}")

print("\nValues:")
for value in person.values():
    print(f"  {value}")

print("\nKey-Value pairs:")
for key, value in person.items():
    print(f"  {key}: {value}")

# 3.5 Sets
print("\n3.5 Sets:")
print("-" * 30)

unique_nums = {1, 2, 3, 4, 5}
print("Set elements:")
for num in unique_nums:
    print(f"  {num}")

# ============================================
# PART 4: range() WITH FOR LOOP
# ============================================

print("\n🔢 PART 4: range() WITH FOR LOOP")
print("-" * 50)

# 4.1 Basic range()
print("\n4.1 range(stop):")
print("-" * 30)

print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# 4.2 range(start, stop)
print("\n4.2 range(start, stop):")
print("-" * 30)

print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

# 4.3 range(start, stop, step)
print("\n4.3 range(start, stop, step):")
print("-" * 30)

print("range(1, 10, 2):", end=" ")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("\nrange(10, 0, -1):", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 4.4 Looping with Index
print("\n4.4 Looping with Index (range + len):")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")

# ============================================
# PART 5: BREAK AND CONTINUE
# ============================================

print("\n⏹️ PART 5: break AND continue")
print("-" * 50)

# 5.1 break
print("\n5.1 break - Exit Loop Early:")
print("-" * 30)

print("Finding first number greater than 5:")
numbers = [1, 3, 5, 7, 9, 11]
for num in numbers:
    print(f"  Checking {num}...")
    if num > 5:
        print(f"  Found! {num} is greater than 5")
        break
print("  Loop stopped!")

# 5.2 continue
print("\n5.2 continue - Skip Current Iteration:")
print("-" * 30)

print("Printing only even numbers:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 != 0:
        continue
    print(f"  {num} is even")

# 5.3 break vs continue
print("\n5.3 break vs continue - Visual Comparison:")
print("-" * 30)

print("break stops the entire loop:")
for i in range(1, 6):
    if i == 3:
        break
    print(f"  {i}")
print("  (Stopped at 3)")

print("\ncontinue skips one iteration:")
for i in range(1, 6):
    if i == 3:
        continue
    print(f"  {i}")
print("  (Skipped 3)")

# ============================================
# PART 6: else WITH FOR LOOP
# ============================================

print("\n📌 PART 6: else WITH FOR LOOP")
print("-" * 50)

print("""
else with for loop executes when:
├── Loop completes normally (no break)
└── Does NOT execute if break occurs
""")

# 6.1 else without break
print("\n6.1 else without break:")
print("-" * 30)

print("Loop completes normally:")
for i in range(1, 4):
    print(f"  i = {i}")
else:
    print("  ✅ else block executes after normal completion!")

# 6.2 else with break
print("\n6.2 else with break:")
print("-" * 30)

print("Loop with break:")
for i in range(1, 6):
    print(f"  i = {i}")
    if i == 3:
        print("  Breaking at i = 3!")
        break
else:
    print("  This won't execute")

print("  ⚠️ else block skipped because of break")

# 6.3 Practical Use: Search
print("\n6.3 Practical Search with else:")
print("-" * 30)

def find_item(items, target):
    for item in items:
        if item == target:
            print(f"  Found '{target}'!")
            break
    else:
        print(f"  '{target}' not found!")

fruits = ['apple', 'banana', 'cherry', 'date']
find_item(fruits, 'banana')
find_item(fruits, 'grape')

# ============================================
# PART 7: NESTED FOR LOOPS
# ============================================

print("\n🏗️ PART 7: NESTED FOR LOOPS")
print("-" * 50)

# 7.1 Basic Nested Loop
print("\n7.1 Basic Nested Loop:")
print("-" * 30)

print("Cartesian product of [1,2] and ['a','b']:")
for i in [1, 2]:
    for letter in ['a', 'b']:
        print(f"  {i}{letter}", end=" ")
    print()

# 7.2 Multiplication Table
print("\n7.2 Multiplication Table (1 to 5):")
print("-" * 30)

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# 7.3 Pattern Printing
print("\n7.3 Pattern Printing:")
print("-" * 30)

print("Right triangle pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\nNumber triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 7.4 Matrix Iteration
print("\n7.4 Matrix Iteration:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix elements with positions:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}")

# ============================================
# PART 8: COMMON PATTERNS
# ============================================

print("\n🎯 PART 8: COMMON PATTERNS")
print("-" * 50)

# 8.1 Sum of Elements
print("\n8.1 Sum of Elements:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers} = {total}")

# 8.2 Find Maximum
print("\n8.2 Find Maximum:")
print("-" * 30)

numbers = [45, 12, 89, 34, 67, 23]
max_val = numbers[0]
for num in numbers:
    if num > max_val:
        max_val = num
print(f"Maximum in {numbers} = {max_val}")

# 8.3 Count Occurrences
print("\n8.3 Count Occurrences:")
print("-" * 30)

text = "hello world"
count = 0
for char in text:
    if char == 'l':
        count += 1
print(f"'l' appears {count} times in '{text}'")

# 8.4 Build a List
print("\n8.4 Build a List using For Loop:")
print("-" * 30)

squares = []
for i in range(1, 6):
    squares.append(i ** 2)
print(f"Squares of 1-5: {squares}")

# 8.5 Reverse Loop
print("\n8.5 Reverse Loop using range:")
print("-" * 30)

print("Countdown from 5:")
for i in range(5, 0, -1):
    print(f"  {i}")

# ============================================
# PART 9: COMMON MISTAKES
# ============================================

print("\n⚠️ PART 9: COMMON MISTAKES")
print("-" * 50)

# 9.1 Forgetting Colon
print("\n9.1 Forgetting Colon:")
print("-" * 30)

print("""
❌ for i in range(5)
      print(i)

✅ for i in range(5):
      print(i)

Always include the colon ':' after the loop condition!
""")

# 9.2 Wrong Indentation
print("\n9.2 Wrong Indentation:")
print("-" * 30)

print("""
❌ for i in range(3):
    print(i)
  print("Done")  # Wrong indentation

✅ for i in range(3):
    print(i)
print("Done")    # Correct indentation (outside loop)
""")

# 9.3 Modifying List While Iterating
print("\n9.3 Modifying List While Iterating:")
print("-" * 30)

print("""
⚠️ Avoid modifying a list while iterating over it!

❌ for item in my_list:
      my_list.append(new_item)  # Infinite loop!

✅ Use a copy or create a new list
""")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Sum of Even Numbers
Find sum of even numbers from 1 to 50.

🎯 EXERCISE 2: Count Vowels
Count vowels in a string.

🎯 EXERCISE 3: Multiplication Table
Print table of any number using for loop.

🎯 EXERCISE 4: Factorial
Find factorial of a number using for loop.

🎯 EXERCISE 5: Reverse String
Print a string in reverse order using for loop.

🎯 EXERCISE 6: Palindrome Check
Check if a string is palindrome.

🎯 CHALLENGE: Star Pattern
Print a pyramid pattern using nested for loops.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Sum of Even Numbers 1-50:")
total_even = 0
for i in range(2, 51, 2):
    total_even += i
print(f"  Sum of even numbers: {total_even}")

# Exercise 2
print("\nEx2 - Count Vowels:")
text = "Hello World"
vowels = 'aeiouAEIOU'
count = 0
for char in text:
    if char in vowels:
        count += 1
print(f"  '{text}' has {count} vowels")

# Exercise 3
print("\nEx3 - Multiplication Table of 7:")
for i in range(1, 11):
    print(f"  7 x {i:2} = {7 * i:3}")

# Exercise 4
print("\nEx4 - Factorial of 5:")
fact = 1
for i in range(1, 6):
    fact *= i
print(f"  5! = {fact}")

# Exercise 5
print("\nEx5 - Reverse String:")
word = "Python"
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(f"  '{word}' reversed: '{reversed_word}'")

# Exercise 6
print("\nEx6 - Palindrome Check:")
def is_palindrome(word):
    reversed_word = ""
    for char in word:
        reversed_word = char + reversed_word
    return word == reversed_word

print(f"  'radar' palindrome? {is_palindrome('radar')}")
print(f"  'python' palindrome? {is_palindrome('python')}")

# Challenge
print("\nChallenge - Pyramid Pattern:")
n = 5
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end="")
    # Stars
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ FOR LOOP MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    FOR LOOP SYNTAX                          │
├─────────────────────────────────────────────────────────────┤
│  for variable in iterable:                                 │
│      # code block                                          │
├─────────────────────────────────────────────────────────────┤
│                    WITH range()                             │
├─────────────────────────────────────────────────────────────┤
│  for i in range(stop):                                     │
│  for i in range(start, stop):                              │
│  for i in range(start, stop, step):                        │
├─────────────────────────────────────────────────────────────┤
│                    CONTROL STATEMENTS                       │
├─────────────────────────────────────────────────────────────┤
│  break     → Exit loop immediately                        │
│  continue  → Skip current iteration                        │
│  else      → Execute after normal completion              │
├─────────────────────────────────────────────────────────────┤
│                    BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────┤
│  ✅ Always include colon after loop condition             │
│  ✅ Indent code block properly                             │
│  ✅ Use meaningful variable names                          │
│  ✅ Don't modify list while iterating                      │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: While Loop Explained
""")