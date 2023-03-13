def solution(n, m, section):
    answer = 0
    idx = 0
    for x in section:
        if idx < x:
            answer += 1
            idx = x + m - 1
    return answer
