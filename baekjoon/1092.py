# 1092 - 배
N = int(input())
crane = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))
count = 0
crane.sort(reverse=True)
box.sort(reverse=True)

if box[0] > crane[0]:
    count = -1
else:
    while box != []:
        for i in crane:
            if box != []:
                if i < box[-1]:
                    continue
            for j in box:
                if i >= j:
                    box.remove(j)
                    break
        count += 1

print(count)
        

