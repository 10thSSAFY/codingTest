import sys
from collections import deque


def inorder_search(node):
    global dist
    if tree[node][1] != -1:
        inorder_search(tree[node][1])
    dist += 1
    visited[node][1] = dist

    if tree[node][2] != -1:
        inorder_search(tree[node][2])


def bfs(root):
    maxdepth = 0
    queue = deque([root])
    visited[root][0] = 0
    while queue:
        node = queue.popleft()
        lc = tree[node][1]
        rc = tree[node][2]
        if lc != -1:
            if visited[lc][0] == -1:
                visited[lc][0] = visited[node][0] + 1
                maxdepth = max(visited[lc][0], maxdepth)
                queue.append(lc)
        if rc!= -1:
            if visited[rc][0] == -1:
                visited[rc][0] = visited[node][0] + 1
                maxdepth = max(visited[rc][0], maxdepth)
                queue.append(rc)
    return maxdepth


n = int(sys.stdin.readline())
tree = [[-1, -1, -1] for x in range(n + 1)]
for i in range(n):
    node, lc, rc = map(int, sys.stdin.readline().split())
    tree[node][1] = lc
    tree[node][2] = rc
    tree[lc][0] = n
    tree[rc][0] = n
root = -1
for i in range(1, n + 1):
    if tree[i][0] == -1:
        root = i

visited = [[-1, -1] for x in range(n + 1)]
maxdepth = bfs(root)

dist = 0
inorder_search(root)

maxDist = 0
minLevel = 1e10

if n == 1:
    print(1, 1)

else:
    for d in range(maxdepth + 1):
        minVal = 1e10
        maxVal = 0
        for i in range(1, n + 1):
            if d == visited[i][0]:
                minVal = min(visited[i][1], minVal)
                maxVal = max(visited[i][1], maxVal)
        if maxDist < maxVal - minVal + 1:
            minLevel = d + 1
            maxDist = maxVal - minVal + 1

    print(minLevel, maxDist)