T = int(input())
n = int(input()); A = list(map(int, input().split()))
m = int(input()); B = list(map(int, input().split()))

prefix = {}

for s in range(n):
    sumA = 0
    for e in range(s, n):
        sumA += A[e]
        if sumA in prefix:
            prefix[sumA] += 1
        else:
            prefix[sumA] = 1

result = 0
for s in range(m):
    sumB = 0
    for e in range(s, m):
        sumB += B[e]
        if T - sumB in prefix:
            result += prefix[T - sumB]

print(result)