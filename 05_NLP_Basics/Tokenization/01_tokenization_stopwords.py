"""
NLP BASICS: Tokenization & Stopwords
NeuralAICodeCraft - Complete NLP Guide

This script demonstrates:
1. Tokenization - Splitting text into words/sentences
2. Stopwords removal - Removing common words (the, is, at, etc.)
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')

print("=" * 60)
print("NLP BASICS: TOKENIZATION & STOPWORDS")
print("NeuralAICodeCraft")
print("=" * 60)

# Sample text
text = """
Natural Language Processing is fascinating. It helps computers understand human language.
ChatGPT, Google Translate, and Siri all use NLP. Isn't that amazing?
"""

print("\n📝 ORIGINAL TEXT:")
print(text)

print("\n" + "=" * 40)
print("1. SENTENCE TOKENIZATION")
print("=" * 40)

sentences = sent_tokenize(text)
print(f"Found {len(sentences)} sentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"  Sentence {i}: {sentence.strip()}")

print("\n" + "=" * 40)
print("2. WORD TOKENIZATION")
print("=" * 40)

words = word_tokenize(text)
print(f"Found {len(words)} words:")
print(f"  {words}")

print("\n" + "=" * 40)
print("3. STOPWORDS REMOVAL")
print("=" * 40)

# Get English stopwords
stop_words = set(stopwords.words('english'))
print(f"Total stopwords in English: {len(stop_words)}")
print(f"Sample stopwords: {list(stop_words)[:20]}")

# Remove stopwords
filtered_words = [word.lower() for word in words if word.lower() not in stop_words and word.isalpha()]

print(f"\nWords after removing stopwords: {len(filtered_words)}")
print(f"  {filtered_words}")

print("\n" + "=" * 40)
print("4. COMPLETE PREPROCESSING PIPELINE")
print("=" * 40)

def preprocess_text(text):
    """Complete text preprocessing function"""
    # Tokenize into words
    words = word_tokenize(text.lower())
    
    # Remove stopwords and non-alphabetic tokens
    stop_words = set(stopwords.words('english'))
    cleaned = [word for word in words if word.isalpha() and word not in stop_words]
    
    return cleaned

sample = "Python is amazing for NLP! It makes text processing very easy and fun."
result = preprocess_text(sample)

print(f"Original: {sample}")
print(f"Preprocessed: {result}")

print("\n✅ Tokenization and stopwords complete! Next: Stemming & Lemmatization")