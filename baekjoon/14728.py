# 14728 - 벼락치기
# 배낭문제에서 1차원 dp 테이블을 사용할 경우 뒤에서부터 탐색하자
N, T = map(int, input().split())
dp = [0] * (T + 1)
study_time = []
score = []
for _ in range(N):
    K, S = map(int, input().split())
    study_time.append(K)
    score.append(S)

for i in range(N):
    temp_time = study_time[i]
    temp_score = score[i]
    for j in range(T, temp_time -1, -1):
        dp[j] = max(dp[j], dp[j - temp_time] + temp_score)
print(dp[-1])
    

