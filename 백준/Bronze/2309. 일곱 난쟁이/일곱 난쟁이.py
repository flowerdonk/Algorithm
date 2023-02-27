data = [int(input()) for _ in range(9)]
diff = sum(data) - 100

for n in data:
    if diff - n != n and (diff - n) in data:
        data.remove(n)
        data.remove(diff - n)
        break

data.sort()
for i in data:
    print(i)