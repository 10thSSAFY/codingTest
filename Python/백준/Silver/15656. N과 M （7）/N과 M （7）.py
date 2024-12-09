def solution(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        result.append(lst[i])
        solution(depth + 1)
        result.pop()


N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

result = []
solution(0)