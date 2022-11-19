# B - Lost Permutation
# https://codeforces.com/problemset/problem/1759/B
import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    m, s = map(int, input().rstrip().split())
    b = list(map(int, input().rstrip().split()))
    temp = []
    for i in range(1, 100):
        if s == 0 and max(max(b), max(temp)) == len(b) + len(temp):
            print('YES')
            break
        elif s < 0:
            print('NO')
            break
        if i not in b:
            m -= 1
            s -= i
            temp.append(i)
        else:
            continue
