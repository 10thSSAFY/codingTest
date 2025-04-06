def solution():
    global result, lst

    for i in range(N - 1, 0, -1):
        if lst[i] < lst[i - 1]:
            x, y = i - 1, i
            for j in range(N - 1, 0, -1):
                if lst[j] < lst[x]:
                    lst[j], lst[x] = lst[x], lst[j]
                    lst = lst[:i] + sorted(lst[i:], reverse=True)
                    result = lst
                    return


N = int(input())
lst = list(map(int, input().split()))

result = [-1]
solution()
print(*result)