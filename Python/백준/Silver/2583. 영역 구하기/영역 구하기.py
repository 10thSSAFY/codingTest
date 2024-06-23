def dfs(r, c):
    visited[r][c] = True
    stack = [(r, c)]
    area = 1
    while stack:
        r, c = stack.pop()
        for dr, dc in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if not visited[nr][nc]:
                visited[nr][nc] = True
                stack.append((nr, nc))
                area += 1
    return area


M, N, K = map(int, input().split())
visited = [[False] * M for _ in range(N)]
for _ in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            visited[r][c] = True


cnt = 0
result = []
for r in range(N):
    for c in range(M):
        if not visited[r][c]:
            cnt += 1
            result.append(dfs(r, c))

result.sort()
print(cnt)
print(*result)