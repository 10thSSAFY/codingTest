import sys
input = sys.stdin.readline


def dfs(y, x, cnt, _sum):
    global answer
    if cnt == k:
        answer = max(answer, _sum)
        return
    for i in range(y, n):
        for j in range(x if i == y else 0, m):
            if visited[i][j]:
                continue
            for z in range(4):
                ny = i + dy[z]
                nx = j + dx[z]
                if 0 <= ny < n and 0 <= nx < m and visited[ny][nx]:
                    break
            else:
                visited[i][j] = True
                dfs(i, j, cnt + 1, _sum + graph[i][j])
                visited[i][j] = False


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

n, m, k = map(int, input().split())
answer = -sys.maxsize
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dfs(0, 0, 0, 0)
print(answer)