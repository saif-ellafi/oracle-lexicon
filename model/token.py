from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

"""
IMPLEMENT ALL POSSIBLE WORD TOKENIZERS HERE
"""

STOP_WORDS = set(stopwords.words('english'))


def tokenize_sentence(sentence):
    return [w for w in word_tokenize(sentence) if w not in STOP_WORDS and len(w) > 3]
