import os

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
sum = 0
for line in data:
    TitleSplit = line.split(":")
    game = TitleSplit[0].split()
    splits = TitleSplit[1].split()
    minRed = 0
    minBlue = 0
    minGreen = 0
    for i in range(len(splits)):
        if splits[i].isdigit():
            if "red" in splits[i+1]:
                if int(splits[i]) > minRed:
                    minRed = int(splits[i])
            if "green" in splits[i+1]:
                if int(splits[i]) > minGreen:
                    minGreen = int(splits[i])
            if "blue" in splits[i+1]:
                if int(splits[i]) > minBlue:
                    minBlue = int(splits[i])
            sum += minRed * minBlue * minGreen
        
print(sum)  