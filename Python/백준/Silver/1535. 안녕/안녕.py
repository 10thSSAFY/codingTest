N = int(input())
knapsack = [list(map(int, input().split())) for _ in range(2)]
knapsack = [(0, 0)] + list(zip(*knapsack))

dp = [[0] * 101 for _ in range(N+1)]
for m in range(1, N+1):
    for w in range(1, 101):
        if w < knapsack[m][0]:
            dp[m][w] = dp[m-1][w]
        else:
            dp[m][w] = max(dp[m-1][w], dp[m-1][w-knapsack[m][0]] + knapsack[m][1])

print(dp[N][99])
