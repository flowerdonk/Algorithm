N = int(input())
data = list(map(int, input().split()))

mx = 1
cnt_i = 1
cnt_d = 1

for l in range(N - 1):
    if data[l] < data[l + 1]:
        cnt_i += 1
        cnt_d = 1

    elif data[l] > data[l + 1]:
        cnt_d += 1
        cnt_i = 1

    else:
        cnt_d += 1
        cnt_i += 1
        
    mx = cnt_d if mx <= cnt_d else mx
    mx = cnt_i if mx <= cnt_i else mx
    
print(mx)