# A - Yes-Yes?
# https://codeforces.com/problemset/problem/1759/A
import sys
input = sys.stdin.readline
compare_word = 'Yes' * 18
t = int(input().rstrip())
for _ in range(t):
    s = input().rstrip()
    if s in compare_word:
        print('YES')
    else:
        print('NO')

