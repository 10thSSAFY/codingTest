from collections import deque


def bfs():
    que = deque()

    for i in range(1, N + 1):
        if parents[i] == -1:
            result[i] = 0
            que.append(i)

    while que:
        curr = que.popleft()
        for child in graph[curr]:
            if result[child] == -1:
                result[child] = result[curr] + 1
                que.append(child)


N = int(input())
graph = [[] for _ in range(N + 1)]
temp = [[] for _ in range(N + 1)]
edges = [0] * (N + 1)
parents = [-1] * (N + 1)
result = [-1] * (N + 1)

for _ in range(1, N + 1):
    s1, s2 = map(int, input().split())
    graph[s1].append(s2)
    graph[s2].append(s1)
    temp[s1].append(s2)
    temp[s2].append(s1)
    edges[s1] += 1
    edges[s2] += 1

while True:
    flag = True
    for i in range(1, N + 1):
        if edges[i] == 1:
            parent = temp[i].pop()
            parents[i] = parent
            temp[parent].remove(i)
            edges[i] = 0
            edges[parent] -= 1
            flag = False

    if flag:
        break

bfs()

print(*result[1:])