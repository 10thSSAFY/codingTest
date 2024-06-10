import sys, heapq
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    lst.append(tuple(map(int, input().split())))
lst.sort()

hq = []
for d, n in lst:
    heapq.heappush(hq, n)
    if len(hq) > d:
        heapq.heappop(hq)

print(sum(hq))