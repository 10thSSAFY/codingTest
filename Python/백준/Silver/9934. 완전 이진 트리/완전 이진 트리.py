def solution(start, end , depth):
    if start == end:
        tree[depth].append(lst[start])
        return
    
    center = (start + end) // 2
    tree[depth].append(lst[center])
    
    solution(start, center - 1, depth + 1)
    solution(center + 1, end, depth + 1)


K = int(input())
lst = list(map(int, input().split()))
tree = [[] for _ in range(K)]

solution(0, len(lst) - 1, 0)
for t in tree:
    print(*t)
