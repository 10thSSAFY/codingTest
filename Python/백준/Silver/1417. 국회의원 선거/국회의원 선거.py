import heapq

N = int(input())
D = int(input())

hq = []
for _ in range(N - 1):
    v = int(input())
    heapq.heappush(hq, -v)

result = 0
while hq and D <= -hq[0]:
    v = heapq.heappop(hq)
    result += 1
    D += 1
    v += 1
    heapq.heappush(hq, v)

print(result)
