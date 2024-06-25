from collections import deque

A, B = map(int, input().split())
q = deque()
q.append((A, 1))

while q:
    n, cnt = q.popleft()
    if n > B:
        continue
    if n == B:
        print(cnt)
        break
    q.append((n * 2, cnt + 1))
    q.append((n * 10 + 1, cnt + 1))
else:
    print(-1)
