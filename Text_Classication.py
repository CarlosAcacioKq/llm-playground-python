#categorizing text into different groups, ex. spam and non-spam e-mails
#Naive Bayes classifier: assumes that all features(like words in a text) are independent from each other. (scikit-learn) library 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

texts = [
  'I love programming.', 'Python is amazing.',
  'I enjoy machine learning.', 'The weather is nice today.', 'I like algo.',
  'Machine learning is fascinating.', 'Natural Language Processing is a part of AI.'
]

labels = [
  'tech', 'tech', 'tech', 'non-tech', 'tech', 'tech', 'tech'
]

#Convert our text data into matrix of tokens
vectorizer = CountVectorizer()
x = vectorizer.fit_transform(texts)

#train_test_split function splits the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size = 0.2, random_state=42)

#MultinomialNB classifier to train the model on our trianing data.
model = MultinomialNB()
model.fit(x_train, y_train)

#Use the trained model to predict the labels for the test set.
y_pred = model.predict(x_test)

#Calculate and print the accuracy of the model by comparing the predicted labels with the actual labels in the set.
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
