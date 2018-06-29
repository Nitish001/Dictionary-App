# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 20:04:23 2018

@author: KP
"""

import json

from difflib import get_close_matches

data  = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead ?.. Type Y for Yes and N for No " %get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        else:
            return "Please check the word entered...."
    else:
        return "Please check the word entered...."
    
word = input("Enter a Word : ")
output = translate(word.lower())
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
