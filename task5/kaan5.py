import trnlp
import nltk
import string
from nltk import FreqDist
import pandas as pd
import numpy as np
from string import punctuation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD


bodytext = open(r'deneme.txt', 'r', encoding='utf-8')
body = bodytext.read()
bodt=body.translate(str.maketrans("", "", string.punctuation + "“" + "”" + "’"))
tokens = nltk.word_tokenize(bodt)

print("--WORDS---")
wordfreq = nltk.FreqDist(tokens)
for i,k in wordfreq.items():
    print (i,k)

print("--bigrams----------")
bigram=nltk.bigrams(tokens)
wordfreq = nltk.FreqDist(bigram)
for i,k in wordfreq.items():
    if(k>=5):
        print (i,k)


trigram = nltk.trigrams(tokens)
print("--trigrams------")
wordfreq = nltk.FreqDist(trigram)
for i,k in wordfreq.items():
    if(k>5):
        print (i,k)


bodytext.close()
bodytext = open(r'deneme.txt', 'r', encoding='utf-8')
body1=bodytext.readlines()
vectorizer = CountVectorizer()
bag_of_words = vectorizer.fit_transform(body1)
bag_of_words.todense()

svd = TruncatedSVD(n_components=2)
lsa = svd.fit_transform(bag_of_words)

topic_encoded_df = pd.DataFrame(lsa, columns=["topic_1", "topic_2"])
topic_encoded_df["body"] = body1
print(topic_encoded_df[["body", "topic_1", "topic_2"]])
dictionary = vectorizer.get_feature_names()


encoding_matrix = pd.DataFrame(svd.components_, index=['topic_1', 'topic_2'], columns=dictionary).T
print(encoding_matrix)

encoding_matrix['abs_topic_1'] = np.abs(encoding_matrix['topic_1'])
encoding_matrix['abs_topic_2'] = np.abs(encoding_matrix['topic_2'])

print(encoding_matrix.sort_values('abs_topic_1', ascending=True))
print(encoding_matrix.sort_values('abs_topic_2', ascending=True))