"""
RANGE FUNCTION & CONTROL STATEMENTS - COMPLETE GUIDE
NeuralAICodeCraft - Master range(), break, continue, pass, else

Topics Covered:
1. range() Function
2. break Statement
3. continue Statement
4. pass Statement
5. else with Loops
"""

print("=" * 70)
print("🐍 RANGE FUNCTION & CONTROL STATEMENTS - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: range() FUNCTION
# ============================================

print("\n📚 PART 1: range() FUNCTION")
print("-" * 50)

print("""
range() generates a sequence of numbers WITHOUT storing them all in memory.
It's a LAZY sequence - numbers are generated on demand!
""")

# 1.1 range(stop)
print("\n1.1 range(stop) - 0 to stop-1:")
print("-" * 30)

print("range(5):", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(3):", end=" ")
for i in range(3):
    print(i, end=" ")
print()

# 1.2 range(start, stop)
print("\n1.2 range(start, stop) - start to stop-1:")
print("-" * 30)

print("range(2, 7):", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

print("range(5, 10):", end=" ")
for i in range(5, 10):
    print(i, end=" ")
print()

# 1.3 range(start, stop, step)
print("\n1.3 range(start, stop, step) - with step:")
print("-" * 30)

print("range(1, 10, 2) - Odd numbers:", end=" ")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("range(0, 10, 2) - Even numbers:", end=" ")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

print("range(10, 0, -1) - Countdown:", end=" ")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# 1.4 Converting range to list
print("\n1.4 Converting range to list:")
print("-" * 30)

my_range = range(5)
my_list = list(my_range)
print(f"  range(5) → {my_range}")
print(f"  list(range(5)) → {my_list}")

# 1.5 Practical Examples
print("\n1.5 Practical Examples:")
print("-" * 30)

# Sum of numbers 1 to 10
total = 0
for i in range(1, 11):
    total += i
print(f"  Sum of 1 to 10: {total}")

# Factorial of 5
factorial = 1
for i in range(1, 6):
    factorial *= i
print(f"  Factorial of 5: {factorial}")

# Multiplication table
print("  Multiplication Table of 7:")
for i in range(1, 11):
    print(f"    7 × {i:2} = {7 * i:2}")

# ============================================
# PART 2: break STATEMENT
# ============================================

print("\n⏹️ PART 2: break STATEMENT")
print("-" * 50)

print("""
break EXITS the loop immediately.
- Stops all further iterations
- Exits the nearest enclosing loop
- Used to stop when a condition is met
""")

# 2.1 Basic break
print("\n2.1 Basic break:")
print("-" * 30)

print("Looping from 1 to 10, break at 5:")
for i in range(1, 11):
    if i == 5:
        break
    print(f"  {i}")
print("  Loop ended!")

# 2.2 Find first even number
print("\n2.2 Find first even number:")
print("-" * 30)

numbers = [3, 7, 12, 9, 15, 4]
for num in numbers:
    if num % 2 == 0:
        print(f"  Found even number: {num}")
        break

# 2.3 Searching in a list
print("\n2.3 Searching for an element:")
print("-" * 30)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
search_item = "cherry"

for fruit in fruits:
    if fruit == search_item:
        print(f"  Found '{search_item}' at position {fruits.index(fruit)}!")
        break
else:
    print(f"  '{search_item}' not found!")

# 2.4 Unlimited input with break
print("\n2.4 Unlimited input with break:")
print("-" * 30)

print("  Enter numbers to sum (type 'stop' to exit):")
print("  (Simulated example)")

# Simulated user input
user_inputs = ["10", "20", "30", "stop"]
total = 0

for inp in user_inputs:
    if inp.lower() == "stop":
        print(f"  Total sum: {total}")
        break
    total += int(inp)
    print(f"  Added {inp}, total: {total}")

# ============================================
# PART 3: continue STATEMENT
# ============================================

print("\n⏭️ PART 3: continue STATEMENT")
print("-" * 50)

print("""
continue SKIPS the current iteration.
- Jumps to the next iteration
- Does NOT exit the loop
- Used to skip unwanted values
""")

# 3.1 Basic continue
print("\n3.1 Basic continue - Skip even numbers:")
print("-" * 30)

print("Printing only odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# 3.2 Skip invalid values
print("\n3.2 Skip invalid values (negative numbers):")
print("-" * 30)

data = [10, -5, 20, -2, 30, 0, 40, -8, 50]

print(f"  Original data: {data}")
print("  Processing only positive numbers:")
for num in data:
    if num <= 0:
        continue
    print(f"    {num} (valid)")

# 3.3 continue with user input
print("\n3.3 Skip empty strings:")
print("-" * 30)

inputs = ["hello", "", "world", "", "python", "   "]
print(f"  Inputs: {inputs}")

valid_inputs = []
for inp in inputs:
    if not inp.strip():
        continue
    valid_inputs.append(inp)
print(f"  Valid inputs: {valid_inputs}")

# 3.4 continue vs break
print("\n3.4 continue vs break - Visual Comparison:")
print("-" * 30)

print("  continue (skips 3):")
for i in range(1, 6):
    if i == 3:
        print("    (skipping 3)")
        continue
    print(f"    {i}")
print("  Loop continues!")

print("\n  break (stops at 3):")
for i in range(1, 6):
    if i == 3:
        print("    (breaking at 3)")
        break
    print(f"    {i}")
print("  Loop ended!")

# ============================================
# PART 4: pass STATEMENT
# ============================================

print("\n⏸️ PART 4: pass STATEMENT")
print("-" * 50)

print("""
pass does NOTHING!
- Acts as a placeholder
- Does not affect loop execution
- Used when syntax requires a statement
- For future code implementation
""")

# 4.1 Basic pass
print("\n4.1 Basic pass - Placeholder:")
print("-" * 30)

print("Loop with pass (no effect):")
for i in range(5):
    pass  # Does nothing
print("  Loop completed!")

# 4.2 pass in if-else
print("\n4.2 pass in if-else (placeholder):")
print("-" * 30)

x = 10
if x > 5:
    # TODO: Add logic later
    pass
else:
    print("x is not greater than 5")
print("  Code continues...")

# 4.3 pass in functions (placeholder)
print("\n4.3 pass in functions (placeholder):")
print("-" * 30)

def future_function():
    """This function will be implemented later"""
    pass

print("  Function defined with pass")
print("  Function name: future_function")

# 4.4 pass vs continue
print("\n4.4 pass vs continue - Difference:")
print("-" * 30)

print("  pass (does nothing):")
for i in range(5):
    if i == 2:
        pass
    print(f"    {i}", end=" ")
print()

print("  continue (skips iteration):")
for i in range(5):
    if i == 2:
        continue
    print(f"    {i}", end=" ")
print()

# ============================================
# PART 5: else WITH LOOPS
# ============================================

print("\n🔀 PART 5: else WITH LOOPS")
print("-" * 50)

print("""
else with loops executes when:
- Loop completes ALL iterations
- No break statement was encountered
- NOT executed if break occurs
- Common use: "search with no match"
""")

# 5.1 Basic else
print("\n5.1 Basic else (no break):")
print("-" * 30)

print("Normal loop completion:")
for i in range(1, 6):
    print(f"  {i}")
else:
    print("  ✅ Loop completed normally!")

# 5.2 else with break
print("\n5.2 else with break (not executed):")
print("-" * 30)

print("Loop with break:")
for i in range(1, 6):
    if i == 3:
        print(f"  Breaking at {i}")
        break
    print(f"  {i}")
else:
    print("  This won't execute!")

# 5.3 Prime number check
print("\n5.3 Prime Number Check using else:")
print("-" * 30)

def is_prime(n):
    """Check if a number is prime using for-else"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"  {n} is divisible by {i}")
            return False
    else:
        print(f"  {n} is PRIME!")
        return True

test_numbers = [2, 7, 12, 17, 25, 29]
for num in test_numbers:
    is_prime(num)
    print()

# 5.4 Search with else
print("\n5.4 Search with 'not found' using else:")
print("-" * 30)

def find_in_list(lst, target):
    """Find element in list using for-else"""
    for item in lst:
        if item == target:
            print(f"  Found '{target}'!")
            return True
    else:
        print(f"  '{target}' not found")
        return False

fruits = ["apple", "banana", "cherry", "date"]

find_in_list(fruits, "cherry")
find_in_list(fruits, "mango")

# ============================================
# PART 6: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 6: REAL-WORLD EXAMPLES")
print("-" * 50)

# 6.1 Password Validator
print("\n6.1 Password Validator:")
print("-" * 30)

def validate_password(password):
    """Validate password using loop control"""
    # Check length
    if len(password) < 8:
        print("  ❌ Password must be at least 8 characters")
        return False
    
    # Check for uppercase, lowercase, digit
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    if not has_upper:
        print("  ❌ Password needs at least one uppercase letter")
        return False
    if not has_lower:
        print("  ❌ Password needs at least one lowercase letter")
        return False
    if not has_digit:
        print("  ❌ Password needs at least one digit")
        return False
    
    print("  ✅ Password is valid!")
    return True

validate_password("Python123")
validate_password("weak")
validate_password("STRONGpass")

# 6.2 Temperature Converter
print("\n6.2 Temperature Converter with continue:")
print("-" * 30)

temperatures = [25, -10, 30, 0, 100, -5, 45]
print(f"  Temperatures: {temperatures}")

print("  Converting to Fahrenheit:")
for temp in temperatures:
    if temp < 0:
        print(f"    {temp}°C → Skipping (below 0)")
        continue
    fahrenheit = (temp * 9/5) + 32
    print(f"    {temp}°C = {fahrenheit:.1f}°F")

# 6.3 Find Multiples
print("\n6.3 Find Multiples with break:")
print("-" * 30)

def find_multiple(number, start=1, limit=50):
    """Find first multiple in range"""
    for i in range(start, limit + 1):
        if i % number == 0:
            print(f"  First multiple of {number} between {start} and {limit}: {i}")
            return i
    else:
        print(f"  No multiple of {number} found between {start} and {limit}")

find_multiple(7)
find_multiple(13)

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: range() Practice
Print all even numbers from 2 to 20 using range()

🎯 EXERCISE 2: break Practice
Find the first number in a list that is divisible by 7

🎯 EXERCISE 3: continue Practice
Print only prime numbers between 1 and 20

🎯 EXERCISE 4: pass Practice
Create a function skeleton using pass

🎯 EXERCISE 5: else Practice
Check if a number is divisible by any number from 2 to 9

🎯 CHALLENGE: Complete Program
Create a program that:
- Takes user input (simulated)
- Uses range() for iteration
- Uses break to exit on "quit"
- Uses continue to skip invalid input
- Uses else to confirm completion
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Even numbers 2 to 20:")
evens = [i for i in range(2, 21, 2)]
print(f"  {evens}")

# Exercise 2
print("\nEx2 - First number divisible by 7:")
numbers = [10, 23, 35, 42, 56, 70]
for num in numbers:
    if num % 7 == 0:
        print(f"  {num} is divisible by 7")
        break

# Exercise 3
print("\nEx3 - Prime numbers 1 to 20:")
def is_prime_num(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(2, 21) if is_prime_num(n)]
print(f"  {primes}")

# Exercise 4
print("\nEx4 - Function skeleton:")
def future_function():
    pass
print("  ✅ Function created with pass")

# Exercise 5
print("\nEx5 - Divisibility check:")
def check_divisibility(n):
    for i in range(2, 10):
        if n % i == 0:
            print(f"  {n} is divisible by {i}")
            break
    else:
        print(f"  {n} is not divisible by 2-9")

check_divisibility(30)
check_divisibility(17)

# Challenge
print("\nChallenge - Complete Program:")
def user_loop():
    """Simulated user input loop"""
    print("  Enter numbers (type 'quit' to exit)")
    total = 0
    for i in range(1, 10):  # Simulate 10 attempts
        simulated_inputs = ["10", "20", "quit", "30", "40"]
        user_input = simulated_inputs[i - 1]
        
        if user_input.lower() == "quit":
            print(f"  Exiting loop at iteration {i}")
            break
        
        try:
            num = int(user_input)
            total += num
            print(f"  Added {num}, total: {total}")
        except ValueError:
            print(f"  Skipping invalid input: '{user_input}'")
            continue
    else:
        print("  Loop completed normally!")
    print(f"  Final total: {total}")

user_loop()

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ RANGE & CONTROL STATEMENTS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    range() FUNCTION                         │
├─────────────────────────────────────────────────────────────┤
│  range(stop)          → 0 to stop-1                        │
│  range(start, stop)   → start to stop-1                    │
│  range(start, stop, step) → start to stop-1 with step      │
├─────────────────────────────────────────────────────────────┤
│                    CONTROL STATEMENTS                       │
├─────────────────────────────────────────────────────────────┤
│  break    → Exit loop completely                           │
│  continue → Skip current iteration                         │
│  pass     → Do nothing (placeholder)                       │
│  else     → Execute when loop completes normally            │
├─────────────────────────────────────────────────────────────┤
│                    USE CASES                                │
├─────────────────────────────────────────────────────────────┤
│  break    → Search and stop, early termination             │
│  continue → Skip invalid values, filter                    │
│  pass     → Placeholder for future code                    │
│  else     → "Not found" condition, post-loop processing    │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Nested Loops & Loop Optimization
""")