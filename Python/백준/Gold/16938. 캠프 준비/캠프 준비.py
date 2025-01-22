def solution(depth, min_num, max_num, total):
    global result
    if depth == N:
        if L <= total <= R and max_num - min_num >= X:
            result += 1
        return

    n = A[depth]
    if max_num + n <= R:
        solution(depth + 1, min(min_num, n), max(max_num, n), total + n)
    solution(depth + 1, min_num, max_num, total)
    return


N, L, R, X = map(int, input().split())
A = list(map(int, input().split()))

result = 0
solution(0, float('inf'), 0, 0)
print(result)
