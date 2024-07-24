from collections import deque
import sys
input = sys.stdin.readline


def solution():
    global result
    while queue:
        (h, r, c, day) = queue.popleft()
        for dh, dr, dc in [(-1, 0, 0), (0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (1, 0, 0)]:
            nh, nr, nc = h + dh, r + dr, c + dc
            if not (0 <= nh < H and 0 <= nr < N and 0 <= nc < M):
                continue
            if arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = 1
                last.remove((nh, nr, nc))
                queue.append((nh, nr, nc, day + 1))
                result = max(result, day + 1)


M, N, H = map(int, input().split())

arr = [[] for _ in range(H)]
for h in range(H):
    for _ in range(N):
        arr[h].append(list(map(int, input().split())))

queue = deque()
last = set()
result = 0
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:
                queue.append((h, r, c, 0))
            elif arr[h][r][c] == 0:
                last.add((h, r, c))

solution()

if last:
    print(-1)
else:
    print(result)