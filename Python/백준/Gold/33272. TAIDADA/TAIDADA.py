N, M, K = map(int, input().split())
S = set()
for i in range(1, M + 1):
    if i in S or (i ^ K) in S:
        continue

    S.add(i)

    if len(S) == N:
        break

if len(S) == N:
    print(' '.join(map(str, S)))
else:
    print(-1)
