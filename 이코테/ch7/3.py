# 3 - 떡볶이 떡 만들기
# 파라메트릭 서치 이용하기

N, M = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = max(data)
ans = 0
while start <= end:
    mid = (start + end) // 2
    temp_sum = 0
    for x in data:
        if x > mid:
            temp_sum += x - mid
    
    if temp_sum >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
