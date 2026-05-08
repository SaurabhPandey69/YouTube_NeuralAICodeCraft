"""
ADVANCED ITERATOR PROBLEMS
NeuralAICodeCraft - Test Your Skills
"""

print("=" * 60)
print("ADVANCED PROBLEMS (⭐⭐⭐)")
print("=" * 60)

print("\n" + "=" * 40)
print("PROBLEM 8: Chain Two Iterators")
print("=" * 40)
"""
PROBLEM:
Create a function chain_iterators(it1, it2) that combines two iterators.
It should yield all elements from first, then all from second.

Your code here:
"""

def chain_iterators(it1, it2):
    """Combine two iterators into one sequence"""
    # Yield all from first iterator
    for item in it1:
        yield item
    # Then yield all from second
    for item in it2:
        yield item

# SOLUTION 8
print("\n--- SOLUTION 8 ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = chain_iterators(iter(list1), iter(list2))
print("Chained iterators:")
for item in combined:
    print(f"  → {item}")

print("\n" + "=" * 40)
print("PROBLEM 9: Even Numbers Iterator")
print("=" * 40)
"""
PROBLEM:
Create a custom iterator class EvenNumbers that yields even numbers 
from 2 up to a given limit.

Your code here:
"""

class EvenNumbers:
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

# SOLUTION 9
print("\n--- SOLUTION 9 ---")
print("Even numbers up to 20:")
for even in EvenNumbers(20):
    print(f"  → {even}")

print("\n" + "=" * 40)
print("PROBLEM 10: Cyclic Iterator")
print("=" * 40)
"""
PROBLEM:
Create a CyclicIterator class that infinitely cycles through a list.
It should never raise StopIteration.
Example: CyclicIterator([1,2,3]) → 1,2,3,1,2,3,1,2,3...

Your code here:
"""

class CyclicIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data[self.index]
        self.index = (self.index + 1) % len(self.data)
        return result

# SOLUTION 10
print("\n--- SOLUTION 10 ---")
print("Cyclic iterator (first 10 values):")
cycle = CyclicIterator([1, 2, 3])
for _ in range(10):
    print(f"  → {next(cycle)}")

print("\n✅ Advanced problems complete! Move to bonus challenge.")