# 1806 - 부분합
N, S = map(int, input().split())
data = list(map(int, input().split()))

start = 0
end = 0
psum = 0
answer = int(1e9)

for start in range(len(data)):
    while psum < S and end < len(data):
        psum += data[end]
        end += 1
        
    if psum >= S:
        answer = min(answer, end - start)
    
    psum -= data[start]

if answer == int(1e9):
    print(0)
else:
    print(answer)
