# 1966 - 프린터 큐
from collections import deque
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    data = deque(list(map(int, input().split())))
    answer = 0
    
    while True:
        if data[0] == max(data):
            data.popleft()
            if M == 0:
                answer += 1
                break
            else:
                answer += 1
                M -= 1
        else:
            data.append(data.popleft())
            if M == 0:
                M += len(data) - 1
            else:
                M -= 1

    print(answer)

