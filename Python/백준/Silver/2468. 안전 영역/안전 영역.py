from collections import deque

def bfs(r, c, high, visited):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if arr[nr][nc] > high and not visited[nr][nc]:
                visited[nr][nc] = True
                q.append((nr, nc))


N = int(input())
arr = []
Max = 0
for _ in range(N):
    line = list(map(int, input().split()))
    Max = max(Max, max(line))
    arr.append(line)

result = 0
for i in range(Max):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > i and not visited[r][c]:
                bfs(r, c, i, visited)
                cnt += 1

    result = max(result, cnt)

print(result)