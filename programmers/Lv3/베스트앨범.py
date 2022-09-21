# def setting(data):
#     return data[1]
from collections import Counter
def solution(genres, plays):
    answer = []
    data = dict()
    genre_count = dict()
    for genre, i, play in zip(genres, range(len(plays)), plays):
        if genre not in data:
            data[genre] = [[i, play]]
            genre_count[genre] = play
        else:
            data[genre].append([i, play])
            genre_count[genre] += play
    for i in list(Counter(genre_count).most_common()):
        data[i[0]].sort(key=lambda x:x[1], reverse=True)
        for j in range(len(data[i[0]])):
            if j >= 2:
                break
            answer.append(data[i[0]][j][0])
    return answer
    # answer = []
    # temp = {}
    # temp2 = {}
    # for i in range(len(genres)):
    #     if temp.get(genres[i]) == None:
    #         temp[genres[i]] = []
    #         temp2[genres[i]] = 0
    #     temp[genres[i]].append((i, plays[i]))
    #     temp2[genres[i]] += plays[i]
    # temp2_arr = []
    # for i in temp2.keys():
    #     temp2_arr.append((i, temp2[i]))
    # temp2_arr.sort(reverse=True, key=setting)
    # for i in temp.keys():
    #     temp[i].sort(reverse=True, key=setting)
    # for i in temp2_arr:
    #     answer.append(temp[i[0]][0][0])
    #     if len(temp[i[0]]) >= 2:
    #         answer.append(temp[i[0]][1][0])
    # return answer
