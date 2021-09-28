import json
import random

config_file = open("settings.json", "r")
data = config_file.read()
config_file.close()
config = json.loads(data)

open('results.txt', 'w').close()

consonants = "BCDFGHJKLMNPQRSTVWXYZ"
vowels = "AEIOU"

for i in range(config["amount"]):
    current_string = ""

    for ii in config["template"]:
        if ii == "c":
            current_string = current_string + consonants[random.randrange(0, len(consonants))]
        
        if ii == "v":
            current_string = current_string + vowels[random.randrange(0, len(vowels))]
            
        if ii == "d":
            current_string = current_string + config["defined"]
    
    file_object = open('results.txt', 'a')

    if not "suffix" in config:
        file_object.write("\n" + current_string)
    else:
        suffix = config["suffix"]
        file_object.write("\n" + current_string + suffix)
    file_object.close()