from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    arr = [[2147483647] * m for _ in range(n)]
    arr[0][0] = 1
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr, nc = r + dr, c + dc
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if maps[nr][nc] == 1 and arr[nr][nc] > arr[r][c] + 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))
    
    answer = -1
    if arr[n - 1][m - 1] != 2147483647:
        answer = arr[n - 1][m - 1]
        
    return answer