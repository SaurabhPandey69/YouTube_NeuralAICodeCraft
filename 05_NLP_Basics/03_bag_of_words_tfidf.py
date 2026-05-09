"""
TEXT REPRESENTATION: Bag of Words & TF-IDF
NeuralAICodeCraft - Converting text to numbers for ML
"""

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd

print("=" * 60)
print("TEXT REPRESENTATION: Bag of Words & TF-IDF")
print("NeuralAICodeCraft")
print("=" * 60)

# Sample documents
documents = [
    "Python is great for machine learning",
    "Machine learning uses Python",
    "Deep learning is a subset of machine learning",
    "I love learning new things"
]

print("\n📝 DOCUMENTS:")
for i, doc in enumerate(documents, 1):
    print(f"  Doc {i}: {doc}")

print("\n" + "=" * 40)
print("1. BAG OF WORDS (CountVectorizer)")
print("=" * 40)

# Create bag of words
vectorizer = CountVectorizer()
bow_matrix = vectorizer.fit_transform(documents)

# Convert to DataFrame for better viewing
bow_df = pd.DataFrame(
    bow_matrix.toarray(),
    columns=vectorizer.get_feature_names_out()
)

print("\nBag of Words Matrix (rows=documents, columns=words):")
print(bow_df)

print("\n" + "=" * 40)
print("2. TF-IDF (Term Frequency - Inverse Document Frequency)")
print("=" * 40)

# TF-IDF explanation
print("""
TF-IDF Formula:
├── TF (Term Frequency) = How often word appears in document
├── IDF (Inverse Document Frequency) = How rare word is across documents
└── TF-IDF = TF × IDF (Higher = More important)
""")

# Create TF-IDF matrix
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

tfidf_df = pd.DataFrame(
    tfidf_matrix.toarray(),
    columns=tfidf_vectorizer.get_feature_names_out()
)

print("\nTF-IDF Matrix (higher numbers = more important):")
print(tfidf_df.round(3))

print("\n" + "=" * 40)
print("3. COMPARING BOW vs TF-IDF")
print("=" * 40)

# Find most important word in each document
print("\nMost important word in each document (TF-IDF):")
for i, doc in enumerate(documents):
    doc_tfidf = tfidf_matrix[i].toarray()[0]
    max_idx = doc_tfidf.argmax()
    max_word = tfidf_vectorizer.get_feature_names_out()[max_idx]
    print(f"  Doc {i+1}: '{max_word}' (score: {doc_tfidf[max_idx]:.3f})")

print("\n" + "=" * 40)
print("4. REAL-WORLD EXAMPLE: Search Engine")
print("=" * 40)

# Simulate search query
query = "machine learning"
query_vector = tfidf_vectorizer.transform([query])

# Calculate similarity
from sklearn.metrics.pairwise import cosine_similarity
similarities = cosine_similarity(query_vector, tfidf_matrix)[0]

print(f"Search Query: '{query}'")
print("\nDocument relevance scores:")
for i, score in enumerate(similarities, 1):
    print(f"  Doc {i}: {score:.3f} → {documents[i-1]}")

print("\n✅ Bag of Words & TF-IDF complete! Next: Word Embeddings")