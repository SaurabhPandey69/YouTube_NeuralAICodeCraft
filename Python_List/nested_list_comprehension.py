"""
NESTED LIST COMPREHENSION - FLATTEN MATRIX
NeuralAICodeCraft - Master Nested Loops in List Comprehension

Topics Covered:
1. Nested For Loops Review
2. Nested List Comprehension Syntax
3. Flattening Nested Lists
4. Creating Matrices
5. Advanced Techniques
"""

print("=" * 70)
print("🐍 NESTED LIST COMPREHENSION - FLATTEN MATRIX")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: NESTED FOR LOOPS REVIEW
# ============================================

print("\n📚 PART 1: NESTED FOR LOOPS REVIEW")
print("-" * 50)

print("""
Before nested list comprehension, understand nested for loops:

for outer in iterable1:
    for inner in iterable2:
        # Do something with outer and inner

The inner loop runs completely for each iteration of the outer loop.
""")

# 1.1 Basic Nested Loop
print("\n1.1 Basic Nested Loop:")
print("-" * 30)

colors = ["red", "blue"]
sizes = ["S", "M", "L"]

print("  Colors:", colors)
print("  Sizes:", sizes)

print("\n  Nested loop execution:")
for color in colors:
    for size in sizes:
        print(f"    {color} - {size}")

# 1.2 Nested Loop to Create Pairs
print("\n1.2 Nested Loop to Create Pairs:")
print("-" * 30)

pairs = []
for color in colors:
    for size in sizes:
        pairs.append((color, size))
print(f"  Pairs: {pairs}")

# ============================================
# PART 2: NESTED LIST COMPREHENSION SYNTAX
# ============================================

print("\n🎯 PART 2: NESTED LIST COMPREHENSION SYNTAX")
print("-" * 50)

print("""
SYNTAX:
    [expression for outer in iterable1 for inner in iterable2]

This is equivalent to:
    result = []
    for outer in iterable1:
        for inner in iterable2:
            result.append(expression)

The for loops are in the SAME ORDER as nested for loops!
""")

# 2.1 Basic Nested Comprehension
print("\n2.1 Basic Nested Comprehension:")
print("-" * 30)

colors = ["red", "blue"]
sizes = ["S", "M", "L"]

# List comprehension
pairs_comp = [(color, size) for color in colors for size in sizes]
print(f"  Pairs (comprehension): {pairs_comp}")

# 2.2 Understanding the Order
print("\n2.2 Understanding the Order:")
print("-" * 30)

print("""
For loops:          List Comprehension:
for color in colors:    [expr for color in colors
    for size in sizes:          for size in sizes]

✅ The order is the same! Outer loop first, inner loop second.
""")

# 2.3 Different Iterables
print("\n2.3 Different Iterables:")
print("-" * 30)

rows = [1, 2, 3]
cols = ["A", "B"]

# List comprehension
grid = [(row, col) for row in rows for col in cols]
print(f"  Grid positions: {grid}")

# ============================================
# PART 3: FLATTENING A MATRIX
# ============================================

print("\n📦 PART 3: FLATTENING A MATRIX (Nested List -> Flat List)")
print("-" * 50)

print("""
Flattening a 2D list (matrix) into a 1D list:
- Use nested comprehension with outer loop (rows) and inner loop (columns)
- Each element is added in row-major order
""")

# 3.1 Basic Flattening
print("\n3.1 Basic Flattening:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Matrix:")
for row in matrix:
    print(f"    {row}")

# For loop flattening
flat_for = []
for row in matrix:
    for num in row:
        flat_for.append(num)
print(f"\n  For loop flatten: {flat_for}")

# List comprehension flattening
flat_comp = [num for row in matrix for num in row]
print(f"  Comprehension flatten: {flat_comp}")

# 3.2 Flattening with Transformation
print("\n3.2 Flattening with Transformation:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Square each element while flattening
squared_flat = [num ** 2 for row in matrix for num in row]
print(f"  Original matrix flattened: {[num for row in matrix for num in row]}")
print(f"  Squared and flattened: {squared_flat}")

# 3.3 Flattening with String Formatting
print("\n3.3 Flattening with String Formatting:")
print("-" * 30)

matrix = [
    ["a", "b", "c"],
    ["d", "e", "f"],
    ["g", "h", "i"]
]

# Flatten and capitalize
flat_capitalized = [letter.upper() for row in matrix for letter in row]
print(f"  Original matrix: {matrix}")
print(f"  Flattened and capitalized: {flat_capitalized}")

# 3.4 Flattening Variable Length Rows
print("\n3.4 Flattening Variable Length Rows:")
print("-" * 30)

jagged = [
    [1, 2],
    [3, 4, 5],
    [6],
    [7, 8, 9, 10]
]

print("  Jagged matrix:")
for row in jagged:
    print(f"    {row}")

flat_jagged = [num for row in jagged for num in row]
print(f"  Flattened: {flat_jagged}")

# ============================================
# PART 4: FLATTENING WITH CONDITIONS
# ============================================

print("\n🔀 PART 4: FLATTENING WITH CONDITIONS")
print("-" * 50)

# 4.1 Filtering While Flattening
print("\n4.1 Filtering While Flattening:")
print("-" * 30)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Flatten only even numbers
even_flat = [num for row in matrix for num in row if num % 2 == 0]
print(f"  Original matrix: {matrix}")
print(f"  Even numbers only: {even_flat}")

# 4.2 Flattening with Multiple Conditions
print("\n4.2 Flattening with Multiple Conditions:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten numbers > 3 and even
filtered = [num for row in matrix for num in row if num > 3 and num % 2 == 0]
print(f"  Original matrix: {matrix}")
print(f"  Numbers > 3 and even: {filtered}")

# 4.3 Flattening with if-else
print("\n4.3 Flattening with if-else Transformation:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Flatten and classify as even/odd
classified = ["even" if num % 2 == 0 else "odd" for row in matrix for num in row]
print(f"  Original matrix: {matrix}")
print(f"  Classified: {classified}")

# ============================================
# PART 5: CREATING MATRICES WITH COMPREHENSION
# ============================================

print("\n🔢 PART 5: CREATING MATRICES WITH COMPREHENSION")
print("-" * 50)

# 5.1 Creating a Matrix
print("\n5.1 Creating a Matrix:")
print("-" * 30)

# 3x3 matrix of zeros
zero_matrix = [[0 for _ in range(3)] for _ in range(3)]
print(f"  3x3 zero matrix: {zero_matrix}")

# 5.2 Multiplication Table
print("\n5.2 Multiplication Table:")
print("-" * 30)

multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print("  5x5 Multiplication Table:")
for row in multiplication_table:
    print(f"    {row}")

# 5.3 Identity Matrix
print("\n5.3 Identity Matrix:")
print("-" * 30)

def identity_matrix(n):
    """Create an n x n identity matrix"""
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]

id_3 = identity_matrix(3)
print("  3x3 Identity Matrix:")
for row in id_3:
    print(f"    {row}")

id_4 = identity_matrix(4)
print("\n  4x4 Identity Matrix:")
for row in id_4:
    print(f"    {row}")

# 5.4 Matrix with Custom Pattern
print("\n5.4 Matrix with Custom Pattern:")
print("-" * 30)

# Checkerboard pattern
checkerboard = [[(i + j) % 2 for j in range(5)] for i in range(5)]
print("  5x5 Checkerboard:")
for row in checkerboard:
    print(f"    {row}")

# 5.5 Triangle Pattern
print("\n5.5 Triangle Pattern:")
print("-" * 30)

triangle = [[1 if j <= i else 0 for j in range(5)] for i in range(5)]
print("  5x5 Lower Triangle:")
for row in triangle:
    print(f"    {row}")

# ============================================
# PART 6: COMPLEX NESTED COMPREHENSIONS
# ============================================

print("\n🚀 PART 6: COMPLEX NESTED COMPREHENSIONS")
print("-" * 50)

# 6.1 Transposing a Matrix
print("\n6.1 Transposing a Matrix:")
print("-" * 30)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("  Original Matrix:")
for row in matrix:
    print(f"    {row}")

# Transpose using nested comprehension
transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
print("  Transposed Matrix:")
for row in transpose:
    print(f"    {row}")

# 6.2 Flattening a 3D List
print("\n6.2 Flattening a 3D List:")
print("-" * 30)

three_d = [
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
]

print("  3D List:")
for matrix_2d in three_d:
    print(f"    {matrix_2d}")

# Flatten to 1D
flat_3d = [num for matrix_2d in three_d for row in matrix_2d for num in row]
print(f"  Flattened to 1D: {flat_3d}")

# Flatten to 2D
flat_2d = [num for matrix_2d in three_d for row in matrix_2d for num in row]
print(f"  Flattened to 1D: {flat_2d}")

# 6.3 Nested Comprehension with Multiple Conditions
print("\n6.3 Nested Comprehension with Multiple Conditions:")
print("-" * 30)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Flatten numbers divisible by 3
divisible_by_3 = [num for row in matrix for num in row if num % 3 == 0]
print(f"  Original matrix: {matrix}")
print(f"  Numbers divisible by 3: {divisible_by_3}")

# ============================================
# PART 7: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 7: REAL-WORLD EXAMPLES")
print("-" * 30)

# 7.1 Reading CSV-like Data
print("\n7.1 Processing CSV-like Data:")
print("-" * 30)

csv_data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "Los Angeles"],
    ["Charlie", "35", "Chicago"]
]

# Extract all values (excluding header)
all_values = [value for row in csv_data[1:] for value in row]
print(f"  All values: {all_values}")

# Extract only ages
ages = [int(row[1]) for row in csv_data[1:]]
print(f"  Ages: {ages}")

# 7.2 Student Grades
print("\n7.2 Student Grades Processing:")
print("-" * 30)

student_grades = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 75, 80],
    [95, 85, 90]
]

# Flatten all grades
all_grades = [grade for student in student_grades for grade in student]
print(f"  All grades: {all_grades}")

# Average of all grades
avg_all = sum(all_grades) / len(all_grades)
print(f"  Average of all grades: {avg_all:.2f}")

# Grades above 85
top_grades = [grade for student in student_grades for grade in student if grade > 85]
print(f"  Grades above 85: {top_grades}")

# 7.3 Flattening for Data Analysis
print("\n7.3 Data Analysis - Flattening Sales Data:")
print("-" * 30)

sales_data = [
    ["Product A", 100, 120, 90],
    ["Product B", 80, 85, 95],
    ["Product C", 150, 140, 160]
]

# Flatten all sales numbers
all_sales = [num for row in sales_data for num in row if isinstance(num, (int, float))]
print(f"  All sales numbers: {all_sales}")

# Total sales
total_sales = sum(all_sales)
print(f"  Total sales: {total_sales}")

# Monthly totals (columns)
month1 = sum([row[1] for row in sales_data])
month2 = sum([row[2] for row in sales_data])
month3 = sum([row[3] for row in sales_data])
print(f"  Monthly totals: Month1={month1}, Month2={month2}, Month3={month3}")

# 7.4 Image Processing Simulation
print("\n7.4 Image Processing - Flattening Pixels:")
print("-" * 30)

# Simulate a 3x3 grayscale image
image = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# Flatten the image
flat_image = [pixel for row in image for pixel in row]
print(f"  Original image: {image}")
print(f"  Flattened pixels: {flat_image}")

# Brighten the image (add 10 to each pixel)
brightened = [pixel + 10 for row in image for pixel in row]
print(f"  Brightened pixels: {brightened}")

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Flatten Matrix
Flatten [[1,2,3],[4,5,6],[7,8,9]] into [1,2,3,4,5,6,7,8,9]

🎯 EXERCISE 2: Create Multiplication Table
Create a 6x6 multiplication table using nested comprehension

🎯 EXERCISE 3: Flatten with Filter
Flatten and keep only odd numbers from a 2D list

🎯 EXERCISE 4: Matrix Transpose
Transpose a 3x4 matrix using nested comprehension

🎯 EXERCISE 5: Flatten Jagged List
Flatten [[1,2],[3,4,5],[6],[7,8,9,10]]

🎯 CHALLENGE: Deep Flatten
Flatten a nested list of any depth (recursive solution)
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Flatten Matrix:")
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat1 = [num for row in matrix1 for num in row]
print(f"  {matrix1} → {flat1}")

# Exercise 2
print("\nEx2 - Multiplication Table:")
table6 = [[i * j for j in range(1, 7)] for i in range(1, 7)]
print("  6x6 Multiplication Table:")
for row in table6:
    print(f"    {row}")

# Exercise 3
print("\nEx3 - Flatten with Filter:")
matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_flat = [num for row in matrix3 for num in row if num % 2 == 1]
print(f"  Original: {matrix3}")
print(f"  Odd numbers only: {odd_flat}")

# Exercise 4
print("\nEx4 - Matrix Transpose:")
matrix4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
transpose4 = [[matrix4[j][i] for j in range(len(matrix4))] for i in range(len(matrix4[0]))]
print("  Original:")
for row in matrix4:
    print(f"    {row}")
print("  Transposed:")
for row in transpose4:
    print(f"    {row}")

# Exercise 5
print("\nEx5 - Flatten Jagged List:")
jagged5 = [[1, 2], [3, 4, 5], [6], [7, 8, 9, 10]]
flat5 = [num for row in jagged5 for num in row]
print(f"  {jagged5} → {flat5}")

# Challenge
print("\nChallenge - Deep Flatten:")
def deep_flatten(nested_list):
    """Recursively flatten a nested list of any depth"""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

deep_nested = [1, [2, 3], [4, [5, 6]], 7, [8, [9, [10, 11]]]]
flattened_deep = deep_flatten(deep_nested)
print(f"  Deep nested: {deep_nested}")
print(f"  Fully flattened: {flattened_deep}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ NESTED LIST COMPREHENSION MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    BASIC SYNTAX                             │
├─────────────────────────────────────────────────────────────┤
│  [expr for outer in iter1 for inner in iter2]             │
│  Same order as nested for loops!                          │
├─────────────────────────────────────────────────────────────┤
│                    FLATTENING A MATRIX                      │
├─────────────────────────────────────────────────────────────┤
│  [num for row in matrix for num in row]                   │
│  ────────────────────────────────────────────────────────  │
│  Outer loop: rows, Inner loop: columns                    │
├─────────────────────────────────────────────────────────────┤
│                    WITH CONDITIONS                          │
├─────────────────────────────────────────────────────────────┤
│  [num for row in matrix for num in row if condition]      │
│  [expr if condition else expr for row...]                 │
├─────────────────────────────────────────────────────────────┤
│                    CREATING MATRICES                        │
├─────────────────────────────────────────────────────────────┤
│  [[expr for j in range(cols)] for i in range(rows)]      │
│  [[i * j for j in range(5)] for i in range(5)]           │
├─────────────────────────────────────────────────────────────┤
│                    KEY POINTS                               │
├─────────────────────────────────────────────────────────────┤
│  ✅ Order of loops: outer loop first, inner loop second    │
│  ✅ Flattening: 2D → 1D (row-major order)                 │
│  ✅ Add conditions after inner loop                       │
│  ✅ Use for transforming data structures                  │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Dictionary & Set Comprehensions
""")