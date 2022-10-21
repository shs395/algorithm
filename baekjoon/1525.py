# 1525 - 퍼즐
from collections import deque
from itertools import permutations

def custom_swap(s, i, j):
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

puzzle_list = list(map(''.join, permutations('012345678', 9)))
puzzle_dict = dict()
for p in puzzle_list:
    puzzle_dict[p] = False
ans_puzzle = '123456780'
input_puzzle = ''
count = -1

for _ in range(3):
    a, b, c = input().split()
    input_puzzle += a + b + c

puzzle_dict[input_puzzle] = True

queue = deque([[input_puzzle, 0]])

while queue:
    temp_puzzle, temp_count = queue.popleft()
    
    if temp_puzzle == ans_puzzle:
        count = temp_count
        break
    
    zero_idx = temp_puzzle.find('0')

    if zero_idx == 0:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])

        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])
        
        
    elif zero_idx == 1:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])

        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])

        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

    elif zero_idx == 2:
        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])

        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

    elif zero_idx == 3:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])

        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])
        
        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])


    elif zero_idx == 4:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])

        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])

        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])

    elif zero_idx == 5:
        temp_b = custom_swap(temp_puzzle, zero_idx, zero_idx + 3)
        if puzzle_dict[temp_b] == False:
            puzzle_dict[temp_b] = True
            queue.append([temp_b, temp_count + 1])

        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])

    elif zero_idx == 6:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])
        
        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])

    elif zero_idx == 7:
        temp_a = custom_swap(temp_puzzle, zero_idx, zero_idx + 1)
        if puzzle_dict[temp_a] == False:
            puzzle_dict[temp_a] = True
            queue.append([temp_a, temp_count + 1])

        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])

    elif zero_idx == 8:         
        temp_c = custom_swap(temp_puzzle, zero_idx, zero_idx - 1)
        if puzzle_dict[temp_c] == False:
            puzzle_dict[temp_c] = True
            queue.append([temp_c, temp_count + 1])

        temp_d = custom_swap(temp_puzzle, zero_idx, zero_idx - 3)
        if puzzle_dict[temp_d] == False:
            puzzle_dict[temp_d] = True
            queue.append([temp_d, temp_count + 1])

print(count)
