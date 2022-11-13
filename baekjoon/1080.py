# 1080 - 행렬
# 그리디
N, M = map(int, input().split())
A = []
B = []
answer = 0
def reverse_matrix(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            A[i][j] = abs(A[i][j] - 1)

def is_matrix_same():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return False
    return True

for _ in range(N):
    A.append(list(map(int, list(input()))))
for _ in range(N):
    B.append(list(map(int, list(input()))))

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            reverse_matrix(i, j)
            answer += 1

if is_matrix_same() == False:
    answer = -1

print(answer)