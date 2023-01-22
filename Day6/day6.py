NUMBER_OF_DAYS = 80
FILENAME = "day6data"

data = open(FILENAME, "r").read()
data = list(map(int, data.split(",")))


class Fish:
    def __init__(self, spawntimer):
        self.spawntimer = spawntimer

    def age(self):
        self.spawntimer -= 1
        if self.spawntimer < 0:
            self.spawntimer = 6
            return Fish(8)


fishlist = []
for val in data:
    fishlist.append(Fish(val))

for i in range(NUMBER_OF_DAYS):
    newfish = []
    for fish in fishlist:
        newfishcheck = fish.age()
        if isinstance(newfishcheck, Fish):
            newfish.append(newfishcheck)
    fishlist = fishlist + newfish

print(len(fishlist))
