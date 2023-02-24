def repeat(letter):
    stack = []
    for i in range(len(letter)):
        if len(stack) == 0:
            stack.append(letter[i])
        else:
            if stack[-1] == letter[i]:
                stack.pop()
            else:
                stack.append(letter[i])

    return len(stack)

T = int(input())
for i in range(1, T + 1):
    letter = input()
    print(f'#{i} {repeat(letter)}')