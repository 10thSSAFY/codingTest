def solution(sizes):
    max_w = max_h = 0
    for size in sizes:
        w, h = sorted(size)
        max_w = max(w, max_w)
        max_h = max(h, max_h)
        
    answer = max_w * max_h
    return answer