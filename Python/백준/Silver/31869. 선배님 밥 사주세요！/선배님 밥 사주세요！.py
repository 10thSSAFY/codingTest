import sys
input = sys.stdin.readline

N = int(input())
d = {}
lst = [0] * 78
for _ in range(N):
    S, W, D, P = map(str, input().split())
    d[S] = (int(W) * 7 + int(D), int(P))

for _ in range(N):
    S, P = map(str, input().split())
    if d[S][1] > int(P):
        del d[S]

for k, v in d.items():
    lst[v[0]] = 1

result = 0
for i in range(77):
    if lst[i] == 1:
        lst[i] += lst[i-1]
        result = max(result, lst[i])

print(result)