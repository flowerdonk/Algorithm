import heapq
'''
def solution(food_times, k):
    answer = -1
    h = []
    food_nums = len(food_times)
    
    for food_idx in range(food_nums):
        heapq.heappush(h, (food_times[food_idx], food_idx + 1))
    
    turn = 0
    
    while h:
        time = (h[0][0] - turn) * food_nums
        
        if k >= time:
            k -= time
            turn, _ = heapq.heappop(h)
            food_nums -= 1
        
        else:
            temp = k % food_nums
            h.sort(key=lambda x: x[1])
            answer = h[temp][1]
            break
    
    return answer
'''

def solution(food_times, k):
    food_num = len(food_times)
    h = []
    answer = -1
    
    for idx in range(food_num):
        heapq.heappush(h, (food_times[idx], idx + 1))
    
    turn = 0
    while h:
        time = (h[0][0] - turn) * food_num
        
        if k >= time:
            turn, _ = heapq.heappop(h)
            k -= time
            food_num -= 1
        
        else:
            idx = k % food_num
            h.sort(key=lambda x:x[1])
            answer = h[idx][1]
            break

    return answer

