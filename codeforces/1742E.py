# 1742E - Scuza
# https://codeforces.com/contest/1742/problem/E
# 계단 개수, 질문의 리스트 길이가 각각 20,000 
# N^2 로 푸는 것은 X
# 계단의 위치를 이진 탐색으로 찾음 -> 인덱스를 이진으로 탐색하고 탐색시마다 해당 범위를 탐색
# 슬라이싱 잘 쓰지 말자, 리스트에 저장해서 쓰자
t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    steps = list(map(int, input().split()))
    max_steps = [0 for _ in range(len(steps))]
    max_steps[0] = steps[0]
    sum_steps = [0 for _ in range(len(steps))]
    sum_steps[0] = steps[0]
    for i in range(1, len(steps)):
        if steps[i] > max_steps[i - 1]:
            max_steps[i] = steps[i]
        else:
            max_steps[i] = max_steps[i - 1]
        sum_steps[i] = steps[i] + sum_steps[i - 1]
    questions = list(map(int, input().split()))
    for question in questions:
        start = 0
        end = len(steps) - 1
        idx = -1
        while start <= end:
            mid = (start + end) // 2
            # if max(steps[:mid + 1]) <= question:
            if max_steps[mid] <= question:
                start = mid + 1
                idx = mid
            else:
                end = mid - 1
        if idx == -1:
            print(0, end=' ')
        else:
            print(sum_steps[idx], end=' ')
            # print(sum(steps[:idx + 1]), end=' ')
    print()


