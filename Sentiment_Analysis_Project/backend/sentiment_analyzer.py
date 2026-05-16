"""
Sentiment Analyzer Module
NeuralAICodeCraft - Model loading and prediction logic
"""

import joblib
import numpy as np
import re
import os
from pathlib import Path
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk

# Download NLTK data if not available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)

# Get the directory of this file
BASE_DIR = Path(__file__).resolve().parent
MODELS_DIR = BASE_DIR / 'saved_models'


def preprocess_text(text):
    """Clean and preprocess text - SAME FUNCTION as in train_models.py"""
    # Initialize stopwords and lemmatizer
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
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


class SentimentAnalyzer:
    """Sentiment Analyzer using pre-trained models"""
    
    def __init__(self):
        """Load all models and preprocessors"""
        print("=" * 50)
        print("Loading Sentiment Analysis Models...")
        print("=" * 50)
        
        # Check if models directory exists
        if not MODELS_DIR.exists():
            error_msg = f"""
            ❌ Models directory not found: {MODELS_DIR}
            
            Please run the training script first:
            
                cd {BASE_DIR}
                python train_models.py
            
            This will create the required model files.
            """
            print(error_msg)
            raise FileNotFoundError(f"Models directory not found at {MODELS_DIR}")
        
        # Load all required files (only 3 files needed - removed preprocessor.pkl)
        required_files = ['vectorizer.pkl', 'logistic_model.pkl', 'naivebayes_model.pkl']
        
        missing_files = []
        for file in required_files:
            file_path = MODELS_DIR / file
            if not file_path.exists():
                missing_files.append(file)
        
        if missing_files:
            raise FileNotFoundError(f"Missing required files: {missing_files}\nPlease run train_models.py first.")
        
        # Load vectorizer
        print("📊 Loading vectorizer...")
        self.vectorizer = joblib.load(MODELS_DIR / 'vectorizer.pkl')
        
        # Load models
        print("🤖 Loading Logistic Regression model...")
        self.logistic_model = joblib.load(MODELS_DIR / 'logistic_model.pkl')
        
        print("🤖 Loading Naive Bayes model...")
        self.naivebayes_model = joblib.load(MODELS_DIR / 'naivebayes_model.pkl')
        
        # Use the local preprocess_text function (not loaded from file)
        print("🔧 Using built-in text preprocessor...")
        self.preprocessor = preprocess_text
        
        print("✅ All models loaded successfully!\n")
    
    def preprocess(self, text):
        """Preprocess input text"""
        return self.preprocessor(text)
    
    def predict_logistic(self, text):
        """Predict sentiment using Logistic Regression"""
        try:
            processed = self.preprocess(text)
            vectorized = self.vectorizer.transform([processed])
            prediction = self.logistic_model.predict(vectorized)[0]
            probability = self.logistic_model.predict_proba(vectorized)[0]
            
            return {
                'sentiment': 'POSITIVE' if prediction == 1 else 'NEGATIVE',
                'confidence': float(max(probability)),
                'probabilities': {
                    'negative': float(probability[0]),
                    'positive': float(probability[1])
                },
                'model': 'Logistic Regression'
            }
        except Exception as e:
            print(f"Error in Logistic Regression: {e}")
            return {
                'sentiment': 'ERROR',
                'confidence': 0.0,
                'probabilities': {'negative': 0.0, 'positive': 0.0},
                'model': 'Logistic Regression',
                'error': str(e)
            }
    
    def predict_naivebayes(self, text):
        """Predict sentiment using Naive Bayes"""
        try:
            processed = self.preprocess(text)
            vectorized = self.vectorizer.transform([processed])
            prediction = self.naivebayes_model.predict(vectorized)[0]
            probability = self.naivebayes_model.predict_proba(vectorized)[0]
            
            return {
                'sentiment': 'POSITIVE' if prediction == 1 else 'NEGATIVE',
                'confidence': float(max(probability)),
                'probabilities': {
                    'negative': float(probability[0]),
                    'positive': float(probability[1])
                },
                'model': 'Naive Bayes'
            }
        except Exception as e:
            print(f"Error in Naive Bayes: {e}")
            return {
                'sentiment': 'ERROR',
                'confidence': 0.0,
                'probabilities': {'negative': 0.0, 'positive': 0.0},
                'model': 'Naive Bayes',
                'error': str(e)
            }
    
    def predict_both(self, text):
        """Predict using both models"""
        return {
            'logistic': self.predict_logistic(text),
            'naivebayes': self.predict_naivebayes(text)
        }
    
    def predict_batch(self, texts, model='logistic'):
        """Predict sentiment for multiple texts"""
        results = []
        
        for text in texts:
            if model == 'logistic':
                result = self.predict_logistic(text)
            else:
                result = self.predict_naivebayes(text)
            results.append({
                'text': text,
                'sentiment': result['sentiment'],
                'confidence': result['confidence']
            })
        
        return results
    
    def get_model_info(self):
        """Get information about loaded models"""
        try:
            return {
                'logistic_regression': {
                    'coefficients_shape': self.logistic_model.coef_.shape,
                    'intercept': float(self.logistic_model.intercept_[0]),
                    'classes': ['NEGATIVE', 'POSITIVE']
                },
                'naive_bayes': {
                    'classes': self.naivebayes_model.classes_.tolist(),
                    'feature_count_shape': self.naivebayes_model.feature_count_.shape
                },
                'features': list(self.vectorizer.get_feature_names_out()[:10])
            }
        except Exception as e:
            return {'error': str(e)}


# Create analyzer instance
print("\n" + "=" * 50)
print("Initializing Sentiment Analyzer...")
print("=" * 50)

try:
    analyzer = SentimentAnalyzer()
    print("✅ Analyzer ready to use!")
except Exception as e:
    print(f"❌ Failed to initialize analyzer: {e}")
    print("\nPlease follow these steps:")
    print("1. Make sure you're in the backend directory:")
    print("   cd Sentiment_Analysis_Project/backend")
    print("2. Run the training script:")
    print("   python train_models.py")
    print("3. Then run the main app:")
    print("   python main.py")
    analyzer = None