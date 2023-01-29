from collections import deque
def solution(n, left, right):
    answer = deque()
    start_idx = left // n + 1
    end_idx = right // n + 1

    for i in range(start_idx, end_idx + 1):
        temp = i
        for _ in range(i):
            answer.append(temp)
        for _ in range(n - i):
            temp += 1
            answer.append(temp)

    for _ in range(left % n):
        answer.popleft()
    if (right + 1) % n != 0:
        for _ in range(n - (right + 1) % n):
            answer.pop()
            
    return list(answer)
