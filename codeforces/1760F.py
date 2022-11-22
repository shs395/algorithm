# 1760F - Quests
# https://codeforces.com/contest/1760/problem/F
t = int(input())
for _ in range(t):
    n, c, d = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    k = -1
    start = 0
    end = d
    while start <= end:
        mid = (start + end) // 2
        if sum(a[:mid + 1]) * (d // (mid + 1)) + sum(a[:d % (mid + 1)]) >= c:
            start = mid + 1
            k = mid
        else:
            end = mid - 1
    if k >= d:
        print('Infinity')
    elif k == -1:
        print('Impossible')
    else:
        print(k)
        
