def solution(result, depth):
    if depth == M:
        print(*result)

    for i in range(N):
        if not bit[i]:
            bit[i] = True
            solution(result + [lst[i]], depth + 1)
            bit[i] = False


N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

bit = [False] * N
result = []
solution(result, 0)