"""
INTERMEDIATE ITERATOR PROBLEMS
NeuralAICodeCraft - Test Your Skills
"""

print("=" * 60)
print("INTERMEDIATE PROBLEMS (⭐⭐)")
print("=" * 60)

print("\n" + "=" * 40)
print("PROBLEM 4: Two Independent Iterators")
print("=" * 40)
"""
PROBLEM:
Create a list [1, 2, 3, 4, 5].
Create TWO separate iterators from the same list.
Use next() on both and show they are independent.

Your code here:
"""

# SOLUTION 4
print("\n--- SOLUTION 4 ---")
data = [1, 2, 3, 4, 5]
iter1 = iter(data)
iter2 = iter(data)

print(f"iter1: {next(iter1)}")  # 1
print(f"iter2: {next(iter2)}")  # 1 (still at beginning!)
print(f"iter1: {next(iter1)}")  # 2
print(f"iter2: {next(iter2)}")  # 2
print(f"iter1: {next(iter1)}")  # 3
print(f"Iterators are INDEPENDENT!")

print("\n" + "=" * 40)
print("PROBLEM 5: Detect Exhaustion")
print("=" * 40)
"""
PROBLEM:
Create an iterator from [100, 200].
Call next() three times. Handle the StopIteration exception gracefully.

Your code here:
"""

# SOLUTION 5
print("\n--- SOLUTION 5 ---")
numbers = [100, 200]
it = iter(numbers)

try:
    print(next(it))  # 100
    print(next(it))  # 200
    print(next(it))  # This will raise StopIteration
except StopIteration:
    print("✅ Caught StopIteration - Iterator exhausted!")

print("\n" + "=" * 40)
print("PROBLEM 6: Convert Iterator Back to List")
print("=" * 40)
"""
PROBLEM:
Create an iterator from [5, 10, 15, 20].
Convert it back to a list using list().

Your code here:
"""

# SOLUTION 6
print("\n--- SOLUTION 6 ---")
data = [5, 10, 15, 20]
iterator = iter(data)
converted_back = list(iterator)
print(f"Original list: {data}")
print(f"Converted back: {converted_back}")

print("\n" + "=" * 40)
print("PROBLEM 7: Skip First N Elements")
print("=" * 40)
"""
PROBLEM:
Create an iterator from [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
Use next() to skip the first 5 elements.
Then iterate through the remaining elements.

Your code here:
"""

# SOLUTION 7
print("\n--- SOLUTION 7 ---")
all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
it = iter(all_numbers)

# Skip first 5
for _ in range(5):
    next(it)

# Print remaining
print("Remaining elements after skipping first 5:")
for num in it:
    print(f"  → {num}")

print("\n✅ Intermediate problems complete! Move to advanced.")