import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))

lst.sort()
res = 0
for i in range(N):
    res = max(res, lst[i] * (N - i))

print(res)