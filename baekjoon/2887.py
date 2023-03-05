# 2887 - 행성 터널
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

data = []

N = int(input().rstrip())

for i in range(N):
    x, y, z = map(int, input().rstrip().split())
    data.append([x, y, z, i + 1])

edges = []
parent = [i for i in range(N + 1)]

for i in range(3):
    tmp = sorted(data, key=lambda x:x[i])
    for j in range(len(tmp) - 1):
        edges.append([tmp[j + 1][i] - tmp[j][i], tmp[j][3], tmp[j + 1][3]])

edges.sort()
answer = 0
for edge in edges:
    if find_parent(parent, edge[1]) != find_parent(parent, edge[2]):
        union_parent(parent, edge[1], edge[2])
        answer += edge[0]

print(answer)