from sys import stdin
N = int(stdin.readline())
data = [list(map(int, stdin.readline().split())) for _ in range(N)]
data.sort(key= lambda x: (x[1], x[0]))

end = data[0][1]
cnt = 1
for s, e in data[1:]:
    if s >= end:
        end = e
        cnt += 1

print(cnt)