import sys
input = sys.stdin.readline

N = int(input())
S = []
res = 0
for _ in range(N):
    x, y = map(int, input().strip().split())
    while S and S[-1] > y:
        res += 1
        S.pop()
    if not S or S and S[-1] != y:
        S.append(y)

while S:
    if S[-1] > 0:
        res += 1
    S.pop()

print(res)