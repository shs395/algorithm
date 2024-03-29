# 1197 - 최소 스패닝 트리
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

v, e = map(int, input().rstrip().split())
edges = []
parent = [0] * (v + 1)
answer = 0

for i in range(1, v + 1):
    parent[i] = i

for _ in range(e):
    a, b, c = map(int, input().rstrip().split())
    edges.append((c, a, b))

edges.sort()

for edge in edges:
    cost = edge[0]
    a = edge[1]
    b = edge[2]
    if find_parent(parent, a) != find_parent(parent, b):
        answer += cost
        union_parent(parent, a, b)

print(answer)






