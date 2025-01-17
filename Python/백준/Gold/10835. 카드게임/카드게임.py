N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [[-1] * (N + 1) for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(N):
        if dp[i][j] != -1:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
            if A[i] > B[j]:
                dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + B[j])

result = max([max(d) for d in dp])
print(result)