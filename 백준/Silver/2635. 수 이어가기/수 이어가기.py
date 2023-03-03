def Numbers(first_num):
    max_list = []
    max_count = 0

    for i in range(1, first_num + 1):
        num_list = [first_num]
        num = first_num//2
        num += i
        count = 0

        while num >= 0:
            num_list.append(num)
            num = num_list[count] - num
            if num < 0:
                break
            count += 1
        
        if max_count <= len(num_list):
            max_count = len(num_list)
            max_list = num_list[:]

    return max_list

first_num = int(input())
num = Numbers(first_num)
print(len(num))
for i in range(len(num)):
    print(num[i], end = ' ')