from collections import deque

N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)

while len(q) >= K:
    q.append(q.popleft())
    for _ in range(K-1):
        q.popleft()

print(q.popleft())