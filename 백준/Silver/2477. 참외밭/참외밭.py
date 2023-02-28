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
    if data[n][1] == length and data[(n + 7) % 6][1] == height:
        l_idx = (n + 7) % 6
    elif data[n][1] == height and data[(n + 7) % 6][1] == length:
        l_idx = (n + 7) % 6

minus1 = data[(l_idx + 2) % 6][1]
minus2 = data[(l_idx + 3) % 6][1]

ans = length * height - minus1 * minus2
print(ans * K)