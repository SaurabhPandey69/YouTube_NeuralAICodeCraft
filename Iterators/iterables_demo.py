"""
Iterables vs Iterators Demo
NeuralAICodeCraft - Understanding Python Iteration
"""

print("=" * 60)
print("PART 1: WHAT ARE ITERABLES?")
print("=" * 60)

# Common iterables in Python
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
my_string = "Python"
my_dict = {"a": 1, "b": 2, "c": 3}

print(f"List is iterable? {hasattr(my_list, '__iter__')}")  # True
print(f"Tuple is iterable? {hasattr(my_tuple, '__iter__')}")  # True
print(f"String is iterable? {hasattr(my_string, '__iter__')}")  # True
print(f"Dict is iterable? {hasattr(my_dict, '__iter__')}")  # True

# All iterables have __iter__ method
print(f"\nList __iter__ method: {my_list.__iter__}")

print("\n" + "=" * 60)
print("PART 2: THE iter() FUNCTION")
print("=" * 60)

# Convert iterable to iterator
my_list = [1, 2, 3, 4, 5]
iterator = iter(my_list)  # Same as my_list.__iter__()

print(f"Type of iterator: {type(iterator)}")
print(f"Is iterator iterable? {hasattr(iterator, '__iter__')}")  # True
print(f"Does iterator have __next__? {hasattr(iterator, '__next__')}")  # True

print("\n" + "=" * 60)
print("PART 3: THE next() FUNCTION")
print("=" * 60)

my_list = [10, 20, 30, 40, 50]
iterator = iter(my_list)

print("Using next() to get elements one by one:")
print(f"First element: {next(iterator)}")   # 10
print(f"Second element: {next(iterator)}")  # 20
print(f"Third element: {next(iterator)}")   # 30
print(f"Fourth element: {next(iterator)}")  # 40
print(f"Fifth element: {next(iterator)}")   # 50

print("\n" + "=" * 60)
print("PART 4: StopIteration EXCEPTION")
print("=" * 60)

my_list = [1, 2]
iterator = iter(my_list)
print(next(iterator))  # 1
print(next(iterator))  # 2

try:
    print(next(iterator))  # No more elements!
except StopIteration:
    print("⚠️ StopIteration: Iterator has no more elements!")

print("\n" + "=" * 60)
print("PART 5: THE for LOOP REVEALED")
print("=" * 60)

# This is what Python does behind the scenes:
my_list = [100, 200, 300]

print("For loop internally does:")

# 1. Get iterator from iterable
iterator = iter(my_list)

# 2. Keep calling next() until StopIteration
while True:
    try:
        element = next(iterator)
        print(f"  → {element}")
    except StopIteration:
        print("  → Loop finished!")
        break