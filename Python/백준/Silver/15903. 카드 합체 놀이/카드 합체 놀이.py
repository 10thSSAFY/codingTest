import sys
input = sys.stdin.readline


n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

for _ in range(m):
    cards.sort()
    cards[0] = cards[1] = cards[0] + cards[1]

print(sum(cards))