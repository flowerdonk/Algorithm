import heapq

# def solution(food_times, k):
#     answer = -1
#     h = []
#     food_len = len(food_times)
#     for idx in range(food_len):
#         # (음식 개수, 음식 번호)
#         heapq.heappush(h, (food_times[idx], idx + 1))
    
#     pre = 0 # 이전에 먹은 음식 수
    
#     while h:
#         # 남은 음식 중 가장 적게 남은 음식을 다 먹는데 걸리는 시간
#         time = (h[0][0] - pre) * food_len
        
#         if k >= time: # 시간이 남았을 경우, 현재 음식 빼고 계속 반복
#             k -= time
#             pre, _ = heapq.heappop(h)
#             food_len -= 1
            
#         else: # 시간이 없는 경우(음식이 남았을 때)
#             idx = k % food_len
#             h.sort(key=lambda x: x[1]) # 음식 번호로 정렬
#             answer = h[idx][1]
#             break
        
#     return answer










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