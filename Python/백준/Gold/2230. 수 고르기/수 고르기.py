import sys
input = sys.stdin.readline


N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

s, e = 0, 0
result = float('inf')
while e < N:
    num = A[e] - A[s]
    if num >= M:
        result = min(result, num)
        s += 1
        if s > e:
            e = s
    else:
        e += 1

print(result)