# 5430 - AC
from collections import deque
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    p = input().rstrip()
    n = int(input().rstrip())
    error_flag = False
    reverse_flag = False
    if n == 0:
        temp = []
        input().rstrip()
    else:
        temp = input().rstrip()
        temp = deque(list(map(int, temp[1:-1].split(','))))
    for func in p:
        if func == 'D':
            if len(temp) == 0:
                print('error')
                error_flag = True
                break
            else:
                if reverse_flag == True:
                    temp.pop()
                else:  
                    temp.popleft()
        else:
            reverse_flag = not reverse_flag
    if error_flag == False:
        result = '['
        if reverse_flag == True:
            for i in range(len(temp)-1, -1, -1):
                result += str(temp[i])
                result += ','
            # while len(temp) != 0:
            #     result += str(temp.pop())
            #     result += ','
        else:
            for t in temp:
                result += str(t)
                result += ','
        if result[-1] == ',':
            result = result[:-1]
        result += ']'
        print(result)