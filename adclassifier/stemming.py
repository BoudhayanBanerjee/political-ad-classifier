from nltk.stem.lancaster import LancasterStemmer
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer
from pprint import pprint

import pandas as pd
import numpy as np
import os

# TODO
# implement stemming algorithms
# compare results


def lancaster(inputpath=None, text=None):
    """
    docstring
    """
    data = ''
    lc = LancasterStemmer()
    if inputpath:
        filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
        lcstemmed_list = []
        for file in filenames:
            with open(file, 'r') as f:
                data = f.read()
                if data:
                    texts = data.split(',')
                    stemmedfile = []
                    for text in texts:
                        lcstemmed = lc.stem(text)
                        stemmedfile.append(lcstemmed)
            lcstemmed_list.extend(stemmedfile)
        return lcstemmed_list
    if text:
        lcstemmed = lc.stem(text)
        return lcstemmed


def porter(inputpath=None, text=None):
    """
    docstring
    """
    data = ''
    p = PorterStemmer()
    if inputpath:
        filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
        pstemmed_list = []
        for file in filenames:
            with open(file, 'r') as f:
                data = f.read()
                if data:
                    texts = data.split(',')
                    stemmedfile = []
                    for text in texts:
                        pstemmed = p.stem(text)
                        stemmedfile.append(pstemmed)
            pstemmed_list.extend(stemmedfile)
        return pstemmed_list
    if text:
        pstemmed = p.stem(text)
        return pstemmed


def snowball(inputpath=None, text=None):
    """
    docstring
    """
    data = ''
    sb = SnowballStemmer('english')
    if inputpath:
        filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
        sbstemmed_list = []
        for file in filenames:
            with open(file, 'r') as f:
                data = f.read()
                if data:
                    texts = data.split(',')
                    stemmedfile = []
                    for text in texts:
                        sbstemmed = sb.stem(text)
                        stemmedfile.append(sbstemmed)
            sbstemmed_list.extend(stemmedfile)
        return sbstemmed_list
    if text:
        sbstemmed = sb.stem(text)
        return sbstemmed

if __name__ == "__main__":
    inputpath = r'D:\ypai\data\json\text'
    filenames = [os.path.join(inputpath, file) for file in os.listdir(inputpath)]
    words = []
    for file in filenames:
        with open(file, 'r') as f:
            data = f.read()
            if data:
                texts = data.split(',')
        words.extend(texts)
    porter = porter(inputpath=inputpath)
    snowball = snowball(inputpath=inputpath)
    lancaster = lancaster(inputpath=inputpath)
    d = {'lancaster': lancaster,
         'porter': porter,
         'snowball': snowball}
    df = pd.DataFrame(d, index=words)
    print(df)
