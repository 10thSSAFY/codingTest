from collections import deque

N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)

res = "<"
while q:
    for _ in range(K-1):
        q.append(q.popleft())
    num = q.popleft()
    res += str(num) + ", "

print(res[:-2] + ">")
