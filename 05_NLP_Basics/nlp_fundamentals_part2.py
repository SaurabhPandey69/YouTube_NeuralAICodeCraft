"""
NLP FUNDAMENTALS PART 2: ADVANCED NLP TECHNIQUES
NeuralAICodeCraft - From Basics to Production-Ready

Topics Covered:
1. Advanced Tokenization (Regex, Custom Patterns)
2. Custom Stopwords (Domain-specific)
3. Advanced Stemming (Snowball, Lancaster)
4. POS-Aware Lemmatization
5. Custom Named Entity Recognition
6. Production-Ready NLP Pipeline
"""

import nltk
import re
import string
from collections import Counter
import pandas as pd
import numpy as np
from nltk.tokenize import RegexpTokenizer, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, SnowballStemmer, LancasterStemmer, WordNetLemmatizer
from nltk import pos_tag, ne_chunk
from nltk.chunk import ne_chunk
import warnings
warnings.filterwarnings('ignore')

# Download required data (uncomment on first run)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

print("=" * 70)
print("🧠 NLP FUNDAMENTALS PART 2: ADVANCED TECHNIQUES")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: QUICK RECAP
# ============================================

print("\n📚 PART 1: QUICK RECAP OF NLP FUNDAMENTALS")
print("-" * 50)

print("""
Part 1 Covered:
├── ✅ Basic Tokenization (word, sentence)
├── ✅ Basic Stemming (Porter)
├── ✅ Basic Lemmatization
├── ✅ Basic POS Tagging
└── ✅ Basic Named Entity Recognition

Part 2 Takes You Further:
├── 🚀 Regex & Custom Tokenization
├── 🚀 Domain-specific Stopwords
├── 🚀 Multiple Stemming Algorithms
├── 🚀 POS-Aware Lemmatization
├── 🚀 Custom NER Models
└── 🚀 Production-Ready Pipeline
""")

# Sample text for demonstrations
sample_text = """
Contact us at support@neuralaicodecraft.com or call +1-800-555-0123.
Visit our website: https://www.neuralaicodecraft.com
Follow us on Twitter: @NeuralAICodeCraft #NLP #Python
The meeting is scheduled for 2024-12-25 at 3:30 PM.
John Doe's email is john.doe@email.com and phone is (555) 123-4567.
"""

print(f"\n📝 Sample Text for Advanced Demos:")
print("-" * 50)
print(sample_text)

# ============================================
# PART 2: ADVANCED TOKENIZATION
# ============================================

print("\n🔤 PART 2: ADVANCED TOKENIZATION")
print("-" * 50)

print("\n2.1 Regex Tokenization - Custom Patterns")

# Tokenizer for words only (no punctuation)
word_tokenizer = RegexpTokenizer(r'\b\w+\b')
word_tokens = word_tokenizer.tokenize(sample_text)
print(f"Word tokenizer (words only): {word_tokens[:10]}...")

# Tokenizer for sentences
sentence_tokenizer = RegexpTokenizer(r'[^.!?]+[.!?]')
sentence_tokens = sentence_tokenizer.tokenize(sample_text)
print(f"\nSentence tokenizer: {[s.strip() for s in sentence_tokens[:3]]}...")

# Tokenizer for emails
email_tokenizer = RegexpTokenizer(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
emails = email_tokenizer.tokenize(sample_text)
print(f"\nEmail extractor: {emails}")

# Tokenizer for URLs
url_tokenizer = RegexpTokenizer(r'https?://\S+|www\.\S+')
urls = url_tokenizer.tokenize(sample_text)
print(f"URL extractor: {urls}")

# Tokenizer for phone numbers
phone_tokenizer = RegexpTokenizer(r'\+\d-\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}')
phones = phone_tokenizer.tokenize(sample_text)
print(f"Phone extractor: {phones}")

# Tokenizer for dates
date_tokenizer = RegexpTokenizer(r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}')
dates = date_tokenizer.tokenize(sample_text)
print(f"Date extractor: {dates}")

# Tokenizer for hashtags
hashtag_tokenizer = RegexpTokenizer(r'#\w+')
hashtags = hashtag_tokenizer.tokenize(sample_text)
print(f"Hashtag extractor: {hashtags}")

# Tokenizer for mentions
mention_tokenizer = RegexpTokenizer(r'@\w+')
mentions = mention_tokenizer.tokenize(sample_text)
print(f"Mention extractor: {mentions}")

print("\n2.2 Custom Combined Tokenizer")
class AdvancedTokenizer:
    """Advanced tokenizer with multiple pattern support"""
    
    def __init__(self):
        self.patterns = {
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'url': r'https?://\S+|www\.\S+',
            'phone': r'\+\d-\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}',
            'date': r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}',
            'hashtag': r'#\w+',
            'mention': r'@\w+',
            'word': r'\b\w+\b',
            'number': r'\b\d+(?:\.\d+)?\b'
        }
        self.tokenizers = {name: RegexpTokenizer(pattern) 
                          for name, pattern in self.patterns.items()}
    
    def tokenize(self, text, token_type='all'):
        if token_type == 'all':
            results = {}
            for name, tokenizer in self.tokenizers.items():
                tokens = tokenizer.tokenize(text)
                if tokens:
                    results[name] = tokens
            return results
        else:
            return self.tokenizers[token_type].tokenize(text)

advanced_tokenizer = AdvancedTokenizer()
all_tokens = advanced_tokenizer.tokenize(sample_text)

print("\nAll extracted tokens by type:")
for token_type, tokens in all_tokens.items():
    print(f"  {token_type:10}: {tokens}")

# ============================================
# PART 3: CUSTOM STOPWORDS
# ============================================

print("\n🚫 PART 3: CUSTOM STOPWORDS")
print("-" * 50)

# Default stopwords
default_stopwords = set(stopwords.words('english'))
print(f"Default English stopwords: {len(default_stopwords)}")

# Create custom stopwords for specific domains
tech_stopwords = {
    'like', 'just', 'actually', 'really', 'basically', 'quite', 
    'very', 'pretty', 'rather', 'somewhat', 'somehow', 'anyway',
    'meanwhile', 'furthermore', 'nevertheless', 'nonetheless'
}

legal_stopwords = {
    'whereas', 'herein', 'therein', 'hereafter', 'thereafter',
    'hereinafter', 'notwithstanding', 'aforementioned'
}

social_media_stopwords = {
    'lol', 'omg', 'wtf', 'lmao', 'rofl', 'smh', 'tbh', 'idk',
    'imo', 'imho', 'fyi', 'btw', 'thx', 'plz', 'omw'
}

# Combine custom stopwords with defaults
custom_stopwords = default_stopwords.union(tech_stopwords)
print(f"Custom stopwords (including tech): {len(custom_stopwords)}")

# Function to remove custom stopwords
def remove_custom_stopwords(tokens, custom_set=None):
    if custom_set is None:
        custom_set = custom_stopwords
    return [token for token in tokens if token.lower() not in custom_set]

# Test stopword removal
test_tokens = word_tokenizer.tokenize(sample_text.lower())
filtered_tokens = remove_custom_stopwords(test_tokens)

print(f"\nOriginal tokens: {len(test_tokens)}")
print(f"After stopword removal: {len(filtered_tokens)}")
print(f"Removed stopwords: {len(test_tokens) - len(filtered_tokens)}")

# Domain-specific stopwords example
domain_text = "Actually, I really like Python for data science. Basically, it's amazing!"
domain_tokens = word_tokenizer.tokenize(domain_text.lower())
print(f"\nDomain text: {domain_text}")
print(f"Tokens: {domain_tokens}")
print(f"After tech stopword removal: {remove_custom_stopwords(domain_tokens, tech_stopwords)}")

# ============================================
# PART 4: ADVANCED STEMMING
# ============================================

print("\n🌳 PART 4: ADVANCED STEMMING (Multiple Algorithms)")
print("-" * 50)

sample_words = ["running", "ran", "runs", "better", "good", "studies", 
                "studying", "studied", "happiness", "unhappiness", 
                "going", "gone", "went", "maximization", "communication"]

print("Sample words:", sample_words[:8], "...")

# Initialize all stemmers
porter = PorterStemmer()
snowball = SnowballStemmer('english')
lancaster = LancasterStemmer()

print("\nComparing Stemming Algorithms:")
print("-" * 70)
print(f"{'Word':15} {'Porter':15} {'Snowball':15} {'Lancaster':15}")
print("-" * 70)

for word in sample_words:
    print(f"{word:15} {porter.stem(word):15} {snowball.stem(word):15} {lancaster.stem(word):15}")

print("\nStemmer Characteristics:")
print("""
PORTER STEMMER:
├── Oldest and most common
├── 5 phases of rules
├── Moderate aggression
└── Best for: General purpose

SNOWBALL STEMMER:
├── Improved version of Porter
├── Supports multiple languages
├── Better handling of irregular words
└── Best for: Multi-lingual applications

LANCASTER STEMMER:
├── Most aggressive
├── Very fast
├── Can produce very short stems
└── Best for: Information retrieval systems
""")

# ============================================
# PART 5: POS-AWARE LEMMATIZATION
# ============================================

print("\n📖 PART 5: POS-AWARE LEMMATIZATION")
print("-" * 50)

lemmatizer = WordNetLemmatizer()

# Function to get WordNet POS tag
def get_wordnet_pos(treebank_tag):
    """Convert Penn Treebank POS tags to WordNet POS tags"""
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN

def pos_aware_lemmatize(text):
    """Lemmatize text using POS tags for accuracy"""
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    
    lemmatized = []
    for token, tag in pos_tags:
        wordnet_tag = get_wordnet_pos(tag)
        lemma = lemmatizer.lemmatize(token, pos=wordnet_tag)
        lemmatized.append((token, tag, lemma))
    
    return lemmatized

# Test POS-aware lemmatization
test_sentences = [
    "I love running every morning",
    "She loves her pet dog",
    "The running water is cold",
    "Better to be safe than sorry",
    "He studied hard for the exam",
    "She is studying at the library"
]

print("\nPOS-Aware Lemmatization Examples:")
print("-" * 70)

for sentence in test_sentences:
    print(f"\nOriginal: {sentence}")
    lemmatized = pos_aware_lemmatize(sentence)
    print(f"Lemmatized: {' '.join([lemma for _, _, lemma in lemmatized])}")
    print(f"Details: {[(token, tag, lemma) for token, tag, lemma in lemmatized[:3]]}...")

# Compare basic vs POS-aware lemmatization
print("\n\nComparison: Basic vs POS-Aware Lemmatization")
print("-" * 60)

ambiguous_words = [
    ("love", "I love programming"),  # Verb
    ("love", "Her love is pure"),     # Noun
    ("run", "I run every day"),       # Verb
    ("run", "The run was long"),      # Noun
]

for word, sentence in ambiguous_words:
    print(f"\nWord: '{word}' in '{sentence}'")
    
    # Basic lemmatization (default = noun)
    basic_lemma = lemmatizer.lemmatize(word)
    
    # POS-aware lemmatization
    tokens = word_tokenize(sentence)
    pos_tags = pos_tag(tokens)
    word_idx = tokens.index(word)
    wordnet_tag = get_wordnet_pos(pos_tags[word_idx][1])
    pos_lemma = lemmatizer.lemmatize(word, pos=wordnet_tag)
    
    print(f"  Basic lemmatization: {basic_lemma}")
    print(f"  POS-aware lemmatization: {pos_lemma} ({pos_tags[word_idx][1]})")

# ============================================
# PART 6: CUSTOM NAMED ENTITY RECOGNITION
# ============================================

print("\n🏷️ PART 6: CUSTOM NAMED ENTITY RECOGNITION")
print("-" * 50)

class CustomNER:
    """Custom Named Entity Recognizer using patterns and rules"""
    
    def __init__(self):
        # Define custom entity patterns
        self.patterns = {
            'EMAIL': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'URL': r'https?://\S+|www\.\S+',
            'PHONE': r'\+\d-\d{3}-\d{3}-\d{4}|\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4}',
            'DATE': r'\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{4}',
            'HASHTAG': r'#\w+',
            'MENTION': r'@\w+',
            'PRODUCT': r'(iPhone|iPad|MacBook|Google Pixel|Samsung Galaxy)\w*',
            'SKILL': r'(Python|Java|JavaScript|React|Angular|Node\.js|SQL|AWS)\w*'
        }
        
        self.compiled_patterns = {name: re.compile(pattern, re.IGNORECASE) 
                                  for name, pattern in self.patterns.items()}
    
    def extract_entities(self, text):
        """Extract custom entities from text"""
        entities = {}
        
        for entity_type, pattern in self.compiled_patterns.items():
            matches = pattern.findall(text)
            if matches:
                entities[entity_type] = matches
        
        return entities
    
    def extract_with_context(self, text):
        """Extract entities with position information"""
        entities = []
        
        for entity_type, pattern in self.compiled_patterns.items():
            for match in pattern.finditer(text):
                entities.append({
                    'entity': match.group(),
                    'type': entity_type,
                    'start': match.start(),
                    'end': match.end()
                })
        
        return sorted(entities, key=lambda x: x['start'])

# Test custom NER
custom_ner = CustomNER()

test_text = """
I'm looking for a Python developer with 5 years of experience.
Contact me at hiring@techcorp.com or call 123-456-7890.
The ideal candidate knows React and AWS.
Check our website: https://www.techcorp.com/careers
Follow us @TechCorp #Hiring #PythonJobs
"""

print(f"Test Text: {test_text}")
print("\nCustom Entity Extraction:")
print("-" * 50)

entities = custom_ner.extract_entities(test_text)
for entity_type, matches in entities.items():
    print(f"  {entity_type}: {matches}")

entities_with_context = custom_ner.extract_with_context(test_text)
print("\nEntities with position information:")
for entity in entities_with_context:
    print(f"  '{entity['entity']}' → {entity['type']} (positions {entity['start']}-{entity['end']})")

# ============================================
# PART 7: PRODUCTION-READY NLP PIPELINE
# ============================================

print("\n🔧 PART 7: PRODUCTION-READY NLP PIPELINE")
print("-" * 50)

import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ProductionNLPPipeline:
    """Complete production-ready NLP pipeline"""
    
    def __init__(self, custom_stopwords=None):
        self.logger = logging.getLogger(__name__)
        
        # Initialize components
        self.word_tokenizer = RegexpTokenizer(r'\b\w+\b')
        self.sentence_tokenizer = RegexpTokenizer(r'[^.!?]+[.!?]')
        self.custom_ner = CustomNER()
        self.lemmatizer = WordNetLemmatizer()
        
        # Setup stopwords
        default_stopwords = set(stopwords.words('english'))
        if custom_stopwords:
            self.stopwords = default_stopwords.union(custom_stopwords)
        else:
            self.stopwords = default_stopwords
        
        self.logger.info("NLP Pipeline initialized")
    
    def preprocess(self, text, remove_stopwords=True):
        """Basic text preprocessing"""
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation (optional)
        text = re.sub(r'[^\w\s]', ' ', text)
        
        # Tokenize
        tokens = self.word_tokenizer.tokenize(text)
        
        # Remove stopwords
        if remove_stopwords:
            tokens = [t for t in tokens if t not in self.stopwords]
        
        return tokens
    
    def advanced_preprocess(self, text):
        """Advanced preprocessing with POS-aware lemmatization"""
        # Tokenize
        tokens = word_tokenize(text.lower())
        
        # POS tagging
        pos_tags = pos_tag(tokens)
        
        # Lemmatize with POS context
        lemmatized = []
        for token, tag in pos_tags:
            if token not in self.stopwords:
                wordnet_tag = get_wordnet_pos(tag)
                lemma = self.lemmatizer.lemmatize(token, pos=wordnet_tag)
                lemmatized.append(lemma)
        
        return lemmatized
    
    def extract_features(self, text):
        """Extract various features from text"""
        features = {}
        
        # Basic statistics
        features['char_count'] = len(text)
        features['word_count'] = len(self.word_tokenizer.tokenize(text))
        features['sentence_count'] = len(self.sentence_tokenizer.tokenize(text))
        
        # Entities
        entities = self.custom_ner.extract_entities(text)
        features['has_email'] = 'EMAIL' in entities
        features['has_phone'] = 'PHONE' in entities
        features['has_url'] = 'URL' in entities
        features['has_hashtag'] = 'HASHTAG' in entities
        
        # Average word length
        words = self.word_tokenizer.tokenize(text)
        if words:
            features['avg_word_length'] = sum(len(w) for w in words) / len(words)
        else:
            features['avg_word_length'] = 0
        
        return features
    
    def process(self, text, verbose=False):
        """Complete NLP pipeline processing"""
        start_time = datetime.now()
        
        try:
            result = {
                'original_text': text,
                'preprocessed_tokens': self.preprocess(text),
                'advanced_tokens': self.advanced_preprocess(text),
                'entities': self.custom_ner.extract_entities(text),
                'features': self.extract_features(text),
                'timestamp': start_time.isoformat()
            }
            
            processing_time = (datetime.now() - start_time).total_seconds()
            result['processing_time'] = processing_time
            
            if verbose:
                self.logger.info(f"Processed {len(text)} chars in {processing_time:.3f}s")
                self.logger.info(f"Found {len(result['entities'])} entity types")
            
            return result
            
        except Exception as e:
            self.logger.error(f"Error processing text: {str(e)}")
            return {'error': str(e)}
    
    def process_batch(self, texts, verbose=False):
        """Process multiple texts in batch"""
        results = []
        for i, text in enumerate(texts):
            if verbose:
                self.logger.info(f"Processing {i+1}/{len(texts)}")
            results.append(self.process(text, verbose=False))
        return results

# Test the production pipeline
nlp_pipeline = ProductionNLPPipeline(custom_stopwords=tech_stopwords)

print("\nTesting Production Pipeline:")
print("-" * 50)

test_input = """
Hello World! This is a test for our NLP pipeline.
Contact me at john.doe@example.com or call (555) 123-4567.
I have 10 years of Python experience and know AWS and React.
Check https://github.com/NeuralAICodeCraft for more!
"""

result = nlp_pipeline.process(test_input, verbose=True)

print("\nPipeline Results:")
print(f"  Preprocessed tokens: {result['preprocessed_tokens'][:10]}...")
print(f"  Advanced tokens: {result['advanced_tokens'][:10]}...")
print(f"  Entities found: {result['entities']}")
print(f"  Features: {result['features']}")
print(f"  Processing time: {result['processing_time']:.3f}s")

# ============================================
# PART 8: REAL-WORLD EXAMPLE - RESUME PARSER
# ============================================

print("\n💼 PART 8: REAL-WORLD EXAMPLE - RESUME PARSER")
print("-" * 50)

class ResumeParser:
    """Custom resume parser using NLP techniques"""
    
    def __init__(self):
        self.skills_keywords = {
            'Programming': ['Python', 'Java', 'JavaScript', 'C++', 'Go', 'Rust'],
            'Web': ['React', 'Angular', 'Vue', 'Node.js', 'Django', 'Flask'],
            'Data': ['SQL', 'Pandas', 'NumPy', 'TensorFlow', 'PyTorch', 'scikit-learn'],
            'Cloud': ['AWS', 'Azure', 'GCP', 'Docker', 'Kubernetes']
        }
        
        self.nlp_pipeline = ProductionNLPPipeline()
        
        # Flatten skills for easy lookup
        self.all_skills = set()
        for category, skills in self.skills_keywords.items():
            self.all_skills.update(skills)
    
    def parse_resume(self, text):
        """Parse resume and extract key information"""
        result = {
            'skills_found': [],
            'emails': [],
            'phones': [],
            'years_experience': None,
            'education': []
        }
        
        # Extract entities
        entities = self.nlp_pipeline.custom_ner.extract_entities(text)
        
        # Extract emails
        if 'EMAIL' in entities:
            result['emails'] = entities['EMAIL']
        
        # Extract phones
        if 'PHONE' in entities:
            result['phones'] = entities['PHONE']
        
        # Extract skills
        tokens = self.nlp_pipeline.preprocess(text, remove_stopwords=True)
        for skill in self.all_skills:
            if skill.lower() in ' '.join(tokens):
                result['skills_found'].append(skill)
        
        # Extract years of experience using regex
        exp_pattern = r'(\d+)\+?\s*(?:years?|yrs?)\s*(?:of\s*)?experience'
        exp_matches = re.findall(exp_pattern, text, re.IGNORECASE)
        if exp_matches:
            result['years_experience'] = int(exp_matches[0])
        
        # Categorize skills
        result['skills_by_category'] = {}
        for category, skills in self.skills_keywords.items():
            category_skills = [s for s in result['skills_found'] if s in skills]
            if category_skills:
                result['skills_by_category'][category] = category_skills
        
        return result

# Test resume parser
sample_resume = """
John Doe
Email: john.doe@email.com | Phone: (555) 123-4567

Summary
Experienced software engineer with 8+ years of experience in Python and cloud technologies.

Skills
- Programming: Python, Java, JavaScript
- Web Frameworks: React, Django
- Data Science: Pandas, NumPy, TensorFlow
- Cloud: AWS, Docker, Kubernetes

Experience
Senior Python Developer at TechCorp (2020-Present)
- Developed microservices using Python and AWS
- Implemented CI/CD pipelines with Docker and Kubernetes

Education
MS in Computer Science, Stanford University
"""

resume_parser = ResumeParser()
parsed_resume = resume_parser.parse_resume(sample_resume)

print("\nParsed Resume Results:")
print("-" * 50)
print(f"  Emails found: {parsed_resume['emails']}")
print(f"  Phones found: {parsed_resume['phones']}")
print(f"  Years experience: {parsed_resume['years_experience']}")
print(f"  Skills found: {parsed_resume['skills_found']}")
print(f"  Skills by category: {parsed_resume['skills_by_category']}")

# ============================================
# PART 9: PERFORMANCE COMPARISON
# ============================================

print("\n📊 PART 9: PERFORMANCE COMPARISON")
print("-" * 50)

import time

def benchmark_stemmers(text, n_iterations=100):
    """Benchmark different stemming algorithms"""
    words = word_tokenizer.tokenize(text)
    
    results = {}
    
    # Porter
    start = time.time()
    for _ in range(n_iterations):
        [porter.stem(w) for w in words]
    results['Porter'] = time.time() - start
    
    # Snowball
    start = time.time()
    for _ in range(n_iterations):
        [snowball.stem(w) for w in words]
    results['Snowball'] = time.time() - start
    
    # Lancaster
    start = time.time()
    for _ in range(n_iterations):
        [lancaster.stem(w) for w in words]
    results['Lancaster'] = time.time() - start
    
    return results

benchmark_text = "The quick brown fox jumps over the lazy dog. " * 100
stemming_times = benchmark_stemmers(benchmark_text)

print("\nStemming Performance (100 iterations):")
print("-" * 40)
for stemmer, duration in stemming_times.items():
    print(f"  {stemmer}: {duration:.4f} seconds")

print("\n" + "=" * 70)
print("✅ NLP FUNDAMENTALS PART 2 COMPLETE!")
print("=" * 70)
print("""
WHAT YOU'VE MASTERED:
├── ✅ Advanced Tokenization (Regex, Custom Patterns)
├── ✅ Custom Stopwords (Domain-specific)
├── ✅ Multiple Stemming Algorithms (Porter, Snowball, Lancaster)
├── ✅ POS-Aware Lemmatization (Context matters!)
├── ✅ Custom Named Entity Recognition
├── ✅ Production-Ready NLP Pipeline
└── ✅ Real-World Example (Resume Parser)

SKILLS ACQUIRED:
├── 🎯 Build production-ready text processing systems
├── 🎯 Extract specific information using custom patterns
├── 🎯 Optimize NLP pipelines for real-world data
├── 🎯 Handle edge cases and domain-specific requirements
└── 🎯 Create reusable NLP components

NEXT STEPS:
├── 🚀 Text Representation (Bag of Words, TF-IDF)
├── 🚀 Sentiment Analysis with Machine Learning
├── 🚀 Topic Modeling (LDA)
├── 🚀 Sequence-to-Sequence Models
├── 🚀 Transformers (BERT, GPT)
└── 🚀 Building Production APIs for NLP

📺 WATCH THE VIDEO TUTORIAL ON NEURALAICODECRAFT
🔗 FULL CODE ON GITHUB
💬 SHARE YOUR CUSTOM NLP PIPELINES IN COMMENTS!
""")
