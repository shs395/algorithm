# 1920 - 수 찾기
N = int(input())
A = list(map(int, input().split()))
M = int(input())
data = list(map(int, input().split()))

A.sort()

def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1
    
for i in data:
    if binary_search(A, i, 0, N - 1) == -1:
        print('0')
    else:
        print('1')
