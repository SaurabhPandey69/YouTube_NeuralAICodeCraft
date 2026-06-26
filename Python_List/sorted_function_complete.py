"""
PYTHON sorted() FUNCTION - COMPLETE GUIDE
NeuralAICodeCraft - Master Custom Sorting with key & reverse

Topics Covered:
1. sorted() Basics
2. sorted() vs sort()
3. reverse Parameter
4. key Parameter
5. Sorting with Lambda
6. Sorting Tuples & Lists
7. Sorting Dictionaries
8. Multiple Criteria Sorting
"""

from operator import itemgetter, attrgetter

print("=" * 70)
print("🐍 PYTHON sorted() FUNCTION - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: sorted() BASICS
# ============================================

print("\n📚 PART 1: sorted() BASICS")
print("-" * 50)

print("""
SYNTAX: sorted(iterable, key=None, reverse=False)

WHAT IT DOES:
- Returns a NEW sorted list
- Does NOT modify the original
- Works with ANY iterable (list, tuple, dict, string, set)
- Default: ascending order (smallest to largest)
- Returns a list (always)
""")

# 1.1 Sorting Lists
print("\n1.1 Sorting Lists:")
print("-" * 30)

numbers = [5, 2, 8, 1, 9, 3]
sorted_numbers = sorted(numbers)

print(f"Original: {numbers}")
print(f"sorted(): {sorted_numbers}")
print(f"Original unchanged: {numbers}")  # Still [5, 2, 8, 1, 9, 3]

# 1.2 Sorting Tuples
print("\n1.2 Sorting Tuples:")
print("-" * 30)

tuple_data = (5, 2, 8, 1, 9)
sorted_tuple = sorted(tuple_data)
print(f"Original tuple: {tuple_data}")
print(f"sorted(tuple): {sorted_tuple}")
print(f"Returns a list: {type(sorted_tuple)}")

# 1.3 Sorting Strings
print("\n1.3 Sorting Strings:")
print("-" * 30)

string_data = "python"
sorted_string = sorted(string_data)
print(f"Original string: {string_data}")
print(f"sorted(string): {sorted_string}")
print(f"Back to string: {''.join(sorted_string)}")

# 1.4 Sorting Sets
print("\n1.4 Sorting Sets:")
print("-" * 30)

set_data = {5, 2, 8, 1, 9}
sorted_set = sorted(set_data)
print(f"Original set: {set_data}")
print(f"sorted(set): {sorted_set}")

# 1.5 Sorting Dictionary Keys
print("\n1.5 Sorting Dictionary Keys:")
print("-" * 30)

dict_data = {'b': 3, 'a': 1, 'c': 2}
sorted_keys = sorted(dict_data)
print(f"Original dict: {dict_data}")
print(f"sorted(dict): {sorted_keys}")
print(f"Sorted keys: {sorted_keys}")

# ============================================
# PART 2: sorted() vs sort()
# ============================================

print("\n⚖️ PART 2: sorted() vs sort()")
print("-" * 50)

print("""
┌─────────────────┬─────────────────────┬──────────────────────┐
│  FEATURE        │  sorted()           │  sort()              │
├─────────────────┼─────────────────────┼──────────────────────┤
│  Type           │  Built-in Function  │  List Method         │
│  Modifies       │  NO (new list)      │  YES (in-place)      │
│  Returns        │  New sorted list    │  None                │
│  Works with     │  ANY iterable       │  Lists only          │
│  Original       │  Unchanged          │  Changed             │
│  Use case       │  Preserve original  │  Modify original     │
└─────────────────┴─────────────────────┴──────────────────────┘
""")

# 2.1 Demonstration
print("\n2.1 sorted() vs sort() Demonstration:")
print("-" * 30)

data = [3, 1, 4, 1, 5]

# Using sorted() - original unchanged
new_list = sorted(data)
print(f"Original: {data}")
print(f"sorted(): {new_list}")
print(f"Original after sorted(): {data}")  # Unchanged

# Using sort() - original changed
data.sort()
print(f"\nAfter sort(): {data}")  # Changed

print("\n💡 TIP: Use sorted() when you need to keep the original intact.")
print("  Use sort() when you want to modify the list in-place.")

# ============================================
# PART 3: reverse PARAMETER
# ============================================

print("\n🔄 PART 3: reverse PARAMETER")
print("-" * 50)

print("""
reverse=False → Ascending (default, smallest to largest)
reverse=True  → Descending (largest to smallest)
""")

# 3.1 Ascending vs Descending
print("\n3.1 Ascending vs Descending:")
print("-" * 30)

numbers = [5, 2, 8, 1, 9, 3]

ascending = sorted(numbers, reverse=False)
descending = sorted(numbers, reverse=True)

print(f"Original: {numbers}")
print(f"Ascending (reverse=False): {ascending}")
print(f"Descending (reverse=True): {descending}")

# 3.2 Strings Descending
print("\n3.2 Strings Descending:")
print("-" * 30)

fruits = ['banana', 'apple', 'cherry', 'date']
ascending = sorted(fruits)
descending = sorted(fruits, reverse=True)

print(f"Original: {fruits}")
print(f"Ascending: {ascending}")
print(f"Descending: {descending}")

# ============================================
# PART 4: key PARAMETER
# ============================================

print("\n🎯 PART 4: key PARAMETER")
print("-" * 50)

print("""
key = function that returns the value to sort by
- Called once per element
- Returns a "sort key"
- Does NOT modify the elements themselves
""")

# 4.1 Sorting by Length
print("\n4.1 Sorting by Length (key=len):")
print("-" * 30)

words = ['python', 'java', 'c', 'javascript', 'rust', 'go']
print(f"Original: {words}")

sorted_by_length = sorted(words, key=len)
print(f"Sort by length: {sorted_by_length}")

# 4.2 Sorting by Last Character
print("\n4.2 Sorting by Last Character (key=lambda x: x[-1]):")
print("-" * 30)

words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(f"Original: {words}")

sorted_by_last = sorted(words, key=lambda x: x[-1])
print(f"Sort by last char: {sorted_by_last}")

# Show the last characters
print("  Last characters:")
for word in sorted_by_last:
    print(f"    {word} → '{word[-1]}'")

# 4.3 Sorting by Second Character
print("\n4.3 Sorting by Second Character (key=lambda x: x[1]):")
print("-" * 30)

words = ['apple', 'banana', 'cherry', 'date']
sorted_by_second = sorted(words, key=lambda x: x[1])
print(f"Original: {words}")
print(f"Sort by second char: {sorted_by_second}")

# 4.4 Sorting by Sum of ASCII Values
print("\n4.4 Sorting by Sum of ASCII Values (key=lambda x: sum(ord(c) for c in x)):")
print("-" * 30)

words = ['cat', 'dog', 'elephant', 'bat', 'ant']

def ascii_sum(word):
    return sum(ord(c) for c in word)

print("  ASCII sums:")
for word in words:
    print(f"    '{word}': {ascii_sum(word)}")

sorted_by_sum = sorted(words, key=ascii_sum)
print(f"\nSort by ASCII sum: {sorted_by_sum}")

# ============================================
# PART 5: SORTING WITH LAMBDA FUNCTIONS
# ============================================

print("\n🔧 PART 5: SORTING WITH LAMBDA FUNCTIONS")
print("-" * 50)

print("""
Lambda functions provide inline, anonymous functions for sorting:
- lambda x: x[0]  → Sort by first element
- lambda x: x[1]  → Sort by second element
- lambda x: len(x)  → Sort by length
""")

# 5.1 Sorting List of Tuples
print("\n5.1 Sorting List of Tuples:")
print("-" * 30)

students = [
    ('Alice', 85, 'A'),
    ('Bob', 92, 'B'),
    ('Charlie', 78, 'C'),
    ('David', 95, 'A'),
    ('Eve', 88, 'B')
]

print(f"Original: {students}")

# Sort by name (first element)
by_name = sorted(students, key=lambda x: x[0])
print(f"Sort by name: {by_name}")

# Sort by score (second element)
by_score = sorted(students, key=lambda x: x[1])
print(f"Sort by score: {by_score}")

# Sort by score descending
by_score_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sort by score (descending): {by_score_desc}")

# 5.2 Sorting List of Dictionaries
print("\n5.2 Sorting List of Dictionaries:")
print("-" * 30)

employees = [
    {'name': 'Alice', 'salary': 50000, 'age': 30},
    {'name': 'Bob', 'salary': 60000, 'age': 25},
    {'name': 'Charlie', 'salary': 45000, 'age': 35},
    {'name': 'David', 'salary': 60000, 'age': 28}
]

print(f"Original: {employees}")

# Sort by salary
by_salary = sorted(employees, key=lambda x: x['salary'])
print(f"Sort by salary: {by_salary}")

# Sort by salary (descending)
by_salary_desc = sorted(employees, key=lambda x: x['salary'], reverse=True)
print(f"Sort by salary (descending): {by_salary_desc}")

# Sort by age
by_age = sorted(employees, key=lambda x: x['age'])
print(f"Sort by age: {by_age}")

# 5.3 Sorting with Custom Objects
print("\n5.3 Sorting Custom Objects:")
print("-" * 30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

people = [
    Person('Alice', 30),
    Person('Bob', 25),
    Person('Charlie', 35),
    Person('David', 28)
]

print(f"Original: {people}")

# Sort by age (attribute)
by_age = sorted(people, key=lambda p: p.age)
print(f"Sort by age: {by_age}")

# Sort by name (attribute)
by_name = sorted(people, key=lambda p: p.name)
print(f"Sort by name: {by_name}")

# ============================================
# PART 6: SORTING DICTIONARIES
# ============================================

print("\n📖 PART 6: SORTING DICTIONARIES")
print("-" * 50)

# 6.1 Sorting Dictionary by Keys
print("\n6.1 Sorting Dictionary by Keys:")
print("-" * 30)

scores = {'Charlie': 78, 'Alice': 85, 'Bob': 92, 'David': 95}
print(f"Original: {scores}")

# Sort keys
sorted_keys = sorted(scores.keys())
print(f"Sorted keys: {sorted_keys}")

# Create sorted dictionary (Python 3.7+ maintains order)
sorted_by_key = {k: scores[k] for k in sorted(scores)}
print(f"Sorted by key: {sorted_by_key}")

# 6.2 Sorting Dictionary by Values
print("\n6.2 Sorting Dictionary by Values:")
print("-" * 30)

scores = {'Charlie': 78, 'Alice': 85, 'Bob': 92, 'David': 95}

# Sort items by value
sorted_by_value = dict(sorted(scores.items(), key=lambda x: x[1]))
print(f"Sorted by value: {sorted_by_value}")

# Sort by value descending
sorted_by_value_desc = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(f"Sorted by value (descending): {sorted_by_value_desc}")

# ============================================
# PART 7: OPERATOR MODULE FOR SORTING
# ============================================

print("\n⚡ PART 7: OPERATOR MODULE FOR SORTING")
print("-" * 50)

print("""
operator module provides faster key functions:
- itemgetter(n) → Get nth item from sequence
- attrgetter(name) → Get attribute from object
""")

# 7.1 Using itemgetter
print("\n7.1 Using itemgetter():")
print("-" * 30)

from operator import itemgetter

students = [
    ('Alice', 85, 'A'),
    ('Bob', 92, 'B'),
    ('Charlie', 78, 'C'),
]

print(f"Original: {students}")

# Sort by name (index 0)
by_name = sorted(students, key=itemgetter(0))
print(f"Sort by name (itemgetter): {by_name}")

# Sort by score (index 1)
by_score = sorted(students, key=itemgetter(1))
print(f"Sort by score (itemgetter): {by_score}")

# 7.2 Multiple itemgetter
print("\n7.2 Multiple Criteria with itemgetter:")
print("-" * 30)

data = [
    (3, 'b'),
    (1, 'a'),
    (3, 'a'),
    (2, 'b'),
    (1, 'b'),
]

print(f"Original: {data}")

# Sort by first, then second
sorted_data = sorted(data, key=itemgetter(0, 1))
print(f"Sort by (first, second): {sorted_data}")

# ============================================
# PART 8: MULTIPLE CRITERIA SORTING
# ============================================

print("\n🎯 PART 8: MULTIPLE CRITERIA SORTING")
print("-" * 50)

# 8.1 Using Tuple as Key
print("\n8.1 Multiple Criteria with Tuple Key:")
print("-" * 30)

students = [
    ('Alice', 'A', 85),
    ('Bob', 'B', 92),
    ('Charlie', 'A', 78),
    ('David', 'B', 95),
]

print(f"Original: {students}")

# Sort by grade, then by score
sorted_students = sorted(students, key=lambda x: (x[1], x[2]))
print(f"Sort by grade, then score: {sorted_students}")

# Sort by grade (ascending), score (descending)
sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))
print(f"Sort by grade (asc), score (desc): {sorted_students}")

# 8.2 Complex Multiple Criteria
print("\n8.2 Complex Multiple Criteria:")
print("-" * 30)

employees = [
    {'name': 'Alice', 'department': 'IT', 'salary': 50000},
    {'name': 'Bob', 'department': 'HR', 'salary': 60000},
    {'name': 'Charlie', 'department': 'IT', 'salary': 45000},
    {'name': 'David', 'department': 'HR', 'salary': 55000},
]

print(f"Original: {employees}")

# Sort by department, then by salary (descending)
sorted_employees = sorted(employees, key=lambda x: (x['department'], -x['salary']))
print(f"Sort by department, salary (desc):")
for emp in sorted_employees:
    print(f"  {emp}")

# ============================================
# PART 9: ADVANCED SORTING TECHNIQUES
# ============================================

print("\n🚀 PART 9: ADVANCED SORTING TECHNIQUES")
print("-" * 50)

# 9.1 Case-Insensitive Sorting
print("\n9.1 Case-Insensitive Sorting:")
print("-" * 30)

words = ['banana', 'Apple', 'cherry', 'Date', 'apple', 'Banana']
print(f"Original: {words}")

# Default (case-sensitive)
default_sorted = sorted(words)
print(f"Default: {default_sorted}")

# Case-insensitive
insensitive_sorted = sorted(words, key=str.lower)
print(f"Case-insensitive: {insensitive_sorted}")

# 9.2 Sorting with str.casefold (Unicode)
print("\n9.2 Sorting with str.casefold (Unicode):")
print("-" * 30)

unicode_words = ['café', 'Café', 'apple', 'Apple']
print(f"Original: {unicode_words}")

# Case-insensitive Unicode
unicode_sorted = sorted(unicode_words, key=str.casefold)
print(f"With str.casefold: {unicode_sorted}")

# 9.3 Stable Sort
print("\n9.3 Stable Sort (Preserves Original Order for Equal Items):")
print("-" * 30)

data = [
    ('Alice', 85),
    ('Bob', 92),
    ('Charlie', 85),
    ('David', 88),
]

print(f"Original: {data}")

# Sort by score (equal scores preserve original order)
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Sort by score: {sorted_data}")
print("  Note: Alice and Charlie both have 85, order preserved!")

# 9.4 Sorting with Custom Class
print("\n9.4 Sorting Custom Class with attrgetter:")
print("-" * 30)

from operator import attrgetter

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})"

employees = [
    Employee('Alice', 50000),
    Employee('Bob', 60000),
    Employee('Charlie', 45000),
]

# Sort by salary
by_salary = sorted(employees, key=attrgetter('salary'))
print(f"Sort by salary: {by_salary}")

# Sort by name
by_name = sorted(employees, key=attrgetter('name'))
print(f"Sort by name: {by_name}")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Basic Sort
Sort [3, 1, 4, 1, 5, 9, 2] using sorted()

🎯 EXERCISE 2: Descending Sort
Sort the same list in descending order.

🎯 EXERCISE 3: Sort by Length
Sort ['python', 'java', 'c', 'javascript'] by length.

🎯 EXERCISE 4: Sort Tuples
Sort [(1, 'b'), (2, 'a'), (1, 'a')] by both values.

🎯 EXERCISE 5: Sort Dictionary
Sort {'a': 5, 'b': 2, 'c': 8} by values.

🎯 EXERCISE 6: Multiple Criteria
Sort employees by department, then salary.

🎯 CHALLENGE: Custom Sort Order
Sort letters with vowels first, then consonants.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Basic Sort:")
nums = [3, 1, 4, 1, 5, 9, 2]
print(f"  sorted(nums): {sorted(nums)}")

# Exercise 2
print("\nEx2 - Descending:")
print(f"  sorted(nums, reverse=True): {sorted(nums, reverse=True)}")

# Exercise 3
print("\nEx3 - Sort by Length:")
words = ['python', 'java', 'c', 'javascript']
print(f"  sorted(words, key=len): {sorted(words, key=len)}")

# Exercise 4
print("\nEx4 - Sort Tuples:")
tuples = [(1, 'b'), (2, 'a'), (1, 'a')]
print(f"  sorted(tuples): {sorted(tuples, key=lambda x: (x[0], x[1]))}")

# Exercise 5
print("\nEx5 - Sort Dictionary:")
d = {'a': 5, 'b': 2, 'c': 8}
print(f"  sorted by value: {dict(sorted(d.items(), key=lambda x: x[1]))}")

# Exercise 6
print("\nEx6 - Multiple Criteria:")
employees = [
    {'name': 'Alice', 'dept': 'IT', 'salary': 50000},
    {'name': 'Bob', 'dept': 'HR', 'salary': 60000},
    {'name': 'Charlie', 'dept': 'IT', 'salary': 45000},
]
sorted_emps = sorted(employees, key=lambda x: (x['dept'], -x['salary']))
print(f"  Sorted: {sorted_emps}")

# Challenge
print("\nChallenge - Vowels First:")
def vowel_first(char):
    vowels = 'aeiouAEIOU'
    return (0 if char in vowels else 1, char)

letters = ['c', 'a', 'e', 'b', 'i', 'd', 'o']
print(f"  Original: {letters}")
print(f"  Vowels first: {sorted(letters, key=vowel_first)}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ sorted() FUNCTION MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    sorted() SYNTAX                          │
├─────────────────────────────────────────────────────────────┤
│  sorted(iterable)                 → Ascending               │
│  sorted(iterable, reverse=True)   → Descending              │
│  sorted(iterable, key=len)        → Sort by length          │
│  sorted(iterable, key=lambda x: x[1]) → Sort by second      │
│  sorted(iterable, key=lambda x: (x[0], -x[1])) → Multiple   │
├─────────────────────────────────────────────────────────────┤
│                    KEY FUNCTIONS                            │
├─────────────────────────────────────────────────────────────┤
│  len                  → Sort by length                     │
│  str.lower            → Case-insensitive                   │
│  str.casefold         → Unicode case-insensitive           │
│  itemgetter(n)        → Get nth item (faster)              │
│  attrgetter(name)     → Get attribute (faster)             │
├─────────────────────────────────────────────────────────────┤
│                    sorted() vs sort()                       │
├─────────────────────────────────────────────────────────────┤
│  sorted()    → NEW list, original intact, ANY iterable     │
│  sort()      → In-place, original changed, LISTS only      │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Python List Comprehensions - The Ultimate Guide
""")