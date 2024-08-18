def solution(node, visited):
    if dp[node][visited] != 0:
        return dp[node][visited]

    if visited == (1 << (N - 1)) - 1:
        if not W[node][0]:
            return float('inf')
        else:
            return W[node][0]

    res = float('inf')
    for i in range(1, N):
        if not W[node][i] or visited & (1 << (i - 1)):
            continue
        cost = W[node][i] + solution(i, visited | (1 << (i - 1)))
        res = min(res, cost)
    dp[node][visited] = res
    return res


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (1 << (N - 1)) for _ in range(N)]
result = solution(0, 0)

print(result)
