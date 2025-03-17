from collections import deque
input = __import__("sys").stdin.readline

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
visit = {(r1, c1)}

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

q = deque([(r1, c1, 0)])
result = -1
while q:
    r, c, cnt = q.popleft()
    for i in range(6):
        nr, nc = r + dr[i], c + dc[i]
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if (nr, nc) not in visit:
            if nr == r2 and nc == c2:
                result = cnt + 1
                q = deque()
                break
            visit.add((nr, nc))
            q.append((nr, nc, cnt + 1))

print(result)
# 문제가 이상하다. 문제가 이상하다. 문제가 이상하다. 문제가 이상하다.
