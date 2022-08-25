# 10814 - 나이순 정렬
import sys
input = sys.stdin.readline
N = int(input())
data = []
for i in range(N):
    age, name = input().split()
    data.append([int(age), name]) 

data.sort(key=lambda x:x[0])

for i in data:
    print(i[0], i[1])
