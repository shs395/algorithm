# 1148 - 단어 만들기
# 조건이 정확히 주어지지 않아서 답답했음
# 처음에는 퍼즐에서 만들 수 있는 모든 경우를 순열로 구해서 dictionary 에 있는지 조회했으나 시간초과
# 반대로 dictionary 에 있는 단어들을 퍼즐에서 만들 수 있는지 확인해서 통과했음
import sys
input = sys.stdin.readline
from itertools import permutations
dictionary = dict()

def is_possible(puzzle, cmp_word):
    temp = puzzle[:]
    for c in cmp_word:
        if temp[ord(c) - 65] > 0:
            temp[ord(c) - 65] -= 1
        else:
            return False
    return True
while True:
    temp = input().rstrip()
    if temp == '-':
        break
    else:
        dictionary[temp] = ''
    
while True:
    temp = input().rstrip()
    if temp == '#':
        break
    else:
        puzzle = [0 for _ in range(26)]
        alphabet_arr = [-1 for _ in range(26)]
        for x in list(temp):
            puzzle[ord(x) - 65] += 1
            alphabet_arr[ord(x) - 65] = 0
        for x in dictionary:
            if is_possible(puzzle, x) == True:
                for y in set(x):
                    alphabet_arr[ord(y) - 65] += 1


        min_word = ''
        min_cnt = 999999
        max_word = ''
        max_cnt = -1
        for a in range(26):
            if alphabet_arr[a] < min_cnt and alphabet_arr[a] >= 0:
                min_cnt = alphabet_arr[a]
                min_word = chr(a + 65)
            elif alphabet_arr[a] == min_cnt and alphabet_arr[a] >= 0:
                min_word += chr(a + 65)
            if alphabet_arr[a] > max_cnt and alphabet_arr[a] >= 0:
                max_cnt = alphabet_arr[a]
                max_word = chr(a + 65)
            elif alphabet_arr[a] == max_cnt and alphabet_arr[a] >= 0:
                max_word += chr(a + 65)

        print(min_word, min_cnt, max_word, max_cnt)