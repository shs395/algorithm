# 1742A - Sum
# https://codeforces.com/contest/1742/problem/A
t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    data.sort()
    if data[2] == data[1] + data[0]:
        print('Yes')
    else:
        print('No')
    