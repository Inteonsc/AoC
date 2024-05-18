import regex as re
import os
#used to not work because twone will output to 22 but it needs to output to 21 but 3rd party regex + overlapped solves this

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
runningTotal = 0
numbers_dict = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
regexstring = "\d"
for i in numbers_dict:
    regexstring += "|" + i
debug = 0
for line in data:
    matches = re.findall(regexstring, line, overlapped = True)
    toAdd = "" 
    if matches[0] in numbers_dict:
        toAdd += str(numbers_dict[matches[0]])
    else:
        toAdd += matches[0]
    if matches[-1] in numbers_dict:
        toAdd += numbers_dict[matches[-1]] 
    else:
        toAdd += matches[-1]
    runningTotal += int(toAdd)
print(runningTotal)
