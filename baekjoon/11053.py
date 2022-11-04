# 11053 - 가장 긴 증가하는 부분 수열

A = int(input())
ans = 1
arr = list(map(int, input().split()))

# 풀이 1 일반적 DP 이용 메모리: 30840 kb, 시간 200 ms
# length = [0 for _ in range(len(arr))]
# for i in range(len(arr)):
#     length[i] = 1
#     for j in range(i):
#         if arr[j] < arr[i]:
#             length[i] = max(length[i], length[j] + 1)
            
# print(max(length))


# 풀이 2 이분탐색 이용, 마지막보다 크면 뒤에 넣고 아니면 이분탐색으로 안에 넣기
# def bs(data, target, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         if data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
        
#     return start

# dp = [arr[0]]

# for i in arr:
#     if i > dp[ans - 1]:
#         dp.append(i)
#         ans += 1
#     else:
#         dp[bs(dp, i, 0, ans - 1)] = i

# print(len(dp))

# 풀이 3 bisect 라이브러리 사용
from bisect import bisect_left

dp = [arr[0]]

for i in arr:
    if i > dp[ans - 1]:
        dp.append(i)
        ans += 1
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp))