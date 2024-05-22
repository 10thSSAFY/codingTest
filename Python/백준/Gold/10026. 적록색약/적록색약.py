import sys
input = sys.stdin.readline


def find_b(r, c):
    visited[r][c] = True
    color = board[r][c]
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N and not visited[nr][nc]):
                continue
            if color == 'B' and board[nr][nc] == color:
                visited[nr][nc] = True
                stack.append((nr, nc))
            elif color != 'B' and board[nr][nc] != 'B':
                visited[nr][nc] = True
                stack.append((nr, nc))


def find(r, c):
    visited[r][c] = True
    color = board[r][c]
    stack = [(r, c)]
    while stack:
        r, c = stack.pop()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < N and not visited[nr][nc]):
                continue
            if board[nr][nc] == color:
                visited[nr][nc] = True
                stack.append((nr, nc))


N = int(input())
board = [list(input().strip()) for _ in range(N)]

cnt = 0
visited = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt += 1
            find(r, c)

cnt_b = 0
visited = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if not visited[r][c]:
            cnt_b +=1
            find_b(r, c)

print(cnt, cnt_b)