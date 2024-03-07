import heapq
import sys
input = sys.stdin.readline

N = int(input())
hqQ = []
hqP = []

for _ in range(N):
    Q, P = map(int, input().split())
    heapq.heappush(hqQ, (10000 - Q, P))
    heapq.heappush(hqP, (P, 10000 - Q))

res = heapq.heappop(hqQ)
print(10000-res[0], res[1], end=' ')
res = heapq.heappop(hqQ)
print(10000-res[0], res[1])
res = heapq.heappop(hqP)
print(10000-res[1], res[0], end=' ')
res = heapq.heappop(hqP)
print(10000-res[1], res[0])