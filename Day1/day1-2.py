file = open("Day1numbers.txt", "r")
datalist = list(map(int, file.readlines()))
incs = 0
for x in range(3, len(datalist)):
    y = datalist[x] + datalist[x-1]+datalist[x-2]
    z = datalist[x-1] + datalist[x-2] + datalist[x-3]
    if y > z:
        incs +=1

print()
print(incs)
input()
