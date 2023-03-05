import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n > 0:
        inorder(left[n])
        inorder(right[n])
        cal.append(result[n]) # 연산하기 위한 리스트에 추가

T = 10
for tc in range(1, T + 1):
    N = int(input())
    result = [0] * (N + 1) # 연산 값 넣을 리스트
    data = [list(input().split()) for _ in range(N)]
    cal = [] # 연산하기 위한 리스트

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    for n in range(N): # 부모 인덱스로 왼쪽, 오른쪽 자식노드 리스트 형성
        idx = int(data[n][0]) # 인풋 첫번째 값 = 부모 노드
        if len(data[n]) == 2: # 값만 들어있을 때
            result[idx] = data[n][1]
        else: # 연산자, 왼쪽, 오른쪽
            result[idx] = data[n][1]
            left[idx] = int(data[n][2])
            right[idx] = int(data[n][3])

    inorder(1)

    stack = []
    for token in cal: # 계산
        if token.isdecimal():
            stack.append(token)
        else:
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            if token == '+':
                stack.append(n2 + n1)
            elif token == '-':
                stack.append(n2 - n1)
            elif token == '/':
                if n1 == 0 or n2 == 0:
                    stack.append(0)
                else:
                    stack.append(n2 // n1)
            elif token == '*':
                stack.append(n2 * n1)

    if len(stack) == 1:
        print(f'#{tc} {stack.pop()}')