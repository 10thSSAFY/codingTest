import heapq

def solution(k, tangerine):
    D = dict()
    for t in tangerine:
        if t in D:
            D[t] += 1
        else:
            D[t] = 1
        
    hq = []
    for K, V in D.items():
        heapq.heappush(hq, (-V, K))
        
    result = 0
    cnt = k
    while cnt > 0:
        result += 1
        cnt += heapq.heappop(hq)[0]
        
    return result
    