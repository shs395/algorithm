# 177D1 - Encrypting Messages
# https://codeforces.com/problemset/problem/177/D1
n, m, c = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(n - m + 1):
    for j in range(len(b)):
        a[i + j] += b[j]
        a[i + j] %= c

print(*a)