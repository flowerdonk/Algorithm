import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    data = input()
    data_l = len(data)
    result = [''] * 5

    for l in data:
        for i in range(5):
            for j in range(4):
                if i == 0 or i == 4:
                    if j == 2:
                        result[i] += '#'
                    else:
                        result[i] += '.'
                elif i == 1 or i == 3:
                    if j == 1 or j == 3:
                        result[i] += '#'
                    else:
                        result[i] += '.'
                elif i == 2:
                    if j == 2:
                        result[i] += l
                    elif j == 0:
                        result[i] += '#'
                    else:
                        result[i] += '.'

    for n in range(5):
        if n == 2:
            print(result[n] + '#')
        else:
            print(result[n] + '.')
