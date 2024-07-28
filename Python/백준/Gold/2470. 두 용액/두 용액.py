N = int(input())
lst = sorted(list(map(int, input().split())))

start, end = 0, N - 1
ans = abs(lst[start] + lst[end])
left, right = lst[start], lst[end]

while start < end:
    currSum = lst[start] + lst[end]

    if abs(currSum) < ans:
        ans = abs(currSum)
        left, right = lst[start], lst[end]
        if ans == 0:
            break

    if currSum < 0:
        start += 1
    else:
        end -= 1

print(left, right)
