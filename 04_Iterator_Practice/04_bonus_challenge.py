"""
BONUS CHALLENGE: Log File Processor
NeuralAICodeCraft - Real-World Iterator Application
"""

print("=" * 60)
print("BONUS CHALLENGE: Log File Processor")
print("=" * 60)

"""
CHALLENGE:
Create an iterator that reads a log file and only yields ERROR lines.
Then, count how many errors occurred.

Sample log format:
[INFO] 2024-01-01: Application started
[ERROR] 2024-01-01: Database connection failed
[INFO] 2024-01-01: Retrying connection
[ERROR] 2024-01-01: Connection timeout
[ERROR] 2024-01-01: Authentication failed
[INFO] 2024-01-01: Shutting down

Your task:
1. Create a ErrorLogIterator class
2. Read a sample log file line by line
3. Only return lines containing "[ERROR]"
4. Count total errors

Your code here:
"""

class ErrorLogIterator:
    """Iterator that yields only ERROR lines from a log file"""
    
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        while True:
            line = self.file.readline()
            if line == '':
                self.file.close()
                raise StopIteration
            if '[ERROR]' in line:
                return line.strip()

# Create sample log file
sample_log = """[INFO] 2024-01-01: Application started
[ERROR] 2024-01-01: Database connection failed
[INFO] 2024-01-01: Retrying connection
[ERROR] 2024-01-01: Connection timeout
[INFO] 2024-01-01: Cache loaded
[ERROR] 2024-01-01: Authentication failed
[INFO] 2024-01-01: User logged in
[ERROR] 2024-01-01: API rate limit exceeded
[INFO] 2024-01-01: Request processed
[ERROR] 2024-01-01: Memory leak detected"""

with open('sample_log.txt', 'w') as f:
    f.write(sample_log)

print("\n--- SOLUTION BONUS ---")
print("Processing log file...")

error_count = 0
for error_line in ErrorLogIterator('sample_log.txt'):
    error_count += 1
    print(f"  🔴 {error_line}")

print(f"\n📊 Total errors found: {error_count}")

print("\n" + "=" * 60)
print("BONUS BONUS: Process Large File")
print("=" * 60)

class LargeFileChunkReader:
    """Reads large files in chunks (memory efficient)"""
    
    def __init__(self, filename, chunk_size=1024):
        self.filename = filename
        self.chunk_size = chunk_size
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'rb')
        return self
    
    def __next__(self):
        chunk = self.file.read(self.chunk_size)
        if not chunk:
            self.file.close()
            raise StopIteration
        return chunk

print("\n💡 Real-world use case: Processing large files in chunks")
print("This reads files without loading entire file into memory!")
print("Perfect for 1GB+ log files, CSV files, or video processing.")

print("\n🎯 Challenge Complete! You've mastered Python iterators!")