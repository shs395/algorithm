# 1764 - 듣보잡
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = set()
b = set()
for _ in range(N):
    a.add(input().rstrip())

for _ in range(M):
    b.add(input().rstrip())

int_list = list(a.intersection(b))
int_list.sort()
print(len(int_list))
for i in int_list:
    print(i)