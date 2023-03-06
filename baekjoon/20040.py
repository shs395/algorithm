# 20040 - 사이클 게임
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

n, m = map(int, input().rstrip().split())

parent = [i for i in range(n)]
flag = True
answer = 0
for i in range(m):
    a, b = map(int, input().rstrip().split())
    if flag:
        if find_parent(parent, a) == find_parent(parent, b):
            answer = i + 1
            flag = False
        else:
            union_parent(parent, a, b)

    
print(answer)



