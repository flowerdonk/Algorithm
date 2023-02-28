T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    arr = [0]
    for d in data:
        ds = list(d)
        for idx in d:
            if idx != '0' and arr[-1] != ds:
                arr.append(ds)
                break

    for a in arr[1:]:
        for i in range(len(a)):
            tmp = int(a[i], 16) # 10진수로 바꾸고
            tmp = bin(tmp).replace('0b', '') # 10진수에서 2진수로 바꾸기
            a[i] = tmp
    codes = []
    for a in arr[1:]:
        result = '' # 한 문장으로
        for l in a:
            while len(l) != 4:
                l = '0' + l
            result += ''.join(l)
        codes.append(result)

    print(codes)

    if tc == 6:
        break

'''
68B46DDB9346F4
06 8B 46 DD B9 34 6F
#1 38
#2 0
#3 36
#4 36
#5 44
#6 80
#7 76
#8 72
#9 182
#10 166
#11 212
#12 192
#13 1164
#14 1196
#15 1272
#16 1584
#17 4378
#18 6908
#19 7736
#20 6604
'''