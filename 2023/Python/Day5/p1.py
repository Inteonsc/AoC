import os

def ConvertInput(input, mapNumber, ranges):
    
    for set in ranges[mapNumber]:
       
        if input >= int(set[1]) and input < int(set[1]) + int(set[2]):
            return int(set[0]) + (input - int(set[1]))
    return input

if __name__ == "__main__":
    data = open(os.path.dirname(os.path.abspath(__file__)) + "\input.txt").readlines()
    seeds = data[0].split(":")[1].strip("\n").split()
    rangesfrominput = []
    i = -1
    for line in data:
        if line == "\n":
            i += 1
            rangesfrominput.append([])
            continue
        if line.endswith(":\n"):
            continue
        if i>=0:
            inputDigits = line.split()
            rangesfrominput[i].append(inputDigits)
    
    output = None
    for seed in seeds:
        soil = ConvertInput(int(seed), 0,rangesfrominput)
        fert = ConvertInput(soil,1,rangesfrominput)
        water = ConvertInput(fert,2,rangesfrominput)
        light = ConvertInput(water,3,rangesfrominput)
        temp = ConvertInput(light,4,rangesfrominput)
        humidity = ConvertInput(temp,5,rangesfrominput)
        location = ConvertInput(humidity,6,rangesfrominput)
        
        if output == None:
            output = location
            continue
        if location < output:
            output = location

    print(output)
    

        
    
