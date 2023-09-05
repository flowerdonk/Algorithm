def solution(play_time, adv_time, logs):
    answer = ''
    
    def count_secs(time):
        h, m, s = map(int, time.split(":"))
        return h * 3600 + m * 60 + s
    
    def return_str(time):
        h = time // 3600
        h = '0' + str(h) if h < 10 else str(h)
        time = time % 3600
        
        m = time // 60
        m = '0' + str(m) if m < 10 else str(m)
        time = time % 60
        
        s = '0' + str(time) if time < 10 else str(time)
        
        return h + ":" + m + ":" + s
    
    play_secs = count_secs(play_time)
    adv_secs = count_secs(adv_time)
    sums = [0] * (play_secs + 1)
    
    for log in logs:
        str_start, str_end = log.split("-")
        start = count_secs(str_start)
        end = count_secs(str_end)
        sums[start] += 1
        sums[end] -= 1
        
    for x in range(1, play_secs + 1):
        sums[x] = sums[x] + sums[x-1]
    
    for x in range(1, play_secs + 1):
        sums[x] = sums[x] + sums[x-1]
    
    max_view = sums[adv_secs - 1]
    max_time = 0
    
    for i in range(adv_secs, play_secs):
        if max_view < sums[i] - sums[i - adv_secs]:
            max_view = sums[i] - sums[i - adv_secs]
            max_time = i - adv_secs + 1
    
    answer = return_str(max_time)
    
    return answer