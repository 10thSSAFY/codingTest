def solution():
    for r in range(N):
        for c in range(N):
            t = int(arr[r][c])
            if t == 0 or dp[r][c] == 0:
                continue
            if r + t < N:
                dp[r + t][c] += dp[r][c]
            if c + t < N:
                dp[r][c + t] += dp[r][c]

    return dp[N - 1][N - 1]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
result = solution()
print(result)