""" This is a dictionary that will return definitions of
    the closest matched word. 


    Variables
        [variable]: [description]
        [data]:[the entire dictionary file found in the working directory]
        [matches]:[list of closest matches]
        [match]:[closest match]
        [word]:[word entered by user]
        [output]:[definitions]
        [stop1]:[flag to stop the while loop]
        [c_word]:[corrected word]
"""

import json
from difflib import get_close_matches

data = json.load(open('data.json'))

#Searching data.json for word
def search(word):
    if word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    else:
        print("Word does not exist in this dictionary. Please check spelling. ")

#returns the closest match of the word
def autocorrect(word):
    matches = get_close_matches(word, data.keys(), cutoff = 0.5)
    match = matches[0]
    return match

#flag 
stop1 = False

#while loop to find definitions of word until user wants to stop
while(stop1 == False):
    word = input("Enter a word or \"stop1\" to stop searching: " + "\n")
    if word == 'stop1':
        stop1 = True
        break
    else:
        c_word = autocorrect(word)
        if(word == c_word):
            pass
        else:
            print("Did you mean: " + c_word + "\n")
    output = search(c_word)
    
#printing words with multiple definitions
    if type(output) == list:
        for item in output:
            print(item +"\n")
    else:
        print(output)

