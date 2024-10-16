from collections import deque

TC = int(input())
for T in range(1, TC + 1):
    N = int(input())
    q = deque(list(map(int, input().split())))

    result = []

    while q:
        P = q.popleft()
        q.remove(P // 3 * 4)
        result.append(P)

    print(f'Case #{T}: {" ".join(map(str, result))}')