from typing import Awaitable
import nltk
from nltk import bigrams, trigrams
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


f = open('./bilim.txt', encoding="utf-8")
raw = f.read()
tokens = nltk.word_tokenize(raw)

fdist = nltk.FreqDist(tokens)
i=0
high_=[]
low_=[]

for k,v in fdist.items():
    if(len(k)>1):
        if(5<v and i<100):
            i+=1
            print(k,v)
            high_.append (k)

        if(5>=v and i<100):
            i+=1
            low_.append(k)


print("\n\n\n\n")
print("low frequency                   high frequency ")
print("----------------                -----------------")
for words in low_:
    value=process.extract(words,high_)
    simWord=value[0][0]
    sim_=value[0][1]
    print(words,"    ->    ",simWord, "   %",sim_,"\n")