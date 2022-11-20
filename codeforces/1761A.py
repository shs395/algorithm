# 1761A - Two Permutations
# https://codeforces.com/problemset/problem/1761/A
# n == a == b 인 경우를 생각해 냈어야 하는 문제
import sys
input = sys.stdin.readline
t = int(input().rstrip())
for _ in range(t):
    n, a, b = map(int, input().rstrip().split())
    if n == 1:
        print('Yes')
    else:
        if n - a - b >= 2:
            print('Yes')
        elif n == a and n == b:
            print('Yes')
        else:
            print('No')