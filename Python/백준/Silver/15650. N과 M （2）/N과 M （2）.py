def solution(start, iterate):
    if iterate == M:
        print(*res)
        return

    for i in range(start, N):
        res.append(lst[i])
        solution(i+1, iterate+1)
        res.pop()

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
res = []
solution(0, 0)