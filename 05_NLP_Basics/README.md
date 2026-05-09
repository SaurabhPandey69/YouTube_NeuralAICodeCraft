# 05_NLP_Basics - Natural Language Processing from Basic to Advanced

## 📚 Complete NLP Guide

This folder contains a **complete NLP pipeline** from basic text preprocessing to sentiment analysis.

## 📂 Files Overview

| File | Topic | Difficulty |
|------|-------|------------|
| `01_tokenization_stopwords.py` | Tokenization & Stopwords removal | ⭐ Basic |
| `02_stemming_lemmatization.py` | Stemming vs Lemmatization | ⭐ Basic |
| `03_bag_of_words_tfidf.py` | Bag of Words & TF-IDF | ⭐⭐ Intermediate |
| `04_word_embeddings.py` | Word2Vec & GloVe concepts | ⭐⭐ Intermediate |
| `05_sentiment_analysis.py` | Complete NLP pipeline | ⭐⭐⭐ Advanced |

## 🚀 Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Download NLTK data (first time)
python -c "import nltk; nltk.download('all')"

# Run each script in order
python 01_tokenization_stopwords.py
python 02_stemming_lemmatization.py
python 03_bag_of_words_tfidf.py
python 04_word_embeddings.py
python 05_sentiment_analysis.py
📖 Learning Path
1. Text Preprocessing (Basic)
Tokenization → Split text into words/sentences

Stopwords → Remove common words

Stemming → Cut word endings

Lemmatization → Find dictionary base form

2. Text Representation (Intermediate)
Bag of Words → Count word frequencies

TF-IDF → Weight words by importance

Word Embeddings → Words as vectors

3. NLP Applications (Advanced)
Sentiment Analysis → Positive/Negative classification

Text Classification → Categorize documents

Named Entity Recognition → Find people, places, etc.

🎯 Real-World Applications
Application	Technology Used
ChatGPT	Transformers
Google Translate	Seq2Seq + Attention
Spam Detection	Naive Bayes + TF-IDF
Voice Assistants	RNNs + Word Embeddings
Recommendation	Text Similarity
💡 Key Takeaways
python
# Complete NLP Pipeline
text → Preprocess → Vectorize → Classify → Result

# Example
review = "This movie is amazing!"
processed = preprocess(review)  # ['amazing', 'movie']
vectorized = tfidf.transform([processed])
sentiment = classifier.predict(vectorized)  # POSITIVE
📊 Performance Tips
Large datasets? Use TF-IDF with max_features

Real-time apps? Use simple embeddings

Maximum accuracy? Use BERT / Transformers

Low resources? Use Bag of Words

🔗 Watch the Video
[https://www.youtube.com/@NeuralAICode - NLP Basic to Advanced]

🎓 Next Steps
Word Embeddings Deep Dive

Recurrent Neural Networks (RNN)

Transformers & BERT

Building a Chatbot

⭐ Star this repo if NLP becomes your favorite subject!

