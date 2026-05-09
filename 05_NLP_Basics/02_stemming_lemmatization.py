"""
NLP BASICS: Stemming vs Lemmatization
NeuralAICodeCraft - Reducing words to root form

Stemming: Cuts word endings (running → runn)
Lemmatization: Uses dictionary to find base form (running → run)
"""

import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

nltk.download('wordnet')
nltk.download('omw-1.4')

print("=" * 60)
print("STEMMING vs LEMMATIZATION")
print("NeuralAICodeCraft")
print("=" * 60)

# Sample words
words = ["running", "ran", "runs", "better", "good", "studies", "studying", "crying", "cried"]

print("\n📝 ORIGINAL WORDS:")
print(words)

print("\n" + "=" * 40)
print("1. STEMMING (Porter Stemmer)")
print("=" * 40)

stemmer = PorterStemmer()
print("Word → Stem")
print("-" * 30)
for word in words:
    stemmed = stemmer.stem(word)
    print(f"{word:12} → {stemmed}")

print("\n" + "=" * 40)
print("2. LEMMATIZATION (WordNet)")
print("=" * 40)

lemmatizer = WordNetLemmatizer()
print("Word → Lemma (base form)")
print("-" * 35)
for word in words:
    lemmatized = lemmatizer.lemmatize(word, pos='v')  # pos='v' for verb
    print(f"{word:12} → {lemmatized}")

print("\n" + "=" * 40)
print("3. STEMMING vs LEMMATIZATION (Detailed)")
print("=" * 40)

test_words = ["studies", "studying", "studied", "better", "good", "went", "gone"]

print(f"{'Word':12} {'Stem':12} {'Lemma':12}")
print("-" * 40)
for word in test_words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(f"{word:12} {stem:12} {lemma:12}")

print("\n" + "=" * 40)
print("4. WHEN TO USE WHAT?")
print("=" * 40)

print("""
STEMMING:
├── Faster (just cuts endings)
├── Less accurate (produces non-words)
├── Good for information retrieval
└── Example: Search engines

LEMMATIZATION:
├── Slower (uses dictionary lookup)
├── More accurate (real words only)
├── Good for chatbots, sentiment analysis
└── Example: Voice assistants (Siri, Alexa)
""")

print("\n✅ Stemming & Lemmatization complete! Next: Bag of Words & TF-IDF")