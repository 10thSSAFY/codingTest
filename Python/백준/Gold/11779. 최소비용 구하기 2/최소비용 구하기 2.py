import heapq
import sys
input = sys.stdin.readline


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((c, e))

S, E = map(int, input().split())

hq = []
heapq.heappush(hq, (0, S))
result = [float('inf')] * (n + 1)
result[S] = 0
path = [False] * (n + 1)
path[S] = [S]

while hq:
    curr_cost, curr_city = heapq.heappop(hq)
    if result[curr_city] < curr_cost:
        continue
    for next_cost, next_curr_city in graph[curr_city]:
        if result[next_curr_city] > curr_cost + next_cost:
            result[next_curr_city] = curr_cost + next_cost
            heapq.heappush(hq, (curr_cost + next_cost, next_curr_city))
            path[next_curr_city] = path[curr_city] + [next_curr_city]

print(result[E])
print(len(path[E]))
print(*path[E])