# 1300 - K번째 수
N = int(input())
k = int(input())

start = 0
end = N * N
answer =0

while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(1, N + 1):
        if i > mid:
            break
        cnt += min(mid // i, N)
    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1
        answer = mid

print(answer)