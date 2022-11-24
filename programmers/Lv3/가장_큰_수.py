def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i]) * 3
    numbers.sort(reverse=True)
    for number in numbers:
        answer += number[:(len(number) // 3)]
    if answer.count('0') == len(answer):
        answer = '0'
    return answer
