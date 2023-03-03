# 2143 - 두 배열의 합
from collections import defaultdict
T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
answer = 0

a_prefix_sum = [0]
b_prefix_sum = [0]

for i in range(len(a)):
    a_prefix_sum.append(a[i] + a_prefix_sum[i])

for i in range(len(b)):
    b_prefix_sum.append(b[i] + b_prefix_sum[i])

a_dict = defaultdict(int)
b_dict = defaultdict(int)
for i in range(len(a_prefix_sum) - 1):
    for j in range(i + 1, len(a_prefix_sum)):
        a_dict[a_prefix_sum[j] - a_prefix_sum[i]] += 1
        
for i in range(len(b_prefix_sum) - 1):
    for j in range(i + 1, len(b_prefix_sum)):
        answer += a_dict[T - (b_prefix_sum[j] - b_prefix_sum[i])]
        
print(answer)