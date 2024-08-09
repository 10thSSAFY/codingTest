import sys
input = sys.stdin.readline


N, M = map(int, input().split())
time = []
for _ in range(N):
    time.append(int(input()))

left, right = min(time), max(time) * M
result = sys.maxsize

while left <= right:
    mid = (left + right) // 2
    cnt = 0

    for t in time:
        cnt += mid // t

    if cnt >= M:
        right = mid - 1
        result = min(result, mid)
    else:
        left = mid + 1

print(result)
