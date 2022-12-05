from collections import deque
def hhmm_to_minute(hhmm):
    hh, mm = hhmm.split(':')
    return int(hh) * 60 + int(mm)

def solution(n, t, m, timetable):
    answer = ''
    timetable.sort()
    start = 60 * 9
    before_time = 0
    idx = 0
    for i in range(n - 1):
        temp_m = 0
        while temp_m < m:
            if hhmm_to_minute(timetable[idx]) > start:
                break
            else:
                idx += 1
                temp_m += 1
                if hhmm_to_minute(timetable[idx]) > before_time:
                    before_time = hhmm_to_minute(timetable[idx])
        start += t
    print(start, idx, m, before_time)
    for i in range(m - 1):
        if hhmm_to_minute(timetable[idx]) > start:
            answer = start
        else:
            if hhmm_to_minute(timetable[idx]) > before_time:
                before_time = hhmm_to_minute(timetable[idx])
            idx += 1
            
    if idx >= len(timetable):
        answer = start
    else:
        if hhmm_to_minute(timetable[idx]) <= start:
            answer = max(before_time - 1, hhmm_to_minute(timetable[idx]) - 1)
        else:
            answer = start
            
    temp = ''  
    if answer // 60 < 10:
        temp += '0' + str(answer // 60)
    else:
        temp += str(answer // 60)
    temp += ':'
    if answer % 60 < 10:
        temp += '0' + str(answer % 60)
    else:
        temp += str(answer % 60)
    answer = temp
    return answer
