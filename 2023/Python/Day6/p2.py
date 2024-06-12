import os

def CalcRecordsBroken(time, dist):
    num = 0
    for i in range(time):
        if((time - i )* i) > dist:
            num += 1
    return num

if __name__ == "__main__":
    data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
    times = data[0].split(":")[1].split()
    dists = data[1].split(":")[1].split()
    output = CalcRecordsBroken(int("".join(times)), int("".join(dists)))
    print(output)
