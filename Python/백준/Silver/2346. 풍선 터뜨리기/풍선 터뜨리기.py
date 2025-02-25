from collections import deque

N = int(input())
lst = list(map(int, input().split()))

q = deque()
for i in range(N):
    q.append((i + 1, lst[i]))

result = []
while True:
    idx, num = q.popleft()
    result.append(idx)

    if not q:
        break

    if num > 0:
        for _ in range(num - 1):
            q.append(q.popleft())
    else:
        for _ in range(-num):
            q.appendleft(q.pop())

print(*result)