for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # case 'd'
    if p1 < x2 or q1 < y2 or p2 < x1 or q2 < y1:
        print('d')

    # case 'b'
    elif x2 == p1 or x1 == p2:
        if y2 == q1 or y1 == q2: # case 'c'
            print('c')
        else:
            print('b')

    elif y2 == q1 or y1 == q2:
        print('b')

    # case 'a'
    else:
        print('a')