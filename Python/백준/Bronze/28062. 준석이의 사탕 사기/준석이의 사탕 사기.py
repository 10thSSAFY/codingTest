N = int(input())
A = list(map(int, input().split()))

min_odd = 1001
for i in range(N):
    if A[i] % 2 == 1:
        min_odd = min(min_odd, A[i])

result = sum(A)
if result % 2 == 1:
    result -= min_odd

print(result)