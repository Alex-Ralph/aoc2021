#I thought yesterday was the worst thing I've ever written
#this is that and so much more
#markdiag shouldn't exist

boardsize = 1000

def markdiag(board, line):
    counter = 0
    if line[0][0] < line [1][0] and line[0][1] < line[1][1]:
        for x in range(line[0][0], line[1][0]+1):
            curx = line[0][0] + counter
            cury = line[0][1] + counter
            board[curx][cury] += 1
            counter += 1

    elif line[1][0] < line [0][0] and line[1][1] < line[0][1]:
        for x in range(line[1][0], line[0][0]+1):
            curx = line[1][0] + counter
            cury = line[1][1] + counter
            board[curx][cury] += 1
            counter += 1

    elif line[0][0] < line [1][0] and line[1][1] < line[0][1]:
        for x in range(line[0][0], line[1][0]+1):
            curx = line[0][0] + counter
            cury = line[0][1] - counter
            board[curx][cury] += 1
            counter += 1

    elif line[1][0] < line [0][0] and line[0][1] < line[1][1]:
        for x in range(line[1][0], line[0][0]+1):
            curx = line[0][0] - counter
            cury = line[0][1] + counter
            board[curx][cury] += 1
            counter += 1

    else:
        print("what the fuck")
        print(line)
        sys.exit()
    return board


def markstraight(board, line):
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
        board[smaller[0]][smaller[1]] += 1
        smaller[axis] += 1
    return board


def markPoints(board, line):

    if line[0][0] == line[1][0] or line[0][1] == line[1][1]:
        return markstraight(board, line)
    else:
        return markdiag(board, line)

#first sort out the data correctly
data = open("day5data", "r").read().splitlines()
entries = []
for line in data:
    points = line.split(" -> ")
    entry = []
    for point in points:
        x = list(map(int, point.split(",")))
        entry.append(x)
    entries.append(entry)


board = [[0 for i in range(boardsize)] for j in range(boardsize)]



for line in entries:
    board = markPoints(board, line)

ans = 0
for x in board:
    print(x)
    for y in x:
        if y > 1:
            ans+=1
print(ans)
