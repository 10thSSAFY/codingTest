import sys
input = sys.stdin.readline


def BF():
    for i in range(N):
        for j in range(len(edges)):
            cur, next, cost = edges[j]
            if dist[next] > dist[cur] + cost:
                dist[next] = dist[cur] + cost
                if i == N - 1:
                    return True
    return False


TC = int(input())
for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    dist = [1e9] * (N + 1)
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    if BF():
        print('YES')
    else:
        print('NO')


