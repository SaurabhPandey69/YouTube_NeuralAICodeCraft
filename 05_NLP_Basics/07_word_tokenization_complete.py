"""
WORD TOKENIZATION IN PYTHON: TreebankWordTokenizer vs word_tokenize
NeuralAICodeCraft - Complete Guide to NLTK Tokenization

Topics Covered:
1. What is Word Tokenization?
2. NLTK Installation & Setup
3. TreebankWordTokenizer (Penn Treebank conventions)
4. word_tokenize() function (Improved version)
5. Comparing Both Tokenizers
6. Real-World Preprocessing Pipeline
"""

import nltk
import re
from nltk.tokenize import TreebankWordTokenizer, word_tokenize
from nltk.tokenize import PunktWordTokenizer, WordPunctTokenizer

# Download required NLTK data (uncomment on first run)
# nltk.download('punkt')
# nltk.download('punkt_tab')

print("=" * 70)
print("🔤 WORD TOKENIZATION IN PYTHON")
print("NeuralAICodeCraft - Complete Guide")
print("=" * 70)

# ============================================
# PART 1: WHAT IS WORD TOKENIZATION?
# ============================================

print("\n📚 PART 1: WHAT IS WORD TOKENIZATION?")
print("-" * 50)

print("""
Word Tokenization is the process of breaking text into individual words (tokens).

Example:
    Input:  "Hello, World!"
    Output: ['Hello', ',', 'World', '!']

Why is this important?
├── First step in any NLP pipeline
├── Creates vocabulary for machine learning
├── Enables further processing (POS tagging, NER)
└── Foundation for sentiment analysis, chatbots, and more
""")

# ============================================
# PART 2: NLTK INSTALLATION & SETUP
# ============================================

print("\n🔧 PART 2: NLTK INSTALLATION & SETUP")
print("-" * 50)

print("""
Installation:
    pip install nltk

Download required data:
    import nltk
    nltk.download('punkt')
    nltk.download('punkt_tab')  # For newer versions

Check if data is available:
""")

try:
    nltk.data.find('tokenizers/punkt')
    print("  ✅ Punkt tokenizer data is available")
except LookupError:
    print("  ❌ Punkt tokenizer data not found. Run nltk.download('punkt')")

# ============================================
# PART 3: TREEBANKWORDTOKENIZER
# ============================================

print("\n🌲 PART 3: TREEBANKWORDTOKENIZER")
print("-" * 50)

print("""
TreebankWordTokenizer follows conventions from the Penn Treebank corpus.
- Created from annotated Wall Street Journal articles (1980s)
- Splits punctuation into separate tokens
- Handles contractions in a specific way
- Widely used in academic NLP
""")

# Create tokenizer instance
treebank_tokenizer = TreebankWordTokenizer()

# Example 1: Basic tokenization
print("\n3.1 Basic Tokenization:")
print("-" * 30)

text1 = "Hello, World! How are you today?"
tokens1 = treebank_tokenizer.tokenize(text1)
print(f"  Input: {text1}")
print(f"  Output: {tokens1}")

# Example 2: Contraction handling
print("\n3.2 Contraction Handling (Important!):")
print("-" * 30)

contractions = [
    "can't",
    "don't",
    "won't",
    "I'm",
    "you're",
    "we've",
    "they'll",
    "it's",
    "hasn't",
    "couldn't"
]

print("  Contraction → Tokenized Output")
print("  " + "-" * 40)
for contract in contractions:
    tokens = treebank_tokenizer.tokenize(contract)
    print(f"  {contract:12} → {tokens}")

# Example 3: Punctuation handling
print("\n3.3 Punctuation Handling:")
print("-" * 30)

text_punct = "Hello!!! What's up? (I'm fine!) - OK."
tokens_punct = treebank_tokenizer.tokenize(text_punct)
print(f"  Input: {text_punct}")
print(f"  Output: {tokens_punct}")

# Example 4: Quotes and parentheses
print("\n3.4 Quotes and Parentheses:")
print("-" * 30)

text_quotes = 'He said, "Python is awesome!" (and I agree)'
tokens_quotes = treebank_tokenizer.tokenize(text_quotes)
print(f"  Input: {text_quotes}")
print(f"  Output: {tokens_quotes}")

# Example 5: Numbers and decimals
print("\n3.5 Numbers and Decimals:")
print("-" * 30)

text_numbers = "The price is $3.99 (roughly 3,99 euros) for 2 items."
tokens_numbers = treebank_tokenizer.tokenize(text_numbers)
print(f"  Input: {text_numbers}")
print(f"  Output: {tokens_numbers}")

# ============================================
# PART 4: WORD_TOKENIZE() FUNCTION
# ============================================

print("\n📝 PART 4: WORD_TOKENIZE() FUNCTION")
print("-" * 50)

print("""
word_tokenize() is NLTK's RECOMMENDED word tokenizer.
- Based on improved TreebankWordTokenizer
- Better handling of Unicode quotes and clitics
- Support for multiple languages
- Used in most production NLP pipelines
""")

# Example 1: Basic usage
print("\n4.1 Basic Usage:")
print("-" * 30)

text2 = "Hello, World! How are you today?"
tokens2 = word_tokenize(text2)
print(f"  Input: {text2}")
print(f"  Output: {tokens2}")

# Example 2: Contraction handling (improved)
print("\n4.2 Contraction Handling (Improved):")
print("-" * 30)

contractions2 = [
    "can't",
    "don't",
    "won't",
    "I'm",
    "you're",
    "we've",
    "they'll",
    "it's",
    "hasn't",
    "couldn't",
    "'cause",
    "gonna",
    "wanna"
]

print("  Contraction → Tokenized Output")
print("  " + "-" * 40)
for contract in contractions2:
    tokens = word_tokenize(contract)
    print(f"  {contract:12} → {tokens}")

# Example 3: Complex sentence
print("\n4.3 Complex Sentence with Mixed Punctuation:")
print("-" * 30)

text_complex = """Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."""
tokens_complex = word_tokenize(text_complex)
print(f"  Input: {text_complex[:80]}...")
print(f"  Output: {tokens_complex[:15]}...")

# Example 4: Unicode handling
print("\n4.4 Unicode and Special Characters:")
print("-" * 30)

text_unicode = "Café München über München. naïve résumé fiancé"
tokens_unicode = word_tokenize(text_unicode)
print(f"  Input: {text_unicode}")
print(f"  Output: {tokens_unicode}")

# Example 5: Multi-language support
print("\n4.5 Multi-language Support:")
print("-" * 30)

text_german = "Das ist ein schöner Tag. Wie geht es dir?"
tokens_german = word_tokenize(text_german, language='german')
print(f"  German: {text_german}")
print(f"  Tokens: {tokens_german}")

# ============================================
# PART 5: COMPARING TOKENIZERS
# ============================================

print("\n⚖️ PART 5: COMPARING TOKENIZERS")
print("-" * 50)

# Test sentences for comparison
test_sentences = [
    "Don't stop believing!",
    "I've been to New York.",
    "The price is $19.99.",
    "He said, 'Hello World!'",
    "It's a beautiful day, isn't it?",
    "Mr. Smith went to Washington, D.C.",
]

print("\n5.1 TreebankWordTokenizer vs word_tokenize()")
print("-" * 40)

for sentence in test_sentences:
    treebank_tokens = treebank_tokenizer.tokenize(sentence)
    word_tokens = word_tokenize(sentence)
    
    print(f"\n  Sentence: {sentence}")
    print(f"  Treebank: {treebank_tokens}")
    print(f"  word_tokenize: {word_tokens}")
    print(f"  Same? {treebank_tokens == word_tokens}")

# ============================================
# PART 6: OTHER TOKENIZERS IN NLTK
# ============================================

print("\n🔧 PART 6: OTHER TOKENIZERS IN NLTK")
print("-" * 50)

# 6.1 PunktWordTokenizer
print("\n6.1 PunktWordTokenizer:")
print("-" * 30)

punkt_tokenizer = PunktWordTokenizer()
text_punkt = "Can't is a contraction. Don't you agree?"
tokens_punkt = punkt_tokenizer.tokenize(text_punkt)
print(f"  Input: {text_punkt}")
print(f"  Output: {tokens_punkt}")
print("  Note: Keeps punctuation attached to words")

# 6.2 WordPunctTokenizer
print("\n6.2 WordPunctTokenizer:")
print("-" * 30)

wordpunct_tokenizer = WordPunctTokenizer()
text_wordpunct = "Can't is a contraction. Don't you agree?"
tokens_wordpunct = wordpunct_tokenizer.tokenize(text_wordpunct)
print(f"  Input: {text_wordpunct}")
print(f"  Output: {tokens_wordpunct}")
print("  Note: Splits ALL punctuation into separate tokens")

# 6.3 Comparison of all tokenizers
print("\n6.3 All Tokenizers Comparison:")
print("-" * 30)

test = "Don't stop!"

print(f"  Input: {test}")
print(f"  TreebankWordTokenizer: {treebank_tokenizer.tokenize(test)}")
print(f"  word_tokenize: {word_tokenize(test)}")
print(f"  PunktWordTokenizer: {punkt_tokenizer.tokenize(test)}")
print(f"  WordPunctTokenizer: {wordpunct_tokenizer.tokenize(test)}")

# ============================================
# PART 7: REAL-WORLD PREPROCESSING PIPELINE
# ============================================

print("\n🚀 PART 7: REAL-WORLD PREPROCESSING PIPELINE")
print("-" * 50)

def preprocess_text(text, remove_punctuation=False, lower=False):
    """
    Complete text preprocessing pipeline
    
    Args:
        text: Input text string
        remove_punctuation: Whether to remove punctuation tokens
        lower: Whether to convert to lowercase
    
    Returns:
        List of processed tokens
    """
    # Step 1: Tokenize
    tokens = word_tokenize(text)
    
    # Step 2: Convert to lowercase (optional)
    if lower:
        tokens = [token.lower() for token in tokens]
    
    # Step 3: Remove punctuation (optional)
    if remove_punctuation:
        import string
        punctuation = set(string.punctuation)
        tokens = [token for token in tokens if token not in punctuation]
    
    return tokens

# Test the preprocessing pipeline
print("\n7.1 Preprocessing Pipeline Examples:")
print("-" * 30)

sample_texts = [
    "Hello, World! How are you today?",
    "Don't forget to subscribe to NeuralAICodeCraft!",
    "The price is $19.99 (on sale!).",
    "I've been learning NLP, and it's fascinating!!!"
]

for text in sample_texts:
    print(f"\n  Original: {text}")
    print(f"  Basic tokens: {word_tokenize(text)}")
    print(f"  Lowercase: {preprocess_text(text, lower=True)}")
    print(f"  No punctuation: {preprocess_text(text, remove_punctuation=True)}")
    print(f"  Clean: {preprocess_text(text, lower=True, remove_punctuation=True)}")

# ============================================
# PART 8: HANDLING SPECIAL CASES
# ============================================

print("\n🎯 PART 8: HANDLING SPECIAL CASES")
print("-" * 50)

# 8.1 URLs
print("\n8.1 URL Handling:")
print("-" * 30)

text_url = "Visit our website at https://www.neuralaicodecraft.com for more tutorials!"
tokens_url = word_tokenize(text_url)
print(f"  Input: {text_url}")
print(f"  Tokens: {tokens_url}")
print("  Note: URLs are split by punctuation!")

# 8.2 Email addresses
print("\n8.2 Email Handling:")
print("-" * 30)

text_email = "Contact us at support@neuralaicodecraft.com for questions."
tokens_email = word_tokenize(text_email)
print(f"  Input: {text_email}")
print(f"  Tokens: {tokens_email}")

# 8.3 Abbreviations
print("\n8.3 Abbreviations:")
print("-" * 30)

text_abbr = "Dr. Smith and Mr. Jones met at 10 a.m. in Washington, D.C."
tokens_abbr = word_tokenize(text_abbr)
print(f"  Input: {text_abbr}")
print(f"  Tokens: {tokens_abbr}")

# 8.4 Hashtags and mentions
print("\n8.4 Social Media Text:")
print("-" * 30)

text_social = "Loving #PythonNLP! @NeuralAICodeCraft is the best channel for learning."
tokens_social = word_tokenize(text_social)
print(f"  Input: {text_social}")
print(f"  Tokens: {tokens_social}")

# ============================================
# PART 9: PERFORMANCE COMPARISON
# ============================================

print("\n⏱️ PART 9: PERFORMANCE COMPARISON")
print("-" * 50)

import time

# Create large text for testing
large_text = "This is a sample sentence. " * 1000

print("Processing 1000 sentences...")

# Time TreebankWordTokenizer
start = time.time()
for _ in range(100):
    tokens = treebank_tokenizer.tokenize(large_text)
treebank_time = time.time() - start

# Time word_tokenize
start = time.time()
for _ in range(100):
    tokens = word_tokenize(large_text)
word_time = time.time() - start

print(f"  TreebankWordTokenizer: {treebank_time:.2f} seconds")
print(f"  word_tokenize: {word_time:.2f} seconds")
print(f"  Difference: {abs(treebank_time - word_time):.2f} seconds")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Tokenize a News Headline
Tokenize the following headline:
"Breaking: AI Breakthrough Achieved at MIT's New Lab!"

🎯 EXERCISE 2: Compare Tokenizers
Compare how different tokenizers handle:
"I'm learning NLTK's tokenization module - it's great!"

🎯 EXERCISE 3: Build a Custom Preprocessor
Create a function that:
1. Tokenizes text
2. Removes punctuation
3. Converts to lowercase
4. Removes stopwords

🎯 EXERCISE 4: Handle Special Cases
Tokenize and analyze:
"Check out https://nltk.org for @NLTK #NLP tutorials! (Best resource ever.)"

🎯 CHALLENGE: Tokenize a Paragraph
Take any paragraph from Wikipedia and tokenize it.
Count the number of tokens, unique words, and punctuation marks.
""")

# Solutions
print("\n💡 QUICK SOLUTIONS:")
print("-" * 30)

# Exercise 1 Solution
print("\nEx1 - News Headline:")
headline = "Breaking: AI Breakthrough Achieved at MIT's New Lab!"
print(f"  Original: {headline}")
print(f"  Tokenized: {word_tokenize(headline)}")

# Exercise 2 Solution
print("\nEx2 - Compare Tokenizers:")
test_contractions = "I'm learning NLTK's tokenization module - it's great!"
print(f"  Original: {test_contractions}")
print(f"  Treebank: {treebank_tokenizer.tokenize(test_contractions)}")
print(f"  word_tokenize: {word_tokenize(test_contractions)}")

# Exercise 3 Solution
print("\nEx3 - Custom Preprocessor:")
def advanced_preprocess(text, remove_stopwords=False):
    """Advanced preprocessing with stopword removal"""
    # Tokenize
    tokens = word_tokenize(text.lower())
    
    # Remove punctuation
    import string
    tokens = [t for t in tokens if t not in string.punctuation]
    
    # Remove stopwords (optional)
    if remove_stopwords:
        from nltk.corpus import stopwords
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
        tokens = [t for t in tokens if t not in stop_words]
    
    return tokens

sample = "This is a sample sentence for preprocessing!"
print(f"  Original: {sample}")
print(f"  Processed: {advanced_preprocess(sample)}")
print(f"  Without stopwords: {advanced_preprocess(sample, remove_stopwords=True)}")

# Exercise 4 Solution
print("\nEx4 - Social Media Text:")
social_text = "Check out https://nltk.org for @NLTK #NLP tutorials! (Best resource ever.)"
print(f"  Original: {social_text}")
print(f"  Tokenized: {word_tokenize(social_text)}")

# ============================================
# SUMMARY
# ============================================

print("\n" + "=" * 70)
print("✅ WORD TOKENIZATION MASTERED!")
print("=" * 70)
print("""
QUICK REFERENCE CARD:

┌─────────────────────────────────────────────────────────────┐
│              TOKENIZER COMPARISON                           │
├─────────────────────────────────────────────────────────────┤
│  Tokenizer              │  "can't"  │  "U.S.A."  │  "Hello!" │
├─────────────────────────┼───────────┼────────────┼───────────┤
│  TreebankWordTokenizer  │ ['ca',    │ ['U.S.A']  │ ['Hello', │
│                         │  "n't"]   │            │  '!']      │
├─────────────────────────┼───────────┼────────────┼───────────┤
│  word_tokenize()        │ ['ca',    │ ['U.S.A']  │ ['Hello', │
│  (Recommended)          │  "n't"]   │            │  '!']      │
├─────────────────────────┼───────────┼────────────┼───────────┤
│  PunktWordTokenizer     │ ["Can't"] │ ["U.S.A"]  │ ["Hello!"] │
├─────────────────────────┼───────────┼────────────┼───────────┤
│  WordPunctTokenizer     │ ['Can',   │ ['U', '.', │ ['Hello', │
│                         │  "'", 't']│ 'S', '.',  │ '!']       │
│                         │           │ 'A']       │           │
└─────────────────────────┴───────────┴────────────┴───────────┘

┌─────────────────────────────────────────────────────────────┐
│                    BEST PRACTICES                           │
├─────────────────────────────────────────────────────────────┤
│  ✅ Use word_tokenize() for most NLP tasks                  │
│  ✅ Understand contraction handling (can't → ca + n't)      │
│  ✅ Remove punctuation if not needed for your task          │
│  ✅ Convert to lowercase for consistent vocabulary          │
│  ✅ Consider language parameter for non-English text        │
│  ⚠️ URLs and emails may be split - handle separately       │
└─────────────────────────────────────────────────────────────┘

NEXT VIDEO: Sentence Tokenization & Custom Tokenizers
""")