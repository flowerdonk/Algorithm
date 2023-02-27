import sys
sys.stdin = open('input.txt')

K = int(input())
data = [list(map(int, input().split())) for _ in range(6)]
l = []
h = []

for d in data:
    if d[0] == 1 or d[0] == 2:
        l.append(d[1])
    else:
        h.append(d[1])

l.sort()
h.sort()

length = l[-1]
height = h[-1]

for n in range(len(data)):
    if data[n][1] == length or data[n][1] == height:
        l_idx = n
# 최종 길이가 5, 1 일때 5를 기준으로 하게 됨

minus1 = data[(l_idx + 2) % 6][1]
minus2 = data[(l_idx + 3) % 6][1]

ans = length * height - minus1 * minus2
print(ans * K)


