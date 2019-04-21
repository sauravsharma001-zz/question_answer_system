from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
import os
import nltk


class WordFeature:
    word = None
    lemma = None
    stem = None
    tag = None
    synonyms = None
    antonyms = None

    def __init__(self, word, tag, stem, lemma, synonyms, antonyms):
            self.word = word
            self.tag = tag
            self.stem = stem
            self.lemma = lemma
            self.synonyms = synonyms
            self.antonyms = antonyms

class LoadWikis:
    stop_words = set()
    file_path = None
    wikis = list()
    sentences = list()
    words = list()
    lemmatizer = None
    words_feature = list()
    pos_tag = dict()

    def __init__(self, file_path):
        self.file_path = file_path
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
        self.stemmer = PorterStemmer()

    def read_file(self, file):
        f = open(file, "r", encoding="utf-8")
        return f.read()

    def load_files(self):
        for file in os.listdir(self.file_path):
            try:
                with open(os.path.join(self.file_path, file), "r", encoding='utf-8-sig') as fd:
                    w = fd.read()
                    self.wikis.append(w)
            except OSError as err:
                print("exception", err)

    def split_file_in_sentence(self):
        for wiki_content in self.wikis:
            self.sentences.extend(sent_tokenize(wiki_content))

    def extract_token(self):
        for sentence in self.sentences:
            word = word_tokenize(sentence)
            pos = nltk.pos_tag(word)
            self.words.extend(word)
            self.pos_tag[sentence] = pos
            # print(sentence, pos)
            # print()
        
    def extract_lemmas(self):
        for word in self.words:
            wf = WordFeature(word, nltk.pos_tag(word), self.stemmer.stem(word), self.lemmatizer.lemmatize(word), None, None)
            self.words_feature.append(wf)
            # print(wf.word, wf.tag, wf.lemma, wf.stem)