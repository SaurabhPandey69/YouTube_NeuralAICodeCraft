"""
PYTHON NESTED LOOPS - COMPLETE GUIDE WITH PATTERNS
NeuralAICodeCraft - Master Nested Loops

Topics Covered:
1. Nested Loop Basics
2. Star Patterns
3. Number Patterns
4. Alphabet Patterns
5. Multiplication Table
6. Matrix Operations
7. Real-World Applications
"""

print("=" * 70)
print("🔄 PYTHON NESTED LOOPS - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: NESTED LOOP BASICS
# ============================================

print("\n📚 PART 1: NESTED LOOP BASICS")
print("-" * 50)

print("""
WHAT IS A NESTED LOOP?
├── A loop inside another loop
├── Outer loop runs once
├── Inner loop runs completely for each outer iteration
├── Total iterations = outer_iterations * inner_iterations

SYNTAX:
for i in range(3):          # Outer loop
    for j in range(2):      # Inner loop
        print(i, j)
""")

# 1.1 Basic Nested Loop
print("\n1.1 Basic Nested Loop:")
print("-" * 30)

print("i: outer loop, j: inner loop")
for i in range(3):
    for j in range(2):
        print(f"  i={i}, j={j}")

print("\nExecution flow:")
print("  i=0 → j=0, j=1 → i=1 → j=0, j=1 → i=2 → j=0, j=1")

# 1.2 Understanding Execution Flow
print("\n1.2 Execution Flow Visualization:")
print("-" * 30)

print("Outer loop i = 0:")
for j in range(3):
    print(f"  Inner loop j = {j}")
print("Inner loop complete!")

print("\nOuter loop i = 1:")
for j in range(3):
    print(f"  Inner loop j = {j}")
print("Inner loop complete!")

print("\nOuter loop i = 2:")
for j in range(3):
    print(f"  Inner loop j = {j}")
print("Inner loop complete!")

# ============================================
# PART 2: STAR PATTERNS
# ============================================

print("\n⭐ PART 2: STAR PATTERNS")
print("-" * 50)

# 2.1 Right Triangle
print("\n2.1 Right Triangle Pattern:")
print("-" * 30)

print("Pattern 1: Right Triangle")
n = 5
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

# 2.2 Left Triangle (Reverse)
print("\n2.2 Left Triangle Pattern:")
print("-" * 30)

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# 2.3 Right-Aligned Triangle
print("\n2.3 Right-Aligned Triangle:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end="")
    # Stars
    for j in range(i):
        print("*", end="")
    print()

# 2.4 Pyramid Pattern
print("\n2.4 Pyramid Pattern:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    # Spaces
    for j in range(n - i):
        print(" ", end="")
    # Stars (2*i-1)
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 2.5 Diamond Pattern
print("\n2.5 Diamond Pattern:")
print("-" * 30)

n = 5
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# 2.6 Hollow Square
print("\n2.6 Hollow Square Pattern:")
print("-" * 30)

n = 5
for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# 2.7 X Pattern
print("\n2.7 X Pattern:")
print("-" * 30)

n = 5
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# ============================================
# PART 3: NUMBER PATTERNS
# ============================================

print("\n🔢 PART 3: NUMBER PATTERNS")
print("-" * 50)

# 3.1 Simple Number Triangle
print("\n3.1 Number Triangle:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 3.2 Same Number Triangle
print("\n3.2 Same Number Triangle:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

# 3.3 Reverse Number Triangle
print("\n3.3 Reverse Number Triangle:")
print("-" * 30)

n = 5
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

# 3.4 Floyd's Triangle
print("\n3.4 Floyd's Triangle:")
print("-" * 30)

n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(f"{num:2}", end=" ")
        num += 1
    print()

# 3.5 Pascal's Triangle
print("\n3.5 Pascal's Triangle:")
print("-" * 30)

n = 5
pascal = []
for i in range(n):
    row = [1]
    if pascal:
        last_row = pascal[-1]
        for j in range(len(last_row) - 1):
            row.append(last_row[j] + last_row[j + 1])
        row.append(1)
    pascal.append(row)

for row in pascal:
    print(" " * (n - len(row)), end="")
    for num in row:
        print(f"{num:4}", end="")
    print()

# 3.6 Pattern of 1 and 0
print("\n3.6 Pattern of 1 and 0:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(1 if j % 2 == 1 else 0, end="")
    print()

# ============================================
# PART 4: ALPHABET PATTERNS
# ============================================

print("\n🔤 PART 4: ALPHABET PATTERNS")
print("-" * 50)

# 4.1 Alphabet Triangle
print("\n4.1 Alphabet Triangle:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# 4.2 Same Alphabet Triangle
print("\n4.2 Same Alphabet Triangle:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(i):
        print(chr(64 + i), end="")
    print()

# 4.3 Reverse Alphabet Triangle
print("\n4.3 Reverse Alphabet Triangle:")
print("-" * 30)

n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

# 4.4 Alphabet Pyramid
print("\n4.4 Alphabet Pyramid:")
print("-" * 30)

n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i):
        print(chr(65 + j), end="")
    for j in range(i - 1, 0, -1):
        print(chr(65 + j - 1), end="")
    print()

# ============================================
# PART 5: MULTIPLICATION TABLE
# ============================================

print("\n📊 PART 5: MULTIPLICATION TABLE")
print("-" * 50)

# 5.1 Single Table using Nested Loop
print("\n5.1 Multiplication Table of 5:")
print("-" * 30)

num = 5
for i in range(1, 11):
    for j in range(1, 2):
        print(f"  {num} x {i:2} = {num * i:3}")

# 5.2 Multiple Tables
print("\n5.2 Tables 1 to 5:")
print("-" * 30)

for num in range(1, 6):
    print(f"\nTable of {num}:")
    print("  " + "-" * 20)
    for i in range(1, 11):
        print(f"  {num} x {i:2} = {num * i:3}")

# 5.3 Table Grid
print("\n5.3 Multiplication Table Grid (1-5):")
print("-" * 30)

# Header
print("   ", end="")
for num in range(1, 6):
    print(f"{num:>6}", end="")
print()
print("   " + "=" * 30)

# Rows
for i in range(1, 6):
    print(f"{i:2} |", end="")
    for num in range(1, 6):
        print(f"{num * i:>6}", end="")
    print()

# 5.4 Table 1-10 (Big Grid)
print("\n5.4 Multiplication Table (1-10):")
print("-" * 30)

def print_table_grid(n):
    print("   ", end="")
    for num in range(1, n + 1):
        print(f"{num:>5}", end="")
    print()
    print("   " + "-" * (5 * n))

    for i in range(1, n + 1):
        print(f"{i:2} |", end="")
        for num in range(1, n + 1):
            print(f"{num * i:>5}", end="")
        print()

print_table_grid(10)

# ============================================
# PART 6: MATRIX OPERATIONS
# ============================================

print("\n📐 PART 6: MATRIX OPERATIONS")
print("-" * 50)

# 6.1 Creating a Matrix
print("\n6.1 Creating a 3x3 Matrix:")
print("-" * 30)

rows, cols = 3, 3
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix.append(row)

print("Matrix:")
for row in matrix:
    for element in row:
        print(f"{element:3}", end="")
    print()

# 6.2 Sum of Matrix Elements
print("\n6.2 Sum of Matrix Elements:")
print("-" * 30)

total = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        total += matrix[i][j]

print(f"Sum of all elements: {total}")

# 6.3 Row Sums
print("\n6.3 Row Sums:")
print("-" * 30)

for i in range(len(matrix)):
    row_sum = 0
    for j in range(len(matrix[i])):
        row_sum += matrix[i][j]
    print(f"  Row {i+1} sum: {row_sum}")

# 6.4 Column Sums
print("\n6.4 Column Sums:")
print("-" * 30)

for j in range(len(matrix[0])):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]
    print(f"  Col {j+1} sum: {col_sum}")

# 6.5 Transpose Matrix
print("\n6.5 Transpose Matrix:")
print("-" * 30)

print("Original:")
for row in matrix:
    print(f"  {row}")

transpose = []
for i in range(len(matrix[0])):
    row = []
    for j in range(len(matrix)):
        row.append(matrix[j][i])
    transpose.append(row)

print("\nTranspose:")
for row in transpose:
    print(f"  {row}")

# ============================================
# PART 7: REAL-WORLD APPLICATIONS
# ============================================

print("\n🚀 PART 7: REAL-WORLD APPLICATIONS")
print("-" * 50)

# 7.1 Student Grades
print("\n7.1 Student Grade Matrix:")
print("-" * 30)

students = ["Alice", "Bob", "Charlie", "David"]
subjects = ["Math", "Science", "English"]
grades = [
    [85, 90, 78],
    [92, 88, 95],
    [78, 82, 80],
    [95, 92, 89]
]

print("  Student   | Math   Science  English | Average")
print("  " + "-" * 50)

for i in range(len(students)):
    total = 0
    print(f"  {students[i]:10}", end="")
    for j in range(len(subjects)):
        print(f"{grades[i][j]:8}", end="")
        total += grades[i][j]
    avg = total / len(subjects)
    print(f"  {avg:8.1f}")

# 7.2 Seat Reservation (2D Grid)
print("\n7.2 Seat Reservation System:")
print("-" * 30)

# 5 rows, 5 columns
seats = [["A" for j in range(5)] for i in range(5)]
print("Initial seats:")
for row in seats:
    print("  " + " ".join(row))

# Reserve some seats
seats[0][0] = "X"
seats[1][2] = "X"
seats[2][4] = "X"
seats[3][1] = "X"

print("\nReserved seats (X):")
for row in seats:
    print("  " + " ".join(row))

# 7.3 Sudoku Grid (Partial)
print("\n7.3 Sudoku Grid (3x3):")
print("-" * 30)

sudoku = [
    [5, 3, 0],
    [6, 0, 0],
    [0, 9, 8]
]

for row in sudoku:
    for num in row:
        print(f"{num:2}", end="")
    print()

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Star Pattern
Print a reverse pyramid of stars.

🎯 EXERCISE 2: Number Pattern
Print a pattern of numbers in reverse order.

🎯 EXERCISE 3: Multiplication Grid
Create a 5x5 multiplication grid.

🎯 EXERCISE 4: Matrix Addition
Add two 3x3 matrices.

🎯 EXERCISE 5: Character Pattern
Print a triangle of letters.

🎯 CHALLENGE: Diamond Pattern with Numbers
Print a diamond pattern filled with numbers.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Reverse Pyramid:")
n = 5
for i in range(n, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()

# Exercise 2
print("\nEx2 - Number Pattern:")
n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()

# Exercise 3
print("\nEx3 - 5x5 Multiplication Grid:")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:4}", end="")
    print()

# Exercise 4
print("\nEx4 - Matrix Addition:")
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]
C = [[0,0],[0,0]]
for i in range(2):
    for j in range(2):
        C[i][j] = A[i][j] + B[i][j]
print("  A + B =", C)

# Exercise 5
print("\nEx5 - Character Triangle:")
n = 5
for i in range(n):
    for j in range(i + 1):
        print(chr(65 + j), end="")
    print()

# Challenge
print("\nChallenge - Diamond with Numbers:")
n = 4
# Upper half
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
# Lower half
for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ NESTED LOOPS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│              NESTED LOOP PATTERNS                           │
├─────────────────────────────────────────────────────────────┤
│  Right Triangle:                                            │
│  for i in range(n):                                        │
│      for j in range(i+1):                                  │
│          print("*", end="")                                │
│      print()                                                │
├─────────────────────────────────────────────────────────────┤
│  Pyramid:                                                    │
│  for i in range(n):                                        │
│      for j in range(n-i-1):                                │
│          print(" ", end="")                                │
│      for j in range(2*i+1):                                │
│          print("*", end="")                                │
│      print()                                                │
├─────────────────────────────────────────────────────────────┤
│  Number Triangle:                                           │
│  for i in range(1, n+1):                                   │
│      for j in range(1, i+1):                               │
│          print(j, end="")                                  │
│      print()                                                │
├─────────────────────────────────────────────────────────────┤
│              KEY RULES                                      │
├─────────────────────────────────────────────────────────────┤
│  ✅ Outer loop controls ROWS                               │
│  ✅ Inner loop controls COLUMNS                            │
│  ✅ Inner loop runs completely for each outer iteration   │
│  ✅ Total iterations = outer * inner                       │
│  ✅ Use end="" to print on same line                      │
│  ✅ Use print() to move to next line                      │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python Pattern Programs - Advanced Practice
""")