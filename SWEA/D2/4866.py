def bracket(string):
    stack = []
    for i in range(len(string)):
        if len(stack) == 0:
            if string[i] == ')' or string[i] == '}':
                return 0

        if string[i] == '(' or string[i] == '{':
            stack.append(string[i])

        elif string[i] == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0

        elif string[i] == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0

        else:
            continue

    if len(stack) == 0:
        return 1

    return 0

T = int(input())
for i in range(1, T + 1):
    string = input()
    print(f'#{i} {bracket(string)}')