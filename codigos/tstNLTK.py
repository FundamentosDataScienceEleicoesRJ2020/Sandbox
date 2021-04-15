import pandas as pd
import json
import ssl
'''
Tools to find the polarity or to perform the sentiment analysis:
 - TextBlob
 - NLTK-Vader
'''
import nltk
from nltk import tokenize
from textblob import TextBlob
from gensim.utils import simple_preprocess
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk import wordnet

ds = pd.read_csv("./datasets/prefeito_rio_2020_clean.csv")
ds.info()
# ------------------------------------------------------

stemmer = SnowballStemmer("portuguese")
nltk.download('stopwords')
nltk.download('wordnet')
stopwords = nltk.corpus.stopwords.words("portuguese")
tokenize = tokenize.word_tokenize(text, "portuguese")
# ------------------------------------------------------

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
VaderAnalyzer = SentimentIntensityAnalyzer()
# ------------------------------------------------------

def lemmatize_stemming(text):
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))


def preprocess(text):
    result = []
    for token in simple_preprocess(text):
        if token not in stopwords and len(token) > 3:
            # result.append(lemmatize_stemming(token))
            result.append(token)
    return result
# ------------------------------------------------------

txtSample = ds.loc[0, "text"]
lemmatize_stemming(txtSample)
preprocess(txtSample)
