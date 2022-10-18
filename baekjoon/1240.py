# 1240 - 노드사이의 거리
from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    count = 0
    queue = deque([[x, count]])
    visited = [False for _ in range(N + 1)]
    visited[x] = True
    while queue:
        temp_x, temp_count = queue.popleft()

        for i in range(1, len(tree[temp_x])):
            if visited[i] == False and tree[temp_x][i] != -1:
                if i == y:
                    return temp_count + tree[temp_x][i]
                visited[i] = True
                queue.append([i, temp_count + tree[temp_x][i]])
                 
    return count



N, M = map(int, input().split())
tree = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, distance = map(int, input().split())
    tree[a][b] = distance
    tree[b][a] = distance

for _ in range(M):
    x, y = map(int, input().split())
    print(bfs(x, y))
