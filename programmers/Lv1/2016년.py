def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU', ]
    days = 0
    days += sum(month[:a - 1])
    days += b - 1
    return day[days % 7]
