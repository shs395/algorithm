# 1021 - 회전하는 큐
from collections import deque
N, M = map(int, input().split())
data = list(map(int, input().split()))
queue = deque([i for i in range(1, N + 1)])

answer = 0
for x in data:
    while True:
        if queue[0] == x:
            queue.popleft()
            break
        else:
            y = queue.index(x)
            if y < len(queue) / 2:
                for _ in range(y):
                    queue.append(queue.popleft())
                    answer += 1
            else:
                for _ in range(len(queue) - y):
                    queue.appendleft(queue.pop())
                    answer += 1


print(answer)