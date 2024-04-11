from collections import deque

t, a, b = map(int, input().split())
result = a

check = [False] * (5000001)

q = deque()
q.append((a, False))
check[a] = True

v = [a]
if not check[b]:
    q.append((b, False))
    check[b] = True
    result = max(result, b)
    v.append(b)

while q:
    cv, ch = q.popleft()
    for i in v:
        nv = i + cv
        if nv <= t and not check[nv]:
            result = max(result, nv)
            check[nv] = True
            q.append((nv, ch))
        if not ch:
            nv = cv // 2 + i
            if nv <= t and not check[nv]:
                result = max(result, nv)
                check[nv] = True
                q.append((nv, True))

print(result)
