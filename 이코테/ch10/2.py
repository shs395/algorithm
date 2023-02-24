# 2 - 팀 결성
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
parent = [0] * (N + 1)

for i in range(N + 1):
    parent[i] = i

for _ in range(M):
    a, b, c = map(int, input().split())
    if a == 0:
        union_parent(parent, b, c)
    elif a == 1:
        if find_parent(parent, b) == find_parent(parent, c):
            print('YES')
        else:
            print('NO')

# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1   
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

# NO
# NO
# YES