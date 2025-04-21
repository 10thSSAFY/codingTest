N, K = map(int, input().split())
lst = list(map(lambda x: int(x) % 2 == 0, input().split()))

result = 0
cnt = 0
left, right, = 0, 0
while right < N:
    if lst[right]:
        right += 1
        result = max(result, right - left - cnt)
    elif cnt < K:
        cnt += 1
        right += 1
        result = max(result, right - left - cnt)
    else:
        if not lst[left]:
            cnt -= 1
        left += 1

print(result)
