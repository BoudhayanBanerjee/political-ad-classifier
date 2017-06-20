from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

import os

# TODO
# compare vectorizers


def countvectorizer(inputpath=None, text=None):
    """
    docstring
    """
    vectorizer = CountVectorizer(min_df=1)
    if inputpath:
        filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
        corpus = []
        for file in filenames:
            with open(file, 'r') as f:
                data = f.read()
                corpus.append(data)
    if text:
        corpus = text

    X = vectorizer.fit_transform(corpus)
    print(X.toarray())
    print(vectorizer.get_feature_names())


def hashvectorizer(inputpath=None, text=None):
    """
    docstring
    """
    # TODO
    hv = HashingVectorizer()
    if inputpath:
        filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
        corpus = []
        for file in filenames:
            with open(file, 'r') as f:
                data = f.read()
                corpus.append(data)
    if text:
        corpus = text
    X = hv.transform(corpus)
    print(X.toarray())
    print(hv.get_params())


def tfidfvectorizer(inputpath=None, text=None):
    """
    docstring
    """
    # TODO
    pass

if __name__ == "__main__":
    inputpath = r'D:\ypai\data\json\text'
    hashvectorizer(inputpath=inputpath)
