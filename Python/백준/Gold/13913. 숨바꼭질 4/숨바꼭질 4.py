from collections import deque


def path(n):
    arr = []
    temp = n
    for _ in range(dist[n] + 1):
        arr.append(temp)
        temp = move[temp]
    return ' '.join(map(str, arr[::-1]))


N, K = map(int, input().split())
dist = [-1] * 100001
move = [0] * 100001

q = deque([N])
dist[N] = 0
while q:
    n = q.popleft()
    if n == K:
        result = path(n)
        break
    for i in (n + 1, n - 1, 2 * n):
        if 0 <= i <= 100000 and dist[i] == -1:
            q.append(i)
            dist[i] = dist[n] + 1
            move[i] = n

print(dist[n])
print(result)