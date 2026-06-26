"""
PYTHON reverse() & sort() METHODS - COMPLETE GUIDE
NeuralAICodeCraft - Sorting and Reversing Lists

Topics Covered:
1. reverse() Method (In-place)
2. reversed() Function (Returns Iterator)
3. reverse() vs reversed()
4. sort() Method (In-place)
5. sort() Parameters (key, reverse)
6. sort() vs sorted()
7. Custom Sorting with key
"""

print("=" * 70)
print("🐍 PYTHON reverse() & sort() METHODS")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: reverse() METHOD
# ============================================

print("\n📚 PART 1: reverse() METHOD")
print("-" * 50)

print("""
SYNTAX: my_list.reverse()

WHAT IT DOES:
- Reverses the order of elements IN-PLACE
- Returns None (modifies original)
- Affects ALL references to the list
- Time Complexity: O(n)
""")

# 1.1 Basic Usage
print("\n1.1 Basic Usage:")
print("-" * 30)

fruits = ['apple', 'banana', 'cherry', 'date']
print(f"Original: {fruits}")
fruits.reverse()
print(f"After reverse(): {fruits}")

# 1.2 All References Affected
print("\n1.2 All References Are Affected:")
print("-" * 30)

original = [1, 2, 3, 4, 5]
reference = original

print(f"Original: {original}")
print(f"Reference: {reference}")

original.reverse()

print(f"\nAfter original.reverse():")
print(f"Original: {original}")    # Reversed!
print(f"Reference: {reference}")  # Also reversed!

print("\n✅ reverse() modifies the list IN-PLACE!")

# 1.3 Reverse Different Data Types
print("\n1.3 Reversing Different Data Types:")
print("-" * 30)

# Numbers
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(f"Numbers reversed: {numbers}")

# Strings
words = ['a', 'b', 'c', 'd']
words.reverse()
print(f"Strings reversed: {words}")

# Mixed types
mixed = [1, 'apple', 3.14, True]
mixed.reverse()
print(f"Mixed list reversed: {mixed}")

# ============================================
# PART 2: reversed() FUNCTION
# ============================================

print("\n🔄 PART 2: reversed() FUNCTION")
print("-" * 50)

print("""
SYNTAX: reversed(my_list)

WHAT IT DOES:
- Returns a REVERSE ITERATOR (lazy)
- Does NOT modify the original list
- Can be converted to list with list()
- Can be used in loops
""")

# 2.1 Basic Usage
print("\n2.1 Basic Usage:")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
reverse_iter = reversed(numbers)

print(f"Original list: {numbers}")
print(f"reversed() object: {reverse_iter}")
print(f"Type: {type(reverse_iter)}")

# Convert to list
reversed_list = list(reverse_iter)
print(f"Convert to list: {reversed_list}")
print(f"Original still intact: {numbers}")  # Unchanged!

# 2.2 Iterating with reversed()
print("\n2.2 Iterating with reversed():")
print("-" * 30)

colors = ['red', 'green', 'blue', 'yellow']
print("Iterating in reverse:")
for color in reversed(colors):
    print(f"  {color}")

print(f"\nOriginal list: {colors}")  # Unchanged!

# 2.3 reversed() with Different Types
print("\n2.3 reversed() with Different Types:")
print("-" * 30)

# With tuple
my_tuple = (1, 2, 3)
print(f"Tuple: {my_tuple}")
print(f"Reversed tuple: {list(reversed(my_tuple))}")

# With string
my_str = "Python"
print(f"String: {my_str}")
print(f"Reversed string: {''.join(reversed(my_str))}")

# With range
for i in reversed(range(5)):
    print(f"  {i}")

# ============================================
# PART 3: reverse() vs reversed()
# ============================================

print("\n⚖️ PART 3: reverse() vs reversed()")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  reverse()          │  reversed()          │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Type           │  Method             │  Built-in Function   │
│  Modifies       │  IN-PLACE           │  NO (new iterator)   │
│  Returns        │  None               │  Iterator object     │
│  Use with       │  Lists only         │  Any sequence        │
│  Memory         │  In-place           │  Lazy (iterator)     │
│  Original       │  Changed            │  Unchanged           │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 3.1 Demonstration
print("\n3.1 Demonstration:")
print("-" * 30)

data = [1, 2, 3, 4, 5]
print(f"Original: {data}")

# reverse() - modifies original
data_copy = data.copy()
data_copy.reverse()
print(f"reverse(): {data_copy}")

# reversed() - returns iterator
rev_iter = reversed(data)
print(f"reversed(): {list(rev_iter)}")
print(f"Original after reversed(): {data}")  # Unchanged!

# ============================================
# PART 4: sort() METHOD
# ============================================

print("\n📊 PART 4: sort() METHOD")
print("-" * 50)

print("""
SYNTAX: my_list.sort(key=None, reverse=False)

WHAT IT DOES:
- Sorts the list IN-PLACE (ascending by default)
- Returns None (modifies original)
- Stable sort (preserves relative order of equal elements)
- Time Complexity: O(n log n)
""")

# 4.1 Basic Sorting
print("\n4.1 Basic Sorting (Ascending):")
print("-" * 30)

numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")
numbers.sort()
print(f"After sort(): {numbers}")

# 4.2 Sorting Descending
print("\n4.2 Sorting Descending:")
print("-" * 30)

numbers = [5, 2, 8, 1, 9, 3]
numbers.sort(reverse=True)
print(f"sort(reverse=True): {numbers}")

# 4.3 Sorting Strings
print("\n4.3 Sorting Strings:")
print("-" * 30)

fruits = ['banana', 'apple', 'cherry', 'date', 'elderberry']
print(f"Original: {fruits}")
fruits.sort()
print(f"Alphabetical: {fruits}")
fruits.sort(reverse=True)
print(f"Reverse alphabetical: {fruits}")

# 4.4 All References Affected
print("\n4.4 All References Are Affected:")
print("-" * 30)

original = [3, 1, 4, 1, 5, 9]
reference = original

print(f"Original: {original}")
print(f"Reference: {reference}")

original.sort()

print(f"\nAfter original.sort():")
print(f"Original: {original}")    # Sorted!
print(f"Reference: {reference}")  # Also sorted!

# ============================================
# PART 5: sort() vs sorted()
# ============================================

print("\n⚖️ PART 5: sort() vs sorted()")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  sort()             │  sorted()            │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Type           │  Method             │  Built-in Function   │
│  Modifies       │  IN-PLACE           │  NO (creates new)    │
│  Returns        │  None               │  New sorted list     │
│  Works with     │  Lists only         │  Any iterable        │
│  Memory         │  In-place           │  Creates new list    │
│  Original       │  Changed            │  Unchanged           │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 5.1 Demonstration
print("\n5.1 Demonstration:")
print("-" * 30)

data = [5, 2, 8, 1, 9]
print(f"Original: {data}")

# sort() - modifies original
data_copy = data.copy()
data_copy.sort()
print(f"sort(): {data_copy}")

# sorted() - returns new list
new_sorted = sorted(data)
print(f"sorted(): {new_sorted}")
print(f"Original after sorted(): {data}")  # Unchanged!

# 5.2 sorted() with Different Types
print("\n5.2 sorted() with Different Types:")
print("-" * 30)

# With tuple
my_tuple = (3, 1, 4, 1, 5)
print(f"Sorted tuple: {sorted(my_tuple)}")

# With string
my_str = "python"
print(f"Sorted string: {sorted(my_str)}")

# With dictionary
my_dict = {'c': 3, 'a': 1, 'b': 2}
print(f"Sorted dict keys: {sorted(my_dict)}")

# ============================================
# PART 6: CUSTOM SORTING WITH key
# ============================================

print("\n🎯 PART 6: CUSTOM SORTING WITH 'key' PARAMETER")
print("-" * 50)

print("""
The 'key' parameter allows custom sorting logic.
- key = function that returns the value to sort by
- key = lambda function for simple custom sorting
- key = existing function like len, str.lower
""")

# 6.1 Sorting by Length
print("\n6.1 Sorting by Length:")
print("-" * 30)

words = ['python', 'java', 'c', 'javascript', 'rust', 'go']
print(f"Original: {words}")

# Sort by length (shortest to longest)
words.sort(key=len)
print(f"Sort by length: {words}")

# Sort by length (longest to shortest)
words.sort(key=len, reverse=True)
print(f"Sort by length (descending): {words}")

# 6.2 Sorting by Last Character
print("\n6.2 Sorting by Last Character:")
print("-" * 30)

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
words.sort(key=lambda x: x[-1])
print(f"Sort by last character: {words}")

# 6.3 Sorting with Tuples
print("\n6.3 Sorting List of Tuples:")
print("-" * 30)

students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 78),
    ('David', 95),
    ('Eve', 88)
]

print(f"Original: {students}")

# Sort by score (second element)
students.sort(key=lambda x: x[1])
print(f"Sort by score: {students}")

# Sort by score (highest first)
students.sort(key=lambda x: x[1], reverse=True)
print(f"Sort by score (descending): {students}")

# Sort by name (first element)
students.sort(key=lambda x: x[0])
print(f"Sort by name: {students}")

# 6.4 Sorting Dictionaries
print("\n6.4 Sorting List of Dictionaries:")
print("-" * 30)

people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

print(f"Original: {people}")

# Sort by age
people.sort(key=lambda x: x['age'])
print(f"Sort by age: {people}")

# Sort by name
people.sort(key=lambda x: x['name'])
print(f"Sort by name: {people}")

# 6.5 Case-Insensitive Sorting
print("\n6.5 Case-Insensitive Sorting:")
print("-" * 30)

names = ['Alice', 'bob', 'Charlie', 'dave', 'Eve']
print(f"Original: {names}")

# Normal sort (case-sensitive) - uppercase before lowercase
names.sort()
print(f"Normal sort: {names}")

# Case-insensitive sort
names.sort(key=str.lower)
print(f"Case-insensitive sort: {names}")

# 6.6 Multiple Criteria Sorting
print("\n6.6 Multiple Criteria Sorting:")
print("-" * 30)

data = [
    (3, 'b'),
    (1, 'a'),
    (3, 'a'),
    (2, 'b'),
    (1, 'b'),
]

print(f"Original: {data}")

# Sort by first element, then second
data.sort(key=lambda x: (x[0], x[1]))
print(f"Sort by (first, second): {data}")

# ============================================
# PART 7: SORTING WITH OPERATOR MODULE
# ============================================

print("\n🔧 PART 7: SORTING WITH operator MODULE")
print("-" * 50)

from operator import itemgetter, attrgetter

print("""
operator.itemgetter() provides faster key functions for sorting.
- itemgetter(n) → get nth item from tuple/list
- attrgetter(name) → get attribute from object
""")

# 7.1 Using itemgetter
print("\n7.1 Using itemgetter:")
print("-" * 30)

students = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 78),
    ('David', 95),
]

print(f"Original: {students}")

# Sort by score using itemgetter
students.sort(key=itemgetter(1))
print(f"Sort by score: {students}")

# Sort by name using itemgetter
students.sort(key=itemgetter(0))
print(f"Sort by name: {students}")

# 7.2 Multiple itemgetter
print("\n7.2 Multiple itemgetter:")
print("-" * 30)

data = [
    (3, 'b'),
    (1, 'a'),
    (3, 'a'),
    (2, 'b'),
]

data.sort(key=itemgetter(0, 1))
print(f"Sort by (first, second): {data}")

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Reverse Practice
Reverse [10, 20, 30, 40, 50] using reverse()

🎯 EXERCISE 2: Sort Ascending
Sort [5, 2, 8, 1, 9] in ascending order

🎯 EXERCISE 3: Sort Descending
Sort [5, 2, 8, 1, 9] in descending order

🎯 EXERCISE 4: Sort Strings by Length
Sort ['python', 'java', 'c', 'javascript'] by length

🎯 EXERCISE 5: Sort Tuples
Sort [(1, 'b'), (2, 'a'), (1, 'a')] by both values

🎯 CHALLENGE: Custom Sorting
Sort a list of employee dictionaries by salary, then by name
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - reverse():")
lst1 = [10, 20, 30, 40, 50]
lst1.reverse()
print(f"  {lst1}")

# Exercise 2
print("\nEx2 - sort ascending:")
lst2 = [5, 2, 8, 1, 9]
lst2.sort()
print(f"  {lst2}")

# Exercise 3
print("\nEx3 - sort descending:")
lst3 = [5, 2, 8, 1, 9]
lst3.sort(reverse=True)
print(f"  {lst3}")

# Exercise 4
print("\nEx4 - sort by length:")
words = ['python', 'java', 'c', 'javascript']
words.sort(key=len)
print(f"  {words}")

# Exercise 5
print("\nEx5 - sort tuples:")
tuples = [(1, 'b'), (2, 'a'), (1, 'a')]
tuples.sort(key=lambda x: (x[0], x[1]))
print(f"  {tuples}")

# Challenge
print("\nChallenge - Sort employees:")
employees = [
    {'name': 'Alice', 'salary': 50000},
    {'name': 'Bob', 'salary': 60000},
    {'name': 'Charlie', 'salary': 45000},
    {'name': 'David', 'salary': 60000}
]

employees.sort(key=lambda x: (x['salary'], x['name']))
print("  Sort by salary, then name:")
for emp in employees:
    print(f"    {emp}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ REVERSE & SORT METHODS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    REVERSING LISTS                          │
├─────────────────────────────────────────────────────────────┤
│  list.reverse()    → In-place reverse (modifies list)      │
│  reversed(list)    → Returns reverse iterator (lazy)       │
│  list[::-1]        → Returns reversed copy                │
├─────────────────────────────────────────────────────────────┤
│                    SORTING LISTS                            │
├─────────────────────────────────────────────────────────────┤
│  list.sort()       → In-place sort (ascending)            │
│  list.sort(reverse=True) → In-place sort (descending)     │
│  sorted(list)      → Returns new sorted list              │
│  sorted(list, reverse=True) → New list (descending)       │
├─────────────────────────────────────────────────────────────┤
│                    CUSTOM SORTING                           │
├─────────────────────────────────────────────────────────────┤
│  list.sort(key=len)                    → Sort by length    │
│  list.sort(key=lambda x: x[1])         → Sort by second    │
│  list.sort(key=itemgetter(1))          → Faster key        │
│  list.sort(key=lambda x: (x[0], x[1])) → Multiple keys    │
├─────────────────────────────────────────────────────────────┤
│                    WHEN TO USE WHAT                         │
├─────────────────────────────────────────────────────────────┤
│  Use reverse() when:                                        │
│  ├── Need to modify the original list                      │
│  ├── Memory efficiency matters                             │
│  └── Only working with lists                               │
│                                                             │
│  Use reversed() when:                                       │
│  ├── Original list should stay intact                      │
│  ├── Working with other sequences (tuples, strings)        │
│  └── Need lazy iteration                                   │
│                                                             │
│  Use sort() when:                                           │
│  ├── Need to modify the original list                      │
│  └── Memory efficiency matters                             │
│                                                             │
│  Use sorted() when:                                         │
│  ├── Original list should stay intact                      │
│  ├── Working with other iterables (tuples, dicts)          │
│  └── Need to preserve original                             │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: List Comprehensions - Python's Most Powerful Feature
""")