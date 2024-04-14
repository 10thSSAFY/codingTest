N, M = map(int, input().split())
lst = list(map(int, input().split()))

left, right = 1, max(lst)
while left <= right:
    mid = (left + right) // 2

    res = 0
    for l in lst:
        if l >= mid:
            res += l - mid

    if res >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)
