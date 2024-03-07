import sys
input = sys.stdin.readline

N = int(input())
Qlst = []
Plst = []

for _ in range(N):
    Q, P = map(int, input().split())
    Qlst.append((Q, 10000 - P))
    Plst.append((P, 10000 - Q))

Qlst.sort(reverse=True)
Plst.sort()
print(Qlst[0][0], 10000-Qlst[0][1], Qlst[1][0], 10000 - Qlst[1][1])
print(10000-Plst[0][1], Plst[0][0], 10000-Plst[1][1], Plst[1][0])