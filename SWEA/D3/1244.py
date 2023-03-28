T = int(input())
for tc in range(1, T + 1):
    Numbers, turn = input().split()
    Numbers = list(map(int, list(Numbers)))
    turn = int(turn)
    N = len(Numbers)

    Ncnt = [0] * 10
    for n in range(N):
        Ncnt[Numbers[n]] += 1

    mxs = []
    if max(Numbers) == Ncnt.index(max(Ncnt)):
        temp = max(Numbers)
        for idx in range(N):
            if Numbers[idx] == temp:
                mxs.append(idx)

    cnt = 0
    i = 0
    while cnt < turn and i < N:
        # 첫 번째 원소부터 큰 수로 바꿈, 바꾸게 되면 cnt + 1
        mx = Numbers[i]
        mx_idx = i
        for j in range(i + 1, N):
            if Numbers[j] >= mx:
                mx = Numbers[j]
                mx_idx = j

        if mx_idx == i:
            i += 1
            continue

        Numbers[i], Numbers[mx_idx] = Numbers[mx_idx], Numbers[i]
        cnt += 1
        i += 1

    if max(Ncnt) < 2:
        for n in range(turn - cnt):
            Numbers[-1], Numbers[-2] = Numbers[-2], Numbers[-1]

    if mxs:
        ls = len(mxs) if len(mxs) <= cnt else cnt
        new_mxs = []
        for l in range(1, ls + 1):
            new_mxs.append(Numbers[mxs[-l]])
        new_mxs.sort()
        for l in range(1, ls + 1):
            Numbers[mxs[-l]] = new_mxs[l - 1]

    print(f'#{tc} ', end='')
    for n in Numbers:
        print(n, end='')
    print()
