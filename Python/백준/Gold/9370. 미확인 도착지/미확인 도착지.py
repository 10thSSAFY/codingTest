import heapq
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append([b, d])
        graph[b].append([a, d])

    arrives = [int(input()) for _ in range(t)]

    visit = []
    heapq.heappush(visit, [0, s, False])
    distance = [[int(10e9), False] for _ in range(n + 1)]
    distance[s] = [0, False]

    while visit:
        cost, node, check = heapq.heappop(visit)

        for next_node, dist in graph[node]:
            # 이번 경로가 g, h를 지나는지를 파악
            check_temp = check
            if (node == g and next_node == h) or (node == h and next_node == g):
                check_temp = True

            # 최단거리 갱신
            if cost + dist < distance[next_node][0]:
                distance[next_node] = [cost + dist, check_temp]
                heapq.heappush(visit, [cost + dist, next_node, check_temp])

            # 같은 거리이지만 현재 경로에서 처음 g, h를 지나게 된다면 갱신
            if not distance[next_node][1] and check_temp and cost + dist == distance[next_node][0]:
                distance[next_node] = [cost + dist, check_temp]
                heapq.heappush(visit, [cost + dist, next_node, check_temp])

    result = []
    for arrive in arrives:
        if distance[arrive][1]:
            result.append(arrive)

    result.sort()
    print(*result)