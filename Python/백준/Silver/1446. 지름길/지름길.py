import sys
input = sys.stdin.readline

N, D = map(int, input().split())

dp = [i for i in range(D + 1)]
shortcuts = []
for _ in range(N):
    s, e, l = map(int, input().split())
    if e - s > l:
        shortcuts.append((s, e, l))
shortcuts.sort()

for shortcut in shortcuts:
    (s, e, l) = shortcut
    for i in range(1, D + 1):
        if i == e:
            dp[i] = min(dp[i], dp[s] + l)
        else:
            dp[i] = min(dp[i], dp[i - 1] + 1)

print(dp[D])
