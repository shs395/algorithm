# 11050 - 이항 계수 1
import math
N, K = map(int, input().split())
print(math.factorial(N) // (math.factorial(K) * math.factorial(N - K)))
