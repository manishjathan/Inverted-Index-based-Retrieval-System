from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#tokenizing -- word tokenizer
#sentence tokenizer
#lexicon and corpora
#corpora is a body of text ex : Medical Journals, Presidential speeches
#lexicons - words and meanings
def generate_tokens(doc):
    token_list = []

    sentence_list = sent_tokenize(doc)
    for sentence in sentence_list:
        token_list.append(word_tokenize(sentence))
    return token_list

#Eliminating Stop words
#Stop Words are a,an,the,is,of.... All those words which are of no use for data analysis
def remove_stop_words(token_list):
    stop_words = set(stopwords.words("english"))
    filtered_sentence = []
    for token in token_list:
        for w in token:
            if w not in stop_words and w not in '.' and w not in ',' and w not in '?':
                filtered_sentence.append(w)
    return filtered_sentence
#Stemming
#Use Stem words
#Python, Pythonly, Pythonize all this words have python as the stem word
def stem(filtered_sentence):
    ps = PorterStemmer()
    stemmed_list = []
    for w in filtered_sentence:
        stemmed_list.append(ps.stem(w))

    return stemmed_list