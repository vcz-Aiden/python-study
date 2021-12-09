import pandas as pd
import nltk
import random
from nltk.tokenize import word_tokenize

nltk.download('punkt')

df = pd.read_excel('comment_youtube_pn.xlsx', engine='openpyxl')

data = ([(pos['comment'], 'positive') for index, pos in df[2:105].iterrows()] +
        [(neg['comment'], 'negative') for index, neg in df[106:204].iterrows()])

print(data[0:3])

tokens = set(word.lower() for words in data for word in word_tokenize(words[0]))
train = [({word: (word in word_tokenize(x[0])) for word in tokens}, x[1]) for x in data]

random.shuffle(train)
train_x = train[0 : len(train) // 11 * 10]
test_x = train[len(train) // 11 * 10 : len(train)]

model = nltk.NaiveBayesClassifier.train(train_x)
print(model.show_most_informative_features())

acc=nltk.classify.accuracy(model, test_x)
print("Accuracy:", acc)