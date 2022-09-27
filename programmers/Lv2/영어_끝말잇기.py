def solution(n, words):
    answer = [0, 0]
    last_word = ''
    for idx, word in enumerate(words):
        if word in words[:idx]:
            answer = [(idx % n) + 1, idx // n + 1]
            break
        if idx == 0:
            last_word = word[-1]
            continue 
        if word[0] == last_word:
            last_word = word[-1]
        else:
            print(idx)
            answer = [(idx % n) + 1, idx // n + 1]
            break
        
    return answer
