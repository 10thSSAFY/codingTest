import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
queue = deque([])
for _ in range(N):
    cmd = input().split()
    if cmd[0] == 'push':
        queue.append(int(cmd[1]))
    elif cmd[0] == 'pop':
        if bool(queue) == True:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(queue))
    elif cmd[0] == 'empty':
        if bool(queue) == False:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if bool(queue) == True:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if bool(queue) == True:
            print(queue[-1])
        else:
            print(-1)
