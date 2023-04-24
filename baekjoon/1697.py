# 1697 - 숨바꼭질
from collections import deque
N, K = map(int, input().split())
INF = int(1e9)
visited = [INF] * 200001
answer = 0
queue = deque()
queue.append((N, 0))
while queue:
    now, cnt = queue.popleft()
    if now == K:
        answer = cnt
        break
    else:
        if 0 <= now + 1 <= 200000 and visited[now + 1] > cnt + 1:
            visited[now + 1] = cnt + 1
            queue.append((now + 1, cnt + 1))
        if 0 <= now - 1 <= 200000 and visited[now - 1] > cnt + 1:
            visited[now - 1] = cnt + 1
            queue.append((now - 1, cnt + 1))
        if 0 <= now * 2 <= 200000 and visited[now * 2] > cnt + 1:
            visited[now * 2] = cnt + 1
            queue.append((now * 2, cnt + 1))
            
print(answer)

