import sys
input = sys.stdin.readline


def dfs(r, c):
    stack = [(r, c)]
    cnt = 1
    while stack:
        (r, c) = stack.pop()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N and not visited[nr][nc]):
                continue
            if board[nr][nc] == 1:
                visited[nr][nc] = True
                cnt += 1
                stack.append((nr, nc))
    return cnt


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

result = 0
lst = []
for r in range(N):
    for c in range(N):
        if not (0 <= r < N and 0 <= c < N and not visited[r][c]):
            continue
        if board[r][c] == 1:
            result += 1
            visited[r][c] = True
            lst.append(dfs(r, c))

lst.sort()
print(result)
for l in lst:
    print(l)
