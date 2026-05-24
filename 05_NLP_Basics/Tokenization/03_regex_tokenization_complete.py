"""
REGULAR EXPRESSIONS & TOKENIZATION IN PYTHON
NeuralAICodeCraft - Complete Guide to re Module and Custom Tokenizers

Topics Covered:
1. Regular Expressions (RegEx) Basics
2. WordPunctTokenizer in NLTK
3. Python re Module (match, search, findall, finditer, sub, split, compile)
4. Custom Tokenizers with RegEx
5. Real-World Pattern Extraction
"""

import re
import nltk
from nltk.tokenize import WordPunctTokenizer, word_tokenize

# Download required data (if needed)
# nltk.download('punkt')

print("=" * 70)
print("🔍 REGULAR EXPRESSIONS & TOKENIZATION IN PYTHON")
print("NeuralAICodeCraft - Complete Guide")
print("=" * 70)

# ============================================
# PART 1: REGEX BASICS
# ============================================

print("\n📚 PART 1: REGULAR EXPRESSIONS (RegEx) BASICS")
print("-" * 50)

print("""
WHAT ARE REGULAR EXPRESSIONS?
├── Sequence of characters defining a search pattern
├── Used for pattern matching and text extraction
└── Powerful tool for string manipulation

COMMON METACHARACTERS:
┌─────────┬──────────────────────────────────────┐
│ Pattern │ Description                          │
├─────────┼──────────────────────────────────────┤
│ .       │ Any character (except newline)       │
│ ^       │ Start of string                      │
│ $       │ End of string                        │
│ *       │ 0 or more repetitions                │
│ +       │ 1 or more repetitions                │
│ ?       │ 0 or 1 repetition                    │
│ {n}     │ Exactly n repetitions                │
│ {n,}    │ n or more repetitions                │
│ {n,m}   │ Between n and m repetitions          │
│ []      │ Set of characters                    │
│ |       │ OR operator                          │
│ ()      │ Grouping                             │
│ \\      │ Escape special character             │
└─────────┴──────────────────────────────────────┘

CHARACTER CLASSES:
┌─────────┬──────────────────────────────────────┐
│ Pattern │ Description                          │
├─────────┼──────────────────────────────────────┤
│ \\d     │ Any digit (0-9)                      │
│ \\D     │ Any non-digit                        │
│ \\w     │ Any word character (a-z, A-Z, 0-9, _)│
│ \\W     │ Any non-word character               │
│ \\s     │ Any whitespace (space, tab, newline) │
│ \\S     │ Any non-whitespace                   │
│ [0-9]   │ Any digit                            │
│ [a-z]   │ Any lowercase letter                 │
│ [A-Z]   │ Any uppercase letter                 │
│ [a-zA-Z]│ Any letter                           │
└─────────┴──────────────────────────────────────┘
""")

# ============================================
# PART 2: REGEX DEMONSTRATION
# ============================================

print("\n🎯 PART 2: REGEX PATTERN DEMONSTRATION")
print("-" * 50)

text_sample = "The quick brown fox jumps over 123 lazy dogs at 2:30 PM on 2024-01-15."

print(f"\nSample Text: {text_sample}\n")

# 2.1 Find all words
print("2.1 Find all words (\\w+):")
words = re.findall(r'\w+', text_sample)
print(f"  Result: {words}")

# 2.2 Find all digits
print("\n2.2 Find all digits (\\d+):")
digits = re.findall(r'\d+', text_sample)
print(f"  Result: {digits}")

# 2.3 Find all lowercase words
print("\n2.3 Find all lowercase words ([a-z]+):")
lower_words = re.findall(r'[a-z]+', text_sample)
print(f"  Result: {lower_words}")

# 2.4 Find all uppercase words
print("\n2.4 Find all uppercase words ([A-Z]+):")
upper_words = re.findall(r'[A-Z]+', text_sample)
print(f"  Result: {upper_words}")

# 2.5 Find date pattern
print("\n2.5 Find date pattern (\\d{4}-\\d{2}-\\d{2}):")
dates = re.findall(r'\d{4}-\d{2}-\d{2}', text_sample)
print(f"  Result: {dates}")

# 2.6 Find time pattern
print("\n2.6 Find time pattern (\\d{1,2}:\\d{2}:?\\d{0,2}):")
times = re.findall(r'\d{1,2}:\d{2}', text_sample)
print(f"  Result: {times}")

# ============================================
# PART 3: WORDPUNCTTOKENIZER
# ============================================

print("\n🔧 PART 3: WORDPUNCTTOKENIZER (NLTK)")
print("-" * 50)

print("""
WordPunctTokenizer splits text on ALL punctuation characters.
- Every punctuation becomes its own token
- Words and punctuation are separated
- Useful for character-level analysis
""")

# Create tokenizer
wordpunct_tokenizer = WordPunctTokenizer()

# 3.1 Basic tokenization
print("\n3.1 Basic Tokenization:")
print("-" * 30)

test_texts = [
    "Hello, World!",
    "Don't stop believing!",
    "Python is great (really!)",
    "Email: user@example.com",
    "The price is $19.99"
]

for text in test_texts:
    tokens = wordpunct_tokenizer.tokenize(text)
    print(f"  Input: {text}")
    print(f"  Output: {tokens}\n")

# 3.2 Comparison with word_tokenize()
print("\n3.2 Comparison: WordPunctTokenizer vs word_tokenize():")
print("-" * 30)

comparison_texts = [
    "Can't",
    "U.S.A.",
    "Hello!!!",
    "price=$19.99",
    "user@example.com"
]

print(f"{'Text':<15} {'WordPunctTokenizer':<35} {'word_tokenize()':<30}")
print("-" * 80)

for text in comparison_texts:
    wp_tokens = wordpunct_tokenizer.tokenize(text)
    w_tokens = word_tokenize(text)
    print(f"{text:<15} {str(wp_tokens):<35} {str(w_tokens):<30}")

# ============================================
# PART 4: re.match() - MATCH AT BEGINNING
# ============================================

print("\n📌 PART 4: re.match() - Match at Beginning")
print("-" * 50)

print("""
re.match() checks for pattern ONLY at the START of the string.
- Returns match object if found, None otherwise
- Use when you know pattern must be at beginning
""")

text_match = "Python is a great programming language"

# Match at beginning
pattern_start = r'Python'
match_start = re.match(pattern_start, text_match)
print(f"  Text: {text_match}")
print(f"  Pattern: '{pattern_start}'")
print(f"  Match found: {match_start is not None}")
if match_start:
    print(f"  Matched text: {match_start.group()}")
    print(f"  Start position: {match_start.start()}")
    print(f"  End position: {match_start.end()}")

# Pattern not at beginning
pattern_middle = r'great'
match_middle = re.match(pattern_middle, text_match)
print(f"\n  Pattern: '{pattern_middle}'")
print(f"  Match found: {match_middle is not None}")
print(f"  (Returns None because 'great' is not at beginning)")

# ============================================
# PART 5: re.search() - SEARCH ANYWHERE
# ============================================

print("\n🔍 PART 5: re.search() - Search Anywhere")
print("-" * 50)

print("""
re.search() scans the ENTIRE string for first match.
- Returns match object if found anywhere
- More flexible than match()
""")

text_search = "Contact us at support@example.com or call 555-1234"

# Search for email
email_pattern = r'\w+@\w+\.\w+'
email_match = re.search(email_pattern, text_search)
print(f"  Text: {text_search}")
print(f"  Pattern: '{email_pattern}'")
if email_match:
    print(f"  Found email: {email_match.group()}")
    print(f"  Position: {email_match.start()}-{email_match.end()}")

# Search for phone
phone_pattern = r'\d{3}-\d{4}'
phone_match = re.search(phone_pattern, text_search)
if phone_match:
    print(f"\n  Found phone: {phone_match.group()}")
    print(f"  Position: {phone_match.start()}-{phone_match.end()}")

# ============================================
# PART 6: re.findall() - FIND ALL MATCHES
# ============================================

print("\n📋 PART 6: re.findall() - Find All Matches")
print("-" * 50)

print("""
re.findall() returns ALL non-overlapping matches as a list.
- Most commonly used regex function
- Great for extracting patterns
""")

text_findall = "Emails: john@example.com, jane@test.com, bob@work.org. Phone: 555-1234, 555-5678"

print(f"  Text: {text_findall}\n")

# Find all emails
emails = re.findall(r'\w+@\w+\.\w+', text_findall)
print(f"  All emails: {emails}")

# Find all phones
phones = re.findall(r'\d{3}-\d{4}', text_findall)
print(f"  All phones: {phones}")

# Find all words
words = re.findall(r'\b\w+\b', text_findall)
print(f"  All words: {words[:10]}...")

# Find all with groups
pattern_group = r'(\w+)@(\w+)\.(\w+)'
matches = re.findall(pattern_group, text_findall)
print(f"  Email parts (username, domain, tld): {matches}")

# ============================================
# PART 7: re.finditer() - ITERATOR OVER MATCHES
# ============================================

print("\n🔄 PART 7: re.finditer() - Iterator Over Matches")
print("-" * 50)

print("""
re.finditer() returns an iterator yielding match objects.
- More memory efficient for large texts
- Access to match positions and groups
""")

text_iter = "The numbers are 42, 100, and 999."

print(f"  Text: {text_iter}\n")

pattern = r'\d+'
matches = re.finditer(pattern, text_iter)

print("  Found numbers:")
for match in matches:
    print(f"    Value: {match.group()}, Position: {match.start()}-{match.end()}")

# ============================================
# PART 8: re.compile() - COMPILE PATTERNS
# ============================================

print("\n⚡ PART 8: re.compile() - Compile Patterns for Performance")
print("-" * 50)

print("""
re.compile() pre-compiles regex pattern for reuse.
- Better performance when using same pattern multiple times
- Makes code more readable
- Flags can be set once
""")

# Without compile (compiled each time)
print("\n8.1 Without compile (re-compiled each iteration):")
import time

text_compile = "test@example.com"
pattern_str = r'\w+@\w+\.\w+'

start = time.time()
for _ in range(10000):
    result = re.findall(pattern_str, text_compile)
no_compile_time = time.time() - start
print(f"  Time: {no_compile_time:.4f} seconds")

# With compile
print("\n8.2 With compile (pre-compiled once):")
compiled_pattern = re.compile(r'\w+@\w+\.\w+')

start = time.time()
for _ in range(10000):
    result = compiled_pattern.findall(text_compile)
compile_time = time.time() - start
print(f"  Time: {compile_time:.4f} seconds")

print(f"\n  Performance improvement: {(no_compile_time - compile_time) / no_compile_time * 100:.1f}% faster")

# Compiled pattern with flags
print("\n8.3 Compiled pattern with flags:")
case_insensitive = re.compile(r'python', re.IGNORECASE)
print(f"  Pattern: {case_insensitive.pattern}")
print(f"  Match 'python': {case_insensitive.search('Python is great') is not None}")

# ============================================
# PART 9: re.sub() - REPLACE PATTERNS
# ============================================

print("\n🔄 PART 9: re.sub() - Replace Patterns")
print("-" * 50)

print("""
re.sub() replaces matched patterns with new text.
- Great for text cleaning and normalization
- Can use backreferences to original text
""")

text_sub = "Contact: john@example.com, Phone: 555-1234"

print(f"  Original: {text_sub}\n")

# Remove emails
no_emails = re.sub(r'\w+@\w+\.\w+', '[EMAIL]', text_sub)
print(f"  Remove emails: {no_emails}")

# Replace phone numbers
no_phones = re.sub(r'\d{3}-\d{4}', '[PHONE]', text_sub)
print(f"  Remove phones: {no_phones}")

# Remove everything except letters and spaces
text_dirty = "Hello!!! This is a #message with @mentions and $pecial ch@racters!"
cleaned = re.sub(r'[^a-zA-Z\s]', '', text_dirty)
print(f"\n  Original: {text_dirty}")
print(f"  Cleaned: {cleaned}")

# Using backreferences
text_date = "Date: 2024-01-15"
reformatted = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\2/\3/\1', text_date)
print(f"\n  Original date: {text_date}")
print(f"  Reformatted: {reformatted} (MM/DD/YYYY)")

# ============================================
# PART 10: re.split() - SPLIT BY PATTERN
# ============================================

print("\n✂️ PART 10: re.split() - Split by Pattern")
print("-" * 50)

text_split = "apple, banana; cherry: orange|grape"

print(f"  Original: {text_split}\n")

# Split by multiple delimiters
delimiters = r'[,;:|]'
parts = re.split(delimiters, text_split)
print(f"  Split by [,;:|]: {parts}")

# Split by whitespace
text_ws = "This  has\tmultiple   whitespace"
parts_ws = re.split(r'\s+', text_ws)
print(f"\n  Original: {text_ws}")
print(f"  Split by whitespace: {parts_ws}")

# ============================================
# PART 11: CUSTOM TOKENIZERS WITH REGEX
# ============================================

print("\n🔧 PART 11: CUSTOM TOKENIZERS WITH REGEX")
print("-" * 50)

class RegexTokenizer:
    """Custom tokenizer using regular expressions"""
    
    def __init__(self, pattern=r'\b\w+\b'):
        """Initialize tokenizer with pattern"""
        self.pattern = re.compile(pattern)
    
    def tokenize(self, text):
        """Tokenize text using compiled pattern"""
        return self.pattern.findall(text)
    
    def tokenize_with_positions(self, text):
        """Tokenize and return positions"""
        return [(match.group(), match.start(), match.end()) 
                for match in self.pattern.finditer(text)]

# 11.1 Word tokenizer
print("\n11.1 Basic Word Tokenizer:")
print("-" * 30)

word_tokenizer = RegexTokenizer(r'\b\w+\b')
text_word = "Hello, World! How are you? It's a beautiful day."
tokens_word = word_tokenizer.tokenize(text_word)
print(f"  Input: {text_word}")
print(f"  Output: {tokens_word}")

# 11.2 Word with apostrophes tokenizer
print("\n11.2 Word Tokenizer (handling apostrophes):")
print("-" * 30)

apostrophe_tokenizer = RegexTokenizer(r"\b\w+(?:'\w+)?\b")
text_apostrophe = "Don't stop believing! It's a wonderful day."
tokens_apostrophe = apostrophe_tokenizer.tokenize(text_apostrophe)
print(f"  Input: {text_apostrophe}")
print(f"  Output: {tokens_apostrophe}")

# 11.3 Email and URL tokenizer
print("\n11.3 Email and URL Tokenizer:")
print("-" * 30)

url_tokenizer = RegexTokenizer(r'\S+@\S+\.\S+|https?://\S+')
text_urls = "Contact us at support@example.com or visit https://neuralaicodecraft.com"
tokens_urls = url_tokenizer.tokenize(text_urls)
print(f"  Input: {text_urls}")
print(f"  Output: {tokens_urls}")

# 11.4 Hashtag and mention tokenizer
print("\n11.4 Social Media Tokenizer (Hashtags & Mentions):")
print("-" * 30)

social_tokenizer = RegexTokenizer(r'@\w+|#\w+')
text_social = "Loving #PythonNLP! @NeuralAICodeCraft is the best. #Coding @NLTK"
tokens_social = social_tokenizer.tokenize(text_social)
print(f"  Input: {text_social}")
print(f"  Output: {tokens_social}")

# 11.5 Combined tokenizer
print("\n11.5 Combined Tokenizer (Multiple Patterns):")
print("-" * 30)

class AdvancedTokenizer:
    """Advanced tokenizer with multiple pattern support"""
    
    def __init__(self):
        self.patterns = {
            'email': re.compile(r'\b\w+@\w+\.\w+\b'),
            'url': re.compile(r'https?://\S+'),
            'phone': re.compile(r'\d{3}-\d{3}-\d{4}|\d{10}'),
            'hashtag': re.compile(r'#\w+'),
            'mention': re.compile(r'@\w+'),
            'word': re.compile(r"\b\w+(?:'\w+)?\b"),
            'number': re.compile(r'\b\d+(?:\.\d+)?\b')
        }
    
    def tokenize_all(self, text):
        """Extract all pattern types"""
        results = {}
        for name, pattern in self.patterns.items():
            matches = pattern.findall(text)
            if matches:
                results[name] = matches
        return results
    
    def tokenize_type(self, text, token_type):
        """Extract specific pattern type"""
        if token_type in self.patterns:
            return self.patterns[token_type].findall(text)
        return []

# Test advanced tokenizer
advanced_tok = AdvancedTokenizer()
text_advanced = """
Contact: john.doe@example.com or call 555-123-4567
Visit https://neuralaicodecraft.com
Follow @NeuralAIC #PythonNLP
The price is $99.99 for 3 items.
"""

results = advanced_tok.tokenize_all(text_advanced)
print("  Extracted patterns:")
for token_type, matches in results.items():
    print(f"    {token_type}: {matches}")

# ============================================
# PART 12: REAL-WORLD PATTERN EXTRACTION
# ============================================

print("\n🌐 PART 12: REAL-WORLD PATTERN EXTRACTION")
print("-" * 50)

# 12.1 Email validation
print("\n12.1 Email Validation:")
print("-" * 30)

def validate_email(email):
    """Validate email address using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

emails = [
    "user@example.com",
    "john.doe@company.co.uk",
    "invalid-email",
    "missing@domain",
    "@missingusername.com"
]

print("  Email validation results:")
for email in emails:
    is_valid = validate_email(email)
    print(f"    {email:30} → {'✅ Valid' if is_valid else '❌ Invalid'}")

# 12.2 Phone number extraction
print("\n12.2 Phone Number Extraction:")
print("-" * 30)

def extract_phone_numbers(text):
    """Extract phone numbers in various formats"""
    patterns = [
        r'\d{3}-\d{3}-\d{4}',           # 555-123-4567
        r'\(\d{3}\)\s?\d{3}-\d{4}',      # (555) 123-4567
        r'\d{10}',                       # 5551234567
        r'\+\d{1,2}\s?\d{3}-\d{3}-\d{4}' # +1 555-123-4567
    ]
    combined = '|'.join(patterns)
    return re.findall(combined, text)

text_phones = "Call me at (555) 123-4567 or 555-987-6543. International: +1 555-111-2222"
phones = extract_phone_numbers(text_phones)
print(f"  Text: {text_phones}")
print(f"  Phone numbers: {phones}")

# 12.3 URL extraction
print("\n12.3 URL Extraction:")
print("-" * 30)

def extract_urls(text):
    """Extract URLs from text"""
    pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+(?:/[-\w%!$&\'()*+,;=:@/]*)?'
    return re.findall(pattern, text, re.IGNORECASE)

text_urls = "Check https://www.python.org and http://nltk.org for resources. Also https://github.com/neuralaicodecraft"
urls = extract_urls(text_urls)
print(f"  URLs found: {urls}")

# 12.4 Hashtag extraction from tweets
print("\n12.4 Hashtag Extraction from Tweets:")
print("-" * 30)

def extract_hashtags(text):
    """Extract hashtags from text"""
    pattern = r'#\w+'
    return re.findall(pattern, text)

tweet = "Loving #PythonNLP and #MachineLearning! #Coding is fun #100DaysOfCode"
hashtags = extract_hashtags(tweet)
print(f"  Tweet: {tweet}")
print(f"  Hashtags: {hashtags}")

# ============================================
# PART 13: COMPLETE PREPROCESSING PIPELINE
# ============================================

print("\n🚀 PART 13: COMPLETE PREPROCESSING PIPELINE")
print("-" * 50)

class TextPreprocessor:
    """Complete text preprocessing pipeline"""
    
    def __init__(self):
        self.url_pattern = re.compile(r'https?://\S+')
        self.email_pattern = re.compile(r'\b\w+@\w+\.\w+\b')
        self.mention_pattern = re.compile(r'@\w+')
        self.hashtag_pattern = re.compile(r'#\w+')
        self.punct_pattern = re.compile(r'[^\w\s]')
        self.whitespace_pattern = re.compile(r'\s+')
    
    def clean_text(self, text):
        """Basic text cleaning"""
        # Remove URLs
        text = self.url_pattern.sub('[URL]', text)
        # Remove emails
        text = self.email_pattern.sub('[EMAIL]', text)
        # Normalize mentions
        text = self.mention_pattern.sub('[MENTION]', text)
        # Normalize hashtags
        text = self.hashtag_pattern.sub('[HASHTAG]', text)
        # Remove punctuation
        text = self.punct_pattern.sub('', text)
        # Normalize whitespace
        text = self.whitespace_pattern.sub(' ', text)
        return text.strip()
    
    def tokenize(self, text):
        """Tokenize cleaned text"""
        return text.lower().split()
    
    def process(self, text):
        """Complete pipeline"""
        cleaned = self.clean_text(text)
        tokens = self.tokenize(cleaned)
        return {
            'original': text,
            'cleaned': cleaned,
            'tokens': tokens,
            'token_count': len(tokens)
        }

# Test the pipeline
preprocessor = TextPreprocessor()

sample_texts = [
    "Check out https://neuralaicodecraft.com for #Python tutorials! Follow @NeuralAIC",
    "Contact us at support@example.com or call (555) 123-4567",
    "Python is AMAZING!!! I've been learning it for 6 months. #CodingLife"
]

print("\nProcessing samples:")
for text in sample_texts:
    result = preprocessor.process(text)
    print(f"\n  Original: {result['original']}")
    print(f"  Cleaned: {result['cleaned']}")
    print(f"  Tokens: {result['tokens']}")
    print(f"  Token count: {result['token_count']}")

# ============================================
# PART 14: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 14: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Date Extractor
Write a regex to extract dates in formats:
- YYYY-MM-DD
- MM/DD/YYYY
- DD-MM-YYYY

🎯 EXERCISE 2: Password Validator
Create a regex that validates passwords:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

🎯 EXERCISE 3: HTML Tag Extractor
Extract all HTML tags from a string

🎯 EXERCISE 4: Price Extractor
Extract prices like $19.99, €29.99, £9.99 from text

🎯 EXERCISE 5: Custom Tokenizer
Create a tokenizer that:
- Keeps URLs as single tokens
- Keeps emails as single tokens
- Splits on punctuation
- Preserves hashtags
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1: Date extractor
print("\nEx1 - Date Extractor:")
date_pattern = r'\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}'
text_dates = "Dates: 2024-01-15, 01/15/2024, 15-01-2024"
dates = re.findall(date_pattern, text_dates)
print(f"  Input: {text_dates}")
print(f"  Dates: {dates}")

# Exercise 2: Password validator
print("\nEx2 - Password Validator:")
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
passwords = ["StrongP@ss1", "weak", "NoDigit!", "noupper1!"]
for pwd in passwords:
    is_valid = bool(re.match(password_pattern, pwd))
    print(f"  {pwd:15} → {'✅ Valid' if is_valid else '❌ Invalid'}")

# Exercise 3: HTML tag extractor
print("\nEx3 - HTML Tag Extractor:")
html = "<div><p>Hello</p><a href='link'>Click</a></div>"
tags = re.findall(r'<[^>]+>', html)
print(f"  HTML: {html}")
print(f"  Tags: {tags}")

# Exercise 4: Price extractor
print("\nEx4 - Price Extractor:")
price_pattern = r'[£$€]\d+(?:\.\d{2})?'
text_prices = "Items: $19.99, €29.99, £9.99, and $5"
prices = re.findall(price_pattern, text_prices)
print(f"  Input: {text_prices}")
print(f"  Prices: {prices}")

# Exercise 5: Custom tokenizer
print("\nEx5 - Custom Tokenizer:")
def custom_tokenizer(text):
    """Custom tokenizer for emails, URLs, words, punctuation"""
    # Pattern for emails and URLs
    special = r'\S+@\S+\.\S+|https?://\S+'
    # Pattern for words with apostrophes
    words = r"\b\w+(?:'\w+)?\b"
    # Pattern for punctuation
    punct = r'[^\w\s]'
    
    combined = f'({special})|({words})|({punct})'
    return re.findall(combined, text)

text_custom = "Check https://site.com or email user@example.com! Don't forget."
matches = custom_tokenizer(text_custom)
# Flatten and filter empty strings
tokens = [m for match in matches for m in match if m]
print(f"  Input: {text_custom}")
print(f"  Tokens: {tokens}")

# ============================================
# PART 15: SUMMARY & CHEATSHEET
# ============================================

print("\n" + "=" * 70)
print("✅ REGULAR EXPRESSIONS MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│              re MODULE FUNCTIONS                            │
├─────────────────────────────────────────────────────────────┤
│  re.match(pattern, str)     → Match at beginning            │
│  re.search(pattern, str)    → Search anywhere               │
│  re.findall(pattern, str)   → Return all matches (list)     │
│  re.finditer(pattern, str)  → Return iterator of matches    │
│  re.sub(pattern, repl, str) → Replace matches               │
│  re.split(pattern, str)     → Split by pattern              │
│  re.compile(pattern)        → Compile for reuse             │
├─────────────────────────────────────────────────────────────┤
│              COMMON PATTERNS                                │
├─────────────────────────────────────────────────────────────┤
│  Email:      r'\b\w+@\w+\.\w+\b'                           │
│  URL:        r'https?://\S+'                                │
│  Phone:      r'\d{3}-\d{3}-\d{4}'                          │
│  Hashtag:    r'#\w+'                                        │
│  Mention:    r'@\w+'                                        │
│  Date:       r'\d{4}-\d{2}-\d{2}'                          │
│  IP Address: r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'         │
├─────────────────────────────────────────────────────────────┤
│              FLAGS                                          │
├─────────────────────────────────────────────────────────────┤
│  re.IGNORECASE (re.I)     → Case insensitive                │
│  re.MULTILINE (re.M)      → ^ and $ match lines             │
│  re.DOTALL (re.S)         → . matches newline               │
│  re.UNICODE (re.U)        → Unicode matching                │
│  re.VERBOSE (re.X)        │ Allow comments in regex        │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Advanced Regex Patterns & Text Processing
""")

print("\n🎉 REGEX & TOKENIZATION COMPLETE!")