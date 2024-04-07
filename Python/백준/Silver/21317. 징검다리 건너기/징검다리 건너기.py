def solution():
    if N == 1:
        return 0

    if N == 2:
        return lst[0][0]

    dp = [0] * N
    dp[1] = lst[0][0]
    dp[2] = min(lst[0][1], lst[0][0] + lst[1][0])
    for i in range(3, N):
        dp[i] = min(lst[i - 1][0] + dp[i - 1], lst[i - 2][1] + dp[i - 2])

    res = dp[-1]
    dp2 = dp[:]

    for i in range(0, N - 3):
        if dp[i + 3] > dp[i] + K:
            dp2[i + 3] = dp[i] + K
            for j in range(i + 4, N):
                dp2[j] = min(dp[j], dp2[j - 1] + lst[j - 1][0], dp2[j - 2] + lst[j - 2][1])
            res = min(res, dp2[-1])
    return res


N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N - 1)]
K = int(input())

result = solution()
print(result)