from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visit = [[False] * 16 for _ in range(16)]

    q = deque([(1, 1)])
    visit[1][1] = True
    result = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < 16 and 0 <= nc < 16) or arr[nr][nc] == 1 or visit[nr][nc]:
                continue

            if arr[nr][nc] == 3:
                result = 1
                break

            q.append((nr, nc))
            visit[nr][nc] = True

    print(f'#{tc} {result}')
