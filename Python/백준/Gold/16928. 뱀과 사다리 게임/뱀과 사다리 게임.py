from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
l = {}
s = {}
for _ in range(N):
    x, y = map(int, input().split())
    l[x] = y

for _ in range(M):
    x, y = map(int, input().split())
    s[x] = y

board = [float('inf')] * 101
board[1] = 0

q = deque([1])
flag = False
while q:
    pos = q.popleft()
    cnt = board[pos]
    for i in range(1, 7):
        if pos + i == 100:
            result = cnt + 1
            flag = True
            break
        if 1 <= pos + i <= 100 and board[pos + i] == float('inf'):
            board[pos + i] = cnt + 1
            if pos + i not in l and pos + i not in s:
                q.append(pos + i)
            elif pos + i in l and board[l[pos + i]] == float('inf'):
                board[l[pos + i]] = cnt + 1
                q.append(l[pos + i])
            elif pos + i in s and board[s[pos + i]] == float('inf'):
                board[s[pos + i]] = cnt + 1
                q.append(s[pos + i])
    if flag:
        break

print(result)