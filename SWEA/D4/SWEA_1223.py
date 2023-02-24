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
                if token == '(':
                    stack.append(token)

                elif token == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()

                elif token == '*' or token == '/':
                    while stack and stack[-1] == '*' or stack[-1] == '/':
                        result += stack.pop()
                    stack.append(token)

                elif token == '+' or token == '-':
                    while stack and stack[-1] != '(':
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

    ans = ''
    stack = []
    for n in postfix:
        if n.isdecimal():
            stack.append(int(n))
        else:
            if n == '.':
                if len(stack) == 1:
                    print(f'#{i} {stack.pop()}')
                    break
                else:
                    print(f'#{i} error')
                    break

            elif len(stack) >= 2:
                n1 = int(stack.pop())
                n2 = int(stack.pop())

                if n == '+':
                    stack.append(n2 + n1)
                elif n == '-':
                    stack.append(n2 - n1)
                elif n == '*':
                    stack.append(n2 * n1)
                elif n == '/':
                    stack.append(n2 // n1)
                else:
                    print(f'#{i} error')
                    break

            else:
                print(f'#{i} error')
                break