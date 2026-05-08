"""
BEGINNER ITERATOR PROBLEMS
NeuralAICodeCraft - Test Your Skills

Instructions: Try to solve each problem before running the code.
Solutions are at the bottom of each section.
"""

print("=" * 60)
print("BEGINNER PROBLEMS (⭐)")
print("=" * 60)

print("\n" + "=" * 40)
print("PROBLEM 1: Create and Access")
print("=" * 40)
"""
PROBLEM: 
Create a list [10, 20, 30, 40, 50]. Convert it to an iterator.
Use next() to get the first 3 elements.

Your code here:
"""

# Write your solution here (uncomment and write)
# my_list = ...
# my_iterator = ...
# print(next(...))
# print(next(...))
# print(next(...))


# SOLUTION 1
print("\n--- SOLUTION 1 ---")
my_list = [10, 20, 30, 40, 50]
my_iterator = iter(my_list)
print(f"First: {next(my_iterator)}")   # 10
print(f"Second: {next(my_iterator)}")  # 20
print(f"Third: {next(my_iterator)}")   # 30

print("\n" + "=" * 40)
print("PROBLEM 2: String to Iterator")
print("=" * 40)
"""
PROBLEM:
Convert the string "Python" to an iterator.
Print each character using next().

Your code here:
"""

# SOLUTION 2
print("\n--- SOLUTION 2 ---")
string = "Python"
char_iterator = iter(string)
print(f"Char 1: {next(char_iterator)}")  # P
print(f"Char 2: {next(char_iterator)}")  # y
print(f"Char 3: {next(char_iterator)}")  # t
print(f"Char 4: {next(char_iterator)}")  # h
print(f"Char 5: {next(char_iterator)}")  # o
print(f"Char 6: {next(char_iterator)}")  # n

print("\n" + "=" * 40)
print("PROBLEM 3: For Loop vs Manual")
print("=" * 40)
"""
PROBLEM:
Create a tuple (1, 2, 3, 4). 
Show two ways to iterate:
1. Using a for loop
2. Using manual iter() and next()

Your code here:
"""

# SOLUTION 3
print("\n--- SOLUTION 3 ---")
my_tuple = (1, 2, 3, 4)

print("Method 1: For loop")
for item in my_tuple:
    print(f"  → {item}")

print("Method 2: Manual iteration")
manual_iter = iter(my_tuple)
while True:
    try:
        print(f"  → {next(manual_iter)}")
    except StopIteration:
        break

print("\n✅ Beginner problems complete! Move to intermediate.")