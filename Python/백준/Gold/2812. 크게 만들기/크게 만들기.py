N, K = map(int, input().split())
lst = list(map(int, input().strip()))
stack = []

cnt = 0
for i in range(N):
    while stack and cnt < K and stack[-1] < lst[i]:
        stack.pop()
        cnt += 1
    stack.append(lst[i])

while cnt < K:
    stack.pop()
    cnt += 1

print(''.join(map(str, stack)))