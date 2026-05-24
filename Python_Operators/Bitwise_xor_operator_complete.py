"""
XOR (^) OPERATOR IN PYTHON - COMPLETE GUIDE
NeuralAICodeCraft - Master Bitwise XOR with 5 Powerful Applications

Topics Covered:
1. XOR Basics (Truth Table, Binary Operations)
2. Properties of XOR
3. 5 Powerful XOR Applications
4. XOR vs Other Bitwise Operators
5. Practice Problems
"""

print("=" * 70)
print("🔢 XOR (^) OPERATOR IN PYTHON - COMPLETE GUIDE")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: XOR BASICS
# ============================================

print("\n📚 PART 1: XOR BASICS")
print("-" * 50)

print("""
WHAT IS XOR (Exclusive OR)?
├── Returns 1 if bits are DIFFERENT
└── Returns 0 if bits are SAME

XOR TRUTH TABLE:
┌─────┬─────┬───────┐
│  A  │  B  │ A ⊕ B │
├─────┼─────┼───────┤
│  0  │  0  │   0   │
│  0  │  1  │   1   │
│  1  │  0  │   1   │
│  1  │  1  │   0   │
└─────┴─────┴───────┘
""")

# 1.1 XOR with Single Bits
print("\n1.1 XOR with Single Bits:")
print("-" * 30)

print(f"  0 ^ 0 = {0 ^ 0}")
print(f"  0 ^ 1 = {0 ^ 1}")
print(f"  1 ^ 0 = {1 ^ 0}")
print(f"  1 ^ 1 = {1 ^ 1}")

# 1.2 XOR with Integers (Binary Representation)
print("\n1.2 XOR with Integers (Binary):")
print("-" * 30)

def print_xor_binary(a, b):
    """Display XOR operation with binary representation"""
    result = a ^ b
    print(f"  {a} ({bin(a)[2:]:>8})")
    print(f"  ^ {b} ({bin(b)[2:]:>8})")
    print(f"  {'-' * 12}")
    print(f"  = {result} ({bin(result)[2:]:>8})")
    print()

print("Example 1: 5 ^ 3")
print_xor_binary(5, 3)

print("Example 2: 12 ^ 9")
print_xor_binary(12, 9)

print("Example 3: 7 ^ 7")
print_xor_binary(7, 7)

print("Example 4: 10 ^ 0")
print_xor_binary(10, 0)

# 1.3 XOR Visualization
print("\n1.3 XOR Visualization:")
print("-" * 30)

def visualize_xor(a, b):
    """Visualize XOR operation bit by bit"""
    result = a ^ b
    print(f"  {a:3} = {bin(a)[2:].zfill(8)}")
    print(f"  ^ {b:3} = {bin(b)[2:].zfill(8)}")
    print(f"  {'-' * 12}")
    print(f"  = {result:3} = {bin(result)[2:].zfill(8)}")
    print("  Rules: 0⊕0=0, 0⊕1=1, 1⊕0=1, 1⊕1=0\n")

visualize_xor(5, 3)
visualize_xor(15, 10)

# ============================================
# PART 2: PROPERTIES OF XOR
# ============================================

print("\n🔧 PART 2: PROPERTIES OF XOR")
print("-" * 50)

print("""
PROPERTY 1: COMMUTATIVE (A ⊕ B = B ⊕ A)
PROPERTY 2: ASSOCIATIVE ((A ⊕ B) ⊕ C = A ⊕ (B ⊕ C))
PROPERTY 3: IDENTITY (A ⊕ 0 = A)
PROPERTY 4: SELF-INVERSE (A ⊕ A = 0)
""")

print("\n2.1 Demonstrating XOR Properties:")
print("-" * 30)

a, b, c = 5, 3, 7

# Commutative
print(f"  Commutative: {a} ^ {b} = {a ^ b}, {b} ^ {a} = {b ^ a}")
print(f"  ✓ {a} ^ {b} == {b} ^ {a}")

# Associative
print(f"  Associative: ({a} ^ {b}) ^ {c} = {(a ^ b) ^ c}")
print(f"  {a} ^ ({b} ^ {c}) = {a ^ (b ^ c)}")
print(f"  ✓ {(a ^ b) ^ c} == {a ^ (b ^ c)}")

# Identity
print(f"  Identity: {a} ^ 0 = {a ^ 0}")
print(f"  ✓ {a} ^ 0 == {a}")

# Self-inverse
print(f"  Self-inverse: {a} ^ {a} = {a ^ a}")
print(f"  ✓ {a} ^ {a} == 0")

# ============================================
# PART 3: APPLICATION 1 - FIND UNIQUE NUMBER
# ============================================

print("\n🎯 PART 3: APPLICATION 1 - FIND UNIQUE NUMBER")
print("-" * 50)

print("""
PROBLEM: In an array where every number appears twice except one, find the unique number.
SOLUTION: XOR all numbers together. Pairs cancel out (x ⊕ x = 0), leaving the unique number.
""")

def find_unique_number(arr):
    """Find the number that appears only once (all others appear twice)"""
    result = 0
    for num in arr:
        result ^= num
    return result

# Test cases
test_arrays = [
    [2, 3, 4, 2, 3],
    [1, 1, 2, 2, 3, 3, 4],
    [7, 5, 7, 9, 5],
    [42]
]

print("Finding unique numbers:")
for arr in test_arrays:
    unique = find_unique_number(arr)
    print(f"  {arr} → Unique: {unique}")

# Step-by-step demonstration
print("\n  Step-by-step: [2, 3, 4, 2, 3]")
steps = [2, 3, 4, 2, 3]
result = 0
for i, num in enumerate(steps):
    result ^= num
    print(f"    Step {i+1}: result ^ {num} = {result} (binary: {bin(result)[2:]})")
print(f"    Final unique number: {result}")

# ============================================
# PART 4: APPLICATION 2 - SWAP VARIABLES
# ============================================

print("\n🔄 PART 4: APPLICATION 2 - SWAP VARIABLES (No Temp Variable)")
print("-" * 50)

print("""
TRADITIONAL SWAP:
    temp = a
    a = b
    b = temp

XOR SWAP (No extra memory):
    a = a ^ b
    b = a ^ b
    a = a ^ b
""")

def xor_swap(a, b):
    """Swap two numbers using XOR (no temporary variable)"""
    print(f"  Before swap: a={a}, b={b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"  After swap:  a={a}, b={b}")
    return a, b

# Test XOR swap
print("\nXOR Swap Examples:")
xor_swap(10, 20)
xor_swap(7, 3)
xor_swap(100, 1)
xor_swap(0, 5)

# Step-by-step demonstration
print("\n  Step-by-step swap: a=5, b=3")
a, b = 5, 3
print(f"    Start: a={a} ({bin(a)[2:]}), b={b} ({bin(b)[2:]})")
a = a ^ b
print(f"    Step 1: a = a ^ b = {a} ({bin(a)[2:]})")
b = a ^ b
print(f"    Step 2: b = a ^ b = {b} ({bin(b)[2:]})")
a = a ^ b
print(f"    Step 3: a = a ^ b = {a} ({bin(a)[2:]})")
print(f"    Result: a={a}, b={b}")

# ============================================
# PART 5: APPLICATION 3 - FIND MISSING NUMBER
# ============================================

print("\n🔍 PART 5: APPLICATION 3 - FIND MISSING NUMBER")
print("-" * 50)

print("""
PROBLEM: Given an array containing n distinct numbers from 0 to n, find the missing one.
SOLUTION: XOR all numbers from 0 to n, then XOR with all array elements.
""")

def find_missing_number(arr, n):
    """Find missing number in array containing 0 to n"""
    xor_all = 0
    xor_arr = 0
    
    # XOR all numbers from 0 to n
    for i in range(n + 1):
        xor_all ^= i
    
    # XOR all numbers in array
    for num in arr:
        xor_arr ^= num
    
    # Missing number is xor_all ^ xor_arr
    return xor_all ^ xor_arr

# Test cases
test_cases = [
    ([0, 1, 2, 4], 4),      # Missing: 3
    ([1, 2, 3, 4], 4),      # Missing: 0
    ([0, 1, 3, 4], 4),      # Missing: 2
    ([0, 1, 2, 3, 5], 5),   # Missing: 4
]

print("Finding missing numbers:")
for arr, n in test_cases:
    missing = find_missing_number(arr, n)
    print(f"  Array: {arr}, n={n} → Missing: {missing}")

# Step-by-step demonstration
print("\n  Step-by-step: arr=[0,1,2,4], n=4 (missing 3)")
arr = [0, 1, 2, 4]
n = 4

xor_all = 0
for i in range(n + 1):
    xor_all ^= i
print(f"    XOR 0→4: {xor_all}")

xor_arr = 0
for num in arr:
    xor_arr ^= num
print(f"    XOR array: {xor_arr}")

missing = xor_all ^ xor_arr
print(f"    Missing number: {xor_all} ^ {xor_arr} = {missing}")

# ============================================
# PART 6: APPLICATION 4 - SIMPLE XOR CIPHER
# ============================================

print("\n🔐 PART 6: APPLICATION 4 - SIMPLE XOR CIPHER (Encryption)")
print("-" * 50)

print("""
XOR ENCRYPTION:
- Encrypt: ciphertext = plaintext ^ key
- Decrypt: plaintext = ciphertext ^ key
- Same operation for encryption and decryption!
""")

def xor_encrypt_decrypt(text, key):
    """Simple XOR encryption/decryption"""
    result = []
    for char in text:
        result.append(chr(ord(char) ^ key))
    return ''.join(result)

def xor_encrypt_decrypt_bytes(data, key):
    """XOR encryption/decryption for bytes"""
    return bytes([b ^ key for b in data])

# String example
print("\nString Encryption Example:")
message = "Hello World!"
key = 42

encrypted = xor_encrypt_decrypt(message, key)
decrypted = xor_encrypt_decrypt(encrypted, key)

print(f"  Original: {message}")
print(f"  Key: {key}")
print(f"  Encrypted: {encrypted}")
print(f"  Decrypted: {decrypted}")
print(f"  ✓ Successfully encrypted and decrypted!")

# Bytes example
print("\nBytes Encryption Example:")
data = b"Python XOR Cipher"
key = 99

encrypted_bytes = xor_encrypt_decrypt_bytes(data, key)
decrypted_bytes = xor_encrypt_decrypt_bytes(encrypted_bytes, key)

print(f"  Original: {data}")
print(f"  Encrypted: {encrypted_bytes}")
print(f"  Decrypted: {decrypted_bytes}")
print(f"  ✓ Bytes encrypted and decrypted!")

# Character-by-character demonstration
print("\n  Character-by-character encryption of 'A' with key=1:")
char = 'A'
key = 1
print(f"    '{char}' ASCII: {ord(char)}")
print(f"    Binary: {bin(ord(char))}")
print(f"    XOR with {key}: {ord(char) ^ key}")
print(f"    Result char: '{chr(ord(char) ^ key)}'")

# ============================================
# PART 7: APPLICATION 5 - PARITY CHECK
# ============================================

print("\n🔢 PART 7: APPLICATION 5 - PARITY CHECK")
print("-" * 50)

print("""
PARITY CHECK:
- Even parity: XOR of all bits = 0
- Odd parity: XOR of all bits = 1
- Used in error detection
""")

def parity_check(num):
    """Check if number has even or odd number of 1 bits"""
    # XOR all bits by shifting
    result = num
    result ^= result >> 16
    result ^= result >> 8
    result ^= result >> 4
    result ^= result >> 2
    result ^= result >> 1
    return result & 1

def simple_parity(num):
    """Simple parity check by counting bits"""
    return bin(num).count('1') % 2

print("Parity Examples:")
test_numbers = [0, 1, 2, 3, 4, 5, 7, 8, 15, 16]

for num in test_numbers:
    binary = bin(num)[2:]
    parity = simple_parity(num)
    parity_type = "Odd" if parity else "Even"
    print(f"  {num:2} ({binary:>8}) → {parity_type} parity ({parity})")

# XOR parity for error detection
print("\n  Simple Error Detection using Parity:")
data_bits = [1, 0, 1, 1, 0, 1, 0]  # 7 data bits
parity_bit = simple_parity(sum(data_bits))

print(f"    Data bits: {data_bits}")
print(f"    Calculated parity bit: {parity_bit}")
print(f"    Transmitted: {data_bits} + [parity={parity_bit}]")

# Simulate error
data_bits_corrupted = data_bits.copy()
data_bits_corrupted[2] = 1 - data_bits_corrupted[2]  # Flip a bit
received_parity = simple_parity(sum(data_bits_corrupted))

print(f"\n    Received data: {data_bits_corrupted}")
print(f"    Received parity: {received_parity}")
print(f"    Expected parity: {parity_bit}")
print(f"    Error detected? {received_parity != parity_bit}")

# ============================================
# PART 8: XOR VS OTHER BITWISE OPERATORS
# ============================================

print("\n⚡ PART 8: XOR VS OTHER BITWISE OPERATORS")
print("-" * 50)

a, b = 5, 3  # 5=0101, 3=0011

print(f"  a = {a} ({bin(a)[2:].zfill(4)}), b = {b} ({bin(b)[2:].zfill(4)})")
print("-" * 50)
print(f"  AND  (a & b)  = {a & b} ({bin(a & b)[2:].zfill(4)})  → Both bits must be 1")
print(f"  OR   (a | b)  = {a | b} ({bin(a | b)[2:].zfill(4)})  → At least one bit is 1")
print(f"  XOR  (a ^ b)  = {a ^ b} ({bin(a ^ b)[2:].zfill(4)})  → Bits are DIFFERENT")
print(f"  NOT  (~a)     = {~a & 0b1111} ({bin(~a & 0b1111)[2:].zfill(4)})  → Flip all bits")
print(f"  LEFT SHIFT  (a << 1) = {a << 1} ({bin(a << 1)[2:]})")
print(f"  RIGHT SHIFT (a >> 1) = {a >> 1} ({bin(a >> 1)[2:]})")

print("\n  When to use XOR?")
print("  ├── Finding unique elements (pairs cancel out)")
print("  ├── Swapping without temporary variable")
print("  ├── Simple encryption/decryption")
print("  ├── Finding missing numbers")
print("  ├── Parity checking")
print("  └── Toggling bits (x ^ 1 flips the last bit)")

# ============================================
# PART 9: XOR TIPS & TRICKS
# ============================================

print("\n💡 PART 9: XOR TIPS & TRICKS")
print("-" * 50)

# Trick 1: Toggle bits
print("\n9.1 Toggling Bits with XOR:")
print("-" * 30)

num = 5  # 0101
print(f"  Original: {num} ({bin(num)[2:].zfill(4)})")
print(f"  Toggle last bit (^1): {num ^ 1} ({bin(num ^ 1)[2:].zfill(4)})")
print(f"  Toggle again: {(num ^ 1) ^ 1} ({bin((num ^ 1) ^ 1)[2:].zfill(4)})")

# Trick 2: Check if two numbers have opposite signs
print("\n9.2 Check Opposite Signs:")
print("-" * 30)

def opposite_signs(x, y):
    """Check if two numbers have opposite signs using XOR"""
    return (x ^ y) < 0

test_pairs = [(5, 3), (-5, 3), (5, -3), (-5, -3)]
for x, y in test_pairs:
    result = opposite_signs(x, y)
    print(f"  {x} and {y} have opposite signs? {result}")

# Trick 3: XOR of numbers from 1 to n
print("\n9.3 XOR of 1 to n (Pattern):")
print("-" * 30)

def xor_1_to_n(n):
    """Efficient XOR of numbers from 1 to n"""
    if n % 4 == 0:
        return n
    elif n % 4 == 1:
        return 1
    elif n % 4 == 2:
        return n + 1
    else:
        return 0

print("  XOR from 1 to n pattern:")
for n in range(1, 11):
    xor_result = xor_1_to_n(n)
    print(f"    XOR(1 to {n}) = {xor_result}")

# Trick 4: Find the only number that appears odd number of times
print("\n9.4 Find Number with Odd Frequency:")
print("-" * 30)

arr = [1, 2, 3, 2, 1, 3, 4, 4, 5]  # 5 appears once (odd)
result = find_unique_number(arr)  # This works for odd frequency!
print(f"  Array: {arr}")
print(f"  Number with odd frequency: {result}")

# ============================================
# PART 10: PRACTICE PROBLEMS
# ============================================

print("\n📝 PART 10: PRACTICE PROBLEMS")
print("-" * 50)

print("""
🎯 PROBLEM 1: Two Unique Numbers
In an array where every number appears twice except two numbers, find both unique numbers.

🎯 PROBLEM 2: XOR of All Subarrays
Find the XOR of all subarrays of an array.

🎯 PROBLEM 3: Maximum XOR of Two Numbers
Find the maximum XOR of any two numbers in an array.

🎯 PROBLEM 4: Missing Two Numbers
Find two missing numbers in array containing 1 to n.

🎯 PROBLEM 5: XOR Query
Given an array and queries, find XOR in given ranges.
""")

# Solutions
print("\n💡 SOLUTION 1: Two Unique Numbers")
print("-" * 30)

def find_two_unique(arr):
    """Find two numbers that appear once (all others appear twice)"""
    # XOR all numbers to get XOR of the two unique numbers
    xor_all = 0
    for num in arr:
        xor_all ^= num
    
    # Find rightmost set bit
    rightmost_bit = xor_all & -xor_all
    
    # Divide numbers into two groups
    num1, num2 = 0, 0
    for num in arr:
        if num & rightmost_bit:
            num1 ^= num
        else:
            num2 ^= num
    
    return num1, num2

test_arr = [1, 2, 3, 2, 1, 4, 5, 5]  # 3 and 4 are unique
unique1, unique2 = find_two_unique(test_arr)
print(f"  Array: {test_arr}")
print(f"  Two unique numbers: {unique1}, {unique2}")

print("\n💡 SOLUTION 2: XOR of All Subarrays")
print("-" * 30)

def xor_of_all_subarrays(arr):
    """Find XOR of all subarrays"""
    result = 0
    n = len(arr)
    for i in range(n):
        # Count how many subarrays include arr[i]
        count = (i + 1) * (n - i)
        if count % 2:  # If odd, include in result
            result ^= arr[i]
    return result

arr = [1, 2, 3]
print(f"  Array: {arr}")
print(f"  XOR of all subarrays: {xor_of_all_subarrays(arr)}")
print("  Subarrays: [1], [2], [3], [1,2], [2,3], [1,2,3]")

print("\n💡 SOLUTION 3: Maximum XOR of Two Numbers")
print("-" * 30)

def find_maximum_xor(arr):
    """Find maximum XOR of any two numbers in array"""
    max_xor = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_xor = max(max_xor, arr[i] ^ arr[j])
    return max_xor

arr = [3, 10, 5, 25, 2, 8]
print(f"  Array: {arr}")
print(f"  Maximum XOR: {find_maximum_xor(arr)}")
print("  Explanation: 5 ^ 25 = 28")

# ============================================
# PART 11: SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ XOR OPERATOR MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│                    XOR TRUTH TABLE                          │
├─────────────────────────────────────────────────────────────┤
│   0 ^ 0 = 0  │  Same bits → 0                              │
│   0 ^ 1 = 1  │  Different bits → 1                         │
│   1 ^ 0 = 1  │                                             │
│   1 ^ 1 = 0  │                                             │
├─────────────────────────────────────────────────────────────┤
│                    XOR PROPERTIES                           │
├─────────────────────────────────────────────────────────────┤
│   A ^ A = 0           (Self-inverse)                       │
│   A ^ 0 = A           (Identity)                           │
│   A ^ B = B ^ A       (Commutative)                        │
│   (A ^ B) ^ C = A ^ (B ^ C)  (Associative)                 │
├─────────────────────────────────────────────────────────────┤
│                    5 POWERFUL USES                          │
├─────────────────────────────────────────────────────────────┤
│   1. Find unique number in pairs                           │
│   2. Swap variables (no temp)                              │
│   3. Find missing number in sequence                       │
│   4. Simple encryption/decryption                          │
│   5. Parity check & error detection                        │
├─────────────────────────────────────────────────────────────┤
│                    TIPS & TRICKS                            │
├─────────────────────────────────────────────────────────────┤
│   x ^ 1 = Toggle last bit                                   │
│   (x ^ y) < 0 = Opposite signs check                        │
│   x ^ x = 0 (Useful for finding duplicates)                 │
│   xor_1_to_n(n) = [n, 1, n+1, 0][n%4]                     │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: More Bitwise Operators (AND, OR, NOT, Shifts)
""")

# ============================================
# BONUS: Interactive XOR Tool
# ============================================

print("\n🎮 BONUS: Interactive XOR Tool")
print("-" * 50)

def xor_tool():
    """Interactive XOR calculator for practice"""
    print("\n  XOR Interactive Tool (type 'exit' to quit)")
    while True:
        user_input = input("\n  Enter two numbers (a b): ").strip()
        if user_input.lower() == 'exit':
            print("  Goodbye!")
            break
        
        try:
            a, b = map(int, user_input.split())
            result = a ^ b
            print(f"  {a} ^ {b} = {result}")
            print(f"  Binary: {bin(a)[2:]} ^ {bin(b)[2:]} = {bin(result)[2:]}")
        except ValueError:
            print("  Please enter two numbers separated by space")

# Uncomment to run interactive tool
# xor_tool()