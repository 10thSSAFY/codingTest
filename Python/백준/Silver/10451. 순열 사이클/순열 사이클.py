def find(num):
    stack = [parent[num]]
    parent[num] = 0
    while stack:
        num = stack.pop()
        if not parent[num]:
            continue
        stack.append(parent[num])
        parent[num] = 0


T = int(input())
for _ in range(T):
    N = int(input())
    parent = [0] + list(map(int, input().split()))
    cnt = 0
    for i in range(1, N+1):
        if parent[i]:
            cnt += 1
            find(i)
    print(cnt)
