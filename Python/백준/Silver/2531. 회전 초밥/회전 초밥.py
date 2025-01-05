from collections import deque
import itertools
import sys
input = sys.stdin.readline


N, d, k, c = map(int, input().split())
q = deque()
result = 0
for _ in range(N):
    q.append(int(input()))

for _ in range(N):
    s = set(itertools.islice(q, 0, k))
    l = len(s) if c in s else len(s) + 1
    result = max(result, l)
    q.append(q.popleft())

print(result)