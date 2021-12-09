import pandas as pd
import nltk
import random
from nltk.tokenize import word_tokenize

def contain_no_name(s):
    result_flag = True
    names = ['지효', '지석진', '전소민']
    for name in names:
        if (name in s):
            result_flag = False
            break

    return result_flag

def word_compress(s):
    if (len(s) == 1) :
        return s

    initial = s[0]
    one_word_flag = True

    for w in s:
        if (initial != w):
            one_word_flag = False
            break

    if (one_word_flag) :
        return initial + initial
    else :
        return s

nltk.download('punkt')

df = pd.read_excel('comment_youtube_pn.xlsx', engine='openpyxl')

data = ([(pos['comment'], 'positive') for index, pos in df[2:105].iterrows()] +
        [(neg['comment'], 'negative') for index, neg in df[106:204].iterrows()])


#make tokens
tokens = set()

for words in data:
    for word in word_tokenize(words[0]):
        word = word_compress(word.lower())
        if (contain_no_name(word)):
            tokens.add(word)


#make train data
train = []

for x in data:
    compare_list = set()
    for word in word_tokenize(x[0]):
        word = word_compress(word.lower())
        if (contain_no_name(word)):
            compare_list.add(word)

    temp = dict()
    for word in tokens:
        temp[word] = word in compare_list

    train.append((temp, x[1]))


#make model and verification
random.shuffle(train)
train_x = train[0 : len(train) // 11 * 10]
test_x = train[len(train) // 11 * 10 : len(train)]

model = nltk.NaiveBayesClassifier.train(train_x)
print(model.show_most_informative_features())

acc=nltk.classify.accuracy(model, test_x)
print("Accuracy:", acc)


input("start testing?")

df2 = pd.read_excel('comment_youtube3.xlsx', engine='openpyxl')
#df2 = pd.read_excel('comment_youtube_pn.xlsx', engine='openpyxl')

print(len(df2['comment']))

for test in df2['comment']:
    t_features = dict()

    compare_list = set()
    for word in word_tokenize(test):
        word = word_compress(word.lower())
        if (contain_no_name(word)):
            compare_list.add(word)

    for word in tokens:
        t_features[word] = word in compare_list

    print(test, " : ", model.classify(t_features))