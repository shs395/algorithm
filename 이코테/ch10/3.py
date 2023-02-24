# 3 - 도시 분할 계획
import sys
input = sys.stdin.readline

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


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
answer = 0
last = 0

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost = edge[0]
    a = edge[1]
    b = edge[2]
    # 싸이클이 아닌 경우
    if find_parent(parent, a) != find_parent(parent, b):
        answer += cost
        last = cost
        union_parent(parent, a, b)

print(answer - last)