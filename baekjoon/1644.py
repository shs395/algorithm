# 1644 - 소수의 연속합
N = int(input())
prime = []
data = [True] * (N + 1)
M = int(pow(N, 1 / 2)) + 1

for i in range(2, M):
    if data[i] == True:
        for j in range(i + i, N + 1, i):
            data[j] = False

for i in range(2, N + 1):
    if data[i] == True:
        prime.append(i)

end = 0
tmp_sum = 0
answer = 0

for start in range(len(prime)):
    while tmp_sum < N and end < len(prime):
        tmp_sum += prime[end]
        end += 1
        
    if tmp_sum == N:
        answer += 1
    tmp_sum -= prime[start]

print(answer)


