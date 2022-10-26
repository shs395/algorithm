# 1620 - 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
pokemon = dict()
for i in range(N):
    temp = input().rstrip()
    pokemon[temp] = i + 1
    pokemon[str(i + 1)] = temp

for i in range(M):
    print(pokemon[input().rstrip()])
