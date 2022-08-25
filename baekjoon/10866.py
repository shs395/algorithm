# 10866 - 덱
from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
data = deque()
for i in range(N):
    temp = input().split()
    if temp[0] == 'push_front':
        data.appendleft(temp[1])
    elif temp[0] == 'push_back':
        data.append(temp[1])
    elif temp[0] == 'pop_front':
        if len(data) != 0:
            print(data.popleft())
        else:
            print('-1')
    elif temp[0] == 'pop_back':
        if len(data) != 0:
            print(data.pop())
        else:
            print('-1')
    elif temp[0] == 'size':
        print(len(data))
    elif temp[0] == 'empty':
        if len(data) != 0:
            print('0')
        else:
            print('1')
    elif temp[0] == 'front':
        if len(data) != 0:
            print(data[0])
        else:
            print('-1')
    elif temp[0] == 'back':
        if len(data) != 0:
            print(data[-1])
        else:
            print('-1')

