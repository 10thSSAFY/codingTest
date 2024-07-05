from collections import deque
import sys
input = sys.stdin.readline


def end():
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 1 and not visited[r][c]:
                arr[r][c] = -1


def bfs(sr, sc):
    arr[sr][sc] = 0
    visited[sr][sc] = True
    q = deque([(sr, sc, 0)])
    while q:
        (r, c, d) = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1,)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if arr[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = True
                arr[nr][nc] = d + 1
                q.append((nr, nc, d + 1))


def start():
    for r in range(n):
        for c in range(m):
            if arr[r][c] == 2:
                return (r, c)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

(sr, sc) = start()
bfs(sr, sc)
end()

for i in range(n):
    print(*arr[i])
