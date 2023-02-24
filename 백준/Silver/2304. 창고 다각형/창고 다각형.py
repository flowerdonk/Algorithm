pillarN = int(input())
store = [] * 1000
input_pillar = []
for i in range(pillarN):
    input_pillar.append(list(map(int, input().split())))

max_L = 0
max_H = 0
max_H_idx = 0
for i in range(pillarN):
    if max_L <= input_pillar[i][0]:
        max_L = input_pillar[i][0]

for i in range(pillarN):
    if max_H <= input_pillar[i][1]:
        max_H = input_pillar[i][1]
        max_H_idx = input_pillar[i][0]

for i in range(1, max_L + 1):
    count = 0
    for r in range(pillarN):
        if input_pillar[r][0] == i:
            store.insert(i, input_pillar[r][1])
            count += 1
            break
    
    if count == 0:
        store.insert(i, 0)

area = 0
big = 0
for i in range(max_H_idx):
    if i < max_H_idx:
        if big < store[i]:
            big = store[i]
        area += big
    elif i == max_H_idx:
        area += max_H
    
big = 0
for i in range(max_L - max_H_idx):
    if big < store[max_L - 1 - i]:
        big = store[max_L - 1 - i]
    area += big
    

print(area)
