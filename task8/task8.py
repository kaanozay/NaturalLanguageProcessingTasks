import spacy
import pandas as pd
import numpy as np
import pandas as pd
from spacy.vectors import Vectors
import nltk



model1= spacy.load('en_core_web_lg')




def find_sent(sen,df):
    senlen=len(sen.split())
    exsentence=model1(sen)
    index=0
    sentence_vector=[]
    max=0
    for i in range(len(df)):
        sentence=model1(df[i])
        sentence_vector.append(sentence)
        distance=sentence.similarity(exsentence)
        if distance>max:
            max=distance
            index=i
    return(sentence_vector[index],max)


