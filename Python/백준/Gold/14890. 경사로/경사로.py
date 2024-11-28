import sys
input = sys.stdin.readline


def solution(lst):
    visited = [False] * N
    for i in range(1, N):
        if abs(lst[i - 1] - lst[i]) > 1:
            return 0
        else:
            if (lst[i - 1] - lst[i]) == 1:
                for j in range(L):
                    if i + j >= N:
                        return 0
                    if lst[i] != lst[i + j]:
                        return 0
                    if visited[i + j]:
                        return 0
                    if not visited[i + j]:
                        visited[i + j] = True
            elif (lst[i - 1] - lst[i]) == -1:
                for j in range(L):
                    if i - j - 1 < 0:
                        return 0
                    if lst[i - 1] != lst[i - j - 1]:
                        return 0
                    if visited[i - j - 1]:
                        return 0
                    if not visited[i - j - 1]:
                        visited[i - j - 1] = True

    return 1


N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for r in range(N):
    result += solution(arr[r])
for c in range(N):
    tmp = [arr[r][c] for r in range(N)]
    result += solution(tmp)

print(result)
