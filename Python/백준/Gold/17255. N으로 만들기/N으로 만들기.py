from collections import deque

q = deque([input()])
result = 0
while q:
    num = q.popleft()

    if len(num) == 1:
        result += 1
        continue

    a = num[1:]
    b = num[:-1]
    if a == b:
        q.append(a)
    else:
        q.append(a)
        q.append(b)

print(result)