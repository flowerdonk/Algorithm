import sys
sys.setrecursionlimit(1000)

def solution(numbers):
    answer = []
    for num in numbers:
        bin_num = bin(num)[2:]
        s_idx = 0
        temp = len(bin_num)
        cnt = 1
        while temp >= 2:
            temp //= 2
            cnt += 1
        for n in range(2**cnt - 1 - len(bin_num)):
            bin_num = '0' + bin_num
        answer.append(check_node(bin_num))
        
    return answer

def check_node(bin_num):
    l = len(bin_num)
    mid = l // 2
    
    if l == 1 or '0' not in bin_num or '1' not in bin_num:
        return 1
    
    if bin_num[mid] == '0':
        return 0
    
    return check_node(bin_num[:mid]) * check_node(bin_num[mid + 1:])