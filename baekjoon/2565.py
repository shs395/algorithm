# 2565 - 전깃줄
import sys
input = sys.stdin.readline
import bisect

def solve():
    n = int(input().rstrip())
    data = []
    for _ in range(n):
        a, b = map(int, input().rstrip().split())
        data.append((a, b))

    data.sort(key=lambda x:x[0])
    lis = [data[0][1]]

    for i in range(1, len(data)):
        if data[i][1] > lis[-1]:
            lis.append(data[i][1])
        elif data[i][1] < lis[-1]:
            lis[bisect.bisect_left(lis, data[i][1])] = data[i][1]

    print(n - len(lis))
            

solve()
