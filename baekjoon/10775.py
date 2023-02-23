# 10775 - 공항
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

import sys
input = sys.stdin.readline
G = int(input().rstrip())
P = int(input().rstrip())

parent = [0] * (G + 1)
answer = 0
flag = True

for i in range(1, G + 1):
    parent[i] = i

for _ in range(P):
    gate = int(input().rstrip())
    if flag:
        if parent[gate] == gate:
            answer += 1
            union_parent(parent, gate, gate - 1)
        else:
            if find_parent(parent, gate) == 0:
                flag = False
            else:
                answer += 1
                union_parent(parent, gate, parent[gate] - 1)
                
print(answer)



