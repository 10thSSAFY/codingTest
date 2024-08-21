N = int(input())
A = list(map(int, input().split()))

dp = [1] * N
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

result = []
LIS_num = max(dp)
for i in range(N - 1, -1, -1):
    if dp[i] == LIS_num:
        result.append(A[i])
        LIS_num -= 1

result.reverse()

print(max(dp))
print(*result)