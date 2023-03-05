T = int(input())
for tc in range(1, T + 1):
    data = list(input())
    l = len(data)
    pipe, lazer = 0, 0
    ans = 0
    for n in range(l - 1):
        if data[n] == '(' and data[n + 1] == ")":
            ans += pipe
        elif data[n] == '(':
            pipe += 1
        elif data[n] == ')' and data[n - 1] != '(':
            pipe -= 1
            ans += 1
    ans += pipe
    print(f'#{tc} {ans}')