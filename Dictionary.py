import json

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

def autocorrect(word):
    pass
#flag 
stop1 = False

#while loop to print definitions until user wants to stop
while(stop1 == False):
    word = input("Enter a word or \"stop1\" to stop searching: " + "\n")
    if word == 'stop1':
        stop1 = True
        break
    output = search(word)
    
#printing words with multiple definitions
    if type(output) == list:
        for item in output:
            print(item +"\n")
    else:
        print(output)

