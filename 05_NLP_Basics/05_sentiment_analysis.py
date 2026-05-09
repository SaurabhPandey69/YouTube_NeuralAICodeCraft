"""
COMPLETE NLP PIPELINE: Sentiment Analysis
NeuralAICodeCraft - Building a real NLP application

This script builds a sentiment classifier for movie reviews
FIXED: 
1. Removed len() calls on sparse matrices
2. Fixed coef_ attribute error for MultinomialNB
"""

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

print("=" * 60)
print("COMPLETE NLP PIPELINE: SENTIMENT ANALYSIS")
print("NeuralAICodeCraft")
print("=" * 60)

# Sample dataset (small for demo)
reviews = [
    # Positive reviews
    "This movie is amazing and wonderful",
    "I absolutely loved this film, it was fantastic",
    "Great acting, great story, highly recommended",
    "Best movie I have ever seen",
    "Brilliant performance by the entire cast",
    
    # Negative reviews
    "This movie is terrible and boring",
    "I hated every minute of it, waste of time",
    "Awful acting, horrible plot, don't watch",
    "Worst movie ever made",
    "Disappointing and completely forgettable"
]

# Labels: 1 = positive, 0 = negative
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

print("\n📝 DATASET OVERVIEW:")
print(f"Total reviews: {len(reviews)}")
print(f"Positive reviews: {sum(labels)}")
print(f"Negative reviews: {len(labels) - sum(labels)}")

print("\n" + "=" * 40)
print("STEP 1: TEXT PREPROCESSING")
print("=" * 40)

import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data (uncomment if first time)
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Clean and preprocess text"""
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize and clean
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    return ' '.join(words)

# Preprocess all reviews
processed_reviews = [preprocess_text(review) for review in reviews]

print("\nSample preprocessing:")
print(f"Original: {reviews[0]}")
print(f"Processed: {processed_reviews[0]}")

print("\n" + "=" * 40)
print("STEP 2: TEXT VECTORIZATION (TF-IDF)")
print("=" * 40)

# Convert text to numbers
vectorizer = TfidfVectorizer(max_features=100)
X = vectorizer.fit_transform(processed_reviews)
y = np.array(labels)

print(f"TF-IDF matrix shape: {X.shape}")
print(f"Samples (rows): {X.shape[0]}")
print(f"Features (columns): {X.shape[1]}")
print(f"Features sample: {list(vectorizer.get_feature_names_out())[:10]}...")

print("\n" + "=" * 40)
print("STEP 3: TRAIN-TEST SPLIT")
print("=" * 40)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

print(f"Training samples: {X_train.shape[0]}")
print(f"Test samples: {X_test.shape[0]}")
print(f"Training labels: {len(y_train)}")
print(f"Test labels: {len(y_test)}")

print("\n" + "=" * 40)
print("STEP 4: TRAIN CLASSIFIER")
print("=" * 40)

# Train Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

print("Model trained successfully!")

print("\n" + "=" * 40)
print("STEP 5: EVALUATE MODEL")
print("=" * 40)

y_pred = classifier.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy:.2%}")
print("\nDetailed classification report:")
print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))

print("\n" + "=" * 40)
print("STEP 6: TEST WITH NEW REVIEWS")
print("=" * 40)

def predict_sentiment(text):
    """Predict sentiment of new text"""
    processed = preprocess_text(text)
    vectorized = vectorizer.transform([processed])
    prediction = classifier.predict(vectorized)[0]
    confidence = classifier.predict_proba(vectorized)[0].max()
    
    sentiment = "POSITIVE 😊" if prediction == 1 else "NEGATIVE 😞"
    return sentiment, confidence

# Test with new reviews
test_reviews = [
    "This movie was absolutely incredible, I loved every second",
    "What a waste of time, terrible plot and acting",
    "It was okay, nothing special but not terrible"
]

print("\nTesting new reviews:")
for review in test_reviews:
    sentiment, confidence = predict_sentiment(review)
    print(f"\n  Review: {review}")
    print(f"  Sentiment: {sentiment}")
    print(f"  Confidence: {confidence:.1%}")

print("\n" + "=" * 40)
print("STEP 7: ANALYZE IMPORTANT WORDS (Log Probabilities)")
print("=" * 40)

# FIXED: For MultinomialNB, use feature_log_prob_ instead of coef_
# feature_log_prob_ gives log probabilities of each feature for each class

feature_names = vectorizer.get_feature_names_out()

# Get log probabilities for each class
# class 0 = Negative, class 1 = Positive
log_probs_negative = classifier.feature_log_prob_[0]  # Negative class
log_probs_positive = classifier.feature_log_prob_[1]  # Positive class

# Convert from log probability to regular probability for easier interpretation
import numpy as np
prob_negative = np.exp(log_probs_negative)
prob_positive = np.exp(log_probs_positive)

# Find most important words for POSITIVE sentiment
# Higher probability means more indicative of that class
positive_importance = prob_positive / (prob_positive + prob_negative)
positive_indices = positive_importance.argsort()[-5:][::-1]

print("\nTop 5 words that indicate POSITIVE sentiment:")
for idx in positive_indices:
    if idx < len(feature_names):
        print(f"  '{feature_names[idx]}' → {positive_importance[idx]:.3f} (probability)")

# Find most important words for NEGATIVE sentiment
negative_importance = prob_negative / (prob_positive + prob_negative)
negative_indices = negative_importance.argsort()[-5:][::-1]

print("\nTop 5 words that indicate NEGATIVE sentiment:")
for idx in negative_indices:
    if idx < len(feature_names):
        print(f"  '{feature_names[idx]}' → {negative_importance[idx]:.3f} (probability)")

print("\n" + "=" * 60)
print("ALTERNATIVE: USING LOGISTIC REGRESSION (WITH coef_)")
print("=" * 60)

print("""
If you want to use coef_ (coefficients), use LogisticRegression instead:

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(X_train, y_train)
coefs = classifier.coef_[0]  # This works!

Naive Bayes uses feature_log_prob_ instead of coef_.
""")

print("\n" + "=" * 60)
print("COMPLETE NLP PIPELINE READY!")
print("=" * 60)

print("""
WHAT YOU'VE BUILT:
├── Text preprocessing (cleaning, lemmatization)
├── TF-IDF vectorization
├── Train/test split
├── Multinomial Naive Bayes classifier
├── Sentiment prediction function
├── Real-time testing capability
└── Feature importance analysis (using log probabilities)

NEXT STEPS:
├── Use larger dataset (IMDB 50k reviews)
├── Try other classifiers (LogisticRegression, SVM)
├── Add deep learning (LSTM, BERT)
├── Deploy as web app using Flask
└── Analyze social media sentiment

NOTE: MultinomialNB doesn't have coef_. Use LogisticRegression if you need coefficients.
""")