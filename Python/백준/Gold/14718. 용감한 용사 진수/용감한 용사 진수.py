import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()
arr = list(zip(*arr))

res = 2147483647
for D in arr[1]:
    for I in arr[2]:
        S = 0
        cnt = 0
        for i in range(N):
            if arr[1][i] <= D and arr[2][i] <= I:
               cnt += 1
               S = arr[0][i]
               if cnt == M:
                   break
        if cnt == M:
            res = min(res, S + D + I)

print(res)
