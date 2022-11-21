# 1742B - Increasing
# https://codeforces.com/contest/1742/problem/B
t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data_set = set(data)
    if len(data) == len(data_set):
        print('YES')
    else:
        print('NO')