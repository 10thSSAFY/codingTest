import sys
input = sys.stdin.readline


def DFS(num):
    visited[num] = True
    stack = [num]
    while stack:
        n = stack.pop()
        for i in TREE[n]:
            if not visited[i]:
                ans[i] = n
                visited[i] = True
                stack.append(i)


N = int(input())
TREE = [[] for _ in range(N + 1)]
ans = [0] * (N + 1)
visited = [False] * (N + 1)

for _ in range(1, N):
    n1, n2 = map(int, input().split())
    TREE[n1].append(n2)
    TREE[n2].append(n1)

DFS(1)

for j in range(2, N + 1):
    print(ans[j])
