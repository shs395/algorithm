# 1713 - 후보 추천하기
from collections import deque
N = int(input())
a = int(input())
recommends = list(map(int, input().split()))
students = [0 for _ in range(a + 1)]
queue = deque()
for recommend in recommends:
    # 사진틀이 남아있는 경우
    if len(queue) < N:
        if students[recommend] == 0:
            queue.append(recommend)
        students[recommend] += 1
    # 사진틀이 없는 경우
    else:
        if students[recommend] != 0:
            students[recommend] += 1
        else:
            min_student = []
            min_cnt = 1001
            for i, s in enumerate(students):
                if s > 0:
                    if s == min_cnt:
                        min_student.append(i)  
                    elif s < min_cnt:
                        min_cnt = s
                        min_student = []
                        min_student.append(i)
            
            if len(min_student) == 1:
                queue.remove(min_student[0])
                students[min_student[0]] = 0
            else:
                for x in queue:
                    if x in min_student:
                        queue.remove(x)
                        students[x] = 0
                        break
            students[recommend] += 1
            queue.append(recommend)
print(*sorted(list(queue)))



    