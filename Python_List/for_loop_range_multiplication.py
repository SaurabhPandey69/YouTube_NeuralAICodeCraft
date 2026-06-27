"""
PYTHON FOR LOOP & RANGE - MULTIPLICATION TABLE WITH F-STRINGS
NeuralAICodeCraft - Complete Guide

Topics Covered:
1. range() Function Basics
2. For Loop with range()
3. Multiplication Table
4. f-string Formatting
5. Nested Loops
6. Advanced Formatting
"""

print("=" * 70)
print("🔄 PYTHON FOR LOOP & RANGE - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: range() FUNCTION BASICS
# ============================================

print("\n📚 PART 1: range() FUNCTION BASICS")
print("-" * 50)

print("""
SYNTAX:
- range(stop)           → 0 to stop-1
- range(start, stop)    → start to stop-1
- range(start, stop, step) → start to stop-1 with step

range() returns an ITERABLE (not a list)
It generates numbers on demand (lazy evaluation)
""")

# 1.1 range(stop)
print("\n1.1 range(stop):")
print("-" * 30)

print("range(5) →", end=" ")
for i in range(5):
    print(i, end=" ")
print()

# 1.2 range(start, stop)
print("\n1.2 range(start, stop):")
print("-" * 30)

print("range(2, 8) →", end=" ")
for i in range(2, 8):
    print(i, end=" ")
print()

# 1.3 range(start, stop, step)
print("\n1.3 range(start, stop, step):")
print("-" * 30)

print("range(1, 10, 2) →", end=" ")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("\nrange(10, 0, -1) →", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 1.4 Converting range to list
print("\n1.4 Converting range to list:")
print("-" * 30)

r = range(5)
print(f"range(5) → {r}")
print(f"list(r) → {list(r)}")

# ============================================
# PART 2: FOR LOOP WITH range()
# ============================================

print("\n🔄 PART 2: FOR LOOP WITH range()")
print("-" * 50)

# 2.1 Basic For Loop
print("\n2.1 Basic For Loop:")
print("-" * 30)

print("Numbers 0 to 4:")
for i in range(5):
    print(f"  {i}")

# 2.2 Starting from 1
print("\n2.2 Starting from 1:")
print("-" * 30)

print("Numbers 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# 2.3 With Step
print("\n2.3 With Step:")
print("-" * 30)

print("Even numbers 2 to 10:")
for i in range(2, 11, 2):
    print(f"  {i}")

# 2.4 Descending
print("\n2.4 Descending:")
print("-" * 30)

print("Countdown 5 to 1:")
for i in range(5, 0, -1):
    print(f"  {i}")

# ============================================
# PART 3: SINGLE MULTIPLICATION TABLE
# ============================================

print("\n📊 PART 3: SINGLE MULTIPLICATION TABLE")
print("-" * 50)

# 3.1 Basic Multiplication Table
print("\n3.1 Basic Multiplication Table (5):")
print("-" * 30)

print("Multiplication Table of 5:")
print("  " + "-" * 30)

for i in range(1, 11):
    print(f"  5 x {i:2} = {5 * i:3}")

# 3.2 Using f-strings for formatting
print("\n3.2 Using f-strings with formatting:")
print("-" * 30)

num = 7
print(f"Multiplication Table of {num}:")
print("  " + "-" * 30)

for i in range(1, 11):
    print(f"  {num} x {i:2} = {num * i:3}")

# 3.3 Function to print multiplication table
print("\n3.3 Function for Multiplication Table:")
print("-" * 30)

def print_table(num):
    """Print multiplication table for given number"""
    print(f"Multiplication Table of {num}:")
    print("  " + "-" * 30)
    for i in range(1, 11):
        print(f"  {num} x {i:2} = {num * i:3}")

# Test the function
print_table(9)
print()

# 3.4 Table with Custom Range
print("\n3.4 Table with Custom Range (1 to 15):")
print("-" * 30)

def print_table_custom(num, upto=10):
    """Print multiplication table with custom upper limit"""
    print(f"Multiplication Table of {num} (1 to {upto}):")
    print("  " + "-" * 35)
    for i in range(1, upto + 1):
        print(f"  {num} x {i:2} = {num * i:3}")

print_table_custom(6, 15)

# ============================================
# PART 4: F-STRING FORMATTING
# ============================================

print("\n🎨 PART 4: F-STRING FORMATTING")
print("-" * 50)

print("""
F-STRING FORMATTING OPTIONS:
- {value}              → Default
- {value:>5}           → Right aligned, width 5
- {value:<5}           → Left aligned, width 5
- {value:^5}           → Center aligned, width 5
- {value:.2f}          → 2 decimal places
- {value:,}            → Thousand separator
""")

# 4.1 Alignment
print("\n4.1 Alignment:")
print("-" * 30)

print("Right aligned:")
for i in range(1, 6):
    print(f"  {i:>5} {i**2:>5} {i**3:>5}")

print("\nLeft aligned:")
for i in range(1, 6):
    print(f"  {i:<5} {i**2:<5} {i**3:<5}")

print("\nCenter aligned:")
for i in range(1, 6):
    print(f"  {i:^5} {i**2:^5} {i**3:^5}")

# 4.2 Formatted Table
print("\n4.2 Formatted Multiplication Table:")
print("-" * 30)

num = 8
print(f"  {num} x 1 = {num*1:>3}")
print(f"  {num} x 2 = {num*2:>3}")
print(f"  {num} x 3 = {num*3:>3}")
print(f"  {num} x 4 = {num*4:>3}")
print(f"  {num} x 5 = {num*5:>3}")
print(f"  {num} x 6 = {num*6:>3}")
print(f"  {num} x 7 = {num*7:>3}")
print(f"  {num} x 8 = {num*8:>3}")
print(f"  {num} x 9 = {num*9:>3}")
print(f"  {num} x 10 = {num*10:>3}")

# 4.3 Using loop with alignment
print("\n4.3 Loop with Alignment:")
print("-" * 30)

num = 4
for i in range(1, 11):
    print(f"  {num} x {i:2} = {num * i:3}")

# ============================================
# PART 5: NESTED LOOPS - MULTIPLE TABLES
# ============================================

print("\n🏗️ PART 5: NESTED LOOPS - MULTIPLE TABLES")
print("-" * 50)

# 5.1 Tables 1 to 5
print("\n5.1 Multiplication Tables 1 to 5:")
print("-" * 30)

for num in range(1, 6):
    print(f"\nTable of {num}:")
    print("  " + "-" * 20)
    for i in range(1, 11):
        print(f"  {num} x {i:2} = {num * i:3}")

# 5.2 Tables in Grid Format
print("\n5.2 Tables 1 to 5 in Grid Format:")
print("-" * 30)

def print_table_grid(start=1, end=5):
    """Print multiplication tables in grid format"""
    # Print header
    print("   ", end="")
    for num in range(start, end + 1):
        print(f"{num:>6}", end="")
    print()
    print("   " + "=" * (6 * (end - start + 1)))

    # Print rows
    for i in range(1, 11):
        print(f"{i:2} |", end="")
        for num in range(start, end + 1):
            print(f"{num * i:>6}", end="")
        print()

print_table_grid(1, 5)

# 5.3 Tables 1 to 10
print("\n5.3 Tables 1 to 10 in Grid Format:")
print("-" * 30)

print_table_grid(1, 10)

# ============================================
# PART 6: ADVANCED EXAMPLES
# ============================================

print("\n🚀 PART 6: ADVANCED EXAMPLES")
print("-" * 50)

# 6.1 Sum of Numbers
print("\n6.1 Sum of Numbers 1 to 100:")
print("-" * 30)

total = 0
for i in range(1, 101):
    total += i

print(f"Sum of 1 to 100: {total}")
print(f"Formula: {100 * 101 // 2}")

# 6.2 Even Numbers Sum
print("\n6.2 Sum of Even Numbers 1 to 100:")
print("-" * 30)

even_sum = 0
for i in range(2, 101, 2):
    even_sum += i

print(f"Sum of even numbers 1 to 100: {even_sum}")

# 6.3 Factorial
print("\n6.3 Factorial (5!):")
print("-" * 30)

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(f"5! = {factorial(5)}")
print(f"10! = {factorial(10)}")

# 6.4 Prime Numbers
print("\n6.4 Prime Numbers up to 50:")
print("-" * 30)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(2, 51):
    if is_prime(i):
        primes.append(i)

print(f"Prime numbers up to 50: {primes}")

# 6.5 Square Root Table
print("\n6.5 Square Root Table (1 to 20):")
print("-" * 30)

import math

print("  Number  Square  Square Root")
print("  " + "-" * 35)
for i in range(1, 21):
    print(f"  {i:>6} {i**2:>7} {math.sqrt(i):>10.4f}")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Table of 12
Print the multiplication table of 12 from 1 to 10.

🎯 EXERCISE 2: All Tables
Print tables from 2 to 5 using nested loops.

🎯 EXERCISE 3: Custom Range
Print table of 7 from 1 to 15.

🎯 EXERCISE 4: Tables in Grid
Print tables 1 to 5 in a grid format.

🎯 EXERCISE 5: Reverse Table
Print table of 8 in reverse order (10 down to 1).

🎯 CHALLENGE: Full Multiplication Grid
Print a 10x10 multiplication table grid.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Table of 12:")
for i in range(1, 11):
    print(f"  12 x {i:2} = {12 * i:3}")

# Exercise 2
print("\nEx2 - Tables 2 to 5:")
for num in range(2, 6):
    print(f"\nTable of {num}:")
    for i in range(1, 11):
        print(f"  {num} x {i:2} = {num * i:3}")

# Exercise 3
print("\nEx3 - Table of 7 (1 to 15):")
for i in range(1, 16):
    print(f"  7 x {i:2} = {7 * i:3}")

# Exercise 4
print("\nEx4 - Tables 1 to 5 in Grid:")
print_table_grid(1, 5)

# Exercise 5
print("\nEx5 - Table of 8 (Reverse):")
for i in range(10, 0, -1):
    print(f"  8 x {i:2} = {8 * i:3}")

# Challenge
print("\nChallenge - 10x10 Multiplication Grid:")
print_table_grid(1, 10)

# ============================================
# PART 8: PERFORMANCE COMPARISON
# ============================================

print("\n⚡ PART 8: PERFORMANCE COMPARISON")
print("-" * 50)

import time

# Test range vs list
print("Testing 10 million iterations...")

# Using range directly (memory efficient)
start = time.time()
total_range = 0
for i in range(10_000_000):
    total_range += i
range_time = time.time() - start

# Using list from range (memory heavy)
start = time.time()
total_list = 0
for i in list(range(10_000_000)):
    total_list += i
list_time = time.time() - start

print(f"range() time: {range_time:.4f}s")
print(f"list(range()) time: {list_time:.4f}s")
print(f"range is {list_time/range_time:.2f}x faster and memory efficient!")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ FOR LOOP & RANGE MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    range() SYNTAX                           │
├─────────────────────────────────────────────────────────────┤
│  range(stop)               → 0 to stop-1                   │
│  range(start, stop)        → start to stop-1               │
│  range(start, stop, step)  → start to stop-1 with step    │
├─────────────────────────────────────────────────────────────┤
│                    FOR LOOP WITH RANGE                     │
├─────────────────────────────────────────────────────────────┤
│  for i in range(5):        → 0,1,2,3,4                    │
│  for i in range(1,6):      → 1,2,3,4,5                    │
│  for i in range(2,11,2):   → 2,4,6,8,10                   │
│  for i in range(5,0,-1):   → 5,4,3,2,1                    │
├─────────────────────────────────────────────────────────────┤
│                    f-string ALIGNMENT                      │
├─────────────────────────────────────────────────────────────┤
│  {value}                   → Default                       │
│  {value:>5}                → Right aligned, width 5       │
│  {value:<5}                → Left aligned, width 5        │
│  {value:^5}                → Center aligned, width 5      │
├─────────────────────────────────────────────────────────────┤
│                    MULTIPLICATION TABLE                    │
├─────────────────────────────────────────────────────────────┤
│  for i in range(1, 11):                                   │
│      print(f"{num} x {i:2} = {num * i:3}")               │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python List Comprehensions - Complete Guide
""")