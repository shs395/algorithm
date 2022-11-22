# 1760D - Challenging Valleys 
# https://codeforces.com/contest/1760/problem/D
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print('YES')
    else:
        l_list = []
        r_list = []
        for i in range(len(a)):
            if i == 0:
                l_list.append((i, a[i]))
            elif a[i - 1] > a[i]:
                l_list.append((i, a[i]))

            if i == len(a) - 1:
                r_list.append((i, a[i]))
            elif a[i] < a[i + 1]:
                r_list.append((i, a[i]))
        if l_list[-1][0] > r_list[0][0]:
            print('NO')
        elif l_list[-1][0] <= r_list[0][0] and l_list[-1][1] == r_list[0][1]:
            print('YES')
        else:
            print('NO')
        