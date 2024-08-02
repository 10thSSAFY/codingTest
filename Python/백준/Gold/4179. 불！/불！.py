from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    while f:
        r, c = f.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not(0 <= nr < R and 0 <= nc < C):
                continue
            if arr[nr][nc] != '#' and not f_time[nr][nc]:
                f_time[nr][nc] = f_time[r][c] + 1
                f.append((nr, nc))

    while j:
        r, c = j.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < R and 0 <= nc < C):
                return j_time[r][c]
            if arr[nr][nc] == '#' or j_time[nr][nc]:
                continue
            if not f_time[nr][nc] or f_time[nr][nc] > j_time[r][c] + 1:
                j_time[nr][nc] = j_time[r][c] + 1
                j.append((nr, nc))

    return "IMPOSSIBLE"


R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

j = deque()
f = deque()
j_time = [[0] * C for _ in range(R)]
f_time = [[0] * C for _ in range(R)]

for r in range(R):
    for c in range(C):
        if arr[r][c] == 'J':
            j.append((r, c))
            j_time[r][c] = 1
        if arr[r][c] == 'F':
            f.append((r, c))
            f_time[r][c] = 1

result = bfs()
print(result)
