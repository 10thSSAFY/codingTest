input = __import__('sys').stdin.readline

N, M = map(int, input().split())
jewel = [int(input()) for _ in range(M)]

start, end = 1, max(jewel)
result = end
while start <= end:
    mid = (start + end) // 2
    cnt = 0

    for j in jewel:
        if j <= mid:
            cnt += 1
            continue

        if j % mid == 0:
            cnt += j // mid
        else:
            cnt += j // mid + 1

    if cnt > N:
        start = mid + 1
    else:
        end = mid - 1
        result = min(result, mid)

print(result)