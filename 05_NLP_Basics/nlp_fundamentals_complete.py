"""
COMPLETE NLP FUNDAMENTALS TUTORIAL
NeuralAICodeCraft - From Tokenization to NER

Topics Covered:
1. What is NLP & Phases of NLP
2. NLTK Installation
3. Tokenization (Word, Sentence, Custom)
4. Stemming & Lemmatization
5. POS Tagging
6. Named Entity Recognition (NER)
"""

import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords, wordnet
from nltk import pos_tag, ne_chunk

# Download required NLTK data (uncomment on first run)
print("🔧 Downloading NLTK data...")
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('punkt_tab')
print("✅ NLTK data ready!\n")

print("=" * 70)
print("🧠 COMPLETE NLP FUNDAMENTALS TUTORIAL")
print("NeuralAICodeCraft")
print("=" * 70)

# ============================================
# PART 1: WHAT IS NLP?
# ============================================

print("\n📚 PART 1: WHAT IS NATURAL LANGUAGE PROCESSING?")
print("-" * 50)

print("""
NLP (Natural Language Processing) is a branch of AI that helps computers 
understand, interpret, and manipulate human language.

REAL-WORLD APPLICATIONS:
├── ChatGPT & Bard (Conversational AI)
├── Google Translate (Machine Translation)
├── Siri & Alexa (Voice Assistants)
├── Email Spam Filters (Text Classification)
├── Grammar Checkers (Grammarly)
├── Sentiment Analysis (Social Media Monitoring)
└── Search Engines (Google, Bing)
""")

# ============================================
# PART 2: PHASES OF NLP
# ============================================

print("\n📚 PART 2: PHASES OF NLP")
print("-" * 50)

print("""
PHASE 1: MORPHOLOGICAL ANALYSIS
├── Studies word structure and formation
├── Breaks words into morphemes (prefix, root, suffix)
└── Example: 'unhappiness' → 'un-' + 'happy' + '-ness'

PHASE 2: SYNTACTIC ANALYSIS (Parsing)
├── Analyzes grammar and sentence structure
├── Checks if sentence follows grammar rules
└── Example: "I love Python" → Subject + Verb + Object

PHASE 3: SEMANTIC ANALYSIS
├── Understands meaning of words and sentences
├── Handles synonyms, antonyms, word senses
└── Example: "Bank" can be financial OR river bank

PHASE 4: DISCOURSE INTEGRATION
├── Considers context across multiple sentences
├── Understands pronouns and references
└── Example: "John arrived. He sat down." → 'He' refers to John

PHASE 5: PRAGMATIC ANALYSIS
├── Understands intent and real-world knowledge
├── Handles sarcasm, idioms, cultural context
└── Example: "Can you pass the salt?" = Request, not question
""")

# ============================================
# PART 3: SAMPLE TEXT
# ============================================

sample_text = """
Natural Language Processing is fascinating. It helps computers understand human language.
ChatGPT, Google Translate, and Siri all use NLP. Mr. John Smith lives in New York City.
He works at Google as an AI Engineer. The meeting is scheduled for January 15th, 2024.
"""

print("\n📝 SAMPLE TEXT FOR DEMONSTRATION:")
print("-" * 50)
print(sample_text)

# ============================================
# PART 4: TOKENIZATION
# ============================================

print("\n🔤 PART 4: TOKENIZATION")
print("-" * 50)

print("\n4.1 SENTENCE TOKENIZATION")
print("Split text into individual sentences:")

sentences = sent_tokenize(sample_text)
for i, sentence in enumerate(sentences, 1):
    print(f"  Sentence {i}: {sentence.strip()}")

print(f"\nTotal sentences: {len(sentences)}")

print("\n4.2 WORD TOKENIZATION")
print("Split text into individual words:")

words = word_tokenize(sample_text)
print(f"Words: {words[:15]}...")  # First 15 words
print(f"Total words: {len(words)}")

print("\n4.3 CUSTOM TOKENIZATION")
print("Using Regular Expressions:")

# Custom tokenizer for specific patterns
custom_pattern = r'\b\w+\b'  # Match words only (no punctuation)
custom_tokens = re.findall(custom_pattern, sample_text.lower())
print(f"Custom tokens (no punctuation): {custom_tokens[:15]}...")
print(f"Total custom tokens: {len(custom_tokens)}")

# Punctuation-based tokenizer
punct_pattern = r'[.!?]+'  # Find sentence boundaries
punct_tokens = re.findall(punct_pattern, sample_text)
print(f"Punctuation tokens: {punct_tokens}")

# ============================================
# PART 5: STEMMING & LEMMATIZATION
# ============================================

print("\n🌳 PART 5: STEMMING & LEMMATIZATION")
print("-" * 50)

# Sample words for demonstration
sample_words = ["running", "ran", "runs", "better", "good", 
                "studies", "studying", "studied", "happiness", 
                "unhappiness", "going", "gone", "went"]

print("Sample words:", sample_words)

print("\n5.1 STEMMING (Porter Stemmer)")
stemmer_porter = PorterStemmer()
print("\nWord → Stem")
print("-" * 30)
for word in sample_words:
    stemmed = stemmer_porter.stem(word)
    print(f"{word:12} → {stemmed}")

print("\n5.2 STEMMING (Snowball Stemmer - Better for English)")
stemmer_snowball = SnowballStemmer('english')
print("\nWord → Stem")
print("-" * 30)
for word in sample_words:
    stemmed = stemmer_snowball.stem(word)
    print(f"{word:12} → {stemmed}")

print("\n5.3 LEMMATIZATION (WordNet)")
lemmatizer = WordNetLemmatizer()
print("\nWord → Lemma (base form)")
print("-" * 35)
for word in sample_words:
    lemma = lemmatizer.lemmatize(word, pos='v')  # pos='v' for verb
    print(f"{word:12} → {lemma}")

print("\n5.4 STEMMING vs LEMMATIZATION - Detailed Comparison")
comparison_words = ["studies", "studying", "studied", "better", "went", "gone"]
print(f"{'Word':12} {'Stem':12} {'Lemma':12}")
print("-" * 40)
for word in comparison_words:
    stem = stemmer_snowball.stem(word)
    lemma = lemmatizer.lemmatize(word, pos='v')
    print(f"{word:12} {stem:12} {lemma:12}")

print("\n5.5 WHEN TO USE WHAT?")
print("""
STEMMING:
├── Faster (just cuts endings)
├── Less accurate (produces non-words)
├── Good for: Search engines, Information retrieval
└── Example: 'running' → 'run'

LEMMATIZATION:
├── Slower (uses dictionary lookup)
├── More accurate (real words only)
├── Good for: Chatbots, Sentiment analysis, Q&A systems
└── Example: 'better' → 'good'
""")

# ============================================
# PART 6: STOPWORDS
# ============================================

print("\n🚫 PART 6: STOPWORDS REMOVAL")
print("-" * 50)

stop_words = set(stopwords.words('english'))
print(f"Total English stopwords: {len(stop_words)}")
print(f"Sample stopwords: {list(stop_words)[:20]}")

# Remove stopwords from tokenized text
filtered_words = [word.lower() for word in words 
                  if word.lower() not in stop_words and word.isalpha()]

print(f"\nOriginal word count: {len(words)}")
print(f"After stopword removal: {len(filtered_words)}")
print(f"Filtered words (first 20): {filtered_words[:20]}")

# ============================================
# PART 7: POS TAGGING
# ============================================

print("\n📖 PART 7: POS TAGGING (Parts of Speech)")
print("-" * 50)

# Get POS tags for the filtered words
pos_tags = pos_tag(filtered_words[:20])  # First 20 words

print("\nPOS Tag Examples:")
print("Tag Description:")
print("-" * 50)
print("""
POS TAG  MEANING          EXAMPLE
───────  ───────────────  ───────────────────
NN       Noun             'python', 'language'
NNS      Plural Noun      'computers', 'dogs'
VB       Verb              'love', 'run'
VBD      Past Tense Verb   'loved', 'ran'
JJ       Adjective         'beautiful', 'great'
RB       Adverb            'quickly', 'very'
DT       Determiner        'the', 'a', 'an'
IN       Preposition       'in', 'on', 'at'
CC       Conjunction       'and', 'but', 'or'
PRP      Pronoun           'he', 'she', 'it'
""")

print("\nPOS Tags for sample text:")
print("-" * 50)
for word, tag in pos_tags[:15]:
    print(f"  {word:15} → {tag}")

# Detailed POS tagging on a sentence
test_sentence = "The quick brown fox jumps over the lazy dog"
test_tokens = word_tokenize(test_sentence)
test_tags = pos_tag(test_tokens)

print(f"\nDetailed POS for: '{test_sentence}'")
print("-" * 50)
for word, tag in test_tags:
    print(f"  {word:10} → {tag}")

# ============================================
# PART 8: NAMED ENTITY RECOGNITION (NER)
# ============================================

print("\n🏷️ PART 8: NAMED ENTITY RECOGNITION (NER)")
print("-" * 50)

print("""
NER identifies real-world entities in text:
├── PERSON: People's names (John Smith, Elon Musk)
├── ORGANIZATION: Companies, agencies (Google, UN)
├── LOCATION: Cities, countries, landmarks (New York, Paris)
├── DATE: Dates, time periods (January 15th, 2024)
├── TIME: Specific times (10:30 AM)
├── MONEY: Monetary values ($100, 50 dollars)
├── PERCENT: Percentages (50%, 25 percent)
└── PRODUCT: Products, software (iPhone, Python)
""")

# Sample text for NER
ner_text = """
Apple Inc. was founded by Steve Jobs and Steve Wozniak in Cupertino, California on April 1, 1976.
Microsoft Corporation, led by Bill Gates, is headquartered in Redmond, Washington.
Google's CEO Sundar Pichai announced a new product worth $1 billion in Mountain View.
"""

print(f"\nSample text for NER: {ner_text}")

# Tokenize and tag
ner_tokens = word_tokenize(ner_text)
ner_pos_tags = pos_tag(ner_tokens)
ner_tree = ne_chunk(ner_pos_tags)

print("\nExtracted Named Entities:")
print("-" * 50)

# Extract entities
entities = []
for subtree in ner_tree:
    if hasattr(subtree, 'label'):
        entity = ' '.join([token for token, pos in subtree])
        label = subtree.label()
        entities.append((entity, label))
        print(f"  {entity:30} → {label}")

# Alternative: Using nltk's ne_chunk with binary=True
print("\nAlternative NER (binary - just recognizes names):")
ner_binary = ne_chunk(ner_pos_tags, binary=True)
entity_count = 0
for subtree in ner_binary:
    if hasattr(subtree, 'label'):
        entity_count += 1
        print(f"  Found: {' '.join([token for token, pos in subtree])}")

print(f"\nTotal named entities found: {len(entities)}")

# ============================================
# PART 9: COMPLETE NLP PIPELINE
# ============================================

print("\n🔗 PART 9: COMPLETE NLP PIPELINE")
print("-" * 50)

def complete_nlp_pipeline(text, verbose=True):
    """
    Complete NLP pipeline from raw text to extracted information
    """
    if verbose:
        print(f"\n📝 INPUT TEXT: {text[:100]}...")
    
    # Step 1: Sentence Tokenization
    sentences = sent_tokenize(text)
    if verbose:
        print(f"\n📌 STEP 1: {len(sentences)} sentences found")
    
    # Step 2: Word Tokenization
    words = word_tokenize(text)
    if verbose:
        print(f"📌 STEP 2: {len(words)} words found")
    
    # Step 3: Stopword Removal
    stop_words = set(stopwords.words('english'))
    filtered_words = [word.lower() for word in words 
                      if word.lower() not in stop_words and word.isalpha()]
    if verbose:
        print(f"📌 STEP 3: {len(filtered_words)} words after stopword removal")
    
    # Step 4: Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized = [lemmatizer.lemmatize(word, pos='v') for word in filtered_words]
    if verbose:
        print(f"📌 STEP 4: Lemmatization complete")
    
    # Step 5: POS Tagging
    pos_tags = pos_tag(filtered_words[:20])  # First 20 for demo
    if verbose:
        print(f"📌 STEP 5: POS tagging complete on first 20 words")
    
    # Step 6: NER
    pos_tags_full = pos_tag(words)
    ner_result = ne_chunk(pos_tags_full)
    entities = []
    for subtree in ner_result:
        if hasattr(subtree, 'label'):
            entity = ' '.join([token for token, pos in subtree])
            entities.append((entity, subtree.label()))
    if verbose:
        print(f"📌 STEP 6: Found {len(entities)} named entities")
    
    return {
        'sentences': sentences,
        'words': words,
        'filtered_words': filtered_words,
        'lemmatized': lemmatized,
        'pos_tags': pos_tags,
        'entities': entities,
        'total_sentences': len(sentences),
        'total_words': len(words),
        'total_filtered': len(filtered_words),
        'total_entities': len(entities)
    }

# Run pipeline on sample
result = complete_nlp_pipeline(sample_text, verbose=True)

print("\n📊 PIPELINE RESULTS SUMMARY:")
print("-" * 50)
print(f"  Total sentences: {result['total_sentences']}")
print(f"  Total words: {result['total_words']}")
print(f"  Words after preprocessing: {result['total_filtered']}")
print(f"  Named entities found: {result['total_entities']}")

if result['entities']:
    print("\n  Extracted Entities:")
    for entity, label in result['entities']:
        print(f"    • {entity:25} → {label}")

# ============================================
# PART 10: PRACTICE EXERCISES
# ============================================

print("\n📝 PART 10: PRACTICE EXERCISES")
print("-" * 50)

print("""
🎯 EXERCISE 1: Tokenization Challenge
Take this text: "Dr. Smith went to New York. He visited the UN headquarters on Jan 15, 2024."
Perform sentence and word tokenization.

🎯 EXERCISE 2: Stemming vs Lemmatization
Apply both stemming and lemmatization to: 'caring', 'cared', 'cares', 'better', 'best'

🎯 EXERCISE 3: POS Tagging
Tag the sentence: "The beautiful flowers bloom in spring"

🎯 EXERCISE 4: NER Challenge
Extract all named entities from: "Elon Musk founded SpaceX in Hawthorne, California"

🎯 EXERCISE 5: Complete Pipeline
Build a function that takes any news article and returns:
- List of all persons mentioned
- List of all organizations
- List of all locations
- Most common verbs

💡 EXTRA: Create your own news article and run the complete pipeline!
""")

print("\n" + "=" * 70)
print("✅ NLP FUNDAMENTALS COMPLETE!")
print("=" * 70)
print("""
WHAT YOU'VE LEARNED:
├── ✅ What is NLP and its real-world applications
├── ✅ The 5 phases of NLP processing
├── ✅ NLTK installation and setup
├── ✅ Word and sentence tokenization
├── ✅ Stemming vs Lemmatization with examples
├── ✅ POS tagging for grammatical analysis
├── ✅ Named Entity Recognition (NER)
├── ✅ Complete NLP pipeline from raw text to insights

NEXT STEPS:
├── Practice with different texts (news, social media, books)
├── Build a simple text summarizer
├── Create a chatbot using NLU
├── Explore advanced NLP with transformers
└── Check out the next video: Text Representation (BoW, TF-IDF)

📺 WATCH THE VIDEO TUTORIAL ON NEURALAICODECRAFT
🔗 GITHUB: Complete code available
💬 COMMENTS: Share your practice results!
""")