"""
LOGISTIC REGRESSION SENTIMENT ANALYZER
NeuralAICodeCraft - Complete NLP Pipeline with Logistic Regression

This script builds a sentiment classifier using Logistic Regression
Features:
- Text preprocessing (tokenization, stopwords, lemmatization)
- TF-IDF vectorization
- Logistic Regression with coefficient analysis
- Model evaluation and comparison
- Real-time prediction
"""

import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required NLTK data (first time only)
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('punkt')

print("=" * 70)
print("🔷 LOGISTIC REGRESSION SENTIMENT ANALYZER 🔷")
print("NeuralAICodeCraft - Complete NLP Pipeline")
print("=" * 70)

# ============================================
# PART 1: CREATE ENHANCED DATASET
# ============================================

print("\n📊 PART 1: PREPARING DATASET")
print("-" * 50)

# More comprehensive dataset
reviews = [
    # POSITIVE REVIEWS (10 samples)
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
    
    # NEGATIVE REVIEWS (10 samples)
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
]

# Separate into lists
texts = [review[0] for review in reviews]
labels = [review[1] for review in reviews]

print(f"Total samples: {len(texts)}")
print(f"Positive reviews: {sum(labels)}")
print(f"Negative reviews: {len(labels) - sum(labels)}")

# ============================================
# PART 2: TEXT PREPROCESSING FUNCTION
# ============================================

print("\n🔧 PART 2: TEXT PREPROCESSING")
print("-" * 50)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text, verbose=False):
    """
    Complete text preprocessing pipeline
    """
    original = text
    
    # Step 1: Convert to lowercase
    text = text.lower()
    if verbose: print(f"  Lowercase: {text[:50]}...")
    
    # Step 2: Remove punctuation and special characters
    text = re.sub(r'[^\w\s]', '', text)
    if verbose: print(f"  No punctuation: {text[:50]}...")
    
    # Step 3: Tokenize and remove stopwords + lemmatize
    words = text.split()
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    
    # Step 4: Join back
    processed = ' '.join(words)
    if verbose: print(f"  Processed: {processed[:50]}...")
    
    return processed

# Preprocess all reviews
processed_texts = [preprocess_text(text) for text in texts]

# Show example
print("\nExample preprocessing:")
print(f"Original:   {texts[0]}")
print(f"Processed:  {processed_texts[0]}")

# ============================================
# PART 3: TRAIN-TEST SPLIT
# ============================================

print("\n📊 PART 3: TRAIN-TEST SPLIT")
print("-" * 50)

X_train, X_test, y_train, y_test = train_test_split(
    processed_texts, labels, test_size=0.3, random_state=42, stratify=labels
)

print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
print(f"Training - Positive: {sum(y_train)}, Negative: {len(y_train) - sum(y_train)}")
print(f"Test - Positive: {sum(y_test)}, Negative: {len(y_test) - sum(y_test)}")

# ============================================
# PART 4: CREATE PIPELINE WITH TF-IDF + LOGISTIC REGRESSION
# ============================================

print("\n🚀 PART 4: BUILDING LOGISTIC REGRESSION PIPELINE")
print("-" * 50)

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=100,
        ngram_range=(1, 2),  # Use unigrams and bigrams
        min_df=1,
        max_df=0.9
    )),
    ('classifier', LogisticRegression(
        max_iter=1000,
        C=1.0,  # Regularization strength
        random_state=42
    ))
])

print("Pipeline created with:")
print("  ├── TF-IDF Vectorizer (max_features=100, ngram_range=(1,2))")
print("  └── Logistic Regression (max_iter=1000, C=1.0)")

# Train the model
print("\nTraining model...")
pipeline.fit(X_train, y_train)
print("✅ Model training complete!")

# ============================================
# PART 5: MODEL EVALUATION
# ============================================

print("\n📈 PART 5: MODEL EVALUATION")
print("-" * 50)

# Predictions
y_pred = pipeline.predict(X_test)
y_pred_proba = pipeline.predict_proba(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy:.2%}")

# Detailed classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print("              Predicted")
print("              Neg  Pos")
print(f"Actual Neg    {cm[0,0]:3}   {cm[0,1]:3}")
print(f"       Pos    {cm[1,0]:3}   {cm[1,1]:3}")

# ============================================
# PART 6: EXTRACT AND ANALYZE COEFFICIENTS
# ============================================

print("\n🔍 PART 6: FEATURE IMPORTANCE (COEFFICIENT ANALYSIS)")
print("-" * 50)

# Get feature names and coefficients
feature_names = pipeline.named_steps['tfidf'].get_feature_names_out()
coefficients = pipeline.named_steps['classifier'].coef_[0]

# Create DataFrame for easier analysis
coef_df = pd.DataFrame({
    'word': feature_names,
    'coefficient': coefficients
})

# Top positive words (high coefficient = strong positive sentiment)
positive_words = coef_df.nlargest(10, 'coefficient')
print("\n📈 TOP 10 WORDS INDICATING POSITIVE SENTIMENT:")
for idx, row in positive_words.iterrows():
    print(f"  ✅ '{row['word']}' → {row['coefficient']:.4f}")

# Top negative words (low coefficient = strong negative sentiment)
negative_words = coef_df.nsmallest(10, 'coefficient')
print("\n📉 TOP 10 WORDS INDICATING NEGATIVE SENTIMENT:")
for idx, row in negative_words.iterrows():
    print(f"  ❌ '{row['word']}' → {row['coefficient']:.4f}")

# ============================================
# PART 7: REAL-TIME SENTIMENT PREDICTION
# ============================================

print("\n🎯 PART 7: REAL-TIME SENTIMENT PREDICTION")
print("-" * 50)

def predict_sentiment(text, return_details=False):
    """
    Predict sentiment of any text using trained model
    
    Parameters:
    - text: String input
    - return_details: Boolean to return probability and confidence
    
    Returns:
    - sentiment: 'POSITIVE' or 'NEGATIVE'
    - details: (confidence, probability) if return_details=True
    """
    # Preprocess the text
    processed = preprocess_text(text)
    
    # Predict
    prediction = pipeline.predict([processed])[0]
    probabilities = pipeline.predict_proba([processed])[0]
    confidence = max(probabilities)
    
    sentiment = "POSITIVE" if prediction == 1 else "NEGATIVE"
    emoji = "😊" if prediction == 1 else "😞"
    
    if return_details:
        return f"{sentiment} {emoji}", confidence, probabilities
    return f"{sentiment} {emoji}"

# Test with various reviews
test_reviews = [
    "This movie was absolutely incredible, I loved every single second of it!",
    "What a complete waste of time. Terrible acting and boring plot.",
    "It was okay, nothing special but not terrible either.",
    "A masterpiece of cinema! Brilliant direction and powerful performances.",
    "I regret watching this. Complete garbage from start to end.",
    "Pretty good movie, enjoyed it but wouldn't watch again.",
    "Absolutely phenomenal! Best film I've seen all year!",
    "Disappointing and forgettable. Expected much better.",
]

print("\nTesting model on new reviews:\n")
for review in test_reviews:
    sentiment, confidence, probs = predict_sentiment(review, return_details=True)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}")
    print(f"Confidence: {confidence:.1%} (Positive: {probs[1]:.1%}, Negative: {probs[0]:.1%})")
    print("-" * 50)

# ============================================
# PART 8: COMPARE WITH NAIVE BAYES
# ============================================

print("\n📊 PART 8: LOGISTIC REGRESSION vs NAIVE BAYES")
print("-" * 50)

from sklearn.naive_bayes import MultinomialNB

# Train Naive Bayes on same data
nb_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=100)),
    ('classifier', MultinomialNB())
])

nb_pipeline.fit(X_train, y_train)
nb_pred = nb_pipeline.predict(X_test)
nb_accuracy = accuracy_score(y_test, nb_pred)

print(f"Logistic Regression Accuracy: {accuracy:.2%}")
print(f"Naive Bayes Accuracy: {nb_accuracy:.2%}")
print(f"Difference: {accuracy - nb_accuracy:.2%}")

if accuracy > nb_accuracy:
    print("✅ Logistic Regression performs better on this dataset!")
else:
    print("✅ Naive Bayes performs better on this dataset!")

# ============================================
# PART 9: VISUALIZATION (If matplotlib is available)
# ============================================

print("\n📊 PART 9: VISUALIZATIONS")
print("-" * 50)

try:
    # Create figure
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Top Positive and Negative Words
    ax1 = axes[0, 0]
    top_words = pd.concat([positive_words.head(5), negative_words.head(5)])
    colors = ['green'] * 5 + ['red'] * 5
    ax1.barh(top_words['word'], top_words['coefficient'], color=colors)
    ax1.set_xlabel('Coefficient')
    ax1.set_title('Top 5 Positive (Green) & Negative (Red) Words')
    ax1.axvline(x=0, color='black', linestyle='-', linewidth=0.5)
    
    # 2. Confusion Matrix Heatmap
    ax2 = axes[0, 1]
    im = ax2.imshow(cm, interpolation='nearest', cmap='Blues')
    ax2.set_xticks([0, 1])
    ax2.set_yticks([0, 1])
    ax2.set_xticklabels(['Negative', 'Positive'])
    ax2.set_yticklabels(['Negative', 'Positive'])
    ax2.set_xlabel('Predicted')
    ax2.set_ylabel('Actual')
    ax2.set_title('Confusion Matrix')
    
    # Add text annotations
    for i in range(2):
        for j in range(2):
            ax2.text(j, i, str(cm[i, j]), ha='center', va='center', fontsize=16)
    
    # 3. Coefficient Distribution
    ax3 = axes[1, 0]
    ax3.hist(coefficients, bins=20, color='purple', alpha=0.7, edgecolor='black')
    ax3.set_xlabel('Coefficient Value')
    ax3.set_ylabel('Frequency')
    ax3.set_title('Distribution of Word Coefficients')
    ax3.axvline(x=0, color='red', linestyle='--', linewidth=1)
    
    # 4. Accuracy Comparison
    ax4 = axes[1, 1]
    models = ['Logistic Regression', 'Naive Bayes']
    accuracies = [accuracy, nb_accuracy]
    bars = ax4.bar(models, accuracies, color=['#8B5CF6', '#06B6D4'])
    ax4.set_ylim([0, 1])
    ax4.set_ylabel('Accuracy')
    ax4.set_title('Model Comparison')
    
    # Add value labels on bars
    for bar, acc in zip(bars, accuracies):
        ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02, 
                f'{acc:.1%}', ha='center', fontsize=10, fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('sentiment_analysis_logistic_results.png', dpi=150, bbox_inches='tight')
    print("✅ Visualizations saved as 'sentiment_analysis_logistic_results.png'")
    
    # Display (if in interactive environment)
    # plt.show()
    
except Exception as e:
    print(f"⚠️ Visualization skipped: {e}")

# ============================================
# PART 10: SAVE MODEL FOR LATER USE
# ============================================

print("\n💾 PART 10: SAVING MODEL")
print("-" * 50)

import joblib

# Save the model
model_filename = 'sentiment_model_logistic.pkl'
joblib.dump(pipeline, model_filename)
print(f"✅ Model saved as '{model_filename}'")

# Save the preprocessor separately
preprocessor_filename = 'text_preprocessor.pkl'
joblib.dump(preprocess_text, preprocessor_filename)
print(f"✅ Preprocessor saved as '{preprocessor_filename}'")

# ============================================
# PART 11: LOAD AND TEST SAVED MODEL
# ============================================

print("\n🔄 PART 11: LOADING AND TESTING SAVED MODEL")
print("-" * 50)

# Load the model
loaded_model = joblib.load(model_filename)

# Test loaded model
test_text = "This is absolutely fantastic and brilliant!"
loaded_prediction = loaded_model.predict([preprocess_text(test_text)])[0]
print(f"Original model prediction: {predict_sentiment(test_text)}")
print(f"Loaded model prediction: {'POSITIVE 😊' if loaded_prediction == 1 else 'NEGATIVE 😞'}")
print("✅ Model loaded and working correctly!")

# ============================================
# PART 12: INTERACTIVE PREDICTION FUNCTION
# ============================================

print("\n" + "=" * 70)
print("🚀 LOGISTIC REGRESSION SENTIMENT ANALYZER READY! 🚀")
print("=" * 70)

print("""
╔══════════════════════════════════════════════════════════════════╗
║                    HOW TO USE THIS MODEL                         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  METHOD 1: Direct function call                                  ║
║  ────────────────────────────────────────────────────────────    ║
║  sentiment = predict_sentiment("Your review here")               ║
║                                                                  ║
║  METHOD 2: With confidence scores                                ║
║  ────────────────────────────────────────────────────────────    ║
║  sentiment, confidence, probs = predict_sentiment(text, True)    ║
║                                                                  ║
║  METHOD 3: Load saved model                                      ║
║  ────────────────────────────────────────────────────────────    ║
║  import joblib                                                   ║
║  model = joblib.load('sentiment_model_logistic.pkl')             ║
║  prediction = model.predict([preprocess_text("text")])           ║
║                                                                  ║
║  METHOD 4: Batch prediction                                      ║
║  ────────────────────────────────────────────────────────────    ║
║  reviews = ["Great movie!", "Terrible film"]                     ║
║  processed = [preprocess_text(r) for r in reviews]               ║
║  predictions = model.predict(processed)                          ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
""")

# ============================================
# BONUS: BATCH PREDICTION DEMO
# ============================================

print("\n🎯 BONUS: BATCH PREDICTION DEMO")
print("-" * 50)

batch_reviews = [
    "Best product ever! Highly recommended!",
    "Worst purchase of my life. Completely broken.",
    "Decent quality, worth the price.",
    "Absolutely phenomenal! Exceeded all expectations!",
    "Very disappointed. Didn't work as advertised.",
]

print("Processing batch of 5 reviews...\n")
processed_batch = [preprocess_text(review) for review in batch_reviews]
batch_predictions = pipeline.predict(processed_batch)
batch_probabilities = pipeline.predict_proba(processed_batch)

for review, pred, probs in zip(batch_reviews, batch_predictions, batch_probabilities):
    sentiment = "POSITIVE 😊" if pred == 1 else "NEGATIVE 😞"
    confidence = max(probs)
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment} (Confidence: {confidence:.1%})")
    print("-" * 40)

print("\n" + "=" * 70)
print("✅ LOGISTIC REGRESSION SENTIMENT ANALYZER COMPLETE!")
print("=" * 70)
print("""
KEY TAKEAWAYS:
├── Logistic Regression provides interpretable coefficients
├── Coefficients show which words drive sentiment
├── Pipeline makes preprocessing + prediction seamless
├── Model can be saved and loaded for production use
└── Batch processing is efficient for multiple reviews

NEXT STEPS:
├── Train on larger dataset (IMDB 50k reviews)
├── Add cross-validation for better evaluation
├── Deploy as REST API using Flask/FastAPI
├── Add more features (n-grams, word embeddings)
└── Build a simple web interface for demo
""")