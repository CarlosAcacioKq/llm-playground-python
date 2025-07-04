import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
nltk.download('punkt')
sample_text = "I am learning NLP (Natural Language Processing)"
tokens = word_tokenize(sample_text)

# Unigram
unigrams = list(ngrams(tokens, 1))
print("Unigrams:", unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))
print("Bigrams:", bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))
print("Trigrams:", trigrams)



#N-grams are sequences of ‘n’ words from text. They help analyze common word patterns, useful for tasks like predicting the next word.
