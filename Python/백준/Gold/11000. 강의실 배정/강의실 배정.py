import sys
import heapq
input = sys.stdin.readline

N = int(input())
lst = []

for _ in range(N):
    lst.append(list(map(int, input().split())))
lst.sort()

hq = []
heapq.heappush(hq, lst[0][1])
for i in range(1, N):
    if lst[i][0] < hq[0]:
        heapq.heappush(hq, lst[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, lst[i][1])

print(len(hq))
