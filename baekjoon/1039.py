# 1039 - 교환
from collections import deque

N, K = map(int, input().split())
N = str(N)
M = len(N)
answer = -1
queue = deque([[N, 0]])
visited = [[] for _ in range(K + 1)]
if M >= 2:
    while queue:
        temp_N, depth = queue.popleft()
        if depth >= K:
            answer = max(answer, int(temp_N))
        elif len(str(temp_N)) == 2 and temp_N[1] == '0':
            break
        else:
            for j in range(2, M + 1):
                for i in range(1, j):
                    if temp_N[j - 1] == 0:
                        continue
                    else:
                        temp_j = temp_N[j - 1]
                        temp_i = temp_N[i - 1]
                        temp = ''
                        temp += temp_N[:i - 1]
                        temp += temp_j
                        temp += temp_N[i:j - 1]
                        temp += temp_i
                        temp += temp_N[j:]
                        if temp not in visited[depth]:
                            visited[depth].append(temp)
                            queue.append([temp, depth + 1])

    print(answer)
else:
    print('-1')