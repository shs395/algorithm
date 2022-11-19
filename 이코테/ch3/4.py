# 4 - 1이 될 때까지
import time
# 내 풀이
N, K = map(int, input().split())
start_time = time.time()
cnt = 0
while N > 1:
    if N % K == 0:
        N //= K
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)
end_time = time.time()
print('내 풀이 :', end_time - start_time)
# 책에 있는 풀이
# 내 풀이는 나눠지지 않을 때 1씩 계속 빼야하지만 책에서는 한 번에 빼줌
# K 가 클수록 효과적
N, K = map(int, input().split())
start_time = time.time()
ans = 0
while True:
    # 다음 K로 나눠지는 수 구하기
    target = (N // K) * K
    ans += (N - target)
    N = target
    if N < K:
        break
    ans += 1
    N //= K

ans += (N - 1)
print(ans)
end_time = time.time()
print('책 풀이 :', end_time - start_time)