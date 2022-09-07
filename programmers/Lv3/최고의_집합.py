def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    if s % n == 0:
        return [s // n for _ in range(n)]
    else:
        r = s % n
        q = s // n
        answer = [q for _ in range(n)]
        while r > 0:
            for i in range(len(answer)):
                if r <= 0:
                    break
                answer[i] += 1
                r -= 1
        answer.sort()
        return answer
