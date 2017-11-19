from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

#tokenizing -- word tokenizer
#sentence tokenizer
#lexicon and corpora
#corpora is a body of text ex : Medical Journals, Presidential speeches
#lexicons - words and meanings
token_list = []
example_text = "Hello there, How are you doing today? The weather is great and Python is awesome. The Sky is pinkish-blue. You should not eat CardBoard."
sentence_list = sent_tokenize(example_text)
for sentence in sentence_list:
    token_list.append(word_tokenize(sentence))


#Eliminating Stop words
#Stop Words are a,an,the,is,of.... All those words which are of no use for data analysis

stop_words = set(stopwords.words("english"))
filtered_sentence = []
for token in token_list:
    for w in token:
        if w not in stop_words and w not in '.' and w not in ',' and w not in '?':
            filtered_sentence.append(w)

#Stemming
#Use Stem words
#Python, Pythonly, Pythonize all this words have python as the stem word

ps = PorterStemmer()
stemmed_list = []
for w in filtered_sentence:
    stemmed_list.append(w)

for stem_words in stemmed_list:
    print(stem_words)