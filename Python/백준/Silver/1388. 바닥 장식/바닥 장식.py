N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
res = 0
for r in range(N):
    for c in range(M):
        if arr[r][c] == '-' and not visited[r][c]:
            visited[r][c] = True
            res += 1
            nc = c
            while True:
                nc += 1
                if not(nc < M and arr[r][nc] == '-'):
                    break
                visited[r][nc] = True
        elif arr[r][c] == '|' and not visited[r][c]:
            visited[r][c] = True
            res += 1
            nr = r
            while True:
                nr += 1
                if not(nr < N and arr[nr][c] == '|'):
                    break
                visited[nr][c] = True
print(res)