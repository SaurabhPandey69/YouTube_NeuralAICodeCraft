"""
WORD EMBEDDINGS: Word2Vec & GloVe Basics
NeuralAICodeCraft - Words as Vectors

Note: This script uses Gensim for Word2Vec. Install with:
pip install gensim
"""

import numpy as np

print("=" * 60)
print("WORD EMBEDDINGS: Word2Vec & GloVe")
print("NeuralAICodeCraft")
print("=" * 60)

print("""
WHAT ARE WORD EMBEDDINGS?
├── Words converted to numbers (vectors)
├── Similar words have similar vectors
├── Example: "king" - "man" + "woman" ≈ "queen"
└── Machines can understand word relationships!
""")

print("\n" + "=" * 40)
print("1. CONCEPTUAL EXAMPLE (Simplified)")
print("=" * 40)

# Simplified word vectors (3D for visualization)
word_vectors = {
    'king':    [0.8, 0.9, 0.7],
    'queen':   [0.7, 0.8, 0.6],
    'man':     [0.5, 0.2, 0.3],
    'woman':   [0.4, 0.3, 0.2],
    'apple':   [0.1, 0.9, 0.1],
    'orange':  [0.2, 0.8, 0.2],
    'car':     [0.9, 0.1, 0.9]
}

print("Sample word vectors (simplified 3D):")
for word, vec in word_vectors.items():
    print(f"  {word:8} → {vec}")

print("\n" + "=" * 40)
print("2. COSINE SIMILARITY (Finding Similar Words)")
print("=" * 40)

def cosine_similarity(vec1, vec2):
    """Calculate similarity between two vectors"""
    dot_product = sum(a*b for a,b in zip(vec1, vec2))
    norm1 = np.sqrt(sum(a*a for a in vec1))
    norm2 = np.sqrt(sum(b*b for b in vec2))
    return dot_product / (norm1 * norm2)

# Find most similar word to 'king'
print("Words most similar to 'king':")
king_vec = word_vectors['king']
similarities = []

for word, vec in word_vectors.items():
    if word != 'king':
        sim = cosine_similarity(king_vec, vec)
        similarities.append((word, sim))

similarities.sort(key=lambda x: x[1], reverse=True)
for word, sim in similarities[:3]:
    print(f"  {word}: {sim:.3f}")

print("\n" + "=" * 40)
print("3. WORD ANALOGIES (king - man + woman = ?)")
print("=" * 40)

# king - man + woman
king_vec = np.array(word_vectors['king'])
man_vec = np.array(word_vectors['man'])
woman_vec = np.array(word_vectors['woman'])

result_vec = king_vec - man_vec + woman_vec
print(f"king - man + woman = {result_vec}")

# Find closest word to result
best_word = None
best_sim = -1
for word, vec in word_vectors.items():
    if word not in ['king', 'man', 'woman']:
        sim = cosine_similarity(result_vec, np.array(vec))
        if sim > best_sim:
            best_sim = sim
            best_word = word

print(f"Closest word: {best_word} (similarity: {best_sim:.3f})")
print("✓ This matches the famous 'queen' analogy!")

print("\n" + "=" * 40)
print("4. REAL WORD2VEC WITH GENSIM (Optional)")
print("=" * 40)

print("""
To use real Word2Vec:

from gensim.models import Word2Vec

# Training data
sentences = [["cat", "say", "meow"], ["dog", "say", "woof"]]

# Train model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1)

# Find similar words
model.wv.most_similar('cat')

Install: pip install gensim
Then download pre-trained embeddings or train your own.
""")

print("\n" + "=" * 40)
print("5. PRE-TRAINED EMBEDDINGS")
print("=" * 40)

print("""
Popular pre-trained word embeddings:

1. GloVe (Stanford)
   ├── 6B, 42B, 840B token versions
   ├── 50, 100, 200, 300 dimensions
   └── Download: nlp.stanford.edu/projects/glove/

2. Word2Vec (Google)
   ├── Trained on 100B words
   ├── 300 dimensions
   └── 1.5GB download

3. FastText (Facebook)
   ├── Handles out-of-vocabulary words
   ├── Subword information
   └── 157 languages available
""")

print("\n✅ Word Embeddings complete! Next: Transformers")
