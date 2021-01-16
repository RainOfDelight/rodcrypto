state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]


def add_round_key(s, k):
    for i in range(0,4):
        partialResult=[]
        for j in range(0,4):
            b1=s[i][j]
            b2=k[i][j]
            partialResult.append(b1 ^ b2)
        s[i]=partialResult

add_round_key(state, round_key)
print(state)
