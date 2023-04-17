# 14621 - 나만 안되는 연애
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


N, M = map(int, input().split())
data = input().rstrip().split()
edges = []
parent = []
for i in range(N + 1):
    parent.append(i)

answer = 0
for _ in range(M):
    u, v, d = map(int, input().split())
    edges.append((d, u, v))

edges.sort()
e_cnt = 0

for d, u, v in edges:
    if data[u - 1] != data[v - 1] and find_parent(parent, u) != find_parent(parent, v):
        answer += d
        union_parent(parent, u, v)
        e_cnt += 1 
        if e_cnt == N - 1:
            break

if e_cnt != N - 1:
    answer = -1

print(answer)