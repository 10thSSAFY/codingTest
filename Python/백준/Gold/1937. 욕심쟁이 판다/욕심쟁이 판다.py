import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(r, c):
    if dp[r][c]:
        return dp[r][c]

    dp[r][c] = 1
    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        nr, nc = r + dr, c + dc
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if arr[r][c] < arr[nr][nc]:
            dp[r][c] = max(dp[r][c], dfs(nr, nc) + 1)
    return dp[r][c]


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for r in range(N):
    for c in range(N):
        if not dp[r][c]:
            dfs(r, c)

max_num = 0
for i in range(N):
    max_num = max(max_num, max(dp[i]))

print(max_num)