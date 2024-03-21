S = int(input())
start = 1
end = S

while start <= end:
    mid = (start + end) // 2
    if mid * (mid + 1) // 2 <= S:
        res = mid
        start = mid + 1
    else:
        end = mid - 1

print(res)