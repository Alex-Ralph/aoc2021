data = open("day3data.txt", "r").read().splitlines()
entries = len(data)
numsize = len(data[0])
counter = [0] * numsize

for number in data:
    for a in range(numsize):
        if number[a] == "1":
            counter[a] += 1

ans = [0] * numsize
for x in range(numsize):
    if counter[x] > entries/2:
        ans[x] = 1

print("Gamma is: ")
print(ans)
