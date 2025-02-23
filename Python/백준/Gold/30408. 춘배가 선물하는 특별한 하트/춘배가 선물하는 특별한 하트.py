from collections import deque

N, M = map(int, input().split())
q = deque([N])
S = set()
result = False
while q:
    w = q.popleft()
    if w == M:
        result = True
        break

    if w < M:
        continue

    if w % 2 == 0:
        if w // 2 not in S:
            S.add(w // 2)
            q.append(w // 2)
    else:
        if (w + 1) // 2 not in S:
            S.add((w + 1) // 2)
            q.append((w + 1) // 2)
        if (w - 1) // 2 not in S:
            S.add((w - 1) // 2)
            q.append((w - 1) // 2)

if result:
    print('YES')
else:
    print('NO')