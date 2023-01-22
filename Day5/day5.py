boardsize = 1000

def markPoints(board, line):
    if line[0][0] == line[1][0]:
        axis = 1
    else:
        axis = 0

    if line[0][axis] > line[1][axis]:
        larger = line[0]
        smaller = line[1]
    else:
        larger = line[1]
        smaller = line[0]

    for x in range(smaller[axis], larger[axis] + 1):
        print(smaller)
        board[smaller[0]][smaller[1]] += 1
        smaller[axis] += 1
    return board

#first sort out the data correctly
data = open("day5data", "r").read().splitlines()
entries = []
for line in data:
    points = line.split(" -> ")
    entry = []
    for point in points:
        x = list(map(int, point.split(",")))
        entry.append(x)

    #discard diagonal entries for some reason
    if entry[0][0] == entry[1][0] or entry[0][1] == entry[1][1]:
        entries.append(entry)


board = [[0 for i in range(boardsize)] for j in range(boardsize)]



for line in entries:
    board = markPoints(board, line)

ans = 0
for x in board:
    for y in x:
        if y > 1:
            ans+=1
print(ans)
