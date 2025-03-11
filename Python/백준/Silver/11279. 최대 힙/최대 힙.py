import sys
import heapq
input = sys.stdin.readline

N = int(input())
hq = []
for _ in range(N):
    num = int(input())
    if num == 0:
        if hq:
            print(heapq.heappop(hq)[1])
        else:
            print(0)
    else:
        heapq.heappush(hq, (-num, num))
