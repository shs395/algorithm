# 2 - 부품 찾기
# 100만 개의 입력을 100만 개의 데이터셋에서 찾는 문제
# 세 가지 풀이를 생각해 볼 수 있다.
N = int(input())
data = list(map(int, input().split()))
data.sort()
M = int(input())
m_list = list(map(int, input().split()))
# 1. 이진탐색
print(data)
def binary_search(target):
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

ans = []
for x in m_list:
    print(x)
    if binary_search(x) != None:
        ans.append('yes')
    else:
        ans.append('no')

for x in ans:
    print(x, end=' ')

# 2. set() -> set 은 해시테이블로 구성되어 있고 찾을 때  O(1) 임
# 3. count sort 이용
