import sys
sys.stdin = open('input.txt')

def caculate(N, arr):
    result = ''
    stack = []

    for token in arr:
        if token.isdecimal():
            result += token

        else:
            if not stack:
                stack.append(token)

            else:
                if token == '*':
                    while stack and stack[-1] == '*':
                        result += stack.pop()
                    stack.append(token)

                elif token == '+':
                    while stack:
                        result += stack.pop()
                    stack.append(token)

    while stack:
        result += stack.pop()

    return result

T = 10
for i in range(1, T + 1):
    N = int(input())
    arr = input()

    postfix = caculate(N, arr)

    stack = []
    for n in postfix:
        if n.isdecimal():
            stack.append(n)
        else:
            n1 = int(stack.pop())
            n2 = int(stack.pop())
            if n == '+':
                stack.append(n2 + n1)
            elif n == '*':
                stack.append(n2 * n1)

    print(f'#{i} {stack.pop()}')