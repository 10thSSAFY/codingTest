import heapq

N = int(input())

hq = []
for _ in range(N):
    S = input()
    L = len(S)
    C = 0
    for i in range(L):
        if S[i].isdigit():
            C += int(S[i])
            
    heapq.heappush(hq, (L, C, S))

while hq:
    print(heapq.heappop(hq)[2])
