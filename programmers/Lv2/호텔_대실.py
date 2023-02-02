def time_to_seconds(x):
    h, m = x.split(':')
    return int(h) * 3600 + int(m) * 60

def solution(book_time):
    data = [0] * (time_to_seconds('23:59') + 1)
    
    for start_time, end_time in book_time:
        data[time_to_seconds(start_time)] += 1
        if time_to_seconds(end_time) + 600 <= time_to_seconds('23:59'):
            data[time_to_seconds(end_time) + 600] -= 1
        
    for i in range(1, len(data)):
        data[i] = data[i - 1] + data[i]
            
    return max(data)
