# 1005 - ACM Craft 
from collections import deque
import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    N, K = map(int, input().rstrip().split())
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]

    D = list(map(int, input().rstrip().split()))
    time = D[:]

    for _ in range(K):
        X, Y = map(int, input().rstrip().split())
        graph[X].append(Y)
        indegree[Y] += 1
    
    W = int(input().rstrip())
    
    queue = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()

        for i in graph[now]:
            indegree[i] -= 1
            time[i - 1] = max(D[i - 1] + time[now - 1], time[i - 1])
            if indegree[i] == 0:
                queue.append(i)
                
    print(time[W - 1])
    
