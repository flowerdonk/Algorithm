def babygin(i, k):
    if i == k:
        if p[0] == p[1] == p[2] or p[0] + 2 == p[1] + 1 == p[2]:
            if p[3] == p[4] == p[5] or p[3] + 2 == p[4] + 1 == p[5]:
                global ans
                ans = True
    else:
        for j in range(i, k):
            p[i], p[j] = p[j], p[i]
            babygin(i + 1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T + 1):
    p = list(map(int, list(input())))
    ans = False
    babygin(0, 6)
    print(ans)