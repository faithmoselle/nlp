"""
PROGRAM: NLP Tokenization with NLTK and spaCy
FILE: nlp_tokenization_demo.ipynb
LANGUAGE: Python 3
TOPIC: Natural Language Processing (NLP) - Tokenization
TECH STACK: NLTK, spaCy, Google Colab

DESCRIPTION:
Demonstrates word tokenization using two major NLP libraries:
- NLTK: Comprehensive, educational, many corpora
- spaCy: Industrial-strength, fast, production-ready
"""

# Install required libraries (run in Colab terminal)
!pip install nltk spacy

# ========== IMPORTS ==========
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from spacy.lang.en import English

# ========== DOWNLOAD NLTK RESOURCES ==========
nltk.download('punkt')       # Tokenizer model for sentence/word splitting
nltk.download('stopwords')   # Common words (is, and, the, etc.)

# ========== LOAD SPA CY MODEL ==========
nlp = English()              # Minimal English model (no vectors)

# ========== TEXT SAMPLES ==========
text = 'NLP is fascinating field'                    # English text
text1 = 'Nag-aaral ako sa La Salle and I am a computer science student'  # Mixed Tagalog/English

# ========== NLTK TOKENIZATION ==========
tokens = word_tokenize(text)
tokens1 = word_tokenize(text1)

print('Tokens using NLTK (English):', tokens)
print('Tokens using NLTK (Mixed):', tokens1)

# ========== SPA CY TOKENIZATION ==========
doc = nlp(text)
doc1 = nlp(text1)

# Extract token texts from spaCy Doc objects
spacy_tokens = [token.text for token in doc]
spacy_tokens1 = [token.text for token in doc1]

print('Tokens using spaCy (English):', spacy_tokens)
print('Tokens using spaCy (Mixed):', spacy_tokens1)