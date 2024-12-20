N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for r in range(N):
    for c in range(M):
        for n in range(1, arr[r][c] + 1):
            tmp = 6
            if n > 1:
                tmp -= 1
            if n < arr[r][c]:
                tmp -= 1
            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= r + dr < N and 0 <= c + dc < M:
                    if n <= arr[r + dr][c + dc]:
                        tmp -= 1
            result += tmp

print(result)