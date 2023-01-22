import statistics
FILENAME = "day7data"
data = open(FILENAME, "r").read()
data = list(map(int, data.split(",")))


def fuelusage(point):
    ans = 0
    for x in data:
        distance = abs(point - x)
        ans += (distance * (distance+1))/2
    return(ans)


point = round(statistics.mean(data))
minReached = False
while(minReached is False):
    if fuelusage(point+1) < fuelusage(point):
        point = point + 1
    else:
        minReached = True

print(fuelusage(point))
