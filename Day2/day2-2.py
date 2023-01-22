file = open("day2data.txt", "r")
datalist = list(map(str, file.readlines()))
x = y = aim = 0
for item in datalist:
    data = item.split(" ")
    if data[0] == "forward":
        x += int(data[1])
        y += int(data[1]) * aim
    elif data[0] == "up":
        aim -= int(data[1])
    elif data[0] == "down":
        aim += int(data[1])
print(x, y, "x*y=", x*y)
input()
