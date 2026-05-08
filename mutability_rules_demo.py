
"""
Python Mutability Rules: Reassignment vs Shared Reference
NeuralAICodeCraft - Core Principle Demo
"""

print("=" * 60)
print("RULE 1: THE SHARED REFERENCE RULE")
print("=" * 60)

# Both variables point to the SAME object
list_a = [1, 2, 3]
list_b = list_a  # Shared reference

print(f"list_a = {list_a}, id = {id(list_a)}")
print(f"list_b = {list_b}, id = {id(list_b)}")
print(f"Same object? {list_a is list_b}")  # True

# Modify through one reference
list_b.append(4)
print(f"\nAfter list_b.append(4):")
print(f"list_a = {list_a}")  # ALSO changed! 🔴
print(f"list_b = {list_b}")

print("\n" + "=" * 60)
print("RULE 2: REASSIGNMENT CREATES A NEW OBJECT")
print("=" * 60)

list_a = [1, 2, 3]
list_b = list_a  # Shared reference

print(f"Before reassignment:")
print(f"list_a id = {id(list_a)}")
print(f"list_b id = {id(list_b)}")
print(f"Same object? {list_a is list_b}")  # True

# REASSIGNMENT - creates NEW object
list_b = [4, 5, 6]

print(f"\nAfter reassignment (list_b = [4,5,6]):")
print(f"list_a = {list_a}, id = {id(list_a)}")  # Unchanged! 🟢
print(f"list_b = {list_b}, id = {id(list_b)}")  # NEW id!
print(f"Same object? {list_a is list_b}")  # False

print("\n" + "=" * 60)
print("RULE 3: MUTABLE VS IMMUTABLE BEHAVIOR")
print("=" * 60)

# IMMUTABLE example (int)
print("\n--- IMMUTABLE (int) ---")
a = 10
b = a
print(f"Before: a={a}, b={b}, same object? {a is b}")
b = b + 1  # Reassignment creates NEW object
print(f"After b+1: a={a}, b={b}, same object? {a is b}")
print("🔵 Immutable: Original SAFE!")

# MUTABLE example (list)
print("\n--- MUTABLE (list) ---")
c = [1, 2, 3]
d = c
print(f"Before: c={c}, d={d}, same object? {c is d}")
d.append(4)  # Modifies in place (NO reassignment)
print(f"After d.append(4): c={c}, d={d}, same object? {c is d}")
print("🔴 Mutable: Original CHANGED!")

print("\n" + "=" * 60)
print("THE CORE PRINCIPLE")
print("=" * 60)

print("""
╔════════════════════════════════════════════════════════════╗
║  CODE BEHAVIOR DEPENDS ON MUTABLE VS IMMUTABLE OBJECTS     ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  IMMUTABLE (int, float, str, tuple):                       ║
║  ▸ Operations create NEW objects                           ║
║  ▸ Original objects NEVER change                           ║
║  ▸ Safe to share references                                ║
║                                                            ║
║  MUTABLE (list, dict, set):                                ║
║  ▸ Modifications change the SAME object                    ║
║  ▸ Shared references = unexpected changes                  ║
║  ▸ Use copy() or reassignment to break links               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""")

print("\n" + "=" * 60)
print("QUIZ: TEST YOUR UNDERSTANDING")
print("=" * 60)

print("""
Question 1:
x = [1, 2, 3]
y = x
x = [4, 5, 6]
print(y)  # What prints?

Answer: [1, 2, 3] (reassignment of x doesn't affect y)

Question 2:
a = [1, 2, 3]
b = a
b.append(4)
print(a)  # What prints?

Answer: [1, 2, 3, 4] (modification through shared reference)

Question 3:
name = "Python"
nickname = name
nickname = nickname + " AI"
print(name)  # What prints?

Answer: "Python" (strings are immutable)
""")

print("\n✅ You now understand the core principle of Python mutability!")

