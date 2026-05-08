# 03_Iterators - Python Iterables & Iterators

## 📚 Topics Covered

1. **Iterables vs Iterators** - What's the difference?
2. **iter() & next() Functions** - Converting and accessing
3. **__iter__() & __next__() Protocols** - The magic behind loops
4. **Custom Iterators** - Building your own from scratch
5. **Memory Efficiency** - Why iterators save RAM

## 🚀 Files in This Folder

| File | Description |
|------|-------------|
| `iterables_demo.py` | Basic iterables, iter(), next(), StopIteration |
| `iterator_protocols_demo.py` | Deep dive into __iter__ and __next__ protocols |
| `custom_iterator_demo.py` | 5 custom iterator examples with real use cases |

## 🎯 Run the Code

```bash
python iterables_demo.py
python iterator_protocols_demo.py
python custom_iterator_demo.py
💡 Key Takeaways
Iterable: An object that can return an iterator (has __iter__)

Iterator: An object that produces values one at a time (has __iter__ AND __next__)

iter(): Converts iterable → iterator

next(): Gets next value from iterator

StopIteration: Signal that iterator is exhausted

🏗️ Custom Iterator Template
python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        result = self.data[self.index]
        self.index += 1
        return result
📺 Watch the Video
[Link to NeuralAICodeCraft YouTube video]

🔗 Related Topics
Generators (Next video)

List comprehensions

For loop internals

⭐ Star this repo if it helped you understand iterators!