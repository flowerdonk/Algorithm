def Letter(str1, str2):
    str_dict = {}
    for key in str1:
        str_dict[key] = 0
    for key in str2:
        if key in str_dict.keys():
            str_dict[key] += 1

    return max(str_dict.values())

T = int(input())
for i in range(1, T + 1):
    str1 = input()
    str2 = input()
    print(f'#{i} {Letter(str1, str2)}')

