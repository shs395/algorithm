# 4195 - 친구 네트워크
import sys
input = sys.stdin.readline
from collections import defaultdict

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b, total_parent):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
        total_parent[a] += total_parent[b]
    elif b < a:
        parent[a] = b
        total_parent[b] += total_parent[a]
    

T = int(input())
for _ in range(T):
    F = int(input())
    idx = 1
    parent = dict()
    total_parent = defaultdict(int)
    for _ in range(F):
        a, b = input().rstrip().split()
        if a not in parent and b not in parent:
            parent[a] = a
            parent[b] = b
            total_parent[a] = 1
            total_parent[b] = 1
        elif a not in parent and b in parent:
            parent[a] = a
            total_parent[a] = 1
        elif b not in parent and a in parent:
            parent[b] = b
            total_parent[b] = 1
        union_parent(parent, a, b, total_parent)
        print(total_parent[find_parent(parent, a)])

