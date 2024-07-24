import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def DFS(num):
    global ans
    visited[num] = True
    c = 0
    for i in TREE[num]:
        if not visited[i] and i != D:
            c += 1
            DFS(i)
    if c == 0:
        ans += 1


N = int(input())
p = list(map(int, input().split()))
D = int(input())
TREE = [[] for _ in range(N)]
visited = [False] * N

for i in range(N):
    if p[i] == -1:
        root = i
    else:
        TREE[i].append(p[i])
        TREE[p[i]].append(i)


ans = 0
if D == root:
    print(0)
else:
    DFS(root)
    print(ans)
