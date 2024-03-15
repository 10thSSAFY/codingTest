import sys
import heapq
input = sys.stdin.readline


def dijkstra(end):
    dist_list = [sys.maxsize] * N
    dist_list[0] = 0

    hq = []
    heapq.heappush(hq, (0, 0))

    while hq:
        dist, node = heapq.heappop(hq)
        if dist > dist_list[node]:
            continue

        for n_dist, n_node in graph[node]:
            if dist_list[n_node] > dist_list[node] + n_dist and not lst[n_node]:
                dist_list[n_node] = dist_list[node] + n_dist
                heapq.heappush(hq, (dist_list[n_node], n_node))

    return dist_list[end]


N, M = map(int, input().split())
lst = list(map(int, input().strip().split()))
lst[-1] = 0

graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, t = map(int, input().split())
    graph[a].append((t, b))
    graph[b].append((t, a))


res = dijkstra(N-1)
print(res if res != sys.maxsize else -1)