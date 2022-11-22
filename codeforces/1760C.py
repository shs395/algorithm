# 1760C - Advantage
# https://codeforces.com/contest/1760/problem/C
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    arr = sorted(s)
    max_num = arr[-1]
    second_num = arr[-2]
    ans = []
    for i in s:
        if i != max_num:
            ans.append(i - max_num)
        else:
            ans.append(i - second_num)
    print(*ans)