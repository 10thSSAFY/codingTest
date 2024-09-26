from collections import deque

def bfs(r, c):
    q = deque([(r, c)])
    visited = [[False] * M for _ in range(N)]
    visited[r][c] = 1
    cnt = 0
    while q:
        (r, c) = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nr][nc] == 'L' and not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                cnt = max(cnt, visited[nr][nc])
                q.append((nr, nc))
    return cnt - 1



N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
