from collections import deque

N, M, C = map(int, input().split())
Sr, Sc = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * M for _ in range(N)]

q = deque([(Sr - 1, Sc - 1)])
visit[Sr - 1][Sc - 1] = True
L = 0
result = T = board[Sr - 1][Sc - 1]
while q:
    L += 1
    for _ in range(len(q)):
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < N and 0 <= nc < M) or visit[nr][nc] or board[nr][nc] == -1:
                continue
            T += board[nr][nc]
            visit[nr][nc] = True
            q.append((nr, nc))
    result = max(result, T - L * C)

print(result)
