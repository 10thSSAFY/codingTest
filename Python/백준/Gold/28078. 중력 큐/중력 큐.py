from collections import deque
import sys
input = sys.stdin.readline


def solution(query):
    global state, b, w
    if query == 'push b':
        q.appendleft(1)
        b += 1
    elif query == 'push w':
        q.appendleft(2)
        w += 1
    elif query == 'pop':
        if q:
            if q.pop() == 1:
                b -= 1
            else:
                w -= 1
    elif query == 'rotate l':
        state = (state + 3) % 4
    elif query == 'rotate r':
        state = (state + 1) % 4
    elif query == 'count b':
        print(b)
    elif query == 'count w':
        print(w)

    if state == 1:
        while q and q[-1] != 2:
            q.pop()
            b -= 1

    elif state == 3:
        while q and q[0] != 2:
            q.popleft()
            b -= 1


Q = int(input())

state, b, w = 0, 0, 0
q = deque()
for _ in range(Q):
    solution(input().strip())
