import statistics
FILENAME = "day7data"
data = open(FILENAME, "r").read()
data = list(map(int, data.split(",")))

point = statistics.median(data)
ans = 0
for x in data:
    ans += abs(point - x)

print(ans)
