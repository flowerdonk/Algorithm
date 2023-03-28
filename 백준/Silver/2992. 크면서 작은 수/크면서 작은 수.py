X = input()
N = ''
mnN = '999999'
l = len(X)
used = [False] * l

def backtrack(depth):
    global N, mnN

    if depth == l:
        if X < N < mnN:
            mnN = N
        return

    for n in range(l):
        if used[n] == True:
            continue
        used[n] = True
        N += X[n]
        backtrack(depth + 1)
        used[n] = False
        N = N[:-1]

backtrack(0)
if mnN == '999999':
    mnN = 0
print(mnN)