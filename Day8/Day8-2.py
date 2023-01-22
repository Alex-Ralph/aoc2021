FILENAME = "testdata8"


def solve(patterns, output):
    for x in patterns:
        if len(x) == 2:
            cf = x
            for y in patterns:
                if len(y) == 6 and ((y.find(x[0] == -1) or y.find(x[1] == -1))):
                    
    return


data = open(FILENAME, "r").read().splitlines()

patternlist = list((x.split(" | ")[0] for x in data))

"""
segments without c && f:
5, 6, 2
5, 2 have length 5
6 has length 6
the other digit with length 6 is 0
find a length 6 without an a or a b (in this case), and the one it has maps to  f. The one it doesn't maps to c

Next: e, f -> b, d
Only one of b, d: 0 (len6), 2(len5), 3(len5),
find a len6 with only one of e and f
the one it has is a d, the one it does not is a b

e, g (fully unknown)

numbers only containing one of e and g:
3(len5), 5(len5), 9(len6)
find a len6 with only one of the two remaining letters
the one it has is a g
the other is an e

Simplified:
find digits in a len2
find a len6 with only one of those digits
find unsolved digits in a len4
find a len6 with only one of those

"""
