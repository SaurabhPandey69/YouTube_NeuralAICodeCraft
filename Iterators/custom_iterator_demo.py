"""
Custom Iterator: Building from Scratch
NeuralAICodeCraft - Real-world Iterator Implementation
"""

print("=" * 60)
print("EXAMPLE 1: SQUARE NUMBERS ITERATOR")
print("=" * 60)

class SquareIterator:
    """Iterator that yields squares of numbers from 1 to n"""
    
    def __init__(self, n):
        self.n = n
        self.current = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

# Using SquareIterator
print("Squares of 1 to 5:")
for square in SquareIterator(5):
    print(f"  → {square}")

print("\n" + "=" * 60)
print("EXAMPLE 2: EVEN NUMBERS ITERATOR")
print("=" * 60)

class EvenNumbers:
    """Iterator that yields even numbers up to a limit"""
    
    def __init__(self, limit):
        self.limit = limit
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current += 2
        if self.current > self.limit:
            raise StopIteration
        return self.current

# Using EvenNumbers
print("Even numbers up to 20:")
for even in EvenNumbers(20):
    print(f"  → {even}")

print("\n" + "=" * 60)
print("EXAMPLE 3: FIBONACCI ITERATOR (INFINITE)")
print("=" * 60)

class FibonacciIterator:
    """Iterator that generates Fibonacci numbers (can be infinite)"""
    
    def __init__(self, max_count=None):
        self.max_count = max_count  # None = infinite
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Check limit if specified
        if self.max_count is not None and self.count >= self.max_count:
            raise StopIteration
        
        # Generate next Fibonacci number
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        
        result = self.a + self.b
        self.a, self.b = self.b, result
        self.count += 1
        return result

# First 10 Fibonacci numbers
print("First 10 Fibonacci numbers:")
for fib in FibonacciIterator(10):
    print(f"  → {fib}")

print("\n" + "=" * 60)
print("EXAMPLE 4: FILE READING ITERATOR (MEMORY EFFICIENT)")
print("=" * 60)

class LargeFileReader:
    """Reads large files line by line - NO memory overload"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        line = self.file.readline()
        if line == '':
            self.file.close()
            raise StopIteration
        return line.strip()

# Creating a sample file for demonstration
with open('sample_data.txt', 'w') as f:
    for i in range(1, 11):
        f.write(f"Line {i}: This is sample data\n")

print("Reading file line by line (memory efficient):")
for line in LargeFileReader('sample_data.txt'):
    print(f"  → {line}")

print("\n" + "=" * 60)
print("EXAMPLE 5: REVERSE ITERATOR")
print("=" * 60)

class ReverseIterator:
    """Iterates through a list in reverse order"""
    
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        result = self.data[self.index]
        self.index -= 1
        return result

# Using ReverseIterator
my_list = [10, 20, 30, 40, 50]
print(f"Original list: {my_list}")
print("Reverse iteration:")
for item in ReverseIterator(my_list):
    print(f"  → {item}")

print("\n" + "=" * 60)
print("REAL-WORLD USE CASE: API PAGINATION")
print("=" * 60)

class APIPageIterator:
    """Simulates paginated API responses (like Twitter, GitHub API)"""
    
    def __init__(self, total_items, page_size=5):
        self.total_items = total_items
        self.page_size = page_size
        self.current_page = 0
        self.current_index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current_index >= self.total_items:
            raise StopIteration
        
        # Simulate API call every 5 items
        if self.current_index % self.page_size == 0:
            self.current_page += 1
            print(f"  📡 Fetching page {self.current_page}...")
        
        result = f"Item {self.current_index + 1}"
        self.current_index += 1
        return result

print("Processing 12 items with page size 5:")
for item in APIPageIterator(12, page_size=5):
    print(f"  → {item}")

print("\n" + "=" * 60)
print("SUMMARY: WHEN TO USE ITERATORS")
print("=" * 60)

print("""
✅ USE ITERATORS WHEN:
├── Processing large datasets (files, databases)
├── Generating infinite sequences
├── Memory is limited
├── You need lazy evaluation
└── Building custom data pipelines

⚠️ AVOID ITERATORS WHEN:
├── You need random access (use lists)
├── You need to revisit elements (use lists)
├── You need to know the length upfront
└── The data set is small anyway
""")

print("\n✅ You now understand iterators and can build custom ones!")
