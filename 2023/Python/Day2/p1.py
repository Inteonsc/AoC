import os


data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
sum = 0
for line in data:
    TitleSplit = line.split(":")
    game = TitleSplit[0].split()
    splits = TitleSplit[1].split()
    invalid = False
    print(game)
    for i in range(len(splits)):
        if splits[i].isdigit():
            if int(splits[i]) > 14:
                invalid = True
            if int(splits[i]) == 14 and "blue" not in splits[i+1]:
                invalid = True 
            if int(splits[i]) == 13 and "red" in splits[i+1]:
                invalid = True 
    if not invalid:
        sum += int(game[1])    
        
print(sum)  