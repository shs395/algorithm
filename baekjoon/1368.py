# 1368 - 물대기
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = parent[a]
    b = parent[b]

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


N = int(input())
parent = [i for i in range(N + 1)]
edges = []

for i in range(N):
    edges.append((int(input()), 0, i + 1))

connect_cost = []
for i in range(N):
    connect_cost.append(list(map(int, input().split())))


for i in range(N - 1):
    for j in range(i + 1, N):
        edges.append((connect_cost[i][j], i + 1, j + 1))

edges.sort()
answer = 0
cnt = 0

for cost, i, j in edges:
    if find_parent(parent, i) != find_parent(parent, j):
        answer += cost
        cnt += 1
        union_parent(parent, i, j)
        if cnt == N:
            break
            
print(answer)