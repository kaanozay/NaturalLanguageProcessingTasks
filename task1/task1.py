sentence = ("He was running and eating at same time. He has bad habit of swimming after playing long hours in the Sun.")


#NLTK Token
"""import nltk
nltk.download('punkt')

tokens = nltk.word_tokenize(sentence)

for token in tokens:
    print(token)"""

#SPACY Token

"""import spacy
nlp = spacy.load("en_core_web_sm")
text = nlp(sentence)

for token in text:
    print(token.text)"""


#NLTK Lemma
"""import nltk
nltk.download("wordnet")
from nltk.stem import WordNetLemmatizer 

lemmatizer = WordNetLemmatizer()
tokens=nltk.word_tokenize(sentence)

for t in tokens:
    print(((lemmatizer.lemmatize(t, pos="v"))))"""


#TEXTBLOB Lemma
from textblob import TextBlob, Word 

text = TextBlob(sentence) 
lemmatized_sentence = "\n".join([word.lemmatize(pos="v") for word in text.words]) 

print(lemmatized_sentence)

8