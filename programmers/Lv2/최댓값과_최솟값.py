def solution(s):
    answer = ''
    a = list(map(int, s.split()))
    answer += str(min(a))
    answer += ' '
    answer += str(max(a))
    return answer
