import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json
import pandas as pd
import os
from matplotlib import pyplot as plt
from matplotlib import style

import re
import string

import glob

import sys
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.text import Text
import numpy
import matplotlib

#regg = re.compile("r'\b\w+\b'")
#regg = re.compile("/^([a-zA-Z ']*)$/", re.I)

str1 = ""
str10 = ""



#THANK YOU TO
#https://natmeurer.com/simple-technical-tricks-to-remember-1-python-regex-to-remove-tags/
#https://stackoverflow.com/questions/20569363/python-regex-alphabet-and-spaces


style.use('ggplot')



q = []
total_word_dict = {}
episode_word_dict = {}
s = {}
good = 0
bad = 0
episode = 0
x = []
y = []
love = 0
love_array = {}
episode_strings = {}

xnum = 0

files = glob.glob(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\*.json")


#files = [(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\Week1.en-us.sample.xjson")]
#files = [(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\Week1.en-us.sample2.xjson")]
#files = [(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\Week1.en-us.json")]
for file in files:

    #with open(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\Week1.sample.en-us.json", encoding='utf-8', errors='ignore') as f:
    with open(file, encoding='utf-8', errors='ignore') as f:
        episode = episode + 1
        print(str(file))
        data_json = f.read()
        data_loads = json.loads(data_json)
        for a in data_loads:
            a1 = a['text']
            #print(a1+" - Original")

            a2 = re.sub("[\(\[].*?[\)\]]", "", a['text'])
            #print(a2+" - remove brackets")

            a3 = re.sub('<.*?>', ' ', a2)
            #print(a3+" - remove html tag")

            a4 = re.sub('\-', ' ', a3)
            #print(a4+" - remove hyphen")

            a5 = a4.replace("  ", " ")
            #print (a5+" - remove double space")

            str1 = str1 + a5




            
            #a3 = re.sub('[.*?]', '', str(a2))
            #print(a3+" - remove bracket tag")
            #a4 = re.sub('\W ', ' ', str(a3))
            #print(a4+" - leave words")
            #a5 = re.sub('\-', ' ', str(a4))
            #print(a5+" - remove dash")
            #a6 = a5.replace('"', ' ')
            #print(a6+" - remove quote")
            #a7 = a6.strip(string.punctuation)
            #print(a7+" - strip punctuation")
            #a8 = re.split("( )",a7)
        #print(str1)
        str2 = str1.replace("♪", "")
        str3 = str2.replace("  ", " ")
        str4 = str3.replace("  ", " ")
        str5 = str4.replace("  ", " ")
        str6 = str5.replace("...", ".")
        str7 = str6.replace(".", ". ")
        str8 = str7.replace("!", "! ")
        str9 = str8.replace("?", "? ")
        str10 = str9.replace("  ", " ")
        
        #print(str10)
        episode_strings[episode] = str10

#print(episode_strings)

tokens = word_tokenize(str10)
textList = Text(tokens)
textList.concordance('love')
#print(tokens)
textList.generate()
#print(textList.count('love'))

#textList.dispersion_plot(['love'])
