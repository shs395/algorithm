def solution(s):
    answer = [0, 0]
    while True:
        if s == '1':
            break
        answer[1] = answer[1] + s.count('0')
        s = len(s.replace('0', ''))
        temp = ''
        while s >= 1:
            temp = str(s % 2) + temp
            s = s // 2
        s = temp
        answer[0] = answer[0] + 1
    return answer


