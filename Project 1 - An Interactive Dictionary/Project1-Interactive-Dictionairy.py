import json
import difflib 

data = json.load(open("data.json"))


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    #To make sure the program returns the definition of words that start with a capital letter (e.g. Delhi, Texas)
    elif (w.capitalize() in data):
        return data[w.capitalize()]
    #To make sure the program returns the definition of acronyms (e.g. USA, NATO) 
    elif (w.upper() in data):
        return data[w.upper()]
    elif len(difflib.get_close_matches(w, data.keys())) > 0:
        Answer = input("Did you mean %s instead? Enter Y if yes, or N if no: " %(difflib.get_close_matches(w, data.keys()))[0])
        if (Answer == "Y"):
            return data[(difflib.get_close_matches(w, data.keys()))[0]]
        elif (Answer == "N"):
            return "Word does not exists as part of this dictionairy. Please double check."
        else:
            return "You did not enter Y or N. We didn't understand your entry."
    else:
        return "Word not part of this dictionairy. Please double check."

word = input("Enter word for which you want definition: ")

output = (translate(word))
#making the output more user friendly by removing list brackets from definition [], and if not list then print output
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
