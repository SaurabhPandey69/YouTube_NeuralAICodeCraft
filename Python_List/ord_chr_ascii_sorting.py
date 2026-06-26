"""
ord() & chr() FUNCTIONS: ASCII & UNICODE GUIDE
NeuralAICodeCraft - Master Character Encoding and Sorting

Topics Covered:
1. ASCII Basics
2. ord() Function
3. chr() Function
4. ASCII Table Reference
5. Sorting with ord()
6. Case-Insensitive Sorting
7. Custom Sort Orders
"""

print("=" * 70)
print("🐍 ord() & chr() FUNCTIONS - ASCII & UNICODE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: ASCII BASICS
# ============================================

print("\n📚 PART 1: ASCII BASICS")
print("-" * 50)

print("""
ASCII = American Standard Code for Information Interchange

WHY ASCII?
├── Computers only understand numbers (0s and 1s)
├── Each character needs a numeric representation
├── ASCII defines standard codes for characters
└── ASCII is a subset of Unicode (first 128 characters)

ASCII RANGES:
├── 0-31: Control characters (non-printable)
├── 32: Space
├── 48-57: Digits (0-9)
├── 65-90: Uppercase letters (A-Z)
├── 97-122: Lowercase letters (a-z)
└── 128-255: Extended ASCII (different per encoding)
""")

# ============================================
# PART 2: ord() FUNCTION
# ============================================

print("\n🔢 PART 2: ord() FUNCTION")
print("-" * 50)

print("""
SYNTAX: ord(character)

WHAT IT DOES:
- Returns the Unicode code point (integer) for a character
- Works for ANY character (ASCII and Unicode)
- Raises TypeError if given more than one character
""")

# 2.1 Basic Usage
print("\n2.1 Basic Usage:")
print("-" * 30)

print(f"ord('A') → {ord('A')}")   # 65
print(f"ord('B') → {ord('B')}")   # 66
print(f"ord('a') → {ord('a')}")   # 97
print(f"ord('0') → {ord('0')}")   # 48
print(f"ord(' ') → {ord(' ')}")   # 32 (space)
print(f"ord('!') → {ord('!')}")   # 33

# 2.2 Unicode Support
print("\n2.2 Unicode Support:")
print("-" * 30)

print(f"ord('€') → {ord('€')}")   # 8364 (Euro sign)
print(f"ord('©') → {ord('©')}")   # 169 (Copyright)
print(f"ord('😊') → {ord('😊')}")   # 128522 (Emoji)
print(f"ord('₹') → {ord('₹')}")   # 8377 (Indian Rupee)

# 2.3 ord() with Single Character Only
print("\n2.3 ord() with Single Character Only:")
print("-" * 30)

try:
    ord('AB')  # Multiple characters will raise TypeError
except TypeError as e:
    print(f"❌ ord('AB') → Error: {e}")

# 2.4 ASCII Codes for All Letters
print("\n2.4 ASCII Values for Letters:")
print("-" * 30)

print("Uppercase letters:")
for i in range(65, 91):
    print(f"  {chr(i)} = {i}", end=", ")
print("\n")

print("Lowercase letters:")
for i in range(97, 123):
    print(f"  {chr(i)} = {i}", end=", ")
print("\n")

# ============================================
# PART 3: chr() FUNCTION
# ============================================

print("\n🔤 PART 3: chr() FUNCTION")
print("-" * 50)

print("""
SYNTAX: chr(integer)

WHAT IT DOES:
- Returns character from Unicode code point (integer)
- Inverse of ord()
- Raises ValueError if integer out of range
""")

# 3.1 Basic Usage
print("\n3.1 Basic Usage:")
print("-" * 30)

print(f"chr(65) → '{chr(65)}'")   # 'A'
print(f"chr(66) → '{chr(66)}'")   # 'B'
print(f"chr(97) → '{chr(97)}'")   # 'a'
print(f"chr(48) → '{chr(48)}'")   # '0'
print(f"chr(32) → '{chr(32)}'")   # ' ' (space)

# 3.2 Extended ASCII and Unicode
print("\n3.2 Extended ASCII and Unicode:")
print("-" * 30)

print(f"chr(8364) → '{chr(8364)}'")  # € (Euro)
print(f"chr(169) → '{chr(169)}'")   # © (Copyright)
print(f"chr(128522) → '{chr(128522)}'")  # 😊 (Emoji)
print(f"chr(8377) → '{chr(8377)}'")   # ₹ (Rupee)

# 3.3 chr() with Multiple Characters
print("\n3.3 Building Strings with chr():")
print("-" * 30)

# Build "Hello" using ASCII codes
hello_codes = [72, 101, 108, 108, 111]
hello = ''.join([chr(code) for code in hello_codes])
print(f"hello = {hello}")

# Build "Python"
python_codes = [80, 121, 116, 104, 111, 110]
python = ''.join([chr(code) for code in python_codes])
print(f"python = {python}")

# 3.4 ASCII Art Generation
print("\n3.4 Simple ASCII Art Generation:")
print("-" * 30)

# Create a simple heart
heart = chr(3)  # ASCII heart symbol (in some terminals)
print(f"  Heart: {heart}")

# Create a smiley face
smiley = chr(1)  # ASCII smiley (in some terminals)
print(f"  Smiley: {smiley}")

# Create Unicode star
star = chr(9733)  # Unicode star
print(f"  Star: {star}")

print("  Simple banner:")
print("  " + chr(9556) + chr(9552) * 20 + chr(9559))
print("  " + chr(9553) + "  ASCII DEMO  " + chr(9553))
print("  " + chr(9562) + chr(9552) * 20 + chr(9565))

# ============================================
# PART 4: ASCII TABLE REFERENCE
# ============================================

print("\n📊 PART 4: ASCII TABLE REFERENCE")
print("-" * 50)

print("""
┌─────────┬─────────┬──────────┬─────────┬──────────┬─────────┐
│  Dec    │  Char   │  Dec     │  Char   │  Dec     │  Char   │
├─────────┼─────────┼──────────┼─────────┼──────────┼─────────┤
│  32     │  Space  │   48-57  │  0-9    │   65-90  │  A-Z    │
│  33     │  !      │   58     │  :      │   91     │  [      │
│  34     │  "      │   59     │  ;      │   92     │  \      │
│  35     │  #      │   60     │  <      │   93     │  ]      │
│  36     │  $      │   61     │  =      │   94     │  ^      │
│  37     │  %      │   62     │  >      │   95     │  _      │
│  38     │  &      │   63     │  ?      │   96     │  `      │
│  39     │  '      │   64     │  @      │   97-122 │  a-z    │
│  40     │  (      │   65-90  │  A-Z    │   123    │  {      │
│  41     │  )      │   91-96  │  [\]^_` │   124    │  |      │
│  42     │  *      │   97-122 │  a-z    │   125    │  }      │
│  43     │  +      │   123-126│  {}|~   │   126    │  ~      │
│  44     │  ,      │         │         │          │         │
│  45     │  -      │         │         │          │         │
│  46     │  .      │         │         │          │         │
│  47     │  /      │         │         │          │         │
└─────────┴─────────┴──────────┴─────────┴──────────┴─────────┘
""")

# 4.1 Printable ASCII Characters
print("\n4.1 Printable ASCII Characters (33-126):")
print("-" * 30)

ascii_chars = []
for i in range(33, 127):
    ascii_chars.append(chr(i))

print("  " + " ".join(ascii_chars))
print(f"  Total printable ASCII characters: {len(ascii_chars)}")

# 4.2 ASCII Table as Dictionary
print("\n4.2 ASCII Table (Selected):")
print("-" * 30)

selected_chars = ['A', 'B', 'C', 'Z', 'a', 'b', 'c', 'z', '0', '1', '9', '!', '@', '#', '$', ' ']

print("  Character → ASCII Code")
print("  " + "-" * 25)
for char in selected_chars:
    print(f"  '{char}' → {ord(char)}")

# ============================================
# PART 5: SORTING WITH ord()
# ============================================

print("\n🔧 PART 5: SORTING WITH ord() KEY")
print("-" * 50)

# 5.1 Basic Sorting with ord()
print("\n5.1 Sorting Characters by ASCII Value:")
print("-" * 30)

chars = ['b', 'A', 'd', 'C', 'a', 'B']
print(f"Original: {chars}")

# Sort by ASCII value (default)
chars.sort()
print(f"sort() default: {chars}")

# Sort using ord (same result for characters)
chars2 = ['b', 'A', 'd', 'C', 'a', 'B']
chars2.sort(key=ord)
print(f"sort(key=ord): {chars2}")

print("  ✅ For single characters, sort() and sort(key=ord) do the same thing!")

# 5.2 Sorting by ASCII Values of First Character
print("\n5.2 Sorting by ASCII Value of First Character:")
print("-" * 30)

words = ['banana', 'Apple', 'cherry', 'Date', 'apple', 'Banana']
print(f"Original: {words}")

# Default sort (case-sensitive)
words_sorted = sorted(words)
print(f"Default sort: {words_sorted}")

# Sort by ASCII of first character
words_sorted_ascii = sorted(words, key=lambda x: ord(x[0]) if x else 0)
print(f"Sort by first char ASCII: {words_sorted_ascii}")

# 5.3 Sorting by Sum of ASCII Values
print("\n5.3 Sorting by Sum of ASCII Values:")
print("-" * 30)

words = ['cat', 'dog', 'elephant', 'bat', 'ant']
print(f"Original: {words}")

# Calculate sum of ASCII values
def ascii_sum(word):
    return sum(ord(c) for c in word)

print("  ASCII sums:")
for word in words:
    print(f"    '{word}': {ascii_sum(word)}")

# Sort by sum of ASCII values
words.sort(key=ascii_sum)
print(f"\nSort by ASCII sum: {words}")

# 5.4 Custom Sort Order with ord()
print("\n5.4 Custom Sort Order (Vowels First):")
print("-" * 30)

def vowel_first(char):
    """Custom key: vowels first, then consonants"""
    vowels = 'aeiouAEIOU'
    if char in vowels:
        return 0, char  # Vowels first (0)
    else:
        return 1, char  # Consonants after (1)

letters = ['c', 'a', 'e', 'b', 'i', 'd', 'o']
print(f"Original: {letters}")
letters.sort(key=vowel_first)
print(f"Vowels first: {letters}")

# ============================================
# PART 6: CASE-INSENSITIVE SORTING
# ============================================

print("\n🔤 PART 6: CASE-INSENSITIVE SORTING")
print("-" * 50)

print("""
Case-Insensitive Sorting Options:
1. key=str.lower → Convert to lowercase for comparison
2. key=lambda x: x.lower() → Same as above
3. key=str.casefold → More aggressive (handles Unicode)
""")

# 6.1 Case-Insensitive Sort
print("\n6.1 Case-Insensitive Sort:")
print("-" * 30)

words = ['banana', 'Apple', 'cherry', 'Date', 'apple', 'Banana']
print(f"Original: {words}")

# Default sort (case-sensitive)
words_default = sorted(words)
print(f"Default sort: {words_default}")

# Case-insensitive sort
words_insensitive = sorted(words, key=str.lower)
print(f"Case-insensitive: {words_insensitive}")

# 6.2 ASCII vs Case-Insensitive Comparison
print("\n6.2 ASCII vs Case-Insensitive Comparison:")
print("-" * 30)

# Show ASCII values
print("  ASCII values:")
for char in ['A', 'a', 'B', 'b']:
    print(f"    '{char}': {ord(char)}")

# Sorting with key=ord
sorted_ascii = sorted(['A', 'a', 'B', 'b'], key=ord)
print(f"  sort(key=ord): {sorted_ascii}")

# Sorting with key=str.lower
sorted_ignore_case = sorted(['A', 'a', 'B', 'b'], key=str.lower)
print(f"  sort(key=str.lower): {sorted_ignore_case}")

# 6.3 Case-Insensitive with Custom Order
print("\n6.3 Case-Insensitive Sort with Reverse:")
print("-" * 30)

words = ['banana', 'Apple', 'cherry', 'Date', 'apple', 'Banana']
print(f"Original: {words}")

# Case-insensitive descending
sorted_desc = sorted(words, key=str.lower, reverse=True)
print(f"Case-insensitive descending: {sorted_desc}")

# ============================================
# PART 7: PRACTICAL APPLICATIONS
# ============================================

print("\n🚀 PART 7: PRACTICAL APPLICATIONS")
print("-" * 30)

# 7.1 Password Strength Checker
print("\n7.1 Password Strength Checker (Using ASCII):")
print("-" * 30)

def check_password_strength(password):
    """Check password strength using ASCII ranges"""
    has_upper = any('A' <= c <= 'Z' for c in password)
    has_lower = any('a' <= c <= 'z' for c in password)
    has_digit = any('0' <= c <= '9' for c in password)
    has_symbol = any(33 <= ord(c) <= 47 or 58 <= ord(c) <= 64 for c in password)
    
    length_score = min(len(password) // 4, 5)
    complexity_score = sum([has_upper, has_lower, has_digit, has_symbol])
    
    total_score = length_score + complexity_score
    
    if total_score >= 7:
        return "STRONG 🔒"
    elif total_score >= 5:
        return "MEDIUM 🔐"
    else:
        return "WEAK 🔓"

test_passwords = ['pass', 'Password123', 'P@ssw0rd!', '123456']
for pwd in test_passwords:
    print(f"  '{pwd}': {check_password_strength(pwd)}")

# 7.2 Caesar Cipher (Simple Encryption)
print("\n7.2 Caesar Cipher using ord() and chr():")
print("-" * 30)

def caesar_cipher(text, shift):
    """Simple Caesar cipher using ord() and chr()"""
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

message = "Hello World"
encrypted = caesar_cipher(message, 3)
decrypted = caesar_cipher(encrypted, -3)

print(f"Original: {message}")
print(f"Encrypted (shift=3): {encrypted}")
print(f"Decrypted: {decrypted}")

# 7.3 ASCII Art Banner
print("\n7.3 ASCII Art Banner Generator:")
print("-" * 30)

def ascii_banner(text, char='#'):
    """Generate a simple ASCII banner"""
    border = char * (len(text) + 4)
    return f"{border}\n{char} {text} {char}\n{border}"

print(ascii_banner("NeuralAICodeCraft", '*'))

# ============================================
# PART 8: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 8: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Find ASCII Values
Find and print ASCII values for all characters in your name.

🎯 EXERCISE 2: Build a String
Build the string "Python" using chr() with ASCII codes.

🎯 EXERCISE 3: Sort with ord
Sort ['c', 'A', 'b', 'D'] using ord as key.

🎯 EXERCISE 4: Case-Insensitive Sort
Sort ['banana', 'Apple', 'cherry'] ignoring case.

🎯 EXERCISE 5: Custom Sort Order
Create a sort that puts digits before letters.

🎯 CHALLENGE: ROT13 Cipher
Implement ROT13 (shift by 13) using ord() and chr().
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1
print("\nEx1 - ASCII Values:")
name = "Python"
print(f"  Name: {name}")
for char in name:
    print(f"    '{char}' → {ord(char)}")

# Exercise 2
print("\nEx2 - Build String:")
codes = [80, 121, 116, 104, 111, 110]
built = ''.join([chr(code) for code in codes])
print(f"  Built: {built}")

# Exercise 3
print("\nEx3 - Sort with ord:")
lst = ['c', 'A', 'b', 'D']
print(f"  Original: {lst}")
lst.sort(key=ord)
print(f"  Sorted (key=ord): {lst}")

# Exercise 4
print("\nEx4 - Case-Insensitive Sort:")
words = ['banana', 'Apple', 'cherry']
print(f"  Original: {words}")
print(f"  Case-insensitive: {sorted(words, key=str.lower)}")

# Exercise 5
print("\nEx5 - Digits Before Letters:")
def digits_first(char):
    if '0' <= char <= '9':
        return 0, char  # Digits first
    elif 'A' <= char <= 'Z' or 'a' <= char <= 'z':
        return 1, char  # Letters after
    else:
        return 2, char  # Others last

chars = ['c', '5', 'A', '3', 'b', '1']
chars.sort(key=digits_first)
print(f"  Sorted (digits first): {chars}")

# Challenge
print("\nChallenge - ROT13 Cipher:")
def rot13(text):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':
            result += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif 'a' <= char <= 'z':
            result += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
        else:
            result += char
    return result

msg = "Hello World"
encoded = rot13(msg)
decoded = rot13(encoded)
print(f"  Original: {msg}")
print(f"  ROT13: {encoded}")
print(f"  Decoded: {decoded}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ ord() & chr() FUNCTIONS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    ASCII/UNICODE                            │
├─────────────────────────────────────────────────────────────┤
│  ASCII = American Standard Code for Information Interchange │
│  Unicode = Superset of ASCII (covers all characters)       │
├─────────────────────────────────────────────────────────────┤
│                    KEY FUNCTIONS                            │
├─────────────────────────────────────────────────────────────┤
│  ord(char)       → Returns Unicode code point (int)        │
│  chr(int)        → Returns character from code point       │
├─────────────────────────────────────────────────────────────┤
│                    IMPORTANT ASCII RANGES                   │
├─────────────────────────────────────────────────────────────┤
│  48-57  → 0-9 (digits)                                    │
│  65-90  → A-Z (uppercase)                                 │
│  97-122 → a-z (lowercase)                                 │
│  32     → Space                                            │
│  33-47  → !"#$%&'()*+,-./                                 │
├─────────────────────────────────────────────────────────────┤
│                    SORTING WITH ord()                       │
├─────────────────────────────────────────────────────────────┤
│  sort(key=ord)     → Sort by ASCII value                   │
│  sort(key=str.lower) → Case-insensitive sort              │
│  sort(key=lambda x: ord(x[0])) → Sort by first char       │
│  sort(key=lambda x: sum(ord(c) for c in x)) → Sort by sum │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: More Advanced Sorting Techniques
""")