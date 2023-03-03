w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

x = (p + t) % w if (p + t) // w % 2 == 0 else w - (p + t) % w
y = (q + t) % h if (q + t) // h % 2 == 0 else h - (q + t) % h
print(x, y)