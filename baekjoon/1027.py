# 1027 - 고층 건물
N = int(input())
heights = list(map(int, input().split()))
ans = 0
def search_right(start):
    dxdy = -1000000000
    cnt = 0
    height_start = heights[start]
    for i in range(start + 1, len(heights)):
        temp_dxdy = (heights[i] - height_start) / (i - start)
        if temp_dxdy > dxdy:
            cnt += 1
            dxdy = temp_dxdy
    return cnt

def search_left(start):
    dxdy = -1000000000
    cnt = 0
    height_start = heights[start]
    for i in range(start - 1, -1, -1):
        temp_dxdy = (heights[i] - height_start) / (start - i)
        if temp_dxdy > dxdy:
            cnt += 1
            dxdy = temp_dxdy
    return cnt

for i in range(len(heights)):
    if i == 0:
        ans = max(ans, search_right(i))
    elif i == len(heights) - 1:
        ans = max(ans, search_left(i))
    else:
        ans = max(ans, search_left(i) + search_right(i))
print(ans)