X, Y = map(int, input().split()) # 원숭 -> 멍멍

# 1일차, 마지막 = 1
# 1씩 차이

n = 0
diff = Y - X
ans = 0

if diff == 0:
    print(0)
else:
    while n * n < diff:
        n += 1

    if n * n != diff:
        n -= 1

    ans = n + n - 1
    temp = diff - (n * n)
    if temp:
        ans += temp // n
        if temp % n:
            ans += 1

    print(ans)