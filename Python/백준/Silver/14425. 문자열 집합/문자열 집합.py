N, M = map(int, input().split())

S = set()
for _ in range(N):
    S.add(input())

result = 0
for _ in range(M):
    if input() in S:
        result += 1

print(result)