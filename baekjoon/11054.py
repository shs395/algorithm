# 11054 - 가장 긴 바이토닉 부분 수열
import bisect
N = int(input())
A = list(map(int, input().split()))
answer = 0

for mid in range(len(A) + 1):
    left = A[:mid]
    right = A[mid:]
    # print(left, right)
    right.reverse()
    left_lis = []
    right_lis = []
    for x in left:
        if len(left_lis) == 0:
            left_lis.append(x)
        else:
            if x > left_lis[-1]:
                left_lis.append(x)
            else:
                left_lis[bisect.bisect_left(left_lis, x)] = x

    if len(left_lis) > 0:
        y = left_lis[-1]
    else:
        y = 1001

    for x in right:
        if x < y:
            if len(right_lis) == 0:
                right_lis.append(x)
            else:
                if x > right_lis[-1]:
                    right_lis.append(x)
                else:
                    right_lis[bisect.bisect_left(right_lis, x)] = x
        
    answer = max(answer, len(left_lis) + len(right_lis))
    # print(y, len(left_lis) + len(right_lis), answer)

print(answer)