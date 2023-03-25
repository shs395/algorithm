# 17398 - 통신망 분할
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, cnt):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
        cnt[a] += cnt[b] 
        cnt[b] = 0
    elif a > b:
        parent[a] = b
        cnt[b] += cnt[a]
        cnt[a] = 0

N, M, Q = map(int, input().split())
data = []
stack = []
parent = [i for i in range(N + 1)]
cnt = [1] * (N + 1)

for _ in range(M):
    X, Y = map(int, input().split())
    data.append((X, Y))

for _ in range(Q):
    A = int(input())
    stack.append(data[A - 1])
    data[A - 1] = 0

for x in data:
    if x != 0:
        a = x[0]
        b = x[1]
        union_parent(parent, a, b, cnt)
        
answer = 0

while stack:
    x = stack.pop()
    a = x[0]
    b = x[1]
    parent_a = find_parent(parent, a)
    parent_b = find_parent(parent, b)
    if parent_a != parent_b:
        answer += (cnt[parent_a] * cnt[parent_b])
        union_parent(parent, a, b, cnt)

print(answer)
