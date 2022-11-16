# 2002 - 추월
import sys
input = sys.stdin.readline
N = int(input().rstrip())
one = []
two = []
cnt = 0
for i in range(N):
    temp = input().rstrip()
    one.append(temp)

for i in range(N):
    two.append(input().rstrip())

for i in range(len(two)):
    if i < one.index(two[i]):
        one.remove(two[i])
        one.insert(i, two[i])
        cnt += 1
print(cnt)