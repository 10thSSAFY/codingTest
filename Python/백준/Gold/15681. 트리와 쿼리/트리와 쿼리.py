input = __import__('sys').stdin.readline
__import__('sys').setrecursionlimit(10 ** 6)

def dfs(n):
    visit[n] = True
    for node in tree[n]:
        if not visit[node]:
            dfs(node)
            dp[n] += dp[node]
    dp[n] += 1


N, R, Q = map(int, input().split())

tree = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)

dp = [0] * (N + 1)
visit = [False] * (N + 1)
dfs(R)

for _ in range(Q):
    U = int(input())
    print(dp[U])
