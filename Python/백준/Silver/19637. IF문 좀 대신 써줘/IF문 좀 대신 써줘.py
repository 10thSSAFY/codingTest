import sys
input = sys.stdin.readline

N, M = map(int, input().split())

power = []
S = set()
for _ in range(N):
    a, b = input().split()
    if b not in S:
        power.append((a, int(b)))
        S.add(b)

p_len = len(power)
for _ in range(M):
    p = int(input())
    l, r = 0, p_len
    while l <= r:
        m = (l + r) // 2
        if p > power[m][1]:
            l = m + 1
        else:
            r = m - 1
    print(power[l][0])
