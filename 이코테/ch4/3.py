# 3 - 게임 개발
#  사실상 bfs 문제 구현이 귀찮아서 패스
N, M = map(int, input().split())
A, B, d = map(int, input().split())
data = []
cnt = 0
for _ in range(N):
    data.append(list(map(int, input().split())))

