import sys
input = sys.stdin.readline

def dfs(start, now, value, cnt):
    global ans

    if cnt == N:
        if W[now][start]:
            value += W[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and W[now][i]:
            visited[i] = True
            dfs(start, i, value + W[now][i], cnt + 1)
            visited[i] = False


N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

ans = sys.maxsize
visited = [False] * N
for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(ans)