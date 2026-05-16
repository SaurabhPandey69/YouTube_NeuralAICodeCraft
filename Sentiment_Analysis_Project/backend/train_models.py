"""
Train and Save Sentiment Analysis Models
NeuralAICodeCraft - Complete NLP Project
"""

import numpy as np
import pandas as pd
import re
import joblib
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

# Download NLTK data
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)
nltk.download('punkt', quiet=True)

print("=" * 60)
print("🚀 TRAINING SENTIMENT ANALYSIS MODELS")
print("NeuralAICodeCraft")
print("=" * 60)

# Create saved_models directory
os.makedirs('saved_models', exist_ok=True)

# ============================================
# 1. PREPARE DATASET
# ============================================

print("\n📊 Preparing dataset...")

# Enhanced dataset with more reviews
reviews = [
    # POSITIVE REVIEWS (20 samples)
    ("This movie is absolutely amazing and wonderful", 1),
    ("I absolutely loved this film, it was fantastic and brilliant", 1),
    ("Great acting, great story, highly recommended to everyone", 1),
    ("Best movie I have ever seen in my entire life", 1),
    ("Brilliant performance by the entire cast, outstanding", 1),
    ("What a masterpiece! The direction and cinematography were perfect", 1),
    ("Heartwarming and inspiring story that stayed with me", 1),
    ("Exceptional writing, great characters, beautiful soundtrack", 1),
    ("A must-watch! Exceeded all my expectations", 1),
    ("Powerful, moving, and absolutely unforgettable", 1),
    ("Fantastic! Could watch this again and again", 1),
    ("Superb! The acting was top-notch", 1),
    ("Excellent movie, great plot twists", 1),
    ("Wonderful experience, highly recommend", 1),
    ("Stunning visuals and incredible story", 1),
    ("This product is amazing, works perfectly!", 1),
    ("Best purchase ever, highly satisfied", 1),
    ("Excellent quality, fast shipping", 1),
    ("Love this! Will buy again", 1),
    ("Perfect! Exactly what I needed", 1),
    
    # NEGATIVE REVIEWS (20 samples)
    ("This movie is terrible and extremely boring", 0),
    ("I hated every minute of it, complete waste of time and money", 0),
    ("Awful acting, horrible plot, don't watch this garbage", 0),
    ("Worst movie ever made, absolutely pathetic", 0),
    ("Disappointing and completely forgettable experience", 0),
    ("What a disaster! The script was terrible and predictable", 0),
    ("Boring, slow, and utterly meaningless", 0),
    ("Poor direction, weak performances, terrible dialogue", 0),
    ("A complete mess from start to finish", 0),
    ("Regret wasting my time on this nonsense", 0),
    ("Terrible! I want my money back", 0),
    ("Horrible acting, boring plot", 0),
    ("Complete disappointment, don't bother", 0),
    ("Waste of time, very predictable", 0),
    ("Poorly made and uninteresting", 0),
    ("This product is garbage, broke immediately", 0),
    ("Worst purchase ever, completely useless", 0),
    ("Terrible quality, fell apart in days", 0),
    ("Don't waste your money on this junk", 0),
    ("Very disappointed, nothing like advertised", 0),
]

texts = [review[0] for review in reviews]
labels = [review[1] for review in reviews]

print(f"Total samples: {len(texts)}")
print(f"Positive: {sum(labels)}, Negative: {len(labels) - sum(labels)}")

# ============================================
# 2. TEXT PREPROCESSING FUNCTION
# ============================================

print("\n🔧 Creating preprocessing function...")

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Clean and preprocess text"""
    if not isinstance(text, str):
        text = str(text)
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Tokenize and clean
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words and len(word) > 1]
    
    return ' '.join(words)


# Test preprocessing
processed_texts = [preprocess_text(text) for text in texts]

print(f"Sample preprocessing:")
print(f"  Original: {texts[0]}")
print(f"  Processed: {processed_texts[0]}")

# ============================================
# 3. TRAIN-TEST SPLIT
# ============================================

print("\n📊 Splitting data...")

X_train, X_test, y_train, y_test = train_test_split(
    processed_texts, labels, test_size=0.2, random_state=42, stratify=labels
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

# ============================================
# 4. TF-IDF VECTORIZATION
# ============================================

print("\n📊 Creating TF-IDF vectors...")

vectorizer = TfidfVectorizer(
    max_features=500,
    ngram_range=(1, 2),
    min_df=1,
    max_df=0.9
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

print(f"Feature matrix shape: {X_train_tfidf.shape}")
print(f"Number of features: {len(vectorizer.get_feature_names_out())}")

# Save vectorizer
joblib.dump(vectorizer, 'saved_models/vectorizer.pkl')
print("✅ Vectorizer saved to 'saved_models/vectorizer.pkl'")

# ============================================
# 5. TRAIN LOGISTIC REGRESSION
# ============================================

print("\n🚀 Training Logistic Regression...")

logistic_model = LogisticRegression(max_iter=1000, C=1.0, random_state=42)
logistic_model.fit(X_train_tfidf, y_train)

logistic_pred = logistic_model.predict(X_test_tfidf)
logistic_accuracy = accuracy_score(y_test, logistic_pred)

print(f"Logistic Regression Accuracy: {logistic_accuracy:.2%}")
print(f"Classification Report:\n{classification_report(y_test, logistic_pred, target_names=['Negative', 'Positive'])}")

# Save logistic model
joblib.dump(logistic_model, 'saved_models/logistic_model.pkl')
print("✅ Logistic Regression model saved to 'saved_models/logistic_model.pkl'")

# ============================================
# 6. TRAIN NAIVE BAYES
# ============================================

print("\n🚀 Training Naive Bayes...")

nb_model = MultinomialNB()
nb_model.fit(X_train_tfidf, y_train)

nb_pred = nb_model.predict(X_test_tfidf)
nb_accuracy = accuracy_score(y_test, nb_pred)

print(f"Naive Bayes Accuracy: {nb_accuracy:.2%}")
print(f"Classification Report:\n{classification_report(y_test, nb_pred, target_names=['Negative', 'Positive'])}")

# Save naive bayes model
joblib.dump(nb_model, 'saved_models/naivebayes_model.pkl')
print("✅ Naive Bayes model saved to 'saved_models/naivebayes_model.pkl'")

# ============================================
# 7. SUMMARY - NO preprocessor.pkl saved!
# ============================================

print("\n" + "=" * 60)
print("✅ TRAINING COMPLETE!")
print("=" * 60)
print(f"""
Model Performance Summary:
├── Logistic Regression: {logistic_accuracy:.2%}
├── Naive Bayes: {nb_accuracy:.2%}
├── Best Model: {'Logistic Regression' if logistic_accuracy > nb_accuracy else 'Naive Bayes'}
└── Features: {len(vectorizer.get_feature_names_out())}

Saved Files (3 files only):
├── saved_models/vectorizer.pkl
├── saved_models/logistic_model.pkl
└── saved_models/naivebayes_model.pkl

✅ All files saved successfully!

Now you can run: python main.py
""")