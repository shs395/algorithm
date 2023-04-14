# 14725 - 개미굴

class Trie():
    def __init__(self):
        self.head = {}

    def insert(self, foods):
        current = self.head

        for food in foods:
            if food not in current:
                current[food] = {}
            current = current[food]
        current[0] = True

    def search(self, level, current):
        if 0 in current:
            return 
        cur = sorted(current)
        for x in cur:
            print('--' * level + x)
            self.search(level + 1, current[x])


N = int(input())
t = Trie()
for _ in range(N):
    x = input().split()
    K = x[0]
    foods = x[1:]
    t.insert(foods)
t.search(0, t.head)
