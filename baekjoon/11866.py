# 11866 - 요세푸스 문제 0
N, K = map(int, input().split())
data = [i + 1 for i in range(N)]
ans = []
count = 1
idx = 0
while len(ans) != N:
    idx = (idx + K - 1) % len(data) 
    ans.append(data[idx])
    data.remove(data[idx]) 

print('<', end='')
for i in range(len(ans) - 1):
    print(f'{ans[i]}, ', end='')
print(f'{ans[-1]}>', end='')