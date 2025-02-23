import heapq
import sys
input = sys.stdin.readline

T, n = map(int, input().split())
hq = []
for i in range(n):
    A, B, C = map(int, input().split())
    heapq.heappush(hq, (-C, A, B))

for _ in range(T):
    if not hq:
        break
    p, i, t = heapq.heappop(hq)
    print(i)
    t -= 1
    if t > 0:
        heapq.heappush(hq, (p + 1, i, t))
