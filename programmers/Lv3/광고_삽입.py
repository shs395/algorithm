def time_to_seconds(time):
    h, m, s = map(int, time.split(':'))
    return 3600 * h + 60 * m + s

def seconds_to_time(time):
    h = time // 3600
    if h < 10:
        h = '0' + str(h)
    time %= 3600
    
    m = time // 60
    if m < 10:
        m = '0' + str(m)  
    time %= 60
    
    s = time
    if s < 10:
        s = '0' + str(s)
    return str(h) + ':' + str(m) + ':' + str(s)
    
def solution(play_time, adv_time, logs):
    answer = 0
    max_num = 0
    data = [0] * (time_to_seconds(play_time) + 1)
    
    for log in logs:
        start_time, end_time = log.split('-')
        data[time_to_seconds(start_time)] += 1
        data[time_to_seconds(end_time)] -= 1
    
    cnt = 0
    for i in range(len(data)):
        cnt += data[i] 
        data[i] = cnt
    
    for i in range(1, len(data)):
        data[i] = data[i] + data[i - 1]
    
    ad_time = time_to_seconds(adv_time)
    
    for i in range(ad_time, len(data)):
        if data[i] - data[i - ad_time] > max_num:
            max_num = data[i] - data[i - ad_time]
            if i == ad_time:
                answer = i - ad_time
            else: 
                answer = i - ad_time + 1
    
    return seconds_to_time(answer)
