import heapq

N = int(input())
hq = []
nums = map(int, input().split())
for num in nums:
    heapq.heappush(hq, num)

for _ in range(N - 1):
    nums = map(int, input().split())
    for num in nums:
        if hq[0] < num:
            heapq.heappop(hq)
            heapq.heappush(hq, num)

print(hq[0])
