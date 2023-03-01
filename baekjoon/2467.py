# 2467 - 용액
def main():
    n = int(input())
    data = list(map(int, input().split()))
    start = 0
    end = len(data) - 1
    cnt = 100000000000
    answer = []
    while start < end:
        x = data[start] + data[end]
        if abs(x) < cnt:
            cnt = abs(x)
            answer = [data[start], data[end]]
        
        if x > 0:
            end -= 1
        elif x < 0:
            start += 1
        else:
            break

    print(*answer)

main()