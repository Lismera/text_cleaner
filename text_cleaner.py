#!/usr/bin/env python
# coding: utf-8

import os
from nltk.corpus import stopwords
import nltk
import nltk.data
import re
#nltk.download()
from pathlib import Path


def exc_stopwords():
    
    stopwords_total = stopwords.words('english')

    #you can add and remove stopwords here
    #stopwords_total = stopwords.append("WORD1", "WORD2")
    #stopwords_total = stopwords.remove("WORD1", "WORD2")

    return(stopwords_total)


def main_logic(text_file_paths, ex_stop, punct, dig, low_case):

    text_file_paths= [t for t in text_file_paths]
    for text_file in text_file_paths:
        with open(text_file, 'r', encoding='ascii', errors='ignore') as f2:
            text ="".join(x for x in f2.read())
        
        #apply modify stopwords
            if ex_stop==True:
                stop = exc_stopwords()
                text = ' '.join([word for word in text.split() if word not in stop])
        
        #remove puntctuation
            if punct==True:
                punc = re.sub(r'[^\w\s]','',text)
                text = punc
        
        #remove digits
            if dig==True:
                rep = re.sub(r'\d','',text)
                text = rep

        #make it all lower case
            if low_case==True:
                text = str.lower(text)


        text_file_new = os.path.basename(os.path.normpath(text_file))

        directory = str(Path(text_file).parent)+'/output'

        if not os.path.exists(directory):
            os.makedirs(directory)

        os.chdir(directory)
        f = open("new " + str(text_file_new),"w", encoding='utf8', errors='ignore')
        f.write(text)
        f.close()

