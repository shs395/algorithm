# 1613 - 역사
import sys 
input = sys.stdin.readline

def floyd():
    for x in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if graph[a][x] == 1 and graph[x][b] == 1:
                    graph[a][b] = 1

                    
n, k = map(int, input().rstrip().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, input().rstrip().split())
    graph[a][b] = 1


floyd()

s = int(input().rstrip())
for _ in range(s):
    a, b = map(int, input().rstrip().split())
    if graph[a][b] == 1:
        print('-1')
    elif graph[b][a] == 1:
        print('1')
    else:
        print('0')