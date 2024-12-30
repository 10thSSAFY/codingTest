N = int(input())
lst = list(map(int, input().split()))

l, r = 0, N - 1

result = abs(lst[l] + lst[r])
result_l, result_r = l, r

while l < r:
    tmp = lst[l] + lst[r]

    if abs(tmp) < result:
        result_l = l
        result_r = r
        result = abs(tmp)
        if result == 0:
            break

    if tmp > 0:
        r -= 1
    else:
        l += 1

print(lst[result_l], lst[result_r])
