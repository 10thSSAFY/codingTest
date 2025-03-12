import sys
input = sys.stdin.readline


def solution(start, end, idx, left, right):
    if start > right or end < left:
        return sys.maxsize
    if left <= start and end <= right:
        return tree[idx]
    mid = (start + end) // 2
    return min(solution(start, mid, idx * 2, left, right), solution(mid + 1, end, idx * 2 + 1, left, right))


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = (start + end) // 2
    tree[idx] = min(init(start, mid, idx * 2), init(mid + 1, end, idx * 2 + 1))
    return tree[idx]


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [0] * (N * 4)

init(0, N - 1, 1)

for _ in range(M):
    a, b = map(int, input().split())
    print(solution(0, N - 1, 1, a - 1, b - 1))
