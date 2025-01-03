def solution():
    if A == B:
        return 0

    cnt = 0
    for r in range(N - 2):
        for c in range(M - 2):
            if A[r][c] != B[r][c]:
                for nr in range(3):
                    for nc in range(3):
                        A[r + nr][c + nc] = 1 - A[r + nr][c + nc]
                cnt += 1
            if A == B:
                return cnt

    return -1


N, M = map(int, input().split())
A = [list(map(int, input())) for _ in range(N)]
B = [list(map(int, input())) for _ in range(N)]

result = solution()
print(result)
