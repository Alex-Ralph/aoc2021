data = open("day3data.txt", "r").read().splitlines()
numsize = len(data[0])
#this is so fucking bad lol


#finds oxygen
oxy = data[:]
co2 = data[:]
numpos = 0
while len(oxy) > 1 and numpos < numsize:
    counter = 0
    for y in oxy:
        if y[numpos] == "1":
            counter += 1
    a = 0
    if counter < len(oxy) / 2:
        while a < len(oxy):
            if oxy[a][numpos] == "1":
                del oxy[a]
            else:
                a += 1
    else:
        while a < len(oxy):
            if oxy[a][numpos] == "0":
                del oxy[a]
            else:
                a += 1
    numpos += 1

#finds CO2
numpos = 0
while len(co2) > 1 and numpos < numsize:
    counter = 0
    for y in co2:
        if y[numpos] == "1":
            counter += 1
    a = 0
    if counter >= len(co2) / 2:
        while a < len(co2):
            if co2[a][numpos] == "1":
                del co2[a]
            else:
                a += 1
    else:
        while a < len(co2):
            if co2[a][numpos] == "0":
                del co2[a]
            else:
                a += 1
    numpos += 1

print("oxygen: ", oxy)
print("CO2: ", co2)
