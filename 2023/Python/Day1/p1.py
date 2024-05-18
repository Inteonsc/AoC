import re
import os

data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
runningTotal = 0

for line in data:
    match = re.findall("\d", line)
    runningTotal += int(str(match[0]) + str(match[-1]))

print(runningTotal)