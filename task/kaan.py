import nltk, re, string, collections
nltk.download('punkt')
import numpy as np
from pathlib import Path
from collections import OrderedDict
#from itertools import chain 

def getNGrams(wordlist, n):#this function helps me to create n-grams.
    ngrams = []
    for i in range(len(wordlist)-(n-1)):
        ngrams.append(wordlist[i:i+n])
    return ngrams


number=input("Please enter a number to apply n-gram algorithm:\n")
number=int(number)
text = Path('deneme.txt').read_text(encoding='utf-8')
punctuationNoPeriod = "[" + re.sub("\.","",string.punctuation) + "]"
text = re.sub(punctuationNoPeriod, "", text)  
    
tokenized = text.split()#split the text.
n_grams = getNGrams(tokenized, number)#get ngrams with the help of the getNGrams function.

ngram_count = collections.Counter(map(tuple, n_grams))#convert this into a tuple, then create a list with appropriate counts.

sorted_ngram = sorted(ngram_count.items(), key=lambda x: x[1], reverse=True)#sort this by counts. it's from reverse because list is ascending.
od = OrderedDict(sorted_ngram)#with this sorted, create an ordered dictionary.


i = 1#print this ordered dictionary that we just created.

print('Top 100 words')
for key, value in od.items():
    stringKey = str(key)
    #stringKey = stringKey.replace(',' , "").replace('(', "").replace(')', "").replace("' '", " ")
    if value>1:
        print('{0} - {1}--> {2}'.format(i,stringKey,value))
        i = i + 1
    if i == 101:
         break

