import sys
sys.stdin = open('input.txt')

'''
divs = [2, 3, 5, 7, 11]
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    cnts = [0] * len(divs)

    for i in range(len(divs)):
        while N % divs[i] == 0:
            cnts[i] += 1
            N = N // divs[i]


    print(f'#{test_case}', *cnts)
'''
def Prime(Number):
    factors = [2, 3, 5, 7, 11]
    expos = [0] * 5
    idx = 0
    while Number > 1:
        if Number % factors[idx] == 0:
            expos[idx] += 1
            Number //= factors[idx]
            continue
        idx += 1

    return expos

# input
T = int(input())
Numbers =[]
for i in range(T):
    Numbers.append(int(input()))

for i in range(T):
    result = Prime(Numbers[i])
    print(f'#{i + 1}', *result)






