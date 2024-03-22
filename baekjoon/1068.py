# 1068 - 트리

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

child_node = [[] for _ in range(N)]
deleted_node = [0 for _ in range(N)]

def dfs(node):
    deleted_node[node] = 1
    for next_node in child_node[node]:
        dfs(next_node)
    return 


for i in range(len(arr)):
    if arr[i] == -1:
        continue
    child_node[arr[i]].append(i)

dfs(X)

ans = 0
for i in range(N):
    flag = 0

    if deleted_node[i] == 0:
        for j in child_node[i]:
            if deleted_node[j] == 0:
                flag = 1
                break
    else:
        flag = 1
        
    if flag == 0:
        ans += 1

print(ans)