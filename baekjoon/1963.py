# 1963 - 소수 경로
from collections import deque 

T = int(input())

data = [-1] * 10000
prime = dict()

for i in range(2, 10000):
    if data[i] == -1:
        data[i] = True
        for j in range(2 * i, 10000, i):
            data[j] = False
    
for i in range(1000, 10000):
    if data[i] == True:
        prime[i] = ''

for _ in range(T):
    visited = [1000000] * 10000
    a, b = map(int, input().split())
    visited[a] = 0
    queue = deque([(a, 0)])
    flag = False

    while queue:
        now, cnt = queue.popleft()
        now = list(str(now))
        for i in range(4):
            for j in range(9):
                now[i] = str((int(now[i]) + 1) % 10)
                if i == 0 and now[i] == '0':
                    continue
                tmp = int(''.join(now))
                if tmp == b:
                    print(cnt + 1)
                    flag = True
                    break
                if tmp in prime and visited[tmp] > cnt + 1:
                    visited[tmp] = cnt + 1
                    queue.append((tmp, cnt + 1))
            if flag:
                break
            now[i] = str((int(now[i]) + 1) % 10)
            tmp = int(''.join(now))
            if tmp == b:
                print(cnt)
                flag = True
                break
        if flag:
            break
    if flag == False:
        print('Impossible')