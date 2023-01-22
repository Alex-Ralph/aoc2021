file = open("day2data.txt", "r")
datalist = list(map(str, file.readlines()))
x = y = 0
for item in datalist:
    data = item.split(" ")
    if data[0] == "forward":
        x += int(data[1])
    elif data[0] == "up":
        y -= int(data[1])
    elif data[0] == "down":
        y += int(data[1])
print(x, y, "x*y=", x*y)
input()
