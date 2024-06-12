import os

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
score = 0
for line in data:
    tmpSplit = line.split(":")
    winningNumbers = tmpSplit[1].split("|")[0].split()
    attemptNumbers = tmpSplit[1].split("|")[1].split()
    matches = 0
    
    for attempt in attemptNumbers:
        for i in range(len(winningNumbers)):
            if winningNumbers[i] == attempt:
                matches += 1
    scoreToAdd = 0
    if matches >= 1:
        scoreToAdd += 1
        matches -= 1
    while matches >= 1:
        scoreToAdd = scoreToAdd * 2
        matches -= 1    
    score += scoreToAdd

testset = ["23, 11, 12"]
test = set(testset)

print(score)