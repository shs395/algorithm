# A - Medium Number
# https://codeforces.com/contest/1760/problem/A

t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    data.sort()
    print(data[1])
    