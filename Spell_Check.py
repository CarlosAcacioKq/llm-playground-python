from textblob import TextBlob

#intentional spelling error
text = 'I love programmig and machine learnig.'

blob = TextBlob(text)

corrected_text = blob.correct()

print('Original Text:', text)
print('Corrected Text:', corrected_text)
