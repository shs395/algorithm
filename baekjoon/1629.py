# 1629 - 곱셈
import bisect
A, B, C = map(int, input().split())
data = [0 for _ in range(32)]
two_square = [pow(2, i) for i in range(1, 32)]
answer = 1
data[0] = A
for i in range(1, len(data)):
    data[i] = (data[i - 1] * data[i - 1]) % C

while B > 0:
    idx = bisect.bisect_left(two_square, B)
    answer = (answer * data[idx]) % C
    B = B - pow(2, idx)

print(answer)