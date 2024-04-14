import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline


def DFS(x, y):
    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    cnt = 0
    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < M and 0 <= ny < N and arr[nx][ny] < arr[x][y]:
            cnt += DFS(nx, ny)

    dp[x][y] = cnt
    return cnt


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
result = DFS(0, 0)
print(result)