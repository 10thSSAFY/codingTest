from collections import deque
import sys
input = sys.stdin.readline


N = int(input())

A = []
B = []
C = []

q = deque()
for _ in range(N):
    case, *data = map(int, input().split())
    if case == 1:
        q.append(data)
    elif case == 2:
        a, b = q.popleft()
        if b == data[0]:
            A.append(a)
        else:
            B.append(a)


if A:
    print(*sorted(A))
else:
    print('None')

if B:
    print(*sorted(B))
else:
    print('None')

if q:
    for a, b in q:
        C.append(a)
    print(*sorted(C))

else:
    print('None')
