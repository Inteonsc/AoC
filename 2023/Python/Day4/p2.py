import os

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
sum = 0
solvedCards = dict()
def SolveScratchCard(cardNumber):
    #base case, 0 matches. iterate and recurse each matching one below
    solvedScratchCards = 1
    matches = 0
    winningNumbers = cards[cardNumber][0]
    if cardNumber in solvedCards.keys():
        return solvedCards.get(cardNumber)
    for attempt in cards[cardNumber][1]:
        if attempt in winningNumbers:
            matches += 1
    if matches == 0:
        solvedCards[cardNumber] = solvedScratchCards
        return solvedScratchCards
    for i in range(matches):
        if i +cardNumber + 1 < len(cards):
            solvedScratchCards += SolveScratchCard(cardNumber + i + 1)
    
    solvedCards[cardNumber] = solvedScratchCards
    return solvedScratchCards

cards = []
for line in data:
    tmpSplit = line.split(":")
    winningNumbers = set(tmpSplit[1].split("|")[0].split())
    attemptNumbers = set(tmpSplit[1].split("|")[1].split()) 
    cards.append([winningNumbers, attemptNumbers])

for i in range(len(cards)):
    sum += SolveScratchCard(i)

print(sum)