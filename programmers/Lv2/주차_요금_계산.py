def solution(fees, records):
    answer = []
    arr = dict()
    # [상태, 시간, 분, 주차시간]
    standard_time, standard_fee, unit_time, unit_fee = fees
    for record in records:
        time, car, data = record.split()
        hour = int(time[:2])
        minute = int(time[3:])
        if data == 'IN':
            if car in arr.keys() and arr[car][0] == 'OUT':
                arr[car] = ['IN', hour, minute, arr[car][3]]
            else:
                arr[car] = ['IN', hour, minute, 0]
        elif data == 'OUT':
            if car in arr.keys() and arr[car][0] == 'IN':
                temp_hour = hour - arr[car][1]
                temp_minute = minute - arr[car][2]
                temp_time = temp_hour * 60 + temp_minute
                arr[car] = ['OUT', hour, minute, arr[car][3] + temp_time]
    
    for x in arr:
        if arr[x][0] == 'IN':
            temp_hour = 23 - arr[x][1]
            temp_minute = 59 - arr[x][2]
            temp_time = temp_hour * 60 + temp_minute
            arr[x][0] = 'OUT'
            arr[x][3] = arr[x][3] + temp_time
    
    for x in arr:
        parking_time = arr[x][3]
        if parking_time <= standard_time:
            arr[x].append(standard_fee)
        else:
            temp = parking_time - standard_time
            if temp % unit_time == 0:
                arr[x].append(standard_fee + (temp // unit_time) * unit_fee)
            else:
                arr[x].append(standard_fee + (temp // unit_time + 1) * unit_fee)
    car_list = list(arr.keys())
    car_list.sort()
    for car in car_list:
        answer.append(arr[car][4])
    return answer
