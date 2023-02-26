# 10825 - 국영수
import sys
input = sys.stdin.readline
N = int(input().rstrip())
data = []
for _ in range(N):
    a, b, c, d = input().rstrip().split()
    data.append((a, int(b), int(c), int(d)))

data.sort(key=lambda x:x[0])
data.sort(reverse=True, key=lambda x:x[3])
data.sort(key=lambda x:x[2])
data.sort(reverse=True, key=lambda x:x[1])

for x in data:
    print(x[0])
