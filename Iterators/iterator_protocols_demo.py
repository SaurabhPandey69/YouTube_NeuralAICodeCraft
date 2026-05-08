"""
Iterator Protocols: __iter__() and __next__()
NeuralAICodeCraft - Understanding the Two Protocols
"""

print("=" * 60)
print("THE TWO ITERATOR PROTOCOLS")
print("=" * 60)

print("""
PROTOCOL 1: __iter__()
├── Returns the iterator object itself
├── Called when you do iter(iterable)
└── Required for any iterable

PROTOCOL 2: __next__()
├── Returns the next value in sequence
├── Called when you do next(iterator)
├── Raises StopIteration when done
└── Required for any iterator
""")

print("\n" + "=" * 60)
print("MANUAL ITERATION WITH PROTOCOLS")
print("=" * 60)

class ManualIterator:
    """Demonstrating the two protocols manually"""
    
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        """Protocol 1: Returns the iterator"""
        print("  → __iter__() called")
        return self
    
    def __next__(self):
        """Protocol 2: Returns next value"""
        print("  → __next__() called")
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result

# Using our manual iterator
my_iterable = ManualIterator([1, 2, 3])

print("Converting to iterator:")
iterator = iter(my_iterable)  # Calls __iter__()

print("\nGetting elements:")
print(next(iterator))  # Calls __next__()
print(next(iterator))
print(next(iterator))

print("\n" + "=" * 60)
print("WHY BOTH PROTOCOLS?")
print("=" * 60)

print("""
An ITERABLE must have __iter__()
An ITERATOR must have BOTH __iter__() AND __next__()

This design allows:
1. Clean separation between data structure and iteration logic
2. Multiple independent iterators on same data
3. Lazy evaluation (compute only when needed)
4. Memory efficiency (no need to store all values)
""")

print("\n" + "=" * 60)
print("MULTIPLE ITERATORS ON SAME DATA")
print("=" * 60)

my_list = [1, 2, 3, 4, 5]

# Create two independent iterators
iter1 = iter(my_list)
iter2 = iter(my_list)

print("Iterator 1:", next(iter1))  # 1
print("Iterator 2:", next(iter2))  # 1 (different iterator!)
print("Iterator 1:", next(iter1))  # 2
print("Iterator 2:", next(iter2))  # 2