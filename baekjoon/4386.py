# 4386 - 별자리 만들기
from collections import deque

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
data = []
edges = []
parent = [0] * n
for i in range(n):
    parent[i] = i


for _ in range(n):
    x, y = map(float, input().split())
    data.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        tmp = pow(pow(data[i][0] - data[j][0], 2) + pow(data[i][1] - data[j][1], 2), 0.5)
        edges.append((tmp, i, j))

edges.sort(key=lambda x:x[0])
answer = 0
cnt = 0

for edge in edges:
    if cnt == n - 1:
        break
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):    
        answer += edge[0]
        cnt += 1
        union_parent(parent, edge[1], edge[2])

print(round(answer, 2))