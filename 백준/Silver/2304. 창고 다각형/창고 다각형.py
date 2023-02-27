pillarN = int(input())
input_pillar = [list(map(int, input().split())) for _ in range(pillarN)]
input_pillar.sort(key= lambda x : x[0])
length = input_pillar[-1][0]
mx_idx, mx_num = max(input_pillar, key = lambda x : x[1])

store = [0] * (length + 1)
for p in input_pillar:
    store[p[0]] = p[1]

mx = 0
area = mx_num
for n in range(mx_idx):
    if store[n] >= mx:
        mx = store[n]
    area += mx

mx = 0
for n in range(length, mx_idx, -1):
    if store[n] >= mx:
        mx = store[n]
    area += mx

print(area)