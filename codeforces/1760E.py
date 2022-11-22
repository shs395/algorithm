# 1760E - Binary Inversions
# https://codeforces.com/contest/1760/problem/E
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    one_cnt = 0
    zero_cnt = 0
    temp = [[] for _ in range(n)]
    for i in range(len(a)): 
        temp[i].append(one_cnt)
        if a[i] == 1:
            one_cnt += 1
        
    for i in range(len(a) - 1, -1, -1):
        temp[i].append(zero_cnt)
        if a[i] == 0:
            zero_cnt += 1

    ans = 0
    add_num = 0
    for i in range(len(temp)):
        if a[i] == 0:
            add_num = max(add_num, temp[i][1] - temp[i][0])
        else:
            ans += temp[i][1]
            add_num = max(add_num, temp[i][0] - temp[i][1])
    print(ans + add_num)