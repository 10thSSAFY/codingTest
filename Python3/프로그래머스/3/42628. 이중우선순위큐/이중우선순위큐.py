import heapq

def solution(operations):
    answer = []
    
    hq = []
    for operation in operations:
        x, num = operation.split()
        num = int(num)
        
        if x == 'I':
            heapq.heappush(hq, num)
        elif x == 'D' and num == 1:
            if hq:
                max_num = max(hq)
                hq.remove(max_num)
        else:
            if hq:
                heapq.heappop(hq)
    
    if len(hq) == 0:
        answer = [0, 0]
    else:
        answer = [max(hq), heapq.heappop(hq)]
        
    return answer