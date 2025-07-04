#Tokens  are small units of data used to train gen AI models that help them understand and generate language
import nltk
#tokenizing some text
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize

sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)

print('Tokens:', tokens)