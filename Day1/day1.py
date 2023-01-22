file = open("Day1numbers.txt", "r")
datalist = list(map(int, file.readlines()))
incs = 0
for x in range(1, len(datalist)):
    if datalist[x] > datalist[x-1]:
        incs +=1


print()
print(incs)
input()
