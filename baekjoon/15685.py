# 15685 - 드래곤 커브

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
arr = [[0 for _ in range(101)] for _ in range(101)]

def make_dragon_curve(x, y, d, g):
    # 0 번째
    dir_arr = [d]
    arr[y][x] = 1
    x = dx[d] + x
    y = dy[d] + y
    arr[y][x] = 1 

    for i in range(g):
        new_dir_arr = dir_arr[:]

        if i == 0:
            for idx in range(len(dir_arr)):
                x = dx[(dir_arr[idx] + 1) % 4] + x
                y = dy[(dir_arr[idx] + 1) % 4] + y
                new_dir_arr.append((dir_arr[idx] + 1) % 4)
                arr[y][x] = 1 
        else:
            for idx in range(len(dir_arr)):
                if idx < len(dir_arr) / 2:
                    new_dir = (dir_arr[idx] + 2) % 4
                else:
                    new_dir = dir_arr[idx]
                x = dx[new_dir] + x
                y = dy[new_dir] + y
                new_dir_arr.append(new_dir)
                arr[y][x] = 1 
        
        dir_arr = new_dir_arr
    
def check_rectangle():
    cnt = 0

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1]:
                cnt += 1

    return cnt


N = int(input())
for _ in range(N):
    x, y, d, g = map(int, input().split())

    make_dragon_curve(x, y, d, g)

print(check_rectangle())

