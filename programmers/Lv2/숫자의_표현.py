def solution(n):
    answer = 0
    temp = 0
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            temp += j
            if temp == n:
                answer += 1
                temp = 0
                break
            elif temp > n:
                temp = 0
                break
    return answer
