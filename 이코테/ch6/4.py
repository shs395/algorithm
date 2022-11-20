# 4 - 두 배열의 원소 교체
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort(reverse=True)
print(sum(A) - sum(A[:K]) + sum(B[:K]))