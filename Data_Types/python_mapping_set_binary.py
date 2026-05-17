"""
PYTHON MAPPING, SETS & BINARY TYPES
NeuralAICodeCraft - Complete Guide with Examples

Topics Covered:
1. Dictionaries (Mapping Type)
2. Sets & Frozenset (Set Types)
3. Boolean Type
4. Binary Types (Bytes, Bytearray, Memoryview)
"""

print("=" * 70)
print("🐍 PYTHON MAPPING, SETS & BINARY TYPES")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: DICTIONARIES (Mapping Type)
# ============================================

print("\n📖 PART 1: DICTIONARIES - KEY-VALUE MAPPINGS")
print("-" * 50)

# 1.1 Creating Dictionaries
print("\n1.1 Creating Dictionaries:")
print("-" * 30)

# Different ways to create dicts
empty_dict = {}
person = {"name": "Alice", "age": 30, "city": "New York"}
dict_constructor = dict(name="Bob", age=25, city="Los Angeles")
list_of_tuples = dict([("a", 1), ("b", 2), ("c", 3)])
dict_comprehension = {x: x**2 for x in range(5)}

print(f"  Empty dict: {empty_dict}")
print(f"  Person dict: {person}")
print(f"  Dict constructor: {dict_constructor}")
print(f"  From list of tuples: {list_of_tuples}")
print(f"  Dict comprehension: {dict_comprehension}")

# Mixed key types
mixed_dict = {
    "name": "John",
    1: "one",
    (1, 2): "tuple key",
    True: "boolean key"
}
print(f"  Mixed keys dict: {mixed_dict}")

# 1.2 Accessing and Modifying
print("\n1.2 Accessing and Modifying:")
print("-" * 30)

person = {"name": "Alice", "age": 30, "city": "New York"}
print(f"  Original: {person}")

# Access by key
print(f"  person['name']: {person['name']}")
print(f"  person.get('age'): {person.get('age')}")
print(f"  person.get('country', 'USA'): {person.get('country', 'USA')}")

# Adding new key-value
person["email"] = "alice@example.com"
print(f"  After adding email: {person}")

# Updating existing
person["age"] = 31
print(f"  After updating age: {person}")

# Update multiple values
person.update({"city": "San Francisco", "profession": "Engineer"})
print(f"  After update: {person}")

# 1.3 Dictionary Methods
print("\n1.3 Dictionary Methods:")
print("-" * 30)

sample = {"a": 1, "b": 2, "c": 3, "d": 2, "e": 1}
print(f"  Sample dict: {sample}")

# Keys, values, items
print(f"  keys(): {list(sample.keys())}")
print(f"  values(): {list(sample.values())}")

