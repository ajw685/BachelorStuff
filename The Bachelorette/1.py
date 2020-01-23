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


#regg = re.compile("r'\b\w+\b'")
#regg = re.compile("/^([a-zA-Z ']*)$/", re.I)





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

xnum = 0

files = glob.glob(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\TheBachelorette\SubtitleJson\*.json")
print(files)

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

            #a2 = re.sub('[.*]', ' ', str(a1))
            #print(a2+" - remove brackets")

            
            
            a2 = re.sub("[\(\[].*?[\)\]]", "", a['text'])
            #print(a2+" - remove brackets")
            a3 = re.sub('<.*?>', ' ', a2)
            #print(a3+" - remove html tag")
            
            #a3 = re.sub('[.*?]', '', str(a2))
            #print(a3+" - remove bracket tag")
            a4 = re.sub('\W ', ' ', str(a3))
            #print(a4+" - leave words")
            a5 = re.sub('\-', ' ', str(a4))
            #print(a5+" - remove dash")
            a6 = a5.replace('"', ' ')
            #print(a6+" - remove quote")
            a7 = a6.strip(string.punctuation)
            #print(a7+" - strip punctuation")
            a8 = re.split("( )",a7)
            for b in a8:
                lower_word = b.lower()

                if lower_word not in total_word_dict:
                    total_word_dict[lower_word] = 1
                else:
                    total_word_dict[lower_word] = total_word_dict[lower_word] + 1
                if lower_word == 'love':
                    love = love + 1
                    if episode not in love_array:
                        love_array[episode] = 1
                    else:
                        love_array[episode] = love_array[episode] + 1
                    #print(a7)
    print(love)
                #if lower_word not in episode_word_dict[episode]:
                #    episode_word_dict[episode][lower_word] = 1
                #else:
                #    episode_word_dict[episode][lower_word] = episode_word_dict[episode][lower_word] + 1

                            
            #a3 = a2.replace("\\", "")
            #a4 = re.split("( )",str(a3))
            #print(a)
        

    ##with open(r"C:\Users\Aaron\OneDrive\Projects\The Bachelor\sum.json") as f:
    ##    data_json = f.read()
    ##    data_loads = json.loads(data_json)
    ##    #a = d['s23e02']['results']['items']
    ##    for episode in data_loads:
    ##        episode_word_dict[episode] = {}
    ##        #print(episode)
    ##        #print(episode_word_dict)
    ##        items = data_loads[episode]['results']['items']
    ##        
    ##        for entry in items:
    ##            sub_entry = entry['alts']
    ##            if sub_entry[0]['cfd'] != None:
    ##                if float(sub_entry[0]['cfd']) > 0.9850: #Other values to try? 0.9900, 0.9800, 0.9850
    ##                    good = good + 1
    ##                    word = sub_entry[0]['ct']
    ##                    lower_word = word.lower()
    ##                    
    ##                    if lower_word not in total_word_dict:
    ##                        total_word_dict[lower_word] = 1
    ##                    else:
    ##                        total_word_dict[lower_word] = total_word_dict[lower_word] + 1
    ##
    ##                    if lower_word not in episode_word_dict[episode]:
    ##                        episode_word_dict[episode][lower_word] = 1
    ##                    else:
    ##                        episode_word_dict[episode][lower_word] = episode_word_dict[episode][lower_word] + 1
    ##                        
    ##                    
    ##                    #s[z] = [c]
    ##                    #if c not in s[z]:
    ##                    #    s[z][c] = 1
    ##                    
    ##                else:
    ##                    bad = bad + 1;
    ##        
    ###for w in sorted(r, key=r.get, reverse=True):
    ##    #print(w, r[w])    
    ##    
    ###print(good)
    ###print(bad)
    ###print(total_word_dict)
    ###print(episode_word_dict)
    ##
for episode in love_array:
    xnum += 1
    
    y.append(love_array[episode])
    x.append(xnum)
plt.bar(x, y, align='center')
plt.title('Mentions of "Love" per Episode')
plt.ylabel('Mentions')
plt.xlabel('Episode')
plt.show()
print("")
##for episode in episode_word_dict:
##    print(episode_word_dict[episode]["happy"])
        
        
    
    #I want to see episode;word;count
    ##
    ###print(total_word_dict)
    ###print(episode_word_dict["s23e08"]["love"])
    ###print(episode_word_dict[1])


print(total_word_dict)
print(love)
print(love_array)
