# 10423 - 전기가 부족해
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

N, M, K = map(int, input().rstrip().split())
pp_list = list(map(int, input().rstrip().split()))
edges = []
parent = [0] * (N + 1)
answer = 0

for i in range(1, N + 1):
    parent[i] = i

if K > 1:
    for i in range(len(pp_list) - 1):
        union_parent(parent, pp_list[i], pp_list[i + 1])

for _ in range(M):
    u, v, w = map(int, input().rstrip().split())
    edges.append((w, u, v))

edges.sort()

for edge in edges:
    cost = edge[0]
    a = edge[1]
    b = edge[2]

    if find_parent(parent, a) != find_parent(parent, b):
        answer += cost
        union_parent(parent, a, b)

print(answer)