from nltk import ngrams
from nltk import FreqDist
import nltk,re,string
from string import punctuation
from pathlib import Path
nltk.download('averaged_perceptron_tagger')

text_ori = Path('deneme.txt').read_text(encoding="utf-8")
text = text_ori.translate(str.maketrans("", "", string.punctuation + "“" + "”" + "’"))

text_ori1=Path('deneme2.txt').read_text(encoding="utf-8")
text1 = text_ori1.translate(str.maketrans("", "", string.punctuation + "“" + "”" + "’"))

number =input("Please enter the threshold value:\n")
number=int(number)

tokens = nltk.word_tokenize(text)
tokens1 = nltk.word_tokenize(text1)


bigrm = nltk.bigrams(tokens)
trigrm = nltk.trigrams(tokens)
bigrm1 = nltk.bigrams(tokens1)
trigrm1 = nltk.trigrams(tokens1)

a=nltk.pos_tag(tokens)
print("------------------------------------------deneme için pos tag---------------------------------------------\n")
print(a)
b=nltk.pos_tag(tokens1)
print("------------------------------------------deneme2 için pos tag-------------------------------------------\n")
print(b)

fdist = nltk.FreqDist(bigrm)#compute frequency distribution 
print("-----------------------Words from deneme for bigrams-----------------------\n")

j=0
for words,tv in fdist.items():
    if(tv>=number and j<=49):
        j+=1
        print (j,words,tv)


fdist = nltk.FreqDist(bigrm1)#compute frequency distribution
print("-----------------------Words from deneme2 for bigrams-----------------------\n")

k=0
for words,tv in fdist.items():
    if(tv>=number and k<=49):
        k+=1
        print (k,words,tv)


fdist = nltk.FreqDist(trigrm)#compute frequency distribution 
print("-----------------------Words from deneme for trigrams-----------------------\n")

i=0
for words,tv in fdist.items():
    if(tv>=number and i<=49):
        i+=1
        print (i,words,tv)


fdist = nltk.FreqDist(trigrm1)#compute frequency distribution 
print("-----------------------Words from deneme2 for trigrams-----------------------\n")

l=0
for words,tv in fdist.items():
    if(tv>=number and l<=49):
        l+=1
        print (l,words,tv)








    