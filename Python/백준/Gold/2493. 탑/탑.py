N = int(input())
lst = list(map(int, input().split()))

res = [0] * N
stack = []
for i in range(N):
    while stack:
        if stack[-1][1] < lst[i]:
            stack.pop()
        else:
            res[i] = stack[-1][0] + 1
            break
    stack.append((i, lst[i]))
print(*res)