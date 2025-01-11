import sys
input = sys.stdin.readline

H, W = map(int, input().split())
N = int(input())
lst = list(list(map(int, input().split())) for _ in range(N))

result = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        r1, c1 = lst[i]
        r2, c2 = lst[j]

        if (r1 + r2 <= H and max(c1, c2) <= W) or (max(r1, r2) <= H and c1 + c2 <= W):
            result = max(result, r1*c1 + r2*c2)
        if (c1 + r2 <= H and max(r1, c2) <= W) or (max(c1, r2) <= H and r1 + c2 <= W):
            result = max(result, r1*c1 + r2*c2)
        if (c1 + c2 <= H and max(r1, r2) <= W) or (max(c1, c2) <= H and r1 + r2 <= W):
            result = max(result, r1*c1 + r2*c2)
        if (r1 + c2 <= H and max(c1, r2) <= W) or (max(r1, c2) <= H and c1 + r2 <= W):
            result = max(result, r1*c1 + r2*c2)

print(result)