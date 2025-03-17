input = __import__('sys').stdin.readline


def dfs(r, c, cnt):
    global result

    if cnt == K and r == 0 and c == M - 1:
        result += 1
    else:
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if graph[nr][nc] == '.' and cnt + 1 <= K:
                graph[nr][nc] = 'T'
                dfs(nr, nc, cnt + 1)
                graph[nr][nc] = '.'


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M, K = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]

result = 0
graph[N - 1][0] = 'T'
dfs(N - 1, 0, 1)
print(result)
