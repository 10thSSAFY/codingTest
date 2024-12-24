def solution(depth):
    if depth == N:
        print(*result)
        return

    for i in range(N):
        if not bit[i]:
            bit[i] = True
            result.append(lst[i])
            solution(depth + 1)
            result.pop()
            bit[i] = False

N = int(input())
lst = [i for i in range(1, N + 1)]
bit = [False] * N

result = []
solution(0)