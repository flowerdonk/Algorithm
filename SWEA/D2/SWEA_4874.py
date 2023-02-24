T = int(input())
for i in range(1, T + 1):
    postfix = list(input().split())
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