NUMBER_OF_DAYS = 256
FILENAME = "day6data"

data = open(FILENAME, "r").read()
data = list(map(int, data.split(",")))

daysleft = [0 for i in range(9)]

for i in data:
    daysleft[i] += 1

for i in range(NUMBER_OF_DAYS):
    newdays = [0 for i in range(9)]
    for j in range(len(daysleft)-1, 0, -1):
        newdays[j-1] = daysleft[j]
    newdays[6] += daysleft[0]
    newdays[8] = daysleft[0]
    daysleft = newdays
ans = 0
for i in daysleft:
    ans += i

print(ans)
