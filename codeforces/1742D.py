# 1742D - Coprime
# https://codeforces.com/contest/1742/problem/D

## 에디토리얼 참고 했으나 pypy3 로 제출시 통과
## 문제의 조건을 잘 읽자 
## 이 문제는 1000까지 범위가 중요했음
## 20000 ^ 2 -> 1000 ^ 2 으로 낮춰서 풀음
import math
t = int(input())
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    arr = [-1 for _ in range(1001)]
    ans = -1
    for i in range(len(data)):
        arr[data[i]] = max(arr[data[i]], i + 1)

    for i in range(1, len(arr)):
        for j in range(i, len(arr)):
            if (arr[i] != -1 and arr[j] != -1) and math.gcd(i, j) == 1:
                ans = max(ans, arr[i] + arr[j])
    print(ans)
