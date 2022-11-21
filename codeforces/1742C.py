# 1742C - Stripes
# https://codeforces.com/contest/1742/problem/C
t = int(input())

for _ in range(t):
    data = []
    ans = ''
    input()
    for _ in range(8):
        data.append(list(input()))

    for i in range(8):
        if data[i].count('R') == 8:
            ans = 'R'
            break

    if ans == '':
        for i in range(8):
            sumB = 0
            for j in range(8):
                if data[j][i] == 'B':
                    sumB += 1
            if sumB == 8:
                ans = 'B'
                break
    print(ans)

    