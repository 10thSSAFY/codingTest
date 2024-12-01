import sys
input = sys.stdin.readline


N = int(input().strip())
M = int(input().strip())
S = input().strip()

P = 'IOI'

cnt = 0
i = 0
answer = 0

while i < (M - 1):
    if S[i : i+3] == P:
        i += 2
        cnt += 1
        if cnt == N:
            answer += 1
            cnt -= 1
    else:
        i += 1
        cnt = 0

print(answer)