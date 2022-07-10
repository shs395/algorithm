def solution(numbers):
    answer = 0
    arr = [0] * 10
    for number in numbers:
        arr[number] += 1
    for idx, cnt in enumerate(arr):
        if cnt == 0:
            answer += idx
    return answer
