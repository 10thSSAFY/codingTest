from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
arr = [input() for _ in range(N)]
starts_1, starts_2 = [], []
for r in range(N):
    for c in range(M):
        if arr[r][c]=="L":
            cnt = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == "L":
                    cnt += 1
            if cnt == 1:
                starts_1.append((r, c))
            elif cnt == 2:
                starts_2.append((r, c))

result = 0
starts = starts_1 if starts_1 else starts_2
while starts:
    sr, sc = starts.pop()
    q = deque([(0, sr, sc)])
    visited = [[0] * M for _ in range(N)]
    visited[sr][sc] = 1
    while q:
        cnt, row, col = q.popleft()
        result = max(result, cnt)
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == "L" and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((cnt + 1, nr, nc))

print(result)