import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

cnt = 0
for num in graph[1]:
    if not visited[num]:
       cnt += 1
       visited[num] = True
    for newNum in graph[num]:
        if newNum == 1:
            continue
        if not visited[newNum]:
            cnt += 1
            visited[newNum] = True

print(cnt)