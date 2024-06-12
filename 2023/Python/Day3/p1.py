import os


def GetNumLength(x, y):
    numLength = 1
    search = True
    while(search):
        if x + numLength == gridWidth:
            search = False
            return numLength
        if grid[y][x + numLength].isdigit():
            numLength +=1
        else:
            search = False
            return numLength 



def CheckAdj(x, y):
    for i in range(-1,2):
        for j in range(-1,2):
            # assumes input only contains digits, empty spaces(.) and symbols
            if y + i < gridHeight and x + j < gridWidth and y + i >= 0 and x + j >= 0:
                if(not grid[y + i][x + j].isdigit() and grid[y + i][x + j] != "."):
                    return True         
    return False

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
grid = []
for line in data:
    grid.append(line.strip())               
#grid = ("..324*..", "*.......", ".333...*", ".....111","")
gridWidth = len(grid[0])
gridHeight = len(grid)         
sum = 0     
#Search the grid
amountToSkip = 0
for y in range(gridHeight):
    for x in range(gridWidth):
        if amountToSkip > 0:
            amountToSkip -=1
            continue
        if grid[y][x].isdigit():
            numLength = GetNumLength(x,y)
            number = ""
            isValid = False
            for i in range(0,numLength):
                number += grid[y][x + i]
                if CheckAdj(x + i, y):
                    isValid = True
            if isValid:
                            sum += int(number)
            amountToSkip = numLength - 1

print(sum)
