import sys
input = sys.stdin.readline
from collections import deque


def melt(lst):
    for (r, c) in lst:
        arr[r][c] = 0


def solution():
    global num, cnt
    while True:
        q = deque([(0, 0)])

        visited = [[False] * M for _ in range(N)]
        visited[0][0] = True
        lst = []
        while q:
            (r, c) = q.popleft()
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < N and 0 <= nc < M) or visited[nr][nc]:
                    continue
                if arr[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))
                elif arr[nr][nc] == 1:
                    arr[nr][nc] = 'c'
                    lst.append((nr, nc))
                    
        if lst:
            cnt += 1
            num = len(lst)
            melt(lst)
        else:
            return


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
num = 0
solution()

print(cnt)
print(num)
