import sys
from collections import deque
input = sys.stdin.readline


def bfs(r, c):
    q = deque()
    q.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if visited[nr][nc] == 0 and arr[nr][nc] == 0:
                q.append((nr, nc))
                visited[nr][nc] = 1
            elif arr[nr][nc] == 1:
                visited[nr][nc] += 1


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
while True:
    visited = [[0] * M for _ in range(N)]
    bfs(0, 0)
    result += 1

    for r in range(N):
        for c in range(M):
            if visited[r][c] >= 2:
                arr[r][c] = 0

    cnt = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 0:
                cnt += 1

    if cnt == N * M:
        break

print(result)
