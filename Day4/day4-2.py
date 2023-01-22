class Board:
    def __init__(self, boardarray):
        self.nums = boardarray

    def getnumber(self, number):
        for i in range(5):
            for j in range(5):
                if self.nums[i][j] == number:
                    self.nums[i][j] = -1

    def checkcorrect(self):
        #check rows
        for i in range(5):
            rowCorrect = True
            for j in range(5):
                if self.nums[i][j] != -1:
                    rowCorrect = False
                    break
            if rowCorrect == True:
                return True

        #check columns
        for j in range(5):

            colCorrect = True
            for i in range(5):
                if self.nums[i][j] != -1:
                    colCorrect = False
                    break
            if colCorrect == True:
                return True
        return False

def findWinner(boardlist):
    winners = []
    for board in boardlist:
        if board.checkcorrect():
            winners.append(board)
    return winners


data = open("day4data", "r").read().splitlines()
#get the list of calls first
calls = list(map(int, data[0].split(",")))
del data[0]

#use the rest of the data to produce boards
boardlist = []
boardarray = []

#removes empty lines
for x in data:
    if x == "":
        data.remove(x)

#makes a bunch of boards
i = 0
for x in data:
    if i < 5:
        boardarray.append(list(map(int, x.split())))
        i += 1
    else:
        boardlist.append(Board(boardarray))
        boardarray = []
        boardarray.append(list(map(int, x.split())))
        i=1

boardlist.append(Board(boardarray))

def findLastWinner(boardlist, calls):
    for call in calls:
        for board in boardlist:
            board.getnumber(call)
        x = findWinner(boardlist)
        if x != []:
            for y in x:
                if len(boardlist) > 1:
                    boardlist.remove(y)
                else:
                    print(y.nums)
                    print(call)
                    return

findLastWinner(boardlist, calls)
