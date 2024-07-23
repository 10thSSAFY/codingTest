from collections import deque
import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    p = input().strip()
    n = int(input())
    arr = deque(input().strip()[1:-1].split(','))
    queue = deque(arr)

    rev, front, back = 0, 0, len(queue) - 1
    flag = 0

    if n == 0:
        queue = []
        front = 0
        back = 0

    for cmd in p:
        if cmd == 'R':
            rev = (rev + 1) % 2
        elif cmd == 'D':
            if not queue:
                flag = 1
                print('error')
                break
            else:
                if rev % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()

    if flag == 0:
        if rev % 2 != 0:
            queue.reverse()
        print('[' + ','.join(queue) + ']')
