import spacy
import pandas as pd
import numpy as np
import pandas as pd
from spacy.vectors import Vectors
import nltk
import task8


model1= spacy.load('en_core_web_lg')
df = pd.read_csv('./winemag-data-130k-v2.csv')
df.head()

sen="I like so much drinking wine "

exsentence=model1(sen)
index=0
sentence_vector=[]
max=0
for i in range(100):
    tup=task8.find_sent(sen,df[df['country']=='US']['description'].values[i].split('. '))
    distance=tup[1]
    
    if distance>max:
        max=distance
        sentence=tup[0]

print(sentence,max)