# 1929 - 소수 구하기
M, N = map(int, input().split())
data = [True] * (N + 1)
data[1] = False
for i in range(2, N + 1):
    if data[i] == True:
        for j in range(i + i, N + 1, i):
            data[j] = False

for i in range(M, N + 1):
    if data[i] == True:
        print(i)