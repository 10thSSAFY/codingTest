import sys
input = sys.stdin.readline

N, M = map(int, input().split())

down = [0] * (M + 2)
up = [0] * (M + 2)

for i in range(1, N // 2 + 1):
    a = int(input())
    b = M - int(input()) + 1
    down[a] += 1
    up[b] += 1

for i in range(1, M + 1):
    down[i] += down[i - 1]
    up[M-i+1] += up[M-i+2]

min_val = N
cnt = 0
for i in range(1, M + 1):
    diff = (down[M] - down[i - 1]) + (up[1] - up[i + 1])

    if diff < min_val:
        min_val = diff
        cnt = 1
    elif diff == min_val:
        cnt += 1

print(min_val, cnt)
