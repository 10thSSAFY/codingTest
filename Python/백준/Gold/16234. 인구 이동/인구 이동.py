import sys
input = sys.stdin.readline

def dfs(r, c, cnt):
    stack = [(r, c)]
    opens[cnt] = [arr[r][c]]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r+dr, c+dc
            if not (0 <= nr < N and 0 <= nc < N):
                continue
            if visited[nr][nc] == -1 and L <= abs(arr[nr][nc] - arr[r][c]) <= R:
                visited[nr][nc] = cnt
                stack.append((nr, nc))
                opens[cnt].append(arr[nr][nc])

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

res = 0
while True:
    visited = [[-1] * N for _ in range(N)]
    cnt = 0
    opens = {}
    for r in range(N):
        for c in range(N):
            if visited[r][c] == -1:
                cnt += 1
                visited[r][c] = cnt
                dfs(r, c, cnt)
    if visited[N-1][N-1] == N**2:
        break
    for open in opens:
        opens[open] = sum(opens[open])//len(opens[open])

    for r in range(N):
        for c in range(N):
            arr[r][c] = opens[visited[r][c]]
    res += 1

print(res)