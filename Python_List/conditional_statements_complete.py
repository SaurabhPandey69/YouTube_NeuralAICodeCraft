"""
IF-ELSE CONDITIONAL STATEMENTS - COMPLETE GUIDE
NeuralAICodeCraft - Master if, elif, else, nested conditions

Topics Covered:
1. if Statement
2. else Statement
3. elif Statement
4. Nested if-else
5. Logical Operators (and, or, not)
6. Real-World Examples
"""

print("=" * 70)
print("🐍 IF-ELSE CONDITIONAL STATEMENTS - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: IF STATEMENT BASICS
# ============================================

print("\n📚 PART 1: IF STATEMENT BASICS")
print("-" * 50)

print("""
SYNTAX:
    if condition:
        # Code to execute if condition is True
        # (Indentation is mandatory!)

KEY POINTS:
├── Condition must evaluate to True or False
├── Indentation is CRITICAL (4 spaces recommended)
├── Can be used with any data type (truthy/falsy)
└── Colon (:) is required after the condition
""")

# 1.1 Basic if statement
print("\n1.1 Basic if statement:")
print("-" * 30)

age = 18
if age >= 18:
    print("  ✅ You are eligible to vote!")
print("  Program continues...")

# 1.2 if with different data types
print("\n1.2 if with different data types:")
print("-" * 30)

name = "Python"
if name:
    print(f"  ✅ '{name}' is truthy (non-empty string)")

num = 5
if num:
    print(f"  ✅ {num} is truthy (non-zero number)")

# Falsy values
empty_list = []
if not empty_list:
    print("  ✅ Empty list is Falsy")

# 1.3 Comparison operators
print("\n1.3 Comparison Operators:")
print("-" * 30)

print("""
OPERATOR  MEANING
────────  ──────────────────
==        Equal to
!=        Not equal to
<         Less than
>         Greater than
<=        Less than or equal to
>=        Greater than or equal to
""")

x, y = 10, 20
print(f"  x = {x}, y = {y}")
print(f"  x == y → {x == y}")
print(f"  x != y → {x != y}")
print(f"  x < y  → {x < y}")
print(f"  x > y  → {x > y}")
print(f"  x <= y → {x <= y}")
print(f"  x >= y → {x >= y}")

# ============================================
# PART 2: ELSE STATEMENT
# ============================================

print("\n🔀 PART 2: ELSE STATEMENT")
print("-" * 50)

print("""
SYNTAX:
    if condition:
        # Code runs if True
    else:
        # Code runs if False

else is OPTIONAL but useful for handling both paths
""")

# 2.1 Basic else
print("\n2.1 Basic else:")
print("-" * 30)

age = 16
if age >= 18:
    print("  ✅ You are eligible to vote!")
else:
    print(f"  ❌ You are {age}, not eligible to vote")

# 2.2 else with input (simulated)
print("\n2.2 else with user input (simulated):")
print("-" * 30)

# Simulated user input
temperature = 30

if temperature > 25:
    print(f"  🔥 It's {temperature}°C - Hot outside!")
else:
    print(f"  ❄️ It's {temperature}°C - Cool outside!")

# 2.3 Multiple else examples
print("\n2.3 Multiple else examples:")
print("-" * 30)

number = 7

if number % 2 == 0:
    print(f"  {number} is even")
else:
    print(f"  {number} is odd")

# ============================================
# PART 3: ELIF STATEMENT (ELSE IF)
# ============================================

print("\n🔀 PART 3: ELIF STATEMENT (Multiple Conditions)")
print("-" * 50)

print("""
SYNTAX:
    if condition1:
        # Runs if condition1 is True
    elif condition2:
        # Runs if condition1 is False AND condition2 is True
    elif condition3:
        # Runs if condition1 & condition2 are False AND condition3 is True
    else:
        # Runs if ALL conditions are False

elif = else if (shorthand for nested if-else)
""")

# 3.1 Basic elif
print("\n3.1 Basic elif:")
print("-" * 30)

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"  Score: {score}, Grade: {grade}")

# 3.2 elif with multiple conditions
print("\n3.2 elif with multiple conditions:")
print("-" * 30)

age = 25

if age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
elif age < 60:
    category = "Adult"
else:
    category = "Senior"

print(f"  Age: {age}, Category: {category}")

# 3.3 elif vs multiple if statements
print("\n3.3 elif vs multiple if statements:")
print("-" * 30)

num = 5

print("  Using elif (only ONE block executes):")
if num > 0:
    print("    Positive")
elif num < 0:
    print("    Negative")
else:
    print("    Zero")

print("  Using multiple if (ALL blocks with True conditions execute):")
if num > 0:
    print("    Positive")
if num < 0:
    print("    Negative")
if num == 0:
    print("    Zero")

print("  💡 TIP: Use elif for mutually exclusive conditions!")

# ============================================
# PART 4: NESTED IF-ELSE
# ============================================

print("\n📦 PART 4: NESTED IF-ELSE")
print("-" * 50)

print("""
Nested if-else means having an if-else statement INSIDE another if-else.
- Used for checking conditions within conditions
- Can go multiple levels deep (but avoid over-nesting)
""")

# 4.1 Basic nested if-else
print("\n4.1 Basic nested if-else:")
print("-" * 30)

age = 25
has_license = True

if age >= 18:
    if has_license:
        print("  ✅ You can drive a car")
    else:
        print("  ⚠️ You need a license to drive")
else:
    print("  ❌ You are too young to drive")

# 4.2 Nested if-else with multiple conditions
print("\n4.2 Nested if-else for movie ticket:")
print("-" * 30)

age = 12
is_student = True
is_senior = False

if age >= 18:
    if is_senior:
        ticket_price = 8
        print(f"  Senior ticket: ${ticket_price}")
    else:
        ticket_price = 12
        print(f"  Adult ticket: ${ticket_price}")
else:
    if is_student:
        ticket_price = 6
        print(f"  Student ticket: ${ticket_price}")
    else:
        ticket_price = 8
        print(f"  Child ticket: ${ticket_price}")

print(f"  Age: {age}, Price: ${ticket_price}")

# 4.3 Nested if-else readability
print("\n4.3 Nested if-else - Better readability:")
print("-" * 30)

# Instead of deep nesting, use elif with logical operators
age = 25
is_employed = True

print("  Deep nesting (less readable):")
if age >= 18:
    if is_employed:
        print("    Adult with job")
    else:
        print("    Adult without job")
else:
    print("    Minor")

print("\n  elif with logical operators (more readable):")
if age < 18:
    print("    Minor")
elif is_employed:
    print("    Adult with job")
else:
    print("    Adult without job")

# ============================================
# PART 5: LOGICAL OPERATORS (and, or, not)
# ============================================

print("\n🔗 PART 5: LOGICAL OPERATORS (and, or, not)")
print("-" * 50)

print("""
LOGICAL OPERATORS:
├── and → Both conditions must be True
├── or  → At least one condition must be True
└── not → Negates the condition (True → False, False → True)

TRUTH TABLE:
┌──────────┬──────────┬─────────────┬────────────┬──────────┐
│    A     │    B     │  A and B    │  A or B    │  not A   │
├──────────┼──────────┼─────────────┼────────────┼──────────┤
│   True   │   True   │   True      │   True     │  False   │
│   True   │   False  │   False     │   True     │  False   │
│   False  │   True   │   False     │   True     │  True    │
│   False  │   False  │   False     │   False    │  True    │
└──────────┴──────────┴─────────────┴────────────┴──────────┘
""")

# 5.1 AND operator
print("\n5.1 AND Operator:")
print("-" * 30)

age = 25
has_id = True

if age >= 18 and has_id:
    print("  ✅ You can enter the club")

# 5.2 OR operator
print("\n5.2 OR Operator:")
print("-" * 30)

is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("  ✅ It's a day off!")

# 5.3 NOT operator
print("\n5.3 NOT Operator:")
print("-" * 30)

is_raining = False

if not is_raining:
    print("  ☀️ It's not raining, go outside!")
else:
    print("  🌧️ It's raining, stay inside!")

# 5.4 Combining logical operators
print("\n5.4 Combining Logical Operators:")
print("-" * 30)

age = 20
is_student = True
has_work_experience = False

if (age >= 18 and is_student) or has_work_experience:
    print("  ✅ You qualify for the internship")
else:
    print("  ❌ You don't qualify for the internship")

# ============================================
# PART 6: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 6: REAL-WORLD EXAMPLES")
print("-" * 50)

# 6.1 Grade Calculator
print("\n6.1 Grade Calculator:")
print("-" * 30)

def calculate_grade(score):
    """Calculate grade based on score"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

test_scores = [95, 82, 67, 55, 88]
for score in test_scores:
    grade = calculate_grade(score)
    print(f"  Score: {score:3} → Grade: {grade}")

# 6.2 Ticket Pricing System
print("\n6.2 Ticket Pricing System:")
print("-" * 30)

def calculate_ticket_price(age, is_student=False, is_senior=False):
    """Calculate ticket price based on age and status"""
    if age < 5:
        return 0  # Free for children under 5
    elif age >= 65 or is_senior:
        return 8  # Senior discount
    elif is_student or age < 18:
        return 10  # Student/Child discount
    else:
        return 15  # Adult price

# Test cases
customers = [
    (3, False, False),   # Child under 5
    (12, True, False),   # Student
    (30, False, False),  # Adult
    (70, False, False),  # Senior
    (45, True, False),   # Adult student
]

for age, is_student, is_senior in customers:
    price = calculate_ticket_price(age, is_student, is_senior)
    status = []
    if is_student:
        status.append("Student")
    if is_senior:
        status.append("Senior")
    if not status and age < 5:
        status.append("Child")
    elif not status:
        status.append("Adult")
    print(f"  Age: {age:2}, {', '.join(status)} → Ticket: ${price}")

# 6.3 Login System
print("\n6.3 Login System (Simulated):")
print("-" * 30)

# Simulated database
USERNAME = "admin"
PASSWORD = "python123"

def login(username, password):
    """Simple login validation"""
    if not username:
        return "Username cannot be empty"
    elif not password:
        return "Password cannot be empty"
    elif username == USERNAME and password == PASSWORD:
        return "✅ Login successful!"
    elif username == USERNAME:
        return "❌ Incorrect password"
    else:
        return "❌ Username not found"

# Test login attempts
attempts = [
    ("", "pass"),
    ("admin", ""),
    ("admin", "wrong"),
    ("user", "python123"),
    ("admin", "python123"),
]

for username, password in attempts:
    result = login(username, password)
    print(f"  Username: '{username}', Password: '{password}' → {result}")

# 6.4 Leap Year Checker
print("\n6.4 Leap Year Checker:")
print("-" * 30)

def is_leap_year(year):
    """Check if a year is a leap year"""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

years = [1900, 2000, 2020, 2023, 2024, 2100]
for year in years:
    result = is_leap_year(year)
    print(f"  {year} → {'✅ Leap Year' if result else '❌ Not Leap Year'}")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Number Checker
Write a program that checks if a number is positive, negative, or zero.

🎯 EXERCISE 2: Grade Calculator
Write a program that assigns grades based on marks.

🎯 EXERCISE 3: Leap Year
Write a program to check if a year is a leap year.

🎯 EXERCISE 4: Simple Calculator
Write a program that takes two numbers and an operator (+, -, *, /).

🎯 EXERCISE 5: Voting Eligibility
Check if a person is eligible to vote based on age and citizenship.

🎯 CHALLENGE: Employee Bonus Calculator
Calculate bonus based on:
- Years of service (>10 years: 10%, 5-10 years: 5%, <5 years: 0%)
- Performance rating (Excellent: 5%, Good: 3%, Fair: 1%)
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - Number Checker:")
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

for num in [-5, 0, 7]:
    print(f"  {num} → {check_number(num)}")

# Exercise 2
print("\nEx2 - Grade Calculator:")
def grade_calc(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

for marks in [95, 82, 67, 55, 88]:
    print(f"  {marks} → {grade_calc(marks)}")

# Exercise 3
print("\nEx3 - Leap Year:")
def leap_year(year):
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

for year in [2020, 2023, 2024, 2100, 2000]:
    print(f"  {year} → {'Yes' if leap_year(year) else 'No'}")

# Exercise 4
print("\nEx4 - Calculator:")
def calculator(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b if b != 0 else "Division by zero"
    else:
        return "Invalid operator"

print(f"  10 + 5 = {calculator(10, 5, '+')}")
print(f"  10 - 5 = {calculator(10, 5, '-')}")
print(f"  10 * 5 = {calculator(10, 5, '*')}")
print(f"  10 / 5 = {calculator(10, 5, '/')}")

# Exercise 5
print("\nEx5 - Voting Eligibility:")
def can_vote(age, citizen):
    if age >= 18 and citizen:
        return "Eligible to vote"
    elif age < 18:
        return "Too young to vote"
    else:
        return "Must be a citizen"

print(f"  Age 20, Citizen: {can_vote(20, True)}")
print(f"  Age 16, Citizen: {can_vote(16, True)}")
print(f"  Age 25, Non-citizen: {can_vote(25, False)}")

# Challenge
print("\nChallenge - Employee Bonus:")
def calculate_bonus(years, performance):
    """Calculate bonus based on years and performance"""
    bonus = 0
    
    # Years of service bonus
    if years > 10:
        bonus += 10
    elif years >= 5:
        bonus += 5
    else:
        bonus += 0
    
    # Performance bonus
    if performance.lower() == "excellent":
        bonus += 5
    elif performance.lower() == "good":
        bonus += 3
    elif performance.lower() == "fair":
        bonus += 1
    
    return bonus

employees = [
    (12, "Excellent"),
    (7, "Good"),
    (3, "Fair"),
    (8, "Excellent"),
    (15, "Good"),
]

for years, performance in employees:
    bonus = calculate_bonus(years, performance)
    print(f"  Years: {years:2}, Performance: {performance:9} → {bonus}% bonus")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ IF-ELSE CONDITIONAL STATEMENTS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    IF-ELSE SYNTAX                           │
├─────────────────────────────────────────────────────────────┤
│  if condition:                                             │
│      # Code if True                                       │
│  elif another_condition:                                   │
│      # Code if first False and this True                  │
│  else:                                                     │
│      # Code if all conditions False                       │
├─────────────────────────────────────────────────────────────┤
│                    COMPARISON OPERATORS                     │
├─────────────────────────────────────────────────────────────┤
│  ==  Equal to         !=  Not equal to                    │
│  >   Greater than     <   Less than                       │
│  >=  Greater/equal    <=  Less/equal                      │
├─────────────────────────────────────────────────────────────┤
│                    LOGICAL OPERATORS                        │
├─────────────────────────────────────────────────────────────┤
│  and → Both must be True                                   │
│  or  → At least one must be True                           │
│  not → Negates the condition                               │
├─────────────────────────────────────────────────────────────┤
│                    TRUTHY vs FALSY                          │
├─────────────────────────────────────────────────────────────┤
│  Falsy: None, False, 0, "", [], {}, set(), range(0)       │
│  Truthy: Everything else!                                  │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: While Loop - Iteration in Python
""")