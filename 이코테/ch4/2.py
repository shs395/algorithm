# 2 - 왕실의 나이트
# 평소에 4방향 탐색 때는 dx, dy 이용해서 range(4)의 for 문으로 해결
# 이 문제는 step 을 튜플 형태로 리스트에 저장해놓아서 풀기

input_data = input()
row = int(input_data[1])
col = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    nr = row + step[0]
    nc = col + step[1]
    if 1 <= nr <= 8 and 1 <= nc <= 8:
        result +=1

print(result)
