# 3 - 성적이 낮은 순서로 학생 출력하기
N = int(input())
data = []
for _ in range(N):
    data.append(input().split())

data.sort(key=lambda x:x[1])

for i in data:
    print(i[0], end=' ')