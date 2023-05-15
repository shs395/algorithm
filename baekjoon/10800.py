# 10800 - 컬러볼
import sys
input = sys.stdin.readline

N = int(input().rstrip())
balls = []
answer = [0] * (N + 1)

for i in range(N):
    c, s = map(int, input().rstrip().split())
    balls.append((c, s, i))

sorted_balls = sorted(balls, key=lambda x:x[0])
sorted_balls.sort(key=lambda x:x[1])

prefix_color = [0] * (N + 1)
before_color = sorted_balls[0][0]
before_color_sum = sorted_balls[0][1]
before_cnt = sorted_balls[0][1]
before_cnt_sum = sorted_balls[0][1]
all_ball_sum = 0

for x in sorted_balls[1:]:
    if x[1] > before_cnt:
        all_ball_sum += before_cnt_sum
        before_cnt_sum = x[1]

        prefix_color[before_color] += before_color_sum
        
        before_color = x[0]
        before_color_sum = x[1]

        before_cnt = x[1]
        
    else:
        if x[0] == before_color:
            before_color_sum += x[1]
            before_cnt_sum += x[1]
        else:
            prefix_color[before_color] += before_color_sum
            before_color = x[0]
            
            before_color_sum = x[1]
            before_cnt_sum += x[1]
    answer[x[2] + 1] = all_ball_sum - prefix_color[x[0]]

for x in answer[1:]:
    print(x)

