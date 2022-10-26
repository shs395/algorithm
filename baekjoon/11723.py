# 11723 - 집합
import sys
input = sys.stdin.readline
M = int(input().rstrip())
data = set()
for _ in range(M):
    temp = input().rstrip().split()
    if temp[0] == 'add':
        if int(temp[1]) not in data:
            data.add(int(temp[1]))
    elif temp[0] == 'check':
        if int(temp[1]) in data:
            print(1)
        else:
            print(0)
    elif temp[0] == 'remove':
        if int(temp[1]) in data:
            data.remove(int(temp[1]))
    elif temp[0] == 'toggle':
        if int(temp[1]) in data:
            data.remove(int(temp[1]))
        else:
            data.add(int(temp[1]))
    elif temp[0] == 'all':
        data = {i for i in range(1, 21)}
    elif temp[0] == 'empty':
        data = set()