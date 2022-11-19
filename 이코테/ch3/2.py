# 2 - 큰 수의 법칙

# 내 풀이
# O(M) 의 풀이
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
temp_K = K
ans = 0
while M > 0:
    if temp_K > 0:
        ans += data[0]
        temp_K -= 1
    elif temp_K == 0:
        ans += data[1]
        temp_K = K
    M -= 1
print(ans)

# 책에 있는 풀이
# 수학적으로 접근 -> 반복되는 수열 찾기
N, M, K = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)
first = data[0]
second = data[1]
cnt = (M // (K + 1))
r = M % (K + 1)
ans = first * (cnt * K + r) + second * cnt
print(ans)
