FILENAME = "data8"
data = open(FILENAME, "r").read().splitlines()

outputs = (x.split(" | ")[1] for x in data)

ans = 0
for line in outputs:
    numbers = line.split(" ")
    for number in numbers:
        if len(number) in [2, 4, 3, 7]:
            ans += 1

print(ans)
