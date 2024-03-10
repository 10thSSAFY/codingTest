from collections import deque


def bfs(i, j):
    global res
    q = deque([(i, j)])
    have_visited[i][j] = True
    visited[i][j] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
                if arr[r][c] < arr[nr][nc]:
                    return
                if arr[r][c] == arr[nr][nc]:
                    have_visited[nr][nc] = True
                    visited[nr][nc] = True
                    q.append((nr, nc))
    res += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
have_visited = [[False] * M for _ in range(N)]

res = 0
for i in range(N):
    for j in range(M):
        if not have_visited[i][j]:
            visited = [[False] * M for _ in range(N)]
            bfs(i, j)

print(res)