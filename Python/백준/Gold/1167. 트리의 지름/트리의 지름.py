import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs(node, currSum):
  global result
  result = max(result, currSum)
  visited[node] = True
  curr_node[node] = max(curr_node[node], currSum)

  for n, s in graph[node]:
    if not visited[n]:
      bfs(n, currSum + s)
  visited[node] = False


V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
  lst = list(map(int, input().split()))
  i = 0
  g_idx = lst[i]
  while True:
    i += 1
    if lst[i] != -1:
      graph[g_idx].append((lst[i], lst[i+1]))
      i += 1
    else:
      break

visited = [False] * (V+1)
result = 0
curr_node = [0] * (V+1)
bfs(1, 0)

maxN = curr_node.index(max(curr_node))
bfs(maxN, 0)
print(result)