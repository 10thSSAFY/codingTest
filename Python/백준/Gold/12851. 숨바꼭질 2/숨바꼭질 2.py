from collections import deque

N, K = map(int, input().split())
q = deque()
q.append(N)

visited = [-1] * 100001
visited[N] = 0

cnt = 0
while q:
    now = q.popleft()

    if now == K:
        cnt += 1

    for move in [now - 1, now + 1, now * 2]:
        if 0 <= move < 100001:
            if visited[move] == -1 or visited[move] >= visited[now] + 1:
                visited[move] = visited[now] + 1
                q.append(move)

print(visited[K])
print(cnt)