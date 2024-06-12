import os

haschecked = list()

def GetAdj(x, y):
    global haschecked 
    haschecked = list()
    numbers = []
    for i in range(-1,2):
        for j in range(-1,2):
            if y + i < gridHeight and x + j < gridWidth and y + i >= 0 and x + j >= 0:
                if grid[y+i][x+j].isdigit():
                    if (y+i,x+j)in haschecked:
                        continue
                    else:
                        numbers.append(GetNum(x+j, y+i))     
    return numbers

def GetNum(x, y):
    global haschecked
    number = grid[y][x]
    haschecked.append((y,x))
    return GetLeft(x -1, y) + number + GetRight(x + 1, y)

def GetLeft(x, y):
    global haschecked
    if x< 0:
        return ""
    if not grid[y][x].isdigit():
        return ""
    haschecked.append((y,x))
    return GetLeft(x-1,y) + grid[y][x]

def GetRight(x, y):
    global haschecked
    if x>= gridWidth:
        return ""
    if not grid[y][x].isdigit():
        return ""
    haschecked.append((y,x))
    return  grid[y][x] + GetRight(x+1,y)



data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
grid = []
for line in data:
    grid.append(line.strip())               
gridWidth = len(grid[0])
gridHeight = len(grid)         
sum = 0     

#Search the grid
for y in range(gridHeight):
    for x in range(gridWidth):
        if grid[y][x] == "*":
            adjNums = GetAdj(x,y)
            if len(adjNums) == 2:
                sum += int(adjNums[0]) * int(adjNums[1])
print(sum)