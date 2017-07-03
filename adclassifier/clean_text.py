import os
import re
import time
import requests


def is_word(word):
    """
        check from wikipedia if the input is a valid dictionary word
    """
    resp = requests.get("http://en.wikipedia.org/w/api.php?action=query&prop=info&format=json&titles=" + word)

    if resp.status_code == 200:
        wiki = resp.json().get('query').get('pages')
        if '-1' in wiki:
            return False
        else:
            return True


def clean_extracted_text(inputPath, outputPath):
    for text_file in os.listdir(inputPath):
        print('processing..{}'.format(text_file))
        # get the absolute path of the file
        abs_file_path = os.path.join(inputPath, text_file)
        # check if path is file or directory
        if (os.path.isfile(abs_file_path) == True):
            with open(abs_file_path, 'r') as f:
                text = f.read().split(',')
                for i in range(len(text)):
                    # remove characters symbols except ',-
                    pattern = re.compile("[^\w'-]")
                    text[i] = pattern.sub('', text[i])
                # remove empty elements from list
                text = ' '.join(text).split()
                moded_text = []
                for i in range(len(text)):
                    if (len(text[i]) > 1):
                        if (is_word(text[i]) == True):
                            moded_text.append(text[i])
            # get the absolute path of the file
            abs_clean_file_path = os.path.join(outputPath, text_file)
            # write to clean text file
            with open(abs_clean_file_path, 'w') as f:
                for i in range(len(moded_text)):
                    f.write(moded_text[i] + ',')
        # fair use of api
        time.sleep(10)

if __name__ == "__main__":
    inputPath = r'D:\adclassifier\labelled_dataset\non_political\text_datasets\vision\original'
    outputPath = r'D:\adclassifier\labelled_dataset\non_political\text_datasets\vision\clean'
    clean_extracted_text(inputPath=inputPath, outputPath=outputPath)
