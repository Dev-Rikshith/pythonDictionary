import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()) > 0):
        res = input("Did you mean %s instead ? Press Y for yes and N for no." % (get_close_matches(word, data.keys())[0]))
        res.upper()
        if res == "Y":
            return data[(get_close_matches(word, data.keys()))[0]]
        elif res == "N":
            return "We are unable to find that word. Please recheck"
        else:
            return "We are unable to understand your input."
    else:
        return "Unable to find that word for you."

word = input("Enter the word for which you would like to find the meaning for: ")
output = translate(word)
if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)