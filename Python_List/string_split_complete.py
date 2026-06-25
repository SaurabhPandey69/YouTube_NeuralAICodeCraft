"""
PYTHON .split() METHOD: COMPLETE GUIDE
NeuralAICodeCraft - Master String Splitting

Topics Covered:
1. Basic .split() Usage (Default Whitespace)
2. Custom Separators
3. maxsplit Parameter
4. Real-World Examples
5. Common Mistakes & Best Practices
"""

print("=" * 70)
print("🔪 PYTHON .split() METHOD - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: BASIC .split() USAGE
# ============================================

print("\n📚 PART 1: BASIC .split() USAGE")
print("-" * 50)

print("""
SYNTAX: string.split(separator, maxsplit)

DEFAULT BEHAVIOR:
- Splits on ANY whitespace (spaces, tabs, newlines)
- Returns a list of words
- Consecutive whitespace is treated as one
""")

# 1.1 Basic Splitting
print("\n1.1 Basic Splitting (Default):")
print("-" * 30)

text = "Hello World Python"
words = text.split()
print(f"  Original: '{text}'")
print(f"  .split() → {words}")  # ['Hello', 'World', 'Python']

# 1.2 Multiple Words
print("\n1.2 Splitting Sentences:")
print("-" * 30)

sentence = "Python is a powerful programming language"
words = sentence.split()
print(f"  Original: '{sentence}'")
print(f"  .split() → {words}")
print(f"  Number of words: {len(words)}")

# 1.3 Handling Multiple Spaces
print("\n1.3 Multiple Whitespace Handling:")
print("-" * 30)

text_multi = "Python  is   a   great   language"
words = text_multi.split()
print(f"  Original: '{text_multi}'")
print(f"  .split() → {words}")

print("  💡 Multiple spaces are treated as ONE separator!")

# ============================================
# PART 2: CUSTOM SEPARATORS
# ============================================

print("\n🎯 PART 2: CUSTOM SEPARATORS")
print("-" * 50)

print("""
You can split on ANY character or substring!
- .split(',') → Split on commas
- .split('-') → Split on hyphens
- .split('|') → Split on pipe
- .split(' ') → Split on spaces (single)
""")

# 2.1 Comma Separated Values
print("\n2.1 Comma Separated Values (CSV):")
print("-" * 30)

csv_data = "apple,banana,cherry,date"
fruits = csv_data.split(',')
print(f"  Original: '{csv_data}'")
print(f"  .split(',') → {fruits}")

# 2.2 Hyphen Separated
print("\n2.2 Hyphen Separated:")
print("-" * 30)

date = "2024-01-15"
parts = date.split('-')
print(f"  Original: '{date}'")
print(f"  .split('-') → {parts}")
print(f"  Year: {parts[0]}, Month: {parts[1]}, Day: {parts[2]}")

# 2.3 Pipe Separated
print("\n2.3 Pipe Separated:")
print("-" * 30)

data = "John|25|Engineer|New York"
fields = data.split('|')
print(f"  Original: '{data}'")
print(f"  .split('|') → {fields}")

# 2.4 Space Separator (Explicit)
print("\n2.4 Space Separator (Explicit):")
print("-" * 30)

text_spaces = "Hello World Python"
words = text_spaces.split(' ')
print(f"  Original: '{text_spaces}'")
print(f"  .split(' ') → {words}")

print("  ⚠️ Note: Explicit space splits on SINGLE spaces only!")
print("     'Hello  World'.split(' ') → ['Hello', '', 'World']")

# 2.5 Splitting on Words/Substrings
print("\n2.5 Splitting on Words/Substrings:")
print("-" * 30)

url = "https://www.python.org/docs"
parts = url.split('://')
print(f"  Original: '{url}'")
print(f"  .split('://') → {parts}")
print(f"  Protocol: {parts[0]}, Rest: {parts[1]}")

# ============================================
# PART 3: MAXSPLIT PARAMETER
# ============================================

print("\n⏸️ PART 3: maxsplit PARAMETER")
print("-" * 50)

print("""
maxsplit limits the number of splits performed.
- Default: No limit (split all occurrences)
- maxsplit=1 → Only split on the first occurrence
- maxsplit=n → Split on first n occurrences
- The remaining part stays together as the last element
""")

# 3.1 Basic maxsplit
print("\n3.1 Basic maxsplit Examples:")
print("-" * 30)

text = "one two three four five"
print(f"  Original: '{text}'")

print(f"  .split() → {text.split()}")
print(f"  .split(maxsplit=1) → {text.split(maxsplit=1)}")
print(f"  .split(maxsplit=2) → {text.split(maxsplit=2)}")
print(f"  .split(maxsplit=3) → {text.split(maxsplit=3)}")

# 3.2 Practical maxsplit - Parsing Email
print("\n3.2 Practical Example: Email Parsing:")
print("-" * 30)

email = "john.doe@example.com"
username, domain = email.split('@', 1)
print(f"  Email: '{email}'")
print(f"  .split('@', 1) → {email.split('@', 1)}")
print(f"  Username: {username}")
print(f"  Domain: {domain}")

# 3.3 CSV with maxsplit
print("\n3.3 Practical Example: CSV with maxsplit:")
print("-" * 30)

csv_line = "name,age,city,country,occupation,salary"
first_fields = csv_line.split(',', 2)
print(f"  Original: '{csv_line}'")
print(f"  .split(',', 2) → {first_fields}")

# 3.4 URL Parsing with maxsplit
print("\n3.4 URL Parsing:")
print("-" * 30)

url = "https://www.python.org/docs/3.12/library"
protocol, rest = url.split('://', 1)
domain, path = rest.split('/', 1)
print(f"  URL: '{url}'")
print(f"  Protocol: {protocol}")
print(f"  Domain: {domain}")
print(f"  Path: {path}")

# ============================================
# PART 4: REAL-WORLD EXAMPLES
# ============================================

print("\n🌐 PART 4: REAL-WORLD EXAMPLES")
print("-" * 50)

# 4.1 Parsing CSV Data
print("\n4.1 Parsing CSV Data:")
print("-" * 30)

csv_data = """id,name,age,city
1,Alice,25,New York
2,Bob,30,Los Angeles
3,Charlie,35,Chicago"""

print("  CSV Data:")
for line in csv_data.split('\n'):
    fields = line.split(',')
    if fields[0] != "id":
        print(f"    ID: {fields[0]}, Name: {fields[1]}, Age: {fields[2]}, City: {fields[3]}")

# 4.2 Processing Log Files
print("\n4.2 Processing Log Files:")
print("-" * 30)

log_line = "2024-01-15 14:30:25 INFO User logged in successfully"
parts = log_line.split(' ', 3)
print(f"  Log: '{log_line}'")
print(f"  Date: {parts[0]}")
print(f"  Time: {parts[1]}")
print(f"  Level: {parts[2]}")
print(f"  Message: {parts[3]}")

# 4.3 Parsing User Input
print("\n4.3 Parsing User Input:")
print("-" * 30)

user_input = "create file data.txt"
command, *args = user_input.split()
print(f"  Input: '{user_input}'")
print(f"  Command: {command}")
print(f"  Arguments: {args}")

# 4.4 Extracting URL Parameters
print("\n4.4 Extracting URL Parameters:")
print("-" * 30)

url = "https://example.com/api?page=2&limit=10&sort=asc"
domain, query = url.split('?', 1)
print(f"  URL: '{url}'")
print(f"  Domain: {domain}")
print(f"  Query String: {query}")

# ============================================
# PART 5: .split() vs .rsplit()
# ============================================

print("\n⚖️ PART 5: .split() vs .rsplit()")
print("-" * 50)

print("""
.rsplit() splits from the RIGHT side of the string.
- .split() → splits from left to right
- .rsplit() → splits from right to left
- Great for getting last n elements!
""")

text = "one two three four five"
print(f"  Original: '{text}'")

print(f"\n  .split(maxsplit=2) → {text.split(maxsplit=2)}")
print(f"  .rsplit(maxsplit=2) → {text.rsplit(maxsplit=2)}")

print("\n  💡 Use .rsplit() when you want to split from the end!")

# Practical: File Extension
print("\n  Practical: Getting filename and extension:")
filename = "document.pdf.txt"
name, ext = filename.rsplit('.', 1)
print(f"  Filename: '{filename}'")
print(f"  Name: {name}")
print(f"  Extension: {ext}")

# ============================================
# PART 6: COMMON MISTAKES
# ============================================

print("\n⚠️ PART 6: COMMON MISTAKES & BEST PRACTICES")
print("-" * 50)

# 6.1 Mistake - Splitting on Empty String
print("\n6.1 Mistake #1: Splitting on Empty String:")
print("-" * 30)

text = "Hello"
print(f"  text.split('') → {text.split('')}")
print("  💡 Use list(text) instead!")

# 6.2 Mistake - Forgetting that .split() returns list
print("\n6.2 Mistake #2: .split() returns a LIST:")
print("-" * 30)

text = "Hello World"
result = text.split()
print(f"  Type of text.split(): {type(result)}")
print("  💡 .split() ALWAYS returns a list of strings!")

# 6.3 Best Practices
print("\n6.3 Best Practices:")
print("-" * 30)

print("""
✅ Use .split() without args for whitespace splitting
✅ Use .split(separator) for custom separators
✅ Use maxsplit when you only need first n parts
✅ Use .rsplit() when splitting from right
✅ Handle empty strings gracefully
""")

# ============================================
# PART 7: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 7: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Sentence to Words
Split "Python is an amazing language" into words

🎯 EXERCISE 2: CSV Parsing
Split "John,Doe,25,Engineer" into fields

🎯 EXERCISE 3: maxsplit Usage
Split "a-b-c-d-e" into ['a', 'b', 'c-d-e']

🎯 EXERCISE 4: Email Parser
Split "user@domain.com" into username and domain

🎯 EXERCISE 5: URL Parser
Split "https://example.com:8080/path" into protocol, host, port, path

🎯 CHALLENGE: Log Parser
Parse a log line: "2024-01-15 14:30:25 ERROR Connection timeout"
Extract date, time, level, message
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
text1 = "Python is an amazing language"
words = text1.split()
print(f"Ex1 - Words: {words}")

# Exercise 2
csv = "John,Doe,25,Engineer"
fields = csv.split(',')
print(f"Ex2 - Fields: {fields}")

# Exercise 3
text3 = "a-b-c-d-e"
parts = text3.split('-', 2)
print(f"Ex3 - Parts: {parts}")

# Exercise 4
email = "user@domain.com"
username, domain = email.split('@', 1)
print(f"Ex4 - Username: {username}, Domain: {domain}")

# Exercise 5
url = "https://example.com:8080/path"
protocol, rest = url.split('://', 1)
host, port, path = rest.split(':', 1)[0], rest.split(':', 1)[1].split('/')[0], '/' + rest.split('/', 1)[1]
# Simplified version
parts = url.split('/')
print(f"Ex5 - Protocol: {url.split('://')[0]}")
print(f"Ex5 - Domain: {url.split('/')[2]}")

# Challenge
log = "2024-01-15 14:30:25 ERROR Connection timeout"
log_parts = log.split(' ', 3)
print(f"Challenge - Date: {log_parts[0]}")
print(f"Challenge - Time: {log_parts[1]}")
print(f"Challenge - Level: {log_parts[2]}")
print(f"Challenge - Message: {log_parts[3]}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ .split() METHOD MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    .split() BASICS                          │
├─────────────────────────────────────────────────────────────┤
│  "a b c".split()       → ['a', 'b', 'c']    (whitespace)   │
│  "a,b,c".split(',')    → ['a', 'b', 'c']    (comma)        │
│  "a-b-c".split('-')    → ['a', 'b', 'c']    (hyphen)       │
│  "a|b|c".split('|')    → ['a', 'b', 'c']    (pipe)         │
├─────────────────────────────────────────────────────────────┤
│                    maxsplit PARAMETER                       │
├─────────────────────────────────────────────────────────────┤
│  "a b c".split(maxsplit=1) → ['a', 'b c']                  │
│  "a,b,c".split(',', 1)    → ['a', 'b,c']                   │
├─────────────────────────────────────────────────────────────┤
│                    .split() vs .rsplit()                    │
├─────────────────────────────────────────────────────────────┤
│  .split(maxsplit=2)  → ['a', 'b', 'c d'] (from left)       │
│  .rsplit(maxsplit=2) → ['a b', 'c', 'd'] (from right)      │
├─────────────────────────────────────────────────────────────┤
│                    BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────┤
│  ✅ Use .split() for whitespace splitting                   │
│  ✅ Use .split(',') for CSV data                           │
│  ✅ Use maxsplit for parsing first n parts                  │
│  ✅ Use .rsplit() to split from the end                     │
│  ⚠️ .split() always returns a list of strings              │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: .join() Method - Combining Strings from Lists
""")