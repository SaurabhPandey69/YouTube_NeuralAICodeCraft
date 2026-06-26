"""
PYTHON NESTED LISTS - FOR LOOP VS LIST COMPREHENSION
NeuralAICodeCraft - Complete Guide to List of Lists

Topics Covered:
1. Nested Lists Basics
2. Creating with For Loops
3. Creating with List Comprehension
4. Accessing Elements
5. Iterating Through Nested Lists
6. For Loop vs List Comprehension
7. Real-World Examples
"""

import time

print("=" * 70)
print("🐍 PYTHON NESTED LISTS - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: NESTED LISTS BASICS
# ============================================

print("\n📚 PART 1: NESTED LISTS BASICS")
print("-" * 50)

print("""
WHAT IS A NESTED LIST?
├── A list that contains other lists as elements
├── Also called a 2D list or matrix
├── Like a table with rows and columns
└── Can be nested to any depth

VISUAL:
    [
        [1, 2, 3],  ← Row 0 (index 0)
        [4, 5, 6],  ← Row 1 (index 1)
        [7, 8, 9]   ← Row 2 (index 2)
    ]
    ↑  ↑  ↑
    │  │  └── Column 2
    │  └──── Column 1
    └─────── Column 0
""")

# 1.1 Manual Creation
print("\n1.1 Manual Creation:")
print("-" * 30)

# Method 1: Direct definition
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Matrix: {matrix}")

# With readable formatting
matrix_readable = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Readable matrix: {matrix_readable}")

# 1.2 Accessing Elements
print("\n1.2 Accessing Elements (Row, Column):")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"matrix[0][0] → {matrix[0][0]}  # Row 0, Column 0")
print(f"matrix[1][2] → {matrix[1][2]}  # Row 1, Column 2")
print(f"matrix[2][1] → {matrix[2][1]}  # Row 2, Column 1")
print(f"matrix[0]    → {matrix[0]}    # Entire row 0")

# 1.3 Printing Like a Matrix
print("\n1.3 Printing Like a Matrix:")
print("-" * 30)

def print_matrix(mat):
    """Print matrix in a readable format"""
    for row in mat:
        print("  " + " ".join(f"{x:3}" for x in row))

print("Matrix:")
print_matrix(matrix)

# ============================================
# PART 2: CREATING WITH FOR LOOPS
# ============================================

print("\n🔄 PART 2: CREATING WITH FOR LOOPS")
print("-" * 50)

print("""
For loops are the traditional way to create nested lists.
- Nested for loops: outer loop for rows, inner for columns
- More readable for complex logic
- Slower than list comprehension
""")

# 2.1 Basic Nested For Loop
print("\n2.1 Basic Nested For Loop:")
print("-" * 30)

rows = 3
cols = 4

# Create empty matrix
matrix_loop = []

# Outer loop: rows
for i in range(rows):
    row = []
    # Inner loop: columns
    for j in range(cols):
        row.append(i * cols + j + 1)
    matrix_loop.append(row)

print(f"Matrix ({rows}x{cols}):")
print_matrix(matrix_loop)

# 2.2 Creating a Multiplication Table
print("\n2.2 Multiplication Table (5x5):")
print("-" * 30)

mult_table = []

for i in range(1, 6):
    row = []
    for j in range(1, 6):
        row.append(i * j)
    mult_table.append(row)

print("Multiplication Table:")
print_matrix(mult_table)

# 2.3 Identity Matrix
print("\n2.3 Identity Matrix (4x4):")
print("-" * 30)

identity = []

for i in range(4):
    row = []
    for j in range(4):
        if i == j:
            row.append(1)
        else:
            row.append(0)
    identity.append(row)

print("Identity Matrix:")
print_matrix(identity)

# 2.4 Custom Values with Nested Loops
print("\n2.4 Custom Pattern Matrix:")
print("-" * 30)

pattern = []

for i in range(5):
    row = []
    for j in range(5):
        if (i + j) % 2 == 0:
            row.append("X")
        else:
            row.append("O")
    pattern.append(row)

print("Checkerboard Pattern:")
print_matrix(pattern)

# ============================================
# PART 3: ITERATING THROUGH NESTED LISTS
# ============================================

print("\n🔍 PART 3: ITERATING THROUGH NESTED LISTS")
print("-" * 50)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 3.1 Using Nested For Loops
print("\n3.1 Nested For Loops:")
print("-" * 30)

print("Iterating all elements:")
for row in matrix:
    for element in row:
        print(f"  {element}", end=" ")
    print()

# 3.2 Using Indexes
print("\n3.2 Iterating with Indexes:")
print("-" * 30)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"  matrix[{i}][{j}] = {matrix[i][j]}")

# 3.3 Sum of All Elements
print("\n3.3 Sum of All Elements:")
print("-" * 30)

total = 0
for row in matrix:
    for element in row:
        total += element

print(f"Total sum of matrix: {total}")

# 3.4 Flattening a Nested List
print("\n3.4 Flattening a Nested List:")
print("-" * 30)

nested = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = []

for sublist in nested:
    for element in sublist:
        flat.append(element)

print(f"Nested: {nested}")
print(f"Flattened: {flat}")

# ============================================
# PART 4: LIST COMPREHENSION BASICS
# ============================================

print("\n⚡ PART 4: LIST COMPREHENSION BASICS")
print("-" * 50)

print("""
LIST COMPREHENSION:
- A concise way to create lists
- Syntax: [expression for item in iterable if condition]
- More Pythonic than for loops
- Often faster than loops
""")

# 4.1 Basic List Comprehension
print("\n4.1 Basic List Comprehension:")
print("-" * 30)

# For loop version
squares_loop = []
for i in range(10):
    squares_loop.append(i ** 2)

# Comprehension version
squares_comp = [i ** 2 for i in range(10)]

print(f"Squares (for loop): {squares_loop}")
print(f"Squares (comprehension): {squares_comp}")
print(f"Same result? {squares_loop == squares_comp}")

# 4.2 With Condition
print("\n4.2 Comprehension with Condition:")
print("-" * 30)

# Even numbers
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Odd numbers
odds = [x for x in range(20) if x % 2 != 0]
print(f"Odd numbers: {odds}")

# 4.3 Multiple Iterables
print("\n4.3 Comprehension with Multiple Iterables:")
print("-" * 30)

pairs = [(x, y) for x in range(3) for y in range(3)]
print(f"All pairs: {pairs}")

# 4.4 Nested List Comprehension (One-dimensional)
print("\n4.4 Nested Comprehension (Flattening):")
print("-" * 30)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat_comp = [element for row in nested for element in row]

print(f"Nested: {nested}")
print(f"Flattened (comprehension): {flat_comp}")

# ============================================
# PART 5: NESTED LIST COMPREHENSION
# ============================================

print("\n🏗️ PART 5: NESTED LIST COMPREHENSION")
print("-" * 50)

print("""
NESTED LIST COMPREHENSION:
- Creates a list of lists
- Syntax: [[expression for j in range(cols)] for i in range(rows)]
- The inner comprehension creates each row
- The outer comprehension creates the list of rows
""")

# 5.1 Creating a Matrix
print("\n5.1 Creating a Matrix (3x3):")
print("-" * 30)

# Using nested comprehension
matrix_comp = [[i * 3 + j + 1 for j in range(3)] for i in range(3)]

print("Matrix (list comprehension):")
print_matrix(matrix_comp)

# 5.2 Step-by-Step Breakdown
print("\n5.2 Step-by-Step Breakdown:")
print("-" * 30)

print("""
[[i * 3 + j + 1 for j in range(3)] for i in range(3)]

Step 1: Outer loop i = 0, 1, 2
Step 2: For each i, inner loop j = 0, 1, 2
Step 3: Calculate i * 3 + j + 1

i=0: j=0→1, j=1→2, j=2→3 → [1,2,3]
i=1: j=0→4, j=1→5, j=2→6 → [4,5,6]
i=2: j=0→7, j=1→8, j=2→9 → [7,8,9]
""")

# 5.3 Multiplication Table with Comprehension
print("\n5.3 Multiplication Table (Comprehension):")
print("-" * 30)

mult_comp = [[i * j for j in range(1, 6)] for i in range(1, 6)]

print("Multiplication Table (list comprehension):")
print_matrix(mult_comp)

# 5.4 Identity Matrix with Comprehension
print("\n5.4 Identity Matrix (Comprehension):")
print("-" * 30)

identity_comp = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

print("Identity Matrix (list comprehension):")
print_matrix(identity_comp)

# 5.5 Checkerboard Pattern with Comprehension
print("\n5.5 Checkerboard Pattern (Comprehension):")
print("-" * 30)

checkerboard = [["X" if (i + j) % 2 == 0 else "O" for j in range(5)] for i in range(5)]

print("Checkerboard (list comprehension):")
print_matrix(checkerboard)

# ============================================
# PART 6: FOR LOOP vs LIST COMPREHENSION
# ============================================

print("\n⚡ PART 6: FOR LOOP vs LIST COMPREHENSION")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  FOR LOOP           │  LIST COMPREHENSION  │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Syntax         │  Multi-line         │  Single line         │
│  Speed          │  Slower             │  Faster              │
│  Readability    │  Very clear         │  Very concise        │
│  Complexity     │  Handles complex    │  Best for simple     │
│  Memory         │  Efficient          │  Efficient           │
│  Debugging      │  Easier             │  Harder              │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 6.1 Performance Comparison
print("\n6.1 Performance Comparison:")
print("-" * 30)

def create_matrix_loop(rows, cols):
    """Create matrix using for loops"""
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(i * cols + j + 1)
        result.append(row)
    return result

def create_matrix_comp(rows, cols):
    """Create matrix using list comprehension"""
    return [[i * cols + j + 1 for j in range(cols)] for i in range(rows)]

# Time the loop version
start = time.time()
loop_result = create_matrix_loop(1000, 100)
loop_time = time.time() - start

# Time the comprehension version
start = time.time()
comp_result = create_matrix_comp(1000, 100)
comp_time = time.time() - start

print(f"Matrix size: 1000 x 100")
print(f"For loop time: {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s")
print(f"Comprehension is {loop_time/comp_time:.1f}x faster!")

# 6.2 When to Use Each
print("\n6.2 When to Use Each:")
print("-" * 30)

print("""
USE FOR LOOPS when:
├── Logic is complex (multiple conditions)
├── Need to modify elements in place
├── Debugging is required
├── Working with large datasets (memory considerations)
└── Code readability is more important than speed

USE LIST COMPREHENSION when:
├── Creating lists from existing data
├── Simple transformations
├── Filtering with a single condition
├── Performance matters
└── Code conciseness is desired
""")

# ============================================
# PART 7: REAL-WORLD EXAMPLES
# ============================================

print("\n🚀 PART 7: REAL-WORLD EXAMPLES")
print("-" * 50)

# 7.1 Student Grades Management
print("\n7.1 Student Grades Management:")
print("-" * 30)

# Create gradebook using comprehension
students = ["Alice", "Bob", "Charlie", "David"]
grades = [
    [85, 90, 78],  # Alice's grades
    [92, 88, 95],  # Bob's grades
    [78, 82, 80],  # Charlie's grades
    [95, 92, 89]   # David's grades
]

print("Student Gradebook:")
print("  Name    |  Math  Science  English")
print("  " + "-" * 40)
for i, name in enumerate(students):
    print(f"  {name:8}| ", end="")
    for grade in grades[i]:
        print(f"  {grade:3}", end="")
    print()

# Calculate averages using comprehension
averages = [sum(row) / len(row) for row in grades]
print(f"\nAverages: {averages}")

# 7.2 Temperature Conversion (Celsius to Fahrenheit)
print("\n7.2 Temperature Conversion Matrix:")
print("-" * 30)

# Celsius values
celsius = [ [0, 10, 20], [30, 40, 50], [60, 70, 80] ]

# Convert to Fahrenheit
fahrenheit = [[round(c * 9/5 + 32, 1) for c in row] for row in celsius]

print("Celsius Matrix:")
print_matrix(celsius)

print("\nFahrenheit Matrix:")
print_matrix(fahrenheit)

# 7.3 Transposing a Matrix
print("\n7.3 Matrix Transposition:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

# Transpose using comprehension
transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print("\nTransposed Matrix:")
print_matrix(transposed)

# 7.4 Filtering a Matrix
print("\n7.4 Filtering a Matrix (Numbers > 5):")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Filter using comprehension
filtered = [[x for x in row if x > 5] for row in matrix]

print("Original:")
print_matrix(matrix)

print("\nFiltered (x > 5):")
print_matrix(filtered)

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: 5x5 Matrix
Create a 5x5 matrix using list comprehension where each element is i*j.

🎯 EXERCISE 2: Pascal's Triangle
Create Pascal's triangle (5 rows) using nested loops.

🎯 EXERCISE 3: Matrix Addition
Add two 3x3 matrices using nested loops.

🎯 EXERCISE 4: Flatten Nested List
Flatten [[1,2],[3,4,5],[6]] using comprehension.

🎯 EXERCISE 5: Custom Matrix
Create a matrix where even rows contain zeros, odd rows contain ones.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - 5x5 Matrix:")
mat1 = [[i * j for j in range(5)] for i in range(5)]
print("  i*j matrix:")
print_matrix(mat1)

# Exercise 2
print("\nEx2 - Pascal's Triangle:")
def pascal(n):
    triangle = []
    for i in range(n):
        row = [1]
        if triangle:
            last_row = triangle[-1]
            row.extend([last_row[j] + last_row[j+1] for j in range(len(last_row)-1)])
            row.append(1)
        triangle.append(row)
    return triangle

pascal_5 = pascal(5)
print("  Pascal's Triangle (5 rows):")
for row in pascal_5:
    print(f"    {row}")

# Exercise 3
print("\nEx3 - Matrix Addition:")
a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
c = [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
print(f"  A: {a}")
print(f"  B: {b}")
print(f"  A+B: {c}")

# Exercise 4
print("\nEx4 - Flatten:")
nested = [[1,2],[3,4,5],[6]]
flat = [x for sublist in nested for x in sublist]
print(f"  {nested} → {flat}")

# Exercise 5
print("\nEx5 - Custom Matrix (4x4):")
custom = [[0 if i % 2 == 0 else 1 for j in range(4)] for i in range(4)]
print("  Even rows=0, Odd rows=1:")
print_matrix(custom)

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ NESTED LISTS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│              NESTED LIST CREATION                           │
├─────────────────────────────────────────────────────────────┤
│  FOR LOOP:                                                  │
│  matrix = []                                                │
│  for i in range(rows):                                     │
│      row = []                                               │
│      for j in range(cols):                                 │
│          row.append(value)                                  │
│      matrix.append(row)                                     │
├─────────────────────────────────────────────────────────────┤
│  LIST COMPREHENSION:                                        │
│  matrix = [[value for j in range(cols)] for i in range(rows)] │
├─────────────────────────────────────────────────────────────┤
│              ACCESSING ELEMENTS                             │
├─────────────────────────────────────────────────────────────┤
│  matrix[row][col]         → Single element                  │
│  matrix[row]              → Entire row                      │
│  [row[col] for row in matrix] → Entire column              │
├─────────────────────────────────────────────────────────────┤
│              COMMON OPERATIONS                              │
├─────────────────────────────────────────────────────────────┤
│  Sum all: sum(sum(row) for row in matrix)                  │
│  Flatten: [x for row in matrix for x in row]              │
│  Transpose: [[row[i] for row in matrix] for i in range(n)] │
│  Filter: [[x for x in row if condition] for row in matrix] │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python Arrays (array module) vs Lists
""")